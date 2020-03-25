from flask import Flask, request

# pip install flask-WTF
from flask_wtf import FlaskForm, Form
from wtforms import DateField, StringField, validators, ValidationError
import datetime


class JobValid(Form):
    job = StringField('Job')

    def validate_job(form, field):
        avail_list = ['IT', 'Bank', 'HR']
        if field not in avail_list:
            raise ValidationError('Job must be IT, Bank or HR')


class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[
        validators.Length(min=4, max=25)
    ])
    email = StringField(label='E-mail', validators=[
        validators.Length(min=6, max=35), validators.Email()
    ])

    job = StringField(label='Job', validators=[
        validators.DataRequired(),
    ])

    birthday = DateField(label='Birthday', validators=[
        validators.DataRequired(),
    ])

    def validate_job(self, job):
        avail_list = ['IT', 'Bank', 'HR']
        if job.data not in avail_list:
            raise ValidationError('Job must be IT, Bank or HR')

    def validate_birthday(self, birthday):
        bd_month = birthday.data.month
        cur_month = datetime.datetime.now().month
        if bd_month != cur_month:
            raise ValueError('Your birthday not in current month.')


app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.form)
        form = ContactForm(request.form)
        print(form.validate())

        if form.validate():
            return ('valid', 200)
        else:
            return ('invalid', 400)

    if request.method == 'GET':
        return 'hello world!', 200

if __name__ == '__main__':
    app.run()
