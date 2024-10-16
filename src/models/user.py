class User:
    def __init__(self, user_name, password, email) -> None:
        self.user_name = user_name
        self.password = password
        self.email = email
    
    def toJson(self):
        return {
            'user_name': self.user_name,
            'password': self.password,
            'email': self.email
        }