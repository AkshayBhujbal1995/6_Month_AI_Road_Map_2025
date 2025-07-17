from flask import Flask  # Import Flask class

app = Flask(__name__)   # Create Flask app instance

@app.route('/')         # Define route (home page)
def index():
    return 'Welcome to first flask deployment'  # Text shown on visiting homepage

# Run the app on localhost (127.0.0.1) and port 5000
app.run(host='127.0.0.1', port=5000)