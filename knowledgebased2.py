from __future__ import division
import nltk
from nltk.corpus import wordnet as wn
from math import *
sent="the girl is wearing a nice red black top"
text=nltk.word_tokenize(sent)
myword='top'
ls=[]
newls=[]
pairs=[]
ls=nltk.pos_tag(text)
length=len(ls)
sense=[0]*100
dist=[]
newdist=[]
print ls

#newls : only verb,noun,adjective,adverb
# JJ:Adjective NN:Noun VB:Verb RBR:A
val=1
for i in range(0,length,1):
    if ls[i][1]=='JJ' or ls[i][1]=='JJR' or ls[i][1]=='JJS' or ls[i][1]=='NN' or ls[i][1]=='NNS' or ls[i][1]=='NNP' or ls[i][1]=='NNPS' or ls[i][1]=='VB' or ls[i][1]=='VBP' or ls[i][1]=='VBD' or ls[i][1]=='VBG' or ls[i][1]=='VBN' or ls[i][1]=='VBZ' or ls[i][1]=='RB' or ls[i][1]=='RBR' or ls[i][1]=='RBS':
        newls.append(tuple(ls[i]))
        dist.append(val)
        val+=1
print dist

#pairs:all word except the ambiguous word
for i in range(0,len(newls),1):
    if newls[i][0]!=myword:
        pairs.append(newls[i][0])
        newdist.append(dist[i])
    else:
        mydist=dist[i]

print newls
print pairs
print newdist
j=0
level=1
for i in wn.synsets(myword):
    sense[j]=0
    j+=1
index=-1
for word in pairs:
    index+=1
    distance=newdist[index]-mydist
    if distance<0:
        distance=distance*(-1)
    print "distance=",distance
    dictionary=[]
    flag=0
    for i in wn.synsets(word):
        dictionary=dictionary+i.lemma_names()
        for j in i.hypernyms():
            dictionary=dictionary+j.lemma_names()
    k=0
    for i in wn.synsets(myword):
        mydict=[]
        mydict=mydict+i.lemma_names()
        for j in i.hypernyms():
            mydict=mydict+j.lemma_names()
       # print mydict
        mydict=set(mydict)
        dictionary=set(dictionary)
        common=mydict.intersection(dictionary)
        if len(common)>0:   
            flag=1
            score=(len(common)**(1/3))/((1**(1/3))*(distance**(1/3)))
            print k,len(common),score,sense[k],i.definition()
            sense[k]=sense[k]+score
            print k,len(common),score,sense[k],i.definition()

        k+=1
        print common
    for i in range(0,k,1):
        print sense[i],
    print
    print "val of flag is ",flag   
    dictionary=[]
    for i in wn.synsets(word):
        dictionary+=i.lemma_names()
        for j in i.hypernyms():
            dictionary+=j.lemma_names()
            for z in j.hypernyms():
                dictionary+=z.lemma_names()
    k=0
    for i in wn.synsets(myword):
        mydict=[]
        mydict+=i.lemma_names()
        for j in i.hypernyms():
            mydict+=j.lemma_names()
            for z in j.hypernyms():
                mydict+=z.lemma_names()
        mydict=set(mydict)
        dictionary=set(dictionary)
        common=mydict.intersection(dictionary)
        print common
        if len(common)>0:
            flag=1
            score=(len(common)**(1/3))/((2**(1/3))*(distance**(1/3)))
            print k,len(common),score,sense[k],i.definition()
            sense[k]=sense[k]+score
            print k,len(common),score,sense[k],i.definition()
        k+=1
    for i in range(0,k,1):
        print sense[i],
    print
    print "val of flagess is ",flag
    dictionary=[]
    for i in wn.synsets(word):
        dictionary=dictionary+i.lemma_names()
        for j in i.hypernyms():
             dictionary+=j.lemma_names()
             for z in j.hypernyms():
                 dictionary+=z.lemma_names()
                 for y in z.hypernyms():
                     dictionary+=y.lemma_names()
    k=0
    for i in wn.synsets(myword):
        mydict=[]
        mydict+=i.lemma_names()
        for j in i.hypernyms():
            mydict+=j.lemma_names()
            for z in j.hypernyms():
                mydict+=z.lemma_names()
                for y in z.hypernyms():
                    mydict+=y.lemma_names()
        mydict=set(mydict)
        dictionary=set(dictionary)
        common=mydict.intersection(dictionary)
        print common
        if len(common)>0:
            flag=1
            score=(len(common)**(1/3))/((3**(1/3))*(distance**(1/3)))
            sense[k]=sense[k]+score
        k+=1
    for i in range(0,k,1):
        print sense[i],
    print
  #  if flag==0:
    dictionary=[]
    for i in wn.synsets(word):
        dictionary=dictionary+i.lemma_names()
        for j in i.hypernyms():
            dictionary=dictionary+j.lemma_names()
            for z in j.hypernyms():
                dictionary=dictionary+z.lemma_names()
                for y in z.hypernyms():
                    dictionary=dictionary+y.lemma_names()
                    for x in y.hypernyms():
                        dictionary=dictionary+x.lemma_names()
    print dictionary
    k=0
    for i in wn.synsets(myword):
        mydict=[]
        mydict+=i.lemma_names()
        for j in i.hypernyms():
            mydict+=j.lemma_names()
            for z in j.hypernyms():
                mydict+=z.lemma_names()
                for y in z.hypernyms():
                    mydict+=y.lemma_names()
                    for x in y.hypernyms():
                        mydict+=x.lemma_names()
        mydict=set(mydict)
        dictionary=set(dictionary)
        common=mydict.intersection(dictionary)
        print common
        if len(common)>0:
            flag=1
            score=(len(common)**(1/3))/((4**(1/3))*(distance**(1/3)))
            sense[k]=sense[k]+score
        k+=1
    for i in range(0,k,1):
        print sense[i],
    print
for i in range(0,k,1):
    print sense[i],
print
mx=-2
mysense=0
for i in range(0,k,1):
    if sense[i]>mx:
        mx=sense[i]
        mysensenum=i
k=0
print mysensenum
mysense
for i in wn.synsets(myword):
    if k==mysensenum:
        mysense=i
        mysensedefinition=i.definition()
    k+=1
print mx,mysense,mysensedefinition
        
                            
        
                
    
            
        
                    
            
                
    
    
        


