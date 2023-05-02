import os
os.environ['OPENAI_API_KEY'] = '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'


from llama_index import GPTSimpleVectorIndex, Document, SimpleDirectoryReader
documents = SimpleDirectoryReader('data').load_data()
index = GPTSimpleVectorIndex(documents)
index.save_to_disk('index.json')

# Bonus (Not required in the code, but for optimisation)
# Read the index.json later on for doing the indexation only once (#MoneySaving)
index = GPTSimpleVectorIndex.load_from_disk('index.json')

print(index.query("¿Cuáles son los artefactos de Scrum?"))