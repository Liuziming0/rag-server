from app.database import db

class UserService:
    collection = db['user']

    def login(self, user_name, pwd):
        user = self.collection.find({
            "user_name": user_name,
            "pwd": pwd
        })
        return user