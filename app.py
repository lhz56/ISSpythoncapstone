from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main HTML page."""
    return render_template('map.html')

@app.route('/iss-now')
def iss_now():
    """Fetch the current location of the ISS."""
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()
    if data['message'] == 'success':
        return jsonify({
            "latitude": data["iss_position"]["latitude"],
            "longitude": data["iss_position"]["longitude"]
        })
    return jsonify({"error": "Unable to fetch ISS location"})

@app.route('/astronauts')
def astronauts():
    """Fetch the list of astronauts currently in space."""
    response = requests.get("http://api.open-notify.org/astros.json")
    data = response.json()
    if data['message'] == 'success':
        return jsonify(data)
    return jsonify({"error": "Unable to fetch astronauts data"})

if __name__ == "__main__":
    app.run(debug=True)
