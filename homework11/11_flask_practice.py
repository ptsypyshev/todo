from random import randint, seed
from simple_settings import settings
from flask import Flask, request, render_template
from flask_wtf import FlaskForm, Form
from wtforms import  IntegerField, validators


class ContactForm(FlaskForm):
    guess = IntegerField(label='Guess number', validators=[
        validators.NumberRange(min=1, max=100, message='Test numberrange')
    ])


app = Flask(__name__)
app.config.update(
    **settings.as_dict()
    # DEBUG=True,
    # SECRET_KEY='This key must be secret!',
    # WTF_CSRF_ENABLED=False,
    # NUM = randint(1, 101)
)


@app.route('/', methods=['GET'])
def home():
    return render_template(
        'home_template.html', status="GET"
    )


@app.route('/guess', methods=['GET', 'POST'])
def guess():
    if request.method == 'POST':
        print(request.form)
        form = ContactForm(request.form)
        print(form.validate())

        if form.validate():
            if app.config['NUM'] < form.guess.data:
                compare = '<'
            elif app.config['NUM'] > form.guess.data:
                compare = '>'
            else:
                compare = '='

            if compare == '=':
                app.config['NUM'] = randint(1, 101)
                return render_template(
                    'congrats.html', status=f' Оно {compare} {form.guess.data}',
                    form=form,
                )
            else:
                return render_template(
                    'home_template.html', status=f' Оно {compare} {form.guess.data}',
                    form=form,
                )
        else:
            return 'invalid', 400

    if request.method == 'GET':
        return render_template(
            'home_template.html', status="GET"
        )


if __name__ == '__main__':
    print(app.config['FLASK_RANDOM_SEED'])
    seed(app.config['FLASK_RANDOM_SEED'])
    app.config['NUM'] = randint(1, 101)
    app.run()