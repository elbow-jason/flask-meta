from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

form_page = Blueprint('form_page', __name__,
                        template_folder='templates')

@form_page.route('/<page>')
def show(page):
    try:
        form = AppForms.query.filter_by(name=page).first()
        return render_template('form.html' form=form)
    except TemplateNotFound:
        abort(404)