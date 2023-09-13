from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load data from a CSV file (make sure your CSV file is in the project directory)
data = pd.read_csv('aggregate-household-income-in-the-past-12-months-in-2015-inflation-adjusted-dollars.csv')  
@app.route('/')
def home():
    return render_template('data.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
