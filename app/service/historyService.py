from app.database import db

class HistoryService:
    collection = db['history']

    def get_history(self, user_id):
        history = self.collection.find({
            'user_id': user_id
        })

    def del_history(self, history_id):
        self.collection.delete_one({
            '_id': history_id
        })

    def create_history(self, user_id):
        history = self.collection.insert_one({
            'user_id': user_id,
            'messages': []
        })
        # return history.inserted_id
