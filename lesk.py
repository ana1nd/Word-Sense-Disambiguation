from nltk.corpus import wordnet
import unicodedata as u
import nltk
#sent=['Your car is parked at the top of the mountain','A star tops the christmas tree','He screamed at his top of his lungs ','The hikers topped the mountain just after the noon']
#word='top'
#sent=['The capital city of India , New delhi is very polluted','Your password should contain atleast one capital letter','our capital concern was to avoid defeat ','the drug capital of spain']
#word='capital'
#sent=['the bass line of the song is too weak','I went fishing for sea bass']
#word='bass'
sent=['The cold helped clear his head','Lets go inside i am feeling cold','Lets go inside it is too cold here','the dogs are attempting to catch a cold scent','dinner has gotton cold','The doctor checked his cold and wrote medicines']
word='cold'
#sent=['The girl is wearing a nice red black top']
#word='top'
sent=sent[0].split()
mx=0
score=[]
k=0
for  i in wordnet.synsets(word):
    lesk=[]
    for j in i.lemma_names():
        newls=[]
        lemma=str(j)
        if '_' in lemma:
            lemma=lemma.split('_')
            lesk+=lemma
        else:
            newls.append(lemma)
            lesk+=newls
    define=i.definition()
    define=str(define)
    define=define.split()
    lesk=lesk+define

    for z in i.examples():
        arr=''
        arr=str(z)
        arr=arr.split()
        lesk=lesk+arr
    for z in i.hypernyms():
        for l in z.lemma_names():
            st=''
            st=u.normalize('NFKD',l).encode('ascii','ignore')
            if '_' in st:
                ls=st.split('_')
            else:
                ls=st.split(' ')
            lesk+=ls
            

    for z in i.hyponyms():
        for l in z.lemma_names():
            st=''
            st=u.normalize('NFKD',l).encode('ascii','ignore')
            if '_' in st:
                ls=st.split('_')
            else:
                ls=st.split(' ')
            lesk+=ls

    lesk=set(lesk)
    sent=set(sent)
    common=lesk.intersection(sent)
    print i
    print sent
    print common
    print lesk
    score.append(len(common))
    k+=1
    print
    if len(common)>mx:
        overlap=[]
        sense=[]
        overlap.append(common)
        sense.append(i)
        mx=len(common)
    elif len(common)==mx:
        overlap.append(common)
        sense.append(i)
for i in range(0,k,1):
    print score[i],
print
print "The following sense have most likely meaning of the ambiguous word"
for i in range (0,len(overlap),1):
    print overlap[i],sense[i].definition(),mx
    print
