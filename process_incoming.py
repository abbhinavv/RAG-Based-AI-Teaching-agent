import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import requests,joblib


df = joblib.load('embedding.joblib')

def create_embedding(text_list):
    r = requests.post("http://localhost:11434/api/embed",
                    json={
                        'model':'bge-m3',
                        'input':text_list
                    })

    embedding = r.json()['embeddings']
    return embedding

def inference(prompt):
    r = requests.post("http://localhost:11434/api/generate", json={
        "model": "phi4-mini",
        "prompt": prompt,
        "stream": False
    })

    response = r.json()
    return response

user_query = input('What is the query today: ')
query_embedded = create_embedding([user_query])[0]

similarities = cosine_similarity(np.vstack(df['embedding']),[query_embedded]).flatten()
no_of_results = 7
top_indexes = similarities.argsort()[::-1][0:no_of_results]

matched_df = df.loc[top_indexes]

prompt = f'''I am teaching web development in my Sigma web development course. Here are video subtitle chunks
 containing video title, video number, start time in seconds, end time in seconds, the text at that time:

{matched_df[["name", "number", "start", "end", "text"]].to_json(orient="records")}
---------------------------------
"{user_query}"
User asked this question related to the video chunks, you have to answer in a human way (dont mention the above
 format, its just for you) where and how much content is taught in which video (in which video and at what timestamp)
   and guide the user to go to that particular video.Exact timestamps (convert seconds to minutes and seconds). If user asks unrelated question, tell him that you can only 
   answer questions related to the course
'''
with open("prompt.txt", "w") as f:
    f.write(prompt)

response = inference(prompt)["response"]
print(response)

with open("response.txt", "w") as f:
    f.write(response)

# print(matched_df[['name','number','text']])

# for index,item in matched_df.iterrows():
#     print(index,item['name'] , item['number'] , item['text'], item['start'], item['end'])