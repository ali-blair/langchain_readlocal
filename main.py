"""

Code for conversion of .pdf, .txt or .docx into embeddings which are then fed
into GPT4All LLM to allow private Q&A with local data as information for LLM to
read from.

"""

import os
from langchain.text_splitter import CharacterTextSplitter, \
                                    RecursiveCharacterTextSplitter
from langchain.embeddings.gpt4all import GPT4AllEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import GPT4All
from langchain.chains import RetrievalQA
from langchain.document_loaders import DirectoryLoader

model_name = "_____"  # LLM file name, eg: "llama-2-13b-chat.ggmlv3.q5_K_M.bin"
model_path = "_____"  # LLM file directory
os.environ["OPENAI_API_KEY"] = "_____"  # Input OpenAI API Key
full_path = os.path.join(model_path, model_name)


""" Data Ingestion """
file_folder = "_____"  # File directory with documents to read inside
pdf_loader = DirectoryLoader(file_folder, glob="**/*.pdf")
excel_loader = DirectoryLoader(file_folder, glob="**/*.txt")
word_loader = DirectoryLoader(file_folder, glob="**/*.docx")
# Can add further file types ...
loaders = [pdf_loader, excel_loader, word_loader]
documents = []
for loader in loaders:
    documents.extend(loader.load())


""" Chunk and Embeddings - Choose Method of Chunking """
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1050,
                                               chunk_overlap=0)
# text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
documents = text_splitter.split_documents(documents)


""" Generate Embeddings + Insert into Vector Database """
obj = GPT4AllEmbeddings()
vectorstore = FAISS.from_documents(documents, embedding=obj)


""" Introduce LLM """
llm = GPT4All(model=full_path, max_tokens=2048)

# %%

""" Ask the LLM a question, vector database is searched for relevant embeddings
"""
qa_chain = RetrievalQA.from_chain_type(llm,
                                       retriever=vectorstore.as_retriever(),
                                       return_source_documents=True)
question = "_____"  # Insert question to ask
result = qa_chain({"query": question})
result["result"]

""" Alternatively - Can return source documents relating to the question..."""
# result["source_documents"]
