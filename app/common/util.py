from passlib.context import CryptContext


# Password crypt context
password_crypt = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Password has and verify utility
def hash_password(password: str) -> str:
    return password_crypt.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return password_crypt.verify(password, hashed_password)
