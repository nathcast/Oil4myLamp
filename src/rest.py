'''
Created on 11 Oct 2019

@author: castells
'''
import json
import random
import requests
import sys


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

def makeList(buster, file='default'):
    
    xname = file +'.txt'
    fxname = open(xname,'w+')
    list = printList(buster)
    fxname.write(list)
    fxname.close()
    print('List of verses on '+ file +' saved in '+ xname)
    
    
def printList(buster):
    list = ''
    fverse = []
    for ref in buster:
        verse = getVerse(ref)
        jverse = json.loads(verse)
        print (ref)
        
        for item in jverse:    
            fverse.append(item['text']) 
            list += '\n'+ ref
            list += '\n'+  item['text'] 
        print ('\n'.join(fverse))
        
        print('\n')
    return list

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
    
    buster =  ["gen 1:1", "exo 1:1", "lev 1:1", "John 3:16", "exodus 14:14", "matthew 7:7-9", "gal 3:1-5", "1 Cor 13:1,4,5"]
    
    index  =  [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    chapter = ["Rom:14","Ps 103","1 Cor 1","1 John 4","1 John 5","Ps 107","Matt 5-7","Rom 15","Ps 34","Matt 10","Ps 27","Eph 2","John 8","John 10","John 6:25-59","Ps 16","John 17","1 John 2","Ps 19","Rom 5","Phil 4","Eph 1","Heb 12","Is 53-55","Col 1","Rom 8","1 Thess 5","1 Tim 6","1 John 3","1 Pet 2",""]
    Bible = ["Ps 1:1","Prov 2:1-5","Ecc 12:11-15","John 1:8","1 John 5:13","Ps 107:43","Matt 5:17","Rom 15:4","2 Cor 3:16","Heb 4:12","Ez 11:19-20","2 pet 1:20-21","Ps 119:5","John 10:34-36","Jer 15:16","Col 3:16","John 17:17","Ps 18:30","Ps 19","Mark 4:11-12","Is 55:10-12","1 Pet 3:5-7","Deut 6:6","Is 59:21","Ps 33:6","1 Pet 3:15","Ps 12:6","Ps 139:17","Prov 30:5-6","Luke 24:27",""]
    Love = [ "John 14:21","Ps 103:17","1 Cor 1:8","1 John 4:16","Is 41:9-10","Ps 107:8-9","Ps 147:11","Is 43:1-2","Is 54:5","Lam 3:22","Ps 94:16","Ps 119:73-80","Songs 2:14","John 10:2-7","Jer 31:1-6","Ps 16:11","Rom 5:8","Ps 90:14","Job 19:26-27","Rom 5:5-8","Gal 2:20","","Heb 12:16","Ps 144:1-2","Ps 12:1-3","Rom 8:37","Ps 36:5-9","Ps 139","1 John 3:1-2","",""]
  
    #print("Example of Learning Page")
   # print(" ")
    #ref = buster[3]
    #learning =  printLearn(ref)
    #for verses in learning:
    #    print(verses)
    print(" ")
    makeList(buster, 'love')
    print(" ")
    #printMem(Love)
    
