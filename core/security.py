import bcrypt

def hash_password(password:str) -> str:
    try:
        return bcrypt.hashpw(password.encode("utf-8"),bcrypt.gensalt()).decode()
    except Exception as e:
        return str(e)

def verfiy_password(password:str, hashed_password:str) -> bool:
    try:
        return bcrypt.checkpw(password.encode("utf-8"),hashed_password.encode("utf-8"))
    except Exception as e:
        return str(e)