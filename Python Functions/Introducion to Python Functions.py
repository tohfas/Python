#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Functions

#Functions are reusable peices of programs. They allow you to give a name to a block of statements, allowing you to run that block using specified name anywhere in you program and any number of times. This is known as calling functions. There are many built in functions such as len and range


# In[2]:


#print sheldon knock
print("knock knock knock")
print("knock knock knock")
print("knock knock knock")


# In[4]:


#using function

def sheldon_knock():
    print("knock knock knock")
    print("knock knock knock")
    print("knock knock knock")


# In[6]:


sheldon_knock()
print(10+20)
for i in range (10):
    print(i)
sheldon_knock()


# In[7]:


#Functions can take Parameters

# Python being dynamically typed doesnot need any datatype declaration for variables unlike C, C+, same goes for return statement...you can return anytype of data
def sheldon_knock(name):
    print("knock knock knock", format(name))
    print("knock knock knock", format(name))
    print("knock knock knock",format(name))
    


# In[8]:


sheldon_knock("penny")


# In[9]:


#you can take multiple parameters

def sheldon_knock(name, number_of_times):
    for i in range(number_of_times):
        print("knock knock knock", format(name))
        

    
    


# In[11]:


sheldon_knock("penny",100)


# In[12]:


#you can give default values to the parameters
def sheldon_knock(name, number_of_times=3):
    for i in range(number_of_times):
        print("knock knock knock", format(name))
        


# In[13]:


sheldon_knock("penny")


# In[14]:


#now seee if you explicitly a value to the parameter lets say 10
sheldon_knock("penny",10)


# In[ ]:




