from flask_wtf import FlaskForm
from wtforms import fields, validators
from wtforms_alchemy import ModelForm

from models import GuestBookItem


class GuestBookItemForm(ModelForm):
    class Meta:
        model = GuestBookItem