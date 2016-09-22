# Assignment 1: How to Python
Hey guys, welcome to Python! Let's start you off on your magical journey by learning some syntax!

If at any point you have an issue, let Jessica (jessica.zhu@thecrimson.com) or Kyle (kyle.kwong@thecrimson.com) know! Don't bash your head against the wall. We're here to help.

## Instructions
Do you have python 2.7 installed? Let's find out! Try typing `python --version` in your terminal. If you don't have it, please consult us, or the internet, for help ASAP.

### Tips
- Write your code as "Pythonically" as possible.
- If it seems like there should be an easier way to do it, there probably is. Use library functions where appropriate.
- Test your code! It makes providing feedback a lot easier <3. Thanks baes :)
  
## Step(s) to it
###swapchars
Write a function that takes one (1) string argument. Return that string with the most common letter swapped with the least common letter. Yes, uppercase and lowercase count towards the same letter.

    >>> swapchars('I\'m just a chi-town coder with a nice flow.')
    "U'm jist a chu-town coder wuth a nuce flow."
You can break ties however you want! (psst! check out [Counters](https://docs.python.org/2/library/collections.html#collections.Counter))

import collections
import string 
def swapchars(s): 
    cnt = collections.Counter()
    for letter in s.lower(): 
        if letter.isalpha(): 
            cnt[letter] +=1 
    (mc, y) = cnt.most_common(1)[0]
    [(lc, z)] = cnt.most_common()[:-2:-1]
    lst = list(s)
    for n,i in enumerate(lst): 
        if i == mc: 
            lst[n] = lc
        else: 
            if i.lower() == mc:
                lst[n] = lc.upper()
            else: 
                if i == lc: 
                    lst[n] = mc
                else: 
                    if i.lower() == lc: 
                        lst[n] = mc.upper()
                    else: 
                        lst[n] = i
    print "".join(lst)


### sortcat
Write a function that takes one (1) integer argument _n_  and **an arbitrary number** of string arguments. Return the concatenation of the longest _n_  arguments from longest to shortest. If _n_  is -1, concatenate all the arguments in this fashion.
 
    >>> sortcat(1, 'abc', 'bc')
    'abc'
    >>> sortcat(2, 'bc', 'c', 'abc')
    'abcbc'

def sortcat(i, *argv): 
    lst = list(argv)
    if i == -1:
        print "".join(lst)
    else: 
        lstf= sorted((sorted(lst, key=len)[-i:]), key=str.lower)
        print "".join(lstf)


### Blue's Clues
Blue just got a letter! She'd like to know where it's coming from, but the return address's state is listed as "PA" and Blue has no idea what state that corresponds to. (come on guys, she's a dog. you can't expect much.)

We've provided a file called `states.txt` that contains all the state names and their abbreviations in the following form.

    Alabama,AL
    Alaska,AK
    ...
    Wyoming,WY

We'd like you to open the file and read its contents into a dictionary indexed by abbreviation. For example:

    abbrev['AL'] = 'Alabama'

Then write a function `bluesclues` that takes in a state abbreviation (assume perfect capitalization) and returns the full name of the state.

with open('states.txt') as f:
    abbrev = dict(reversed(line.strip().split(',',1)) for line in f)

def bluesclues(a): 
    print (abbrev[a])

        
### Blue's Booze
Blue owns a vineyard (she's really made it big since her hit TV show) and needs to ship wine to Nebraska. However, she doesn't know what the state abbreviation is! 

Using your dictionary from above, write a function `bluesbooze` that takes in the full name of a state (again, assume perfect capitalization) and returns the state's abbreviation.

def bluesbooze(a):
    print abbrev.keys()[abbrev.values().index(a)]

# Feedback?
You're done! Congrats! Be sure to save your changes and push to your Github. Thanks, dude!

