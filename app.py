from datetime import datetime

from flask import Flask, render_template, request, redirect, \
    jsonify, flash, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import ContactUs, Base

app = Flask(__name__)

# Connect to Database and create database session
engine = create_engine('sqlite:///almozaini_website.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def homepage():
    return render_template(
        'index.html',
        title='Almozaini &#8211; The Real, Real Estate Developer',
        current_year=datetime.today().year
    )


@app.route('/contact-us', methods=['GET', 'POST'])
def contact_us():
    if request.method == 'POST':
        new_contact_us = ContactUs(
            name=request.form['name'],
            title=request.form['title'],
            message=request.form['message'],
        )
        session.add(new_contact_us)
        flash('Message successfully sent')
        session.commit()
        return redirect(url_for('contact_us'))
    else:
        return render_template(
            'contact-us.html',
            title='Contact Us',
            current_year=datetime.today().year
        )


@app.route('/contacts')
def contacts():
    return render_template(
        'contacts.html',
        title='Contacts',
        contacts=session.query(ContactUs),
        current_year=datetime.today().year
    )


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000, threaded=False)
