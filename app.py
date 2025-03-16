from flask import Flask, render_template, jsonify, request
from cam import detect_crowd_density  # Ensure this module exists for crowd detection

app = Flask(__name__)

# Route for the home page
@app.route("/")
def home():
    return render_template("index.html")

# Route for the dashboard page
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# Route for the booking page
@app.route("/booking")
def booking():
    return render_template("booking.html")

# Route for the login page
@app.route("/login")
def login():
    return render_template("login.html")

# API endpoint to fetch crowd density
@app.route("/get_crowd_density")
def get_crowd_density():
    station = request.args.get('station')
    
    # Call the crowd detection function with the station parameter
    density = detect_crowd_density(station)  # Pass the station name to the function
    return jsonify({'density': density})

if __name__ == "__main__":
    app.run(debug=True)
