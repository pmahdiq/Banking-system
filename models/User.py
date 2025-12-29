class User:
    def __init__(self, name, username, age, number, email, hashed_password = ""):
        self.name = name
        self.username = username
        self.age = age
        self.number = number
        self.email = email
        self.hashed_password = hashed_password
    
        