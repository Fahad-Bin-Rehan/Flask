from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///firstapp.db"
with app.app_context():
    db = SQLAlchemy(app)
    
    
class Firstapp(db.Model):
    sno = db.Column(db.Integer, primary_key = True, autoincrement = True)
    fname = db.Column(db.String(100), nullable = False)
    lname = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False)
    
    def __repr__(self):
        return f"{self.sno} {self.fname}"
    
        
@app.route('/', methods = ['GET','POST'])
def hello_world():
    if request.method=="POST":
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        if fname and lname and email:
            firstapp = Firstapp(fname=fname,lname=lname, email = email)
            db.session.add(firstapp)
            db.session.commit()
    
    allpeople = Firstapp.query.all()
    print(allpeople)
    return render_template('Index.html',allpeople=allpeople)
    #return 'Hello, World!'

@app.route('/home')
def home():
	return 'Welcome to the Home Page'

if __name__ == "__main__":
	app.run(debug=True)