################################################################################
# Regex - email matching.
################################################################################
import pandas as pd

# At first we need a example list of strings. You can extend or change it later:
texts = ['This is my email: donald.trump@whitehouse.net',
         'pkurek@wne.uw.edu.pl',
         'm.wysocki9@ uw.edu.pl',
         'cat',
         '2020@07-14',
         'verystrangemail_845088424_443@gmail.com',
         'student@tstudent.org',
         'This is my mail: vim.creator (at) vim.org, I hide my mail from robots :)',
         '@domain.org',
         '.net']

# We will be using regex available in pandas series, so we just make
# a pandas data frame.
d = pd.DataFrame({'texts':texts})

# Regular expression:
regex = '\w\S*@.*\w'
#regex = '[A-Za-z]+@[A-Za-z]+\.(?:net|edu|com|org)'
#regex = '[A-Za-z\._]+@[A-Za-z]+\.[a-z]{3}'
#regex = '[A-Za-z\._]+@[A-Za-z]+\.[a-z]{2,3}'

# We add boolean vector to our data frame - wether regex doex match or do not:
d['regex_result'] = d.texts.str.contains(regex)
d['regex_matched'] = d.texts.str.findall(regex)

# This code allows to print full pandas data frame no matter how big:
print(d.to_string())

################################################################################
# As simple excercises run different suggested regexes.
# Try to use this code to experiment on your own!
# Can you make a perfect email-searching regex?
