from .. import main
from flask import render_template, redirect, flash, url_for


@main.route('/')
@main.route('/index')
def index():
    """
    Function for rendering the root page.
    """
    return render_template('index.html')


