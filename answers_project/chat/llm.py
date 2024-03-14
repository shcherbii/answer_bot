from langchain_community.document_loaders.generic import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain import hub
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI


openai_api_key="change me"


def load_queryset_data(queryset):
    texts = [obj.file_text for obj in queryset]
    return texts

def load_data_from_queryset(queryset):
    documents = [Document(page_content=text) for text in load_queryset_data(queryset)]

    return documents

def load_data(queryset):
    documents = load_data_from_queryset(queryset)
    return documents


def data_split(data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 0)
    all_splits = text_splitter.split_documents(data)

    return all_splits


def store_splits(queryset):
    data = load_data(queryset)
    splits = data_split(data)
    openai = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vectorstore = Chroma.from_documents(documents=splits, embedding=openai)

    return vectorstore


def save_vector(queryset, user):
    data = load_data(queryset)
    splits = data_split(data)
    openai = OpenAIEmbeddings(openai_api_key=openai_api_key)

    Chroma.from_documents(splits, openai, persist_directory=f'vectorstore/{user}_db')


def get_vector(user):
    openai = OpenAIEmbeddings(openai_api_key=openai_api_key)

    return Chroma(persist_directory=f'vectorstore/{user}_db',  embedding_function=openai)


def get_rag_promt():
    prompt = hub.pull("rlm/rag-prompt")
    return prompt



def get_llm(vectorstore, prompt):
    llm = ChatOpenAI(model_name="gpt-3.5-turbo-0613", openai_api_key="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")

    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=vectorstore.as_retriever(),
        chain_type_kwargs={"prompt": prompt}
    )
    return qa_chain

def crate_llm(queryset):
    data = load_data(queryset)
    split = data_split(data)
    vectorstore = store_splits(split)
    prompt = get_rag_promt()
    model = get_llm(vectorstore, prompt)

    return model

