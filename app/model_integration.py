import bs4
import os
from langchain_openai import ChatOpenAI
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader,PyMuPDFLoader
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from openai import OpenAI
from app.model_config import ModelConfig

current_directory = os.getcwd()
collection_name = "rag_db_text"
persist_directory = os.path.join(current_directory, "knowledge\\database")
path_dataset = os.path.join(current_directory, "knowledge\\dataset\\wiki")


# def get_gpt_api_model():
#     model = OpenAI(
#         api_key=ModelConfig.API_KEY,
#         base_url=ModelConfig.REQUEST_URL
#     )
#     return model


def get_model(model_name=None, model_type=None): 
    if model_name == None:
        model_name = ModelConfig.MODEL
    if model_type == None:
        model_type = 'gpt'
    if model_type == 'gpt':
        return ChatOpenAI(
            api_key=ModelConfig.API_KEY,
            base_url=ModelConfig.REQUEST_URL,
            model=model_name,
            temperature=0
        )
    return None


def get_embedding(embedding_name = 'bge'):
    if embedding_name == 'bge':
        return HuggingFaceBgeEmbeddings(
            model_name=ModelConfig.MODEL_PATH,
            model_kwargs={'device': ModelConfig.DEVICE},
            encode_kwargs={'normalize_embeddings': True}
        )
    elif embedding_name == 'openai':
        return OpenAIEmbeddings(
            openai_api_key=ModelConfig.API_KEY,
            base_url=ModelConfig.REQUEST_URL
        )
    return None


def get_prompt(template = ModelConfig.TEMPLATE):
    prompt = PromptTemplate(
        template=template
    )
    return prompt

vectorstore = Chroma(
    persist_directory=persist_directory, 
    collection_name=collection_name,
    embedding_function=get_embedding()
)
def get_retriever(doc_k = None):
    if doc_k == None:
        doc_k = ModelConfig.DOC_K
    retriever = vectorstore.as_retriever(
        search_kwargs={'k': doc_k}
    )
    return retriever


def get_model_chain(
    model_name = None,
    doc_k = None
):
    retriever = get_retriever(doc_k)
    prompt = get_prompt()
    model = get_model(model_name)
    output_parser = StrOutputParser()
    
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)
    
    rag_chain = (
        {"question": RunnablePassthrough(), "context": retriever | format_docs}
        | prompt
        | model
        | output_parser
    )
    return rag_chain


