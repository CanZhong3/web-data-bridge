from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,template_folder="flaskbridge/templates",
            static_folder="flaskbridge/static")
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.ukzurcfeoofrbmkvhrkl:sian060116@aws-0-us-east-1.pooler.supabase.com:6543/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(20), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    snippet = db.Column(db.Text, nullable=False)
    from_ = db.Column(db.String(100), nullable=False)
    to = db.Column(db.String(100), nullable=False, default='sian060116@gmail.com')

    def __repr__(self):
        return f"Post('{self.subject}', '{self.date_posted}')"


@app.route("/")
@app.route("/home")
def home():
    emails = Email.query.order_by(Email.date_posted.desc()).all()
    return render_template('home.html', emails=emails)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
