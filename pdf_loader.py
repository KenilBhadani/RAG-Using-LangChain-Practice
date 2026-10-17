# for scanned images pdf go for unstructured pdf loader
# for table/columns pdf go for pdflumber loader


from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader('sample.pdf')

docs = loader.load()

# print(docs)

print(len(docs))

print(docs[0].page_content)
print(docs[0].metadata)