
class ModelConfig:
    API_KEY = 'sk-fU33M065uKd4YJ4H1a9f5aB59b734cF5Ac2c76783e1946C3'
    REQUEST_URL = 'https://api.vveai.com/v1/'
    MODEL = 'gpt-3.5-turbo'
    INS = {
        'role': 'system',
        'content': 'You are a friendly assistant and always ready to help the user.'
    }
    DOC_K = 7
    PATH_MODEL = './models'
    DEVICE = 'cpu'
    MODEL_PATH = './models/bge-m3'
    TEMPLATE = """你是问答任务助手。
    你的回答需要尽可能在上下文中找到依据，特别是触及到健康和利益的
    答案不要过长，只回答问题，不要出现类似于“根据上下文，根据要求”之类的回答
    问题:{question}
    上下文：{context}
    回答：
    """