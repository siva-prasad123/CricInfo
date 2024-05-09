from flask import Flask, render_template
from fetch_cricket_data import fetch_live_cricket_data

app = Flask(__name__)

# Route to display live cricket data
@app.route('/')
def display_cricket_data():
    # Fetch live cricket data
    url = "https://crex.live/scoreboard/PBV/1L8/1st-Match/MP/MQ/fr-vs-mlt-1st-match-mdina-cup-t20-2024/live"
    data = fetch_live_cricket_data(url)
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
