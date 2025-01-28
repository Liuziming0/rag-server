from app.model_integration import get_model_chain


# def openapiGenerateService(data):
#     model_name = data['model']
#     messages = [ModelConfig.INS] + data['messages']
#     print(f"data:{data}")
#     chat_completion = client.chat.completions.create(
#         model = model_name,
#         messages = messages  
#     )
#     response = chat_completion.choices[0].message.content
#     print(f"reponse:{response}")
#     return response
class ChatService:
    @staticmethod
    def ragGenerateService(data):
        chain = get_model_chain()
        print(data)
        print(data['content'])
        output = chain.invoke(data['content'])
        return output


