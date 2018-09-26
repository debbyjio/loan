
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np
import matplotlib as plt
get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_csv("E:loan.csv")


# In[12]:


df.head(10)


# In[13]:


df.head(20)


# In[14]:


df.describe( include = 'all')


# In[15]:


df['ApplicantIncome'].hist(bins=50)


# In[34]:


df['Loan_Status'].value_counts()


# In[16]:


df.boxplot(column = 'ApplicantIncome')


# In[17]:


#confirms presence of extreme values due to high income disparity in the society


# In[18]:


df.boxplot(column='ApplicantIncome', by ='Education')


# In[19]:


#almost same measures of central tendency in graduates and non graduates but most outliers lie wiith graduates


# In[20]:


df['LoanAmount'].hist(bins=50)


# In[21]:


df.boxplot(column='LoanAmount')


# In[22]:


#There are some extreme values. Both ApplicantIncome and LoanAmount require some amount of data munging.
#LoanAmount has missing and well as extreme values values, while ApplicantIncome has a few extreme values,


# In[23]:


#now we look at chances of getting loan with credit history


# In[39]:


temp1 = df['Credit_History'].value_counts(ascending=True)
temp2 = df.pivot_table(values='Loan_Status', index=['Credit_History'], aggfunc=lambda x : x.map ({'Y' : 1, 'N' : 0}).mean())
print('Frequency table for credit history:')
print(temp1)

print('\n Prbababilty of getting loan for different categories of credit history')
print(temp2)


# In[32]:


import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8,6))
ax1 = fig.add_subplot(121)
ax1.set_xlabel('Credit_History')
ax1.set_ylabel('Count of Applicants')
ax1.set_title("Applicants by Credit_History")
temp1.plot(kind='bar')

ax2 = fig.add_subplot(122)
ax2.set_xlabel('Credit_History')
ax2.set_ylabel('Probability of getting loan')
ax2.set_title("Probability of getting loan by credit history")
temp2.plot(kind = 'bar')


# In[36]:


temp3 = pd.crosstab(df['Credit_History'], df['Loan_Status'])
temp3.plot(kind='bar', stacked=True, color=['red','blue'], grid=False)


# In[44]:


temp4 = pd.crosstab(df['Credit_History'], df['Loan_Status'])
temp4.plot(kind='bar', stacked=True, color=['red','blue'], grid=False)


# In[ ]:


#now we add gender to the mix


# In[62]:


temp5 = df.pivot_table(values='Loan_Status', index=['Credit_History','Gender'], aggfunc=lambda x : x.map ({'Y' : 1, 'N' : 0}).mean())
print (temp5)


# In[57]:


import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8,6))
ax1 = fig.add_subplot(121)
ax1.set_xlabel('Credit_History,Gender')
ax1.set_ylabel('Count of Applicants')
ax1.set_title("Applicants by Credit_History")
temp5.plot(kind='bar')


# In[63]:


#Thus we see that Male with credit history have the greatest chance of getting loan aproved.

