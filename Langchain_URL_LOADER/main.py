import os
import streamlit as st
import langchain
import magic
from apikey import apikey
from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import CharacterTextSplitter
import pickle 
import faiss
from langchain.indexes import VectorstoreIndexCreator
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.question_answering import load_qa_chain
from langchain import OpenAI
from langchain.document_loaders import CSVLoader
from langchain.chains import RetrievalQA

#KEYS 
os.environ['OPENAI_API_KEY'] = apikey

urls = [
    ''
]

loaders = UnstructuredURLLoader(urls=urls ,continue_on_failure=False, headers={"User-Agent": "value"}) 
data = loaders.load()

#text splitter
text_splitter = CharacterTextSplitter(separator='\n', chunk_size=1000, chunk_overlap=200)
docs = text_splitter.split_documents(data)

embeddings = OpenAIEmbeddings()
vector_openAI= FAISS.from_documents(docs, embeddings)

with open("faiss_store_openai.pkl" , "wb") as f:
    pickle.dump(vector_openAI, f)

with open("faiss_store_openai.pkl", "rb") as f:
    VectorStore = pickle.load(f)

llm=OpenAI(temperature=0.5,model_name='text-davinci-003')
chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=VectorStore.as_retriever())

# Streamlit app
st.title("Question-Answering with OpenAI")

user_input = st.text_input("Enter your question here:", '')
if st.button('Send'):
    if user_input:
        response = chain({"question": user_input}, return_only_outputs=True)
        st.text_area("Response:", value=response, height=200, max_chars=None, key=None)
    else:
        st.write("Please enter a question.")
