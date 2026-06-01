#!/usr/bin/python3
import hashlib

class User:
    def __init__(self, name, password=None):
        self.name = name
        if password is not None:
            self.password = self.__encrypt(password)
        else:
            self.password = None

    def __encrypt(self, password):
        """Encrypt password using SHA256"""
        return hashlib.sha256(password.encode()).hexdigest()

    def is_valid_password(self, password):
        """Check if provided password matches stored hash"""
        if self.password is None:
            return False
        return self.password == self.__encrypt(password)


if __name__ == "__main__":
    print("Test User")
    user = User("Test User", "Password123")
    assert user.is_valid_password("Password123")
    assert not user.is_valid_password("WrongPassword")
    print("is_valid_password should return True if it's the right password")
