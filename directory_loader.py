from langchain_community.document_loaders import PyPDFLoader , DirectoryLoader

loader= DirectoryLoader(
    path="collection",
    glob='*.pdf',
    loader_cls=PyPDFLoader
) 

docs = loader.load()

print(len(docs))

print(docs[1].page_content)
print(docs[1].metadata)