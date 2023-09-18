from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:///myregistration.db'  # MYSQL database

db = SQLAlchemy(app)

class User (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80))
    lname = db.Column(db.String(80))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(80))
    pin = db.Column(db.String(80))
    
@app.route('/')
def user():
    users = User.query.all()
    return render_template('regpage.html', users=users)

@app.route('/', methods=['POST'])
def add_user():
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    phone = request.form['phone']
    pin = request.form['pin']
    user = User(fname=fname, lname=lname, email=email, phone=phone, pin=pin)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('regpage'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
