from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

form_page = Blueprint('form_page', __name__,
                        template_folder='templates')

form_page.route('/form/<page>')
def show(page):
    try:
      
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)