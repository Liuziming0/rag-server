# from langchain_community.document_loaders import WebBaseLoader
# from app.models import get_chat_openai,get_openai_embedding,get_prompt


# import bs4
# from langchain_chroma import Chroma
# from langchain_community.document_loaders import WebBaseLoader, PyMuPDFLoader
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.runnables import RunnablePassthrough
# from langchain_openai import OpenAIEmbeddings
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_core.prompts import PromptTemplate


# def loader_test():
#     model = get_chat_openai()

#     embedding = get_openai_embedding()

#     loader = WebBaseLoader(
#         web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",
#                    "https://baike.baidu.com/item/街头霸王6/57343271",
#                    "https://baike.baidu.com/item/拳皇/62260")
#     )

#     # loader = PyMuPDFLoader("./knowledge/Retrieval-Augmented Generation for Large Language Models A Survey.pdf")
#     docs = loader.load()
#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
#     split = text_splitter.split_documents(docs)
#     vectorstore = Chroma.from_documents(documents=split, embedding=embedding)


#     retriever = vectorstore.as_retriever()

#     prompt = get_prompt()

#     def format_docs(docs):
#         return "\n\n".join(doc.page_content for doc in docs)

#     rag_chain = (
#         {"question": RunnablePassthrough(), "context": retriever | format_docs}
#         | prompt
#         | model
#         | StrOutputParser()
#     )
#     print(rag_chain.invoke("拳皇是什么"))

# loader_test()


# from datasets import load_dataset, load_from_disk


# def data_test():
#     path_dataset = "./knowledge/dataset/wiki/"
#     ds = load_from_disk(path_dataset)
#     ds_train = ds['train']
#     print(type(ds_train))
#     print(len(ds_train))

# data_test()

from app.service.chatService import ChatService


if __name__ == "__main__":
    data = {
        'content': 'Which newspaper did Jackie Kennedy work for just before her marriage?'
    }
    print(ChatService.ragGenerateService(data))


# {
#     "aliases": [ 
#         "(Harry) Sinclair Lewis", "Harry Sinclair Lewis", "Lewis, (Harry) Sinclair", "Grace Hegger", "Sinclair Lewis" 
#     ], 
#     "normalized_aliases": [ 
#         "grace hegger", "lewis harry sinclair", "harry sinclair lewis", "sinclair lewis" 
#     ],
#     "matched_wiki_entity_name": "",
#     "normalized_matched_wiki_entity_name": "", 
#     "normalized_value": "sinclair lewis", 
#     "type": "WikipediaEntity", 
#     "value": "Sinclair Lewis" 
# }