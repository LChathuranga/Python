#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
dataset = pd.read_csv(r"C:\Users\User\Desktop\Book1.csv")
print(dataset)


# In[2]:


dataset=dataset.values
print(dataset)


# In[3]:


import numpy as np
avg=np.mean(dataset[:,1:],axis=1)
print(avg)


# In[4]:


avg=avg.reshape(-1,1)
print(avg)


# In[5]:


def findGrade(x):
    if(x>=75 and x<=100):
        grade='A'
    elif(75>x and x>=65):
        grade='B'
    elif(65>x and x>=55):
        grade='C'
    elif(55>x and x>=35):
        grade='S'
    elif(35>x and x>=0):
        grade='F'
    return grade


# In[6]:


matGrade=np.array([findGrade(i) for i in dataset[:,1]])
matGrade=matGrade.reshape(-1,1)
print(matGrade)


# In[7]:


phyGrade= np.array([findGrade(i) for i in dataset[:,2]])
phyGrade=phyGrade.reshape(-1,1)
print(phyGrade)


# In[8]:


chemGrade=np.array([findGrade(i) for i in dataset[:,3]])
chemGrade=chemGrade.reshape(-1,1)
print(chemGrade)


# In[9]:


dataset=np.append(dataset,matGrade,axis=1)
print(dataset)


# In[10]:


dataset=np.append(dataset,phyGrade,axis=1)
print(dataset)


# In[11]:


dataset=np.append(dataset,chemGrade,axis=1)
print(dataset)


# In[12]:


dataset=np.append(dataset,avg,axis=1)
print(dataset)


# In[15]:


df=pd.DataFrame(data=dataset,columns=['name','maths','Physics','Chemstry','M-grade','p-grade','c-grade','avg'])
print(df)


# In[16]:


df.to_csv('stu.csv',index=False)


# In[ ]:




