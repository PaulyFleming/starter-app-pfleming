from flask import Flask, request, render_template 
import os 

app = Flask(__name__)

development = os.environ.get('DEVELOPMENT')

# Define routes and methods here
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


# Run the flask app
if __name__ == '__main__':
    app.run() 

