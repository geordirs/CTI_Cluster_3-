from passlib.context import CryptContext

# Configuración del contexto de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

print("Hashed 'grdy':", hash_password("grdy"))
print("Hashed 'user':", hash_password("user"))
