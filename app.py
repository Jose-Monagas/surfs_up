# Import Flask
from flask import Flask

# Create a new Flask App Instance
app = Flask(__name__)

# Create Flask route
@app.route('/')
def hello_world():
    return 'Hello world'

