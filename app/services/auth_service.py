from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from datetime import timedelta
from app.models.user import User  # Asegurate de tener este modelo

class AuthService:

    @staticmethod
    def login(email: str, password: str):
        # Buscar el usuario por correo
        user = User.query.filter_by(email=email).first()

        if not user:
            return {"msg": "Usuario no encontrado"}, 404

        # Verificar la contraseña hasheada
        if not check_password_hash(user.password, password):
            return {"msg": "Contraseña incorrecta"}, 401

        # Generar el token JWT
        access_token = create_access_token(
            identity={"id": user.id, "role": user.role},
            expires_delta=timedelta(hours=6)
        )

        return {
            "access_token": access_token,
            "role": user.role,
            "usuario": user.email
        }, 200
