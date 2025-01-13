from flask import jsonify
from flask_httpauth import HTTPBasicAuth
from app.models.user import User

auth = HTTPBasicAuth()

# Simulasi database
users = {
    "admin": User("admin", "secret")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username].check_password(password):
        return username

class AuthViews:
    @staticmethod
    def public():
        return jsonify({"message": "Ini adalah endpoint publik"})
    
    @staticmethod
    @auth.login_required
    def private():
        return jsonify({
            "message": "Ini adalah endpoint private",
            "user": auth.current_user()
        })