import projects
from flask import Flask, render_template
#from flask_sqlalchemy import SQLAlchemy 

#create a Flask instance
app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI']

#connects default URL to a function
@app.route('/')
def home():
    #Flask import uses Jinga to render HTML
    return render_template("home.html")

@app.route('/amazon')
def amazon(): 
  return render_template("amazon.html")
  
@app.route('/testing')
def testing():
  return render_template("testing.html")

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='3000', host='0.0.0.0')

## hi
