import os
import json
import pandas as pd
from tqdm import tqdm

'''
    READING FILES
'''

dirs = ["biorxiv_medrxiv"]

docs = []
for d in dirs:
    print(d)
    for file in tqdm(os.listdir(f"{d}/{d}")):
        file_path = f"{d}/{d}/{file}"
        j = json.load(open(file_path,"rb"))
   
        title = j['metadata']['title']
        try:
            abstract = j['abstract']
        except:
            abstract = ""

        full_text = ""
        for text in j['body_text']:
            full_text += text['text']+'\n\n'

        # print(full_text)
        docs.append([title,abstract,full_text])
        # break
df = pd.DataFrame(docs,columns=['title','abstract','full_text'])
# print(df.head())

incubation = df[df['full_text'].str.contains('incubation')]
# print(incubation.head(10))

texts = incubation['full_text'].values

for t in texts:
    # print(t)
    for sentence in t.split('. '):
        if 'incubation' in sentence:
            print(sentence)
        
    break