import requests
import os,json
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import joblib 

def create_embedding(text_list):
    r = requests.post("http://localhost:11434/api/embed",
                    json={
                        'model':'bge-m3',
                        'input':text_list
                    })

    embedding = r.json()['embeddings']
    return embedding

json_lists = os.listdir('newjsons')
chunk_id = 0
embed_dicts = []


for json_files in json_lists:
    with open(f'newjsons/{json_files}','r') as f:
        content = json.load(f)
    embeddings = create_embedding([c['text'] for c in content['chunks']])  
    print(f'Embedding created for {json_files}')
    for i,chunk in enumerate(content['chunks']): 
        chunk['chunk_id'] = chunk_id
        chunk['embedding'] = embeddings[i]
        chunk_id +=1
        embed_dicts.append(chunk)

df = pd.DataFrame.from_records(embed_dicts)
joblib.dump(df,'embedding.joblib')

