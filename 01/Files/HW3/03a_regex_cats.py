################################################################################
# Regex - an experiment on cats.
################################################################################
import pandas as pd

# At first we need a example list of strings. You can extend it or change later:
texts = ['cat',
         'Cat',
         'catt',
         'concatenate',
         'Hi, we have cats!',
         'Catty! Come here!',
         'A Cat Is Good Pet',
         'catastrophic event',
         'Cats ate my dog.']

# We will be using regex available in pandas series, so we just make
# a pandas data frame.
d = pd.DataFrame({'texts':texts})

# Regular expression:
regex = 'cat'
#regex = '[cC]at'
#regex = '[cC]ats?'
#regex = '\s[cC]ats?\s'
#regex = '(?:\s|^)+[cC]ats?(?:\s|$)+'

# We add boolean column to our data frame - wether regex doex match or do not:
d['regex_result'] = d.texts.str.contains(regex)
d['regex_matched'] = d.texts.str.findall(regex)

# This code allows to print full pandas data frame no matter how big:
print(d.to_string())

################################################################################
# As simple excercises run different suggested regexes.
# Try to use this code to experiment on your own!
# Can you make a perfect cat-searching regex?
