
ASSIGNMENT 1: 

#1. swapchars

import collections
import string 
import unittest 

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
    str = "".join(lst)
    print str 

#2. sortcat

def sortcat(i, *argv): 
lst = list(argv)
if i == -1:
    print "".join(lst)
else: 
    lstf= sorted((sorted(lst, key=len)[-i:]), key=str.lower)
    print "".join(lstf)

#3. blue's clues

with open('states.txt') as f:
    abbrev = dict(reversed(line.strip().split(',',1)) for line in f)

def bluesclues(a): 
    print (abbrev[a])

#4. blue's booze
def bluesbooze(a):
    print abbrev.keys()[abbrev.values().index(a)]


# testing 
class TestStringMethods(unittest.TestCase):
    def test_swapchars(self):
        self.assertEqual(swapchars('I\'m just a chi-town coder with a nice flow.'), 'U\'m jist a chu-town coder wuth a nuce flow.')

if __name__ == '__main__':
    unittest.main()
