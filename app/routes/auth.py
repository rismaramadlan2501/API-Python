from flask import Blueprint
from app.views.auth_views import AuthViews, auth

auth_bp = Blueprint('auth', __name__)

auth_bp.route('/public', methods=['GET'])(AuthViews.public)
auth_bp.route('/private', methods=['GET'])(AuthViews.private)