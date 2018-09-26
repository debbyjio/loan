
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib as plt
get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_csv("E:loan.csv")


# In[2]:


df.head(10)


# In[14]:


#Create a new function:
def num_missing(x):
  return sum(x.isnull())

#Applying per column:
print ("Missing values per column:")
print (df.apply(num_missing, axis=0)) #axis=0 defines that function is to be applied on each column

#Applying per row:
print ("\nMissing values per row:")
print (df.apply(num_missing, axis=1)).head() #axis=1 defines that function is to be applied on each row


# In[15]:


impute_grps = df.pivot_table(values=["LoanAmount"], index=["Gender","Married","Self_Employed"], aggfunc=np.mean)
print (impute_grps)


# In[17]:


pd.crosstab(df["Credit_History"],df["Loan_Status"],margins=True)


# In[23]:


df['LoanAmount'].fillna(df['LoanAmount'].mean(), inplace=True) #missing values filled.


# In[25]:


df['Self_Employed'].value_counts()


# In[27]:


#Create a new function:
def num_missing(x):
  return sum(x.isnull())

#Applying per column:
print ("Missing values per column:")
print (df.apply(num_missing, axis=0)) #axis=0 defines that function is to be applied on each column

#Applying per row:
print ("\nMissing values per row:")
print (df.apply(num_missing, axis=1)).head() #axis=1 defines that function is to be applied on each row


# In[28]:


#loan amount has no more missing values


# In[29]:


df['Self_Employed'].fillna('No',inplace=True)


# In[33]:


df['LoanAmount_log'] = np.log(df['LoanAmount'])
df['LoanAmount_log'].hist(bins=20)


# In[34]:


#Let’s analyze LoanAmount first. Since the extreme values are practically possible So instead of treating them as outliers, 
#let’s try a log transformation to nullify their effect:


# In[42]:


#now we plot histogram of total income
df['TotalIncome'] = df['ApplicantIncome'] + df['CoapplicantIncome']
df['TotalIncome_log'] = np.log(df['TotalIncome'])
df['TotalIncome'].hist(bins=60) 


# In[44]:


df['TotalIncome_log'].hist(bins=50) 


# In[45]:


#log of total income is almost normalised.

