from llama_index import download_loader
from dotenv import load_dotenv
from llama_index import VectorStoreIndex, ServiceContext
from llama_index.llms import MistralAI

load_dotenv()

URL = "https://buchkodex.de/blog/verben/"

BeautifulSoupWebReader = download_loader("BeautifulSoupWebReader")
loader = BeautifulSoupWebReader()
documents = loader.load_data(urls=[URL])

service_context = ServiceContext.from_defaults(llm=MistralAI())
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine(service_context=service_context)

query = "What is this web page about?"
response = query_engine.query(query)
print(f"RESPONSE:\n{response}")

query = "What is one interesting fact about the website?"
response = query_engine.query(query)
print(f"RESPONSE:\n{response}")