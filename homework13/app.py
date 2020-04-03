from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__, template_folder='templates')
app.config.from_object(config)

db = SQLAlchemy(app)


@app.route('/', methods=['GET'])
def index():
    from models import GuestBookItem

    messages = GuestBookItem.query.all()

    for item in messages:
        author = item.author
        message = item.message
        date = item.date_created
        is_visible = item.is_visible

        if is_visible:
            print(message)

    return render_template('gb.txt', messages=messages)

@app.route('/create', methods=['GET', 'POST'])
def create():
    from models import GuestBookItem
    from forms import GuestBookItemForm

    if request.method == 'POST':
        print(request.form)
        form = GuestBookItemForm(request.form)

        try:
            gb_item = GuestBookItem(**form.data)
            db.session.add(gb_item)
            db.session.commit()

            flash('Message created!')

        except AssertionError as e:
            flash('Form is not valid! Message was not created.')
            flash(str(form.errors))
        return render_template('created.txt')
    return render_template('create.html')


if __name__ == "__main__":
    from models import *
    db.create_all()

    app.run()

