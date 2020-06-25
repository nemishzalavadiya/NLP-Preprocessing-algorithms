#!/usr/bin/env python
# coding: utf-8

# ## Soundex

# Let's create a function which calculates the soundex of any given string 

# In[1]:


def get_soundex(token):
    """Get the soundex code for the string"""
    token = token.upper()

    soundex = ""
    
    # first letter of input is always the first letter of soundex
    soundex += token[0]
    
    # create a dictionary which maps letters to respective soundex codes. Vowels and 'H', 'W' and 'Y' will be represented by '.'
    dictionary = {"BFPV": "1", "CGJKQSXZ":"2", "DT":"3", "L":"4", "MN":"5", "R":"6", "AEIOUHWY":"."}

    for char in token[1:]:
        for key in dictionary.keys():
            if char in key:
                code = dictionary[key]
                if code != soundex[-1]:
                    soundex += code

    # remove vowels and 'H', 'W' and 'Y' from soundex
    soundex = soundex.replace(".", "")
    
    # trim or pad to make soundex a 4-character code
    soundex = soundex[:4].ljust(4, "0")
        
    return soundex


# Let's see what's the soudex of 'Bombay' and 'Bambai'

# In[2]:


print(get_soundex("Bombay"))
print(get_soundex("Bambai"))


# Let's see soundex of 'Aggrawal', 'Agrawal', 'Aggarwal' and 'Agarwal'

# In[3]:


print(get_soundex("Aggrawal"))
print(get_soundex("Agrawal"))
print(get_soundex("Aggarwal"))
print(get_soundex("Agarwal"))

