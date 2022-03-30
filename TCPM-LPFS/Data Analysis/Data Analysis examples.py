#!/usr/bin/env python
# coding: utf-8

# In[1]:


data = {'Name':['John','Tim','Rob'],
       'Age':[34,23,42],
        'Salary':[42000,32000,62000]
       }


# In[2]:


from pandas import DataFrame
frame = DataFrame(data)


# In[3]:


frame


# In[4]:


new_frame = DataFrame(data, columns=['Name','Salary','Age'])


# In[5]:


new_frame


# In[6]:


frame


# In[7]:


new_frame = DataFrame(data, columns=['Name','Salary','Age','Profile'])


# In[8]:


new_frame


# In[9]:


new_frame['Salary']


# In[16]:


new_frame.iloc[1]


# In[17]:


new_frame['Profile']='Doctor'
new_frame


# In[18]:


new_frame = DataFrame(data, columns=['Name','Age','Salary','Profile'])
new_frame


# In[19]:


new_frame['Profile']='Doctor'
new_frame


# In[20]:


new_frame['Education']='Masters Degree'
new_frame


# In[21]:


new_frame['Education']='Ph.D'
new_frame


# In[23]:


new_frame.iloc[1]


# In[24]:


new_frame = new_frame.T


# In[25]:


new_frame


# In[26]:


new_frame = new_frame.T


# In[27]:


new_frame


# In[28]:


from pandas import Series
obj = Series([100,200,300,400,500], index=['d','a','b','e','c'])
obj


# In[31]:


obj = obj.reindex(['a','b','c','d','e'])
obj


# In[32]:


data = {'Name':['John','Tim','Rob'],
       'Age':[34,23,42],
        'Salary':[42000,32000,62000]
       }
frame = DataFrame(data)
frame


# In[33]:


test_frame = frame.reindex([0,2,1])
test_frame


# In[36]:


fields = ['Age','Name','Salary']
hold_frame = test_frame.reindex(columns=fields)
hold_frame


# In[37]:


fields = ['Name','Age','Salary']
hold_frame = hold_frame.reindex(columns=fields)
hold_frame


# In[38]:


hold = frame.reindex([0,1,2])
hold


# In[39]:


hold_frame = hold_frame.reindex([0,1,2])
hold_frame


# In[40]:


frame2 = hold_frame.drop([2])
frame2


# In[41]:


frame


# In[44]:


frame4 = frame.drop('Salary', axis=1)
frame4


# In[46]:


from pandas import Series
series1 = Series([1,2,3,4,5])
series2 = Series([100,200,300,400,500,600])
series1 + series2


# In[47]:


from pandas import Series
series1 = Series([1,2,3,4,5,6])
series2 = Series([100,200,300,400,500,600])
series1 + series2


# In[48]:


from pandas import DataFrame
data1 = {'Speed':[100,103,105], 'Temp':[34,23,42],}
frame1 = DataFrame(data1)
frame1


# In[49]:


data2 = {'Speed':[101,109,106], 'Temp':[34,23,42], 'Humidity':[45,23,58]}
frame2 = DataFrame(data2)
frame2


# In[50]:


frame1 + frame2


# In[51]:


series2 = Series([100,200,300], index=['Speed','Temperature','Humidity'])
series2


# In[52]:


frame2 - series2


# In[53]:


frame2
series2


# In[54]:


frame2


# In[57]:


series3 = Series([100,200], index=['Speed','Temp'])
series3


# In[58]:


frame2


# In[59]:


frame2 - series3


# In[60]:


frame2 + series3


# In[62]:


ser = Series([3,7,1,4,7,2], index=[2,7,3,5,9,1])
ser


# In[63]:


ser.sort_index()


# In[64]:


data2 = {'Speed':[101,109,106], 'Temp':[34,23,42], 'Humidity':[45,23,58]}
frame2 = DataFrame(data2)
frame2


# In[65]:


frame2 = frame2.reindex([2,1,0])
frame2


# In[66]:


frame2.sort_index()


# In[68]:


frame2.reindex(columns=['Speed', 'Humidity','Temp'])


# In[69]:


frame2.sort_index(axis=1)


# In[72]:


frame2.sort_index(axis=0)


# In[74]:


frame2


# In[75]:


frame2 = frame2.reindex([0,1,2])
frame2


# In[77]:


frame2.sort_index(axis=1,ascending=False)


# In[78]:


frame2.sort_values()


# In[79]:


series4 = Series([100,200,300], index=['Speed','Temp','Humidty'])
series4


# In[80]:


series4.sort_values()


# In[81]:


frame2


# In[82]:


frame2.sort_values(by='Humidity')


# In[83]:


frame2.sort_values(by='Temp')


# In[84]:


frame2.sort_values(by='Speed')


# In[86]:


series5 = Series([100,200,300],index=['a','b','b'])
series5


# In[87]:


series5.index.is_unique


# In[88]:


series5 = Series([100,200,300],index=['a','b','c'])
series5


# In[89]:


series5.index.is_unique


# In[90]:


frame2


# In[91]:


frame2.sum()


# In[92]:


frame2.sum(axis=1)


# In[93]:


frame2.idxmax()


# In[94]:


frame2.idxmin()


# In[95]:


import numpy as np
ser = Series([1,2,3,4,np.nan],index=['a','b','c','d','e'])
ser


# In[96]:


ser.dropna()


# In[97]:


ser


# In[98]:


ser = ser.dropna()
ser


# In[99]:


frame2


# In[100]:


data2 = {'Speed':[101,np.nan,106], 'Temp':[34,np.nan,42], 'Humidity':[45,np.nan,58]}
frame3 = DataFrame(data2)
frame3


# In[101]:


frame3.dropna()


# In[102]:


frame3 = frame3.dropna()
frame3


# In[103]:


data2 = {'Speed':[101,np.nan,106], 'Temp':[34,np.nan,42], 'Humidity':[45,np.nan,58]}
frame3 = DataFrame(data2)
frame3


# In[105]:


frame3.fillna(0)


# In[106]:


import pandas
data_frame = pandas.read_csv("test.csv")
data_frame


# In[108]:


data_frame2 = data_frame.fillna(0)
data_frame2


# In[110]:


from pandas import DataFrame
data_frame = DataFrame(data_frame, columns=['order_id','product_name','product_price','customer_name','product_category','brand'])
data_frame


# In[111]:


data_frame = data_frame.drop([1])
data_frame


# In[113]:


data_frame = data_frame.drop('product_category',axis=1)
data_frame


# In[114]:


data_frame.sort_values(by='product_price')


# In[115]:


data_frame.sum(numeric_only=True)


# In[ ]:




