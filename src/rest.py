'''
Created on 11 Oct 2019

@author: castells
'''
import requests
import json
import random


class APIError(Exception):
    """An API Error Exception"""

    def __init__(self, status):
        self.status = status

    def __str__(self):
        return "APIError: status={}".format(self.status)

def getVerse(ref="genesis:1"):
    base = "http://labs.bible.org/api/?type=json&formatting=plain&passage="
    #print(base+ref)
    verse = requests.get(base + ref)
    
    if verse.status_code != 200:
        # This means something went wrong.
        raise APIError('GET /tasks/ {}'.format(verse.status_code))
    #for todo_item in resp.json():
        #print('{} {}'.format(todo_item['id'], todo_item['summary']))
    

    return verse.text

def printList(buster):
    for ref in buster:
        verse = getVerse(ref)
        
        jverse = json.loads(verse)
        print (ref)
        fverse = []
        for item in jverse:    
            fverse.append(item['text'])    
        print ('\n'.join(fverse))
        print('\n')

def printMem(buster):
    for ref in buster:
        verse = getVerse(ref)
        
        jverse = json.loads(verse)
        print (ref)

        fabbr = []
        for item in jverse:      
            fabbr.append('  '.join([x[0]  for i, x in  enumerate(item['text'].split())]).upper())      
        print('\n'.join(fabbr))
        print('\n') 
        
        
def printLearn(ref):
    verse = getVerse(ref)
    jverse = json.loads(verse)
    for item in jverse:
            
        words = item['text'].split()
        used = []
        space = "_____ "
        last = len(words)-1
        phrase = [item['text']]
        sprd = 0
        while len(used) < len(words):            
            while sprd in used:
                sprd = random.randint(0,last)                
            used.append(sprd)
            words[sprd] = words[sprd][0] + space
            phrase.append(" ".join(items for items in words))
    return phrase        
            
            
    
          
   
if __name__ == '__main__':
    
    buster = ["gen 1:1", "exo 1:1", "lev 1:1", "John 3:16", "exodus 14:14", "matthew 7:7-9", "gal 3:1-5", "1 Cor 13:1,4,5"]
    
    for ref in buster: 
        learning =  printLearn(ref)
        for verses in learning:
            print(verses)
    printList(buster)
    printMem(buster)
    
