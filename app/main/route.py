from flask import render_template, url_for, Blueprint
from app.Posts.forms import ComplaintsForm
from app.models import Notice,Complaints
from sqlalchemy import asc, desc

main= Blueprint('main',__name__)

@main.route('/')
def home():
    # All pitches here
    notice=Notice.query.order_by(desc(Notice.date_created)).all()
    complaint=Complaints.query.order_by(desc(Complaints.date_created)).all()

    return render_template('home.html',notice=notice,complaint=complaint)





