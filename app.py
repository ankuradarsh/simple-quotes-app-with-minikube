from flask import Flask, render_template
import requests

app = Flask(__name__)

# Define a route to fetch and display quotes
@app.route('/')
def display_quotes():
    # Make a request to the Quotable API
    response = requests.get('https://api.quotable.io/random')
    if response.status_code == 200:
        quote = response.json()
        return render_template('index.html', quote=quote)
    else:
        return "Error fetching quote"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
