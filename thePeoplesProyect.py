from flask import Flask, render_template, url_for

thePeoplesProyect = Flask(__name__)

@thePeoplesProyect.route('/')
def home():
    return render_template('index.html')

@thePeoplesProyect.route('/api')
def api():
    return {
        "name": "thePeoplesProyect",
        "version": "1.0.0",
        "description": "A simple API for the people"
    }

if __name__ == '__main__':
    thePeoplesProyect.run(debug=True, port=3300)