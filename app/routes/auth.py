from flask import Blueprint, jsonify
from flask_httpauth import HTTPBasicAuth
from app.models.user import User

auth_bp = Blueprint('auth', __name__)
auth = HTTPBasicAuth()

# Simulasi database
users = {
    "admin": User("admin", "secret")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username].check_password(password):
        return username

@auth_bp.route('/public')
def public():
    return jsonify({"message": "Ini adalah endpoint publik"})

@auth_bp.route('/private')
@auth.login_required
def private():
    return jsonify({
        "message": "Ini adalah endpoint private",
        "user": auth.current_user()
    })
