from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

url="https://www.flipkart.com/hp-15-i5-14th-gen-intel-core-5-120u-16-gb-512-gb-ssd-windows-11-home-15-fd0640tu-15-fd0682tu-15-fd0746tu-thin-light-laptop/p/itm1c0ebc1fda7cf?pid=COMHDZVEH5XGAYBF&lid=LSTCOMHDZVEH5XGAYBFBGQQHG&marketplace=FLIPKART&store=6bo%2Fb5g&srno=b_1_1&otracker=browse&fm=organic&iid=5ba83ed9-23dd-4f9b-82f7-ebf481e10cfc.COMHDZVEH5XGAYBF.SEARCH&ppt=None&ppn=None&ssid=qivjl2r58g0000001792240148453&ov_redirect=true"

loader =WebBaseLoader(url)

docs = loader.load()

load_dotenv()

model = ChatGroq(
    model="qwen/qwen3.8-27b"
)

prompt = PromptTemplate(
    template="write the answer to the question: {question} based on the text: {input_text}",
    input_variables=["input_text", "question"]
)

parser = StrOutputParser()


chain = prompt | model | parser

print(chain.invoke({"input_text": docs[0].page_content, "question": "What is the product name?"}))
# print(len(docs))
# print(docs[0].page_content) 