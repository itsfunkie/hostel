from flask import Blueprint
apiobj = Blueprint('bpapi', __name__, template_folder='templates', static_folder='static',url_prefix='/api/v1.0')

from . import apiroutes