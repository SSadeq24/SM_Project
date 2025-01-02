from multiprocessing import get_context
from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')

class Hash():
    def bcrypt(password: str):
        return pwd_cxt.hash(password)

    def verify(hashed_password, plain_password):
        return pwd_cxt.verify(plain_password, hashed_password)
    
def hash_password(password: str) -> str:
    return get_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return get_context.verify(plain_password, hashed_password)    