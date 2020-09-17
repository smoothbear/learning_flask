from flask import Blueprint, url_for, request

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/register')
def _register():
    return "Hello"

