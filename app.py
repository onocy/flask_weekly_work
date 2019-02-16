from flask import request, render_template, Flask
from flask_sqlalchemy import SQLAlchemy
from email.mime.text import MIMEText
import smtplib

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@localhost/work'
db = SQLAlchemy(app)


class Data(db.Model): 
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120))
    time=db.Column(db.Integer)

    def __init__(self, email_, time_):
        self.email_=email_
        self.time=time_

@app.route("/")
def index(): 
    return render_template("index.html")

@app.route("/success", methods = ["POST"])
def success(): 
    if request.method == 'POST':
        email = request.form['email_name']
        print(email)
        print(type(email))
        time = request.form['time_name']
        data = Data(email, time)
        db.session.add(data)
        db.session.commit()
        send_email(email, time)
        return render_template("success.html")
    return render_template("index.html")


def send_email(email, time):
    from_address = "your_email@gmail.com"
    body = "Today you have worked <br>%s</br> hours" % (time)
    message = MIMEText(body, 'html')
    message['Subject'] = "Daily Hours"
    message['To'] = email
    message['From'] = from_address

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_address, "password")
    print('sending email...')


if __name__ == '__main__': 
    app.debug = True
    app.run()