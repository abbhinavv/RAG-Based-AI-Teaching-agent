import os,json,math

n = 5

for filename in os.listdir('jsons'):
    if filename.endswith('.json'):
        filepath = os.path.join('jsons',filename)
        with open(filepath,'r',encoding='utf-8') as f:
            data = json.load(f)
            new_chunks = []
            num_chunks = len(data['chunks'])
            num_groups = math.ceil(num_chunks/n)

            for group in range(num_groups):
                start_indx = group * n
                end_indx = min((group+1) * n , num_chunks)
                chunk_group = data['chunks'][start_indx:end_indx]

                new_chunks.append({
                    "number" : data['chunks'][0]['number'],
                    "name" : chunk_group[0]['name'],
                    "start" : chunk_group[0]['start'],
                    "end" : chunk_group[-1]['end'],
                    "text" : " ".join(c['text'] for c in chunk_group)
                })

            # Saving file
            os.makedirs('newjsons',exist_ok=True)
            with open(os.path.join("newjsons",filename),'w',encoding='utf-8') as json_file:
                json.dump({"chunks":new_chunks, "text":data['text']},json_file,indent=4)
