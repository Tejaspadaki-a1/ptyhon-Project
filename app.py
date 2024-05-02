from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process_query', methods=['POST'])
def process_query():
    query = request.form['query']
    # Add logic to process the query here
    return query

if __name__ == "__main__":
    app.run(debug=True)
