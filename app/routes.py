from flask import Blueprint, jsonify, request
from app.result import Result
from app.service.chatService import ChatService
from app.service.userService import UserService
from app.service.historyService import HistoryService


main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def connect_test():
    return 'success'

# @main_bp.route('/api/generate/openapi', methods=['POST'])
# def generate_openapi():
#     if request.method == 'POST':
#         try:
#             result = chatService.openapiGenerateService(request.get_json())
#             return jsonify(Result.success(result))
#         except Exception as e:
#             print(f"error:{e}")
#             return jsonify(Result.error())
        

@main_bp.route('/api/generate/rag', methods=['POST'])
def generate_rag():
    if request.method == 'POST':
        try:
            result = HistoryService.ragGenerateService(request.get_json())
            return jsonify(Result.success(result))
        except Exception as e:
            print(f"error:{e}")
            return jsonify(Result.error())
        

@main_bp.route('/api/user/login', methods=['POST'])
def login():
    if request.method == 'POST':
        try:
            data = request.get_json()
            user_name = data['user_name']
            pwd = data['password']
            user = UserService.login(user_name, pwd)
            if user == None:
                return jsonify(Result.error('user not found'))
            return jsonify(Result.success())
        except Exception as e:
            print(f"error:{e}")
            return jsonify(Result.error())         
        

@main_bp.route('/api/history/get/{user_id}', methods=['GET'])
def history_get(user_id):
    if request.method == 'GET':
        try:
            history = HistoryService.get_history(user_id)
            return jsonify(Result.success(history))
        except Exception as e:
            print(f"error:{e}")
            return jsonify(Result.error())     
            
@main_bp.route('/api/history/del/{history_id}', methods=['DELETE'])
def history_del(history_id):
    if request.method == 'DELETE':
        try:
            HistoryService.del_history(history_id)
            return jsonify(Result.success())
        except Exception as e:
            print(f"error:{e}")
            return jsonify(Result.error())  