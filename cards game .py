card=["2","3","4","K","Q","J","5","6","7","8","9","10","A"]
ty=["Spade","Diamond","Club","Heart"]
def shape(card,ty):
    a="|-------------------|\n"
    for i in range(4):
        a=a+"|"+cards(card,i)+"     "+typ(ty,i)+"|\n"
    a=a+"|                   |\n"*4
    for i in range(4):
        a=a+"|"+typ(ty,i)+"     "+cards(card,i)+"|"
        if i!=3:
            a=a+"\n"
    print a
    print "|-------------------|\n"
def manyshape(card,times=None):
    if times==None:
        times=len(card)
    print "|----------"*(times)+"--------|"    
    for l in range(4):
        for j in card:
            if card[-1]!=j:
                print ("|"+cards(j[0],l)+"  "),
            else:
                print "|"+cards(j[0],l)+"    "+typ(j[1],l)+"|"
    print ("|          "*times+"        |"+"\n")*3,
    for l in range(4):
        for j in card:
            if card[-1]!=j:
                print ("|"+typ(j[1],l)+"  "),
            else:
                print "|"+typ(j[1],l)+"    "+cards(j[0],l)+"|"
    print "|----------"*(times)+"--------|"
def cards(a,i):
    if a=="K":
        a=" | /   \n"
        a=a+" |/    \n"
        a=a+" |\    \n"
        a=a+" | \   \n"
    elif a=="Q":
        a="""  __   
 |  |  
 |_\|  
    \  """
    elif a=="J":
       a=""" ____  
   |   
   |   
 |_|   """
    elif a=="A":
        a="""       
  /\   
 /__\  
/    \ """
    elif a=="2":
        a="""  __   
  __|  
 |__   
       """
    elif a=="3":
        a=""" ____  
 ____| 
 ____| 
       """
    elif a=="4":
        a=""" |   | 
 |___| 
     | 
     | """
    elif a=="5":
        a="""  ____ 
 |____ 
  ____|
       """
    elif a=="6":
        a="""  ____ 
 |____ 
 |____|
       """
    elif a=="7":
        a=""" ____  
    /  
   /   
  /    """
    elif a=="8":
        a="""  ___  
 |___| 
 |___| 
       """
    elif a=="9":
        a="""  ___  
 |___| 
  ___| 
       """
    elif a=="10":
        a="""/|  __ 
 | |  |
_|_|__|
       """
    a=a.split("\n")
    return a[i]
def typ(a,i):
    if a=="Diamond":
        a="  /\   \n"
        a=a+" /  \  \n"
        a=a+" \  /  \n"
        a=a+"  \/   \n"
    elif a=="Spade":
        a="  /\   \n"
        a=a+" /  \  "
        a=a+"\n \/\/  \n"
        a=a+"  ||   \n"
    elif a=="Heart":
        a=" /\/\  \n"
        a=a+" \  /  \n"
        a=a+"  \/   \n"
        a=a+"       \n"
    elif a=="Club":
        a="  /\   \n"
        a=a+r"/\\//\ "
        a=a+"\n\/||\/ \n"
        a=a+"  ||   \n"
    a=a.split("\n")
    return a[i]
def sep(card,ty):
    import random
    a=1
    lis=[]
    while len(lis)!=52:
        a=random.randint(0,12)
        b=random.randint(0,3)
        a=[a,b]
        if a in lis:
            continue
        else:
            lis.append(a)
    for i in lis:
        i[0]=card[i[0]]
        i[1]=ty[i[1]]
    return lis
def Preccedenceorder(a,b):
    card={"2":1,"3":2,"4":3,"5":4,"6":5,"7":6,"8":7,"9":8,"10":9,"J":10,"Q":11,"K":12,"A":13}
    ty={"Club":1,"Diamond":2,"Heart":3,"Spade":4}
    if a[0]==b[0]:
        if ty[a[1]]>ty[b[1]]:
            return b,(ty[a[1]]-ty[b[1]])
        else:
            return a,(ty[b[1]]-ty[a[1]])
    elif card[a[0]]>card[b[0]]:
        return b,(card[a[0]]+ty[a[1]]-card[b[0]]-ty[b[1]])
    else:
        return a,(card[b[0]]+ty[b[1]]-card[a[0]]-ty[a[1]])
def computerplay(computercards,playercard):
    computer={}
    print computercards
    a="absent"
    for i in computercards:
        if i[1]==playercard[1]:
            a="Present"
    if a=="Present":
        for i in computercards:
            if i[1]==playercard[1]:
                c=Preccedenceorder(i,playercard)
                print c
                if c[0]==playercard:
                    if computer=={}:
                        computer[c[1]]=i
                        print computer
                    else:
                        for j in computer:
                            if j<c[1]:
                                del(computer[j])
                                computer[c[1]]=i
                else:
                    if computer=={}:
                        computer[c[1]]=i
                    else:
                        for j in computer:
                            if j<c[1]:
                                del(computer[j])
                                computer[c[1]]=i
    else:
        for i in computercards:
            c=Preccedenceorder(i,playercard)
            if c[0]==playercard:
                if computer=={}:
                    computer[c[1]]=i
                else:                    
                    for j in computer:
                        if j<c[1]:
                            del(computer[j])
                            computer[c[1]]=i
            else:
                if computer=={}:
                    computer[c[1]]=c[0]
                else:
                    for j in computer:
                        if j<c[1]:
                            del(computer[j])
                            computer[c[1]]=c[0]
    for i in computer:
        return list(computer[i])
def play(card,ty):
    a=raw_input("Enter your name")
    Allcards=sep(card,ty)
    playercards=Allcards[:13]
    computercards=Allcards[13:26]
    computercards1=Allcards[26:39]
    computercards2=Allcards[39:52]
    manyshape(playercards)
#    manyshape(computercards)
#    manyshape(computercards1)
#    manyshape(computercards2)
    for i in range(1,len(playercards)+1):
        print str(i)+" "*9,
    print
    while playercards!=[] or (computercards!=[] and computercards1!=[] and computercards2!=[]):
        lis=[]
        thelist=[]
        playercard=input("Enter the card you would like to play")
        shape(playercards[(playercard-1)][0],playercards[(playercard-1)][1])
        if computercards!=[]:
            computer1=computerplay(computercards,playercards[playercard-1])
            lis=[playercards[playercard-1]]
            thelist.append(playercards[playercard-1])
            lis.append(computer1)
            thelist.append(computer1)
            manyshape(lis)
            if computer1[1]!=playercards[playercard-1][1]:
                newcard=[playercards[playercard-1]]
            else:
                newcard=Preccedenceorder(playercards[playercard-1],computer1)
            
        if computercards1!=[]:

            computer2=computerplay(computercards1,newcard[0])
            lis.append(computer2)
            thelist.append(computer2)
            manyshape(lis)
            if computer2[1]!=playercards[playercard-1]:
                newcard=Preccedenceorder(newcard[0],playercards[playercard-1])
            else:
                newcard=Preccedenceorder(newcard[0],computer2)
        if computercards2!=[]:
            computer3=computerplay(computercards2,newcard[0])
            lis.append(computer3)
            thelist.append(computer3)
            manyshape(lis)
        print "   Your      computer1  computer2  computer3"
        try:
            if lis[0][1]==lis[1][1]:
                a=Preccedenceorder(lis[0],lis[1])
                lis.remove(a[0])
            else:
                lis.remove(lis[1])
        except:
            pass
        try:
            if lis[0][1]==lis[1][1]:
                b=Preccedenceorder(lis[0],lis[1])
                lis.remove(b[0])
            else:
                lis.remove(lis[1])
        except:
            pass
        try:
            if lis[0][1]==lis[1][1]:
                c=Preccedenceorder(lis[0],lis[1])
                lis.remove(c[0])
            else:
                lis.remove(lis[1])
        except IndexError:
            pass
        if lis[0] in playercards:
            playercards.append(thelist[1])
            playercards.append(thelist[2])
            playercards.append(thelist[3])
            computercards.remove(thelist[1])
            computercards1.remove(thelist[2])
            computercards2.remove(thelist[3])
        elif lis[0] in computercards:
            computercards.append(thelist[0])
            computercards.append(thelist[2])
            computercards.append(thelist[3])
            playercards.remove(thelist[0])
            computercards1.remove(thelist[2])
            computercards2.remove(thelist[3])
        elif lis[0] in computercards1:
            computercards1.append(thelist[0])
            computercards1.append(thelist[1])
            computercards1.append(thelist[3])
            playercards.remove(thelist[0])
            computercards.remove(thelist[1])
            computercards2.remove(thelist[3])
        elif lis[0] in computercards2:
            computercards2.append(thelist[0])
            computercards2.append(thelist[1])
            computercards2.append(thelist[2])
            playercards.remove(thelist[0])
            computercards.remove(thelist[1])
            computercards1.remove(thelist[2])
        if len(playercards)<=14:
            manyshape(playercards)
            for i in range(1,len(playercards)+1):
                print str(i)+" "*9,
            print
        else:
            i=len(playercards)/14
            a=-14
            b=0
            for j in range(i):
                a=a+14
                b=b+14
                manyshape(playercards[a:b])
                for i in range(a+1,b+1):
                    print str(i)+" "*9,
                print 
            manyshape(playercards[b:])
            for i in range(b+1,b+len(playercards)%14+1):
                print str(i)+" "*9,
            print
    if playercards==[]:
        print "You Win"
    elif computercards==[]:
        print "You lost"
    elif computercards1==[]:
        print "You lost"
    else:
        print "You lost"
play(card,ty)
