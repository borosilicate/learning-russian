import easygui 
import pandas as pd
import numpy as np
import glob
import random
title="Time to Study!"
lists=('codenames','city','family','animals','kitchen','nature','professions')
path = '~/Downloads/unsplash-research-dataset-lite-latest/'
documents = ['photos', 'keywords', 'collections', 'conversions', 'colors']
datasets = {}
'''
for doc in documents:
  print(doc)
  files = [path + doc + ".tsv000"]
  print(files,"files")
  subsets = []
  #print(filename,"filename")
  df = pd.read_csv(files[0], sep='\t', header=0)
  print(df,"df")
  subsets.append(df)
  datasets[doc] = pd.concat(subsets, axis=0, ignore_index=True)

print(datasets['photos'].head())
datasets['keywords'].head()
datasets['collections'].head()
datasets['conversions'].head()
datasets['colors'].head()
'''

temp=easygui.multchoicebox("Pick the lists to study",title,lists)
here=[]
for lists in temp:
    here+=pd.read_csv('CSVs/'+lists+'.csv', sep=',',header=None)
df=pd.concat(here)
print(df.head)    
size=len(df)

while(True):
    word=random.randint(0, size)
    a=word
    b=0
    c=0
    while(a==word or b==word or c==word or (a==b or b==c or c==a)):
        a=random.randint(0, size)
        b=random.randint(0, size)
        c=random.randint(0, size)
        d=random.randint(0, size)
    r_ans=df.values[word,0]
    e_ans=df.values[word,1]
    e_a=df.values[a,1]
    e_b=df.values[b,1]
    e_c=df.values[c,1]
    e_d=df.values[d,1]
    tup =(e_a,e_b,e_c,e_d,e_ans) 
    l = list(tup)
    random.shuffle(l)
    tup=tuple(l)
    image="./pictures/"+e_ans+".jpg"
    out=easygui.buttonbox('Click on the word '+r_ans, image=image, choices=tup) 
    print(out,"  ",e_ans)
    if(out==e_ans):
        print('Great Job:'+r_ans+"  = "+out)
    else:
        print('Nice  Try:'+r_ans+" == "+e_ans+"    Not "+out)
