from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import DirectoryLoader
from langchain.vectorstores import Chroma, Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
import os
import pinecone

API='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'
def get_answer(API):
    pinecone.init(
        api_key="dbc3319f-4371-4224-983c-bf7330325dc8",
        environment="northamerica-northeast1-gcp"
    )
    os.environ["OPENAI_API_KEY"] = API
    loader = DirectoryLoader('./content/', glob='**/*.txt')
    # 将数据转成 document 对象，每个文件会作为一个 document
    documents = loader.load()
    # 初始化加载器
    text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
    # 切割加载的 document
    split_docs = text_splitter.split_documents(documents)
    index_name="test"
    embeddings = OpenAIEmbeddings()
    # 持久化数据
    docsearch = Pinecone.from_texts([t.page_content for t in split_docs], embeddings, index_name=index_name)
    query = "算力和经济发展有什么关系？"
    docs = docsearch.similarity_search(query, include_metadata=False)
    llm = OpenAI(temperature=0)
    chain = load_qa_chain(llm, chain_type="stuff", verbose=False)
    return chain.run(input_documents=docs, question=query)
