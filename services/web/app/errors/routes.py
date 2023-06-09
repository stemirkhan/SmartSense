from flask import render_template

from . import bp_errors


@bp_errors.app_errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@bp_errors.app_errorhandler(500)
def page_not_found(e):
    return render_template('errors/500.html'), 500

