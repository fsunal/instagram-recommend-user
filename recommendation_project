from instagram import *
import json
import instagram.client
from instagram.client import InstagramAPI
import sys
from Tkinter import *
import webbrowser



api = InstagramAPI(client_id='your client id', client_secret='your client secret',access_token="your acces_token")

top = Tk()
top.title("Find people to Follow")
t = []

def showme():
    address = "http://instagram/" +str(rec)[6:]
    top3.destroy()
    webbrowser.open(address)
    

def finalshow():
    global top3
    top3 = Tk()
    top3.title("Recommendation to Follow")
    lab = Label(top3,text="This is the person you may want to follow:")
    lab.pack()
    lab2 = Label(top3,text=rec)
    lab2.pack()
    bt = Button(top3,text="Show",command=showme)
    bt.pack()
    top3.geometry("350x250")
    top3.mainloop()
def finalrecommendation():
    l = []
    for i in tags:
        tagSearch = api.tag_recent_media(count = 100, tag_name = i)
        l.append(tagSearch)
    
    com ={}
    lc3 = []
    fl = api.user_follows(userId)
    #print fl
    followingList = []
    for i in fl[0]:
        followingList.append(str(i)[6:])
    #print l
    for i in range(len(l)):
        for c in l[i][0]:
          #print c  
            if str(c.id) not in com:
                com[str(c.id)] = [c,1]
            else:
                com[str(c.id)][1] +=1
    #print com
    for c in com:
        if (com[c][1] >= 2) and (str(com[c][0].user)[6:] != x) and (str(com[c][0].user)[6:] not in followingList):
            lc3.append((com[c][0].like_count,com[c][0].user))


    lc3 = sorted(lc3,reverse=True)
    global rec
    rec= lc3[0][1]
    finalshow()
def finalrecommendation2(t):
    l = []
    for i in t:
        tagSearch = api.tag_recent_media(count = 100, tag_name = i)
        l.append(tagSearch)
    com ={}
    lc3 = []
    for i in range(len(l)):
        for c in l[i][0]:
          #print c  
            if str(c.id) not in com:
                com[str(c.id)] = [c,1]
            else:
                com[str(c.id)][1] +=1
    #print com
    for c in com:
        if (com[c][1] >= 2) and (str(com[c][0].user)[6:] not in lc3):
            lc3.append((com[c][0].like_count,com[c][0].user))


    lc3 = sorted(lc3,reverse=True)
    global rec
    rec = lc3[0][1]
    finalshow()    
def getusertags():
    global x
    x = ent0.get()
    top.destroy()
    a = api.user_search(x)
    a = a[0]
    global userId
    userId = a.id
    um= api.user_recent_media(user_id=userId)
    pzr=[]
    for i in range(len(um[0])):
        if um[0][i] not in pzr:
            pzr.append(um[0][i])
    total_tags=[]
    for i in range(len(pzr)-1):
        try:
            total_tags.append(pzr[i].tags)
        except Exception:
            pass

    global tags
    tags=[]
    for i in total_tags:
        for j in i:
            if j not in tags:
                tags.append(str(j.name))
    tags = tags[:20]
    finalrecommendation()

print total_tags
def getHashtags():
    t = []
    for i in range(1,y+1):
        v = globals()["e" + str(i)].get()
        t.append(v)
    print t
    #top2.destroy()
    print finalrecommendation2(t)

def tags(x):
    
    top2 = Tk()
    top2.title("Tags")
    for i in range(1,y+1):
        globals()["l"+str(i)] = Label(top2,text="Search Hashtag %d\n"%i)
        globals()["l"+str(i)].pack()
        globals()["e"+str(i)] = Entry(top2)
        globals()["e"+str(i)].pack()
    

    b = Button(top2,text="Find", command=getHashtags)
    b.pack()
    top2.geometry("250x%d00"%y)
    top2.mainloop()


labl = Label(top,text="\nPlease choose one way to find common user\n \n")
labl.pack()
lab0 = Label(top,text="Please enter a username: \n")
lab0.pack()
ent0 = Entry(top)
ent0.pack()



but0 = Button(top,text="Enter",command=getusertags)
but0.pack()
lab = Label(top,text="\nHow many hashtags you want to search? \n")
lab.pack()
ent = Entry(top)
ent.pack()

def getnum():
    global y
    y = ent.get()
    y = int(y)
    print y
    top.destroy()
    tags(y)
but = Button(top,text="Submit",command=getnum)
but.pack()


top.geometry("500x300")
top.mainloop()







