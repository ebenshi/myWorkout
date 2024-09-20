# app.py

from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

    @app.route('/form')
def form():
    return render_template('form.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Retrieve form data
    goal = request.form['goal']
    level = request.form['level']
    equipment = request.form['equipment']
    time = request.form['time']

    # Create the prompt for OpenAI API
    prompt = f"""
    You are a certified fitness trainer. Create a one-week workout plan for a {level.lower()} individual whose goal is {goal.lower()}. They have {equipment.lower()} available and can dedicate {time} minutes per day. Provide detailed daily workouts including exercises, sets, reps, and rest periods.
    """

    # Call the OpenAI API
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1000,
            temperature=0.7,
        )
        # Extract the generated text
        workout_plan = response.choices[0].text.strip()
    except Exception as e:
        return render_template('error.html', error_message=str(e))

    return render_template('result.html', workout_plan=workout_plan)

    