import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hallo There!</h1>"
    
app.run(port=os.getenv('PORT, 8080'), host=int(os.getenv('IP, 0.0.0.0')), debu=True)    