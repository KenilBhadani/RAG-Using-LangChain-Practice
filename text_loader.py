from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="qwen/qwen3.8-27b"
)

prompt = PromptTemplate(
    template="write a summary  from the text: {input_text}",
    input_variables=["input_text"]
)

parser = StrOutputParser()

loader = TextLoader('myself.txt', encoding='utf-8')

documents = loader.load()

# print(documents)

# print(len(documents))

# print(type(documents))

# print(documents[0])

chain = prompt | model | parser

print(chain.invoke({"input_text": documents[0].page_content}))