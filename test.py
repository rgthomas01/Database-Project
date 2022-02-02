from flask import Flask
import os

# Configuration

app = Flask(__name__)

# Routes 

@app.route('/')
def root():
    return "Welcome to Three Eight Cycles"

# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3838)) 
    #                                 ^^^^
    #              You can replace this number with any valid port
    
    app.run(port=port, debug = True) 