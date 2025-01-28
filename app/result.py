class Result:
    def __init__(self):
        pass

    @staticmethod
    def success(content = None):
        if content is not None:
            return {
                "code": 1,
                "content": content,
                "message": 'success'
            }
        else:
            return {
                "code": 1,
                "message": 'success'
            }     
        
    @staticmethod
    def error():
        return {
            "code": 0,
            "message": 'fail'
        }
