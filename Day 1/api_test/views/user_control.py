from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/user/register')
def user_register():
    return 'hello world!'

