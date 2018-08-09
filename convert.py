import os
import pandas as  pd
import shutil


treino = []

gs = 'gs://{seu-projeto}-vcm/imgs/carros/'

for root, dirs, files in os.walk("."):  
    for filename in files:
        if filename.endswith(".jpg") :
            treino.append((gs + root.split('/')[-1].replace(" ", "_")+ '/' + filename ,  root.split('/')[-1]))

pd.DataFrame(treino).to_csv('train.csv', index=False, header=False)
