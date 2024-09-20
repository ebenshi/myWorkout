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