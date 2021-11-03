import requests
from bs4 import BeautifulSoup
import pandas as pd

Questions=[]
A=[]
B=[]
C=[]
D=[]
Correct=[]
for pg_no in range(1,29):
    url='https://www.atrochatro.com/quiz_personalities-'+str(pg_no)+'.html'
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')

    for question in soup.select('blockquote:has(b)'):
        q = question.b.find_next_sibling(text=True).strip()
        #print(q)
        Questions.append(q)
        correct = int(question.input['onclick'].split("'")[-2])
        for i, l in enumerate(question.select('label'), 1):
            #print('{:<30} {}'.format(l.text.strip(), '<-- CORRECT' if i==correct else ''))
            if i==1:
                A.append(l.text.strip())
            elif i==2:
                B.append(l.text.strip())
            elif i==3:
                C.append(l.text.strip())
            else:
                D.append(l.text.strip())
            if i==correct:
                if i==1:
                    Correct.append('[A,'+l.text.strip()+']')
                if i==2:
                    Correct.append('[B,'+l.text.strip()+']')
                if i==3:
                    Correct.append('[C,'+l.text.strip()+']')
                if i==4:
                    Correct.append('[D,'+l.text.strip()+']')
        #print('-'*80)

    print("Page Number",pg_no,"Processed")

data_dict={"Question":Questions,"A":A,"B":B,"C":C,"D":D,"Answer":Correct}

df = pd.DataFrame(data=data_dict)

df.to_excel('personalities.xlsx')
