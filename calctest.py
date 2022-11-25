szamok=[320,32,100,20]
cmnds=["/","+","-"]

osztassz=cmnds.count("/")
szorzassz=cmnds.count("x")

osztasind=0
szorzasind=0

while szorzassz+osztassz!=0:
    print(szorzassz+osztassz)
    if osztassz!=0:
        osztasind=cmnds.index("/")
    elif szorassz!=0:
        szorzasind=cmnds.index("x")
    #szamolas
    if szorzasind<osztasind:
        szam1=szamok[szorzasind]
        szam2=szamok[szorzasind+1]

        eredmeny=szam1*szam2

        szamok[szorzasind]=eredmeny
        szamok[szorzasind+1]=0

        cmnds[szorzasind]=0

    else:
        szam1=szamok[osztasind]
        szam2=szamok[osztasind+1]

        eredmeny=szam1/szam2

        szamok[osztasind]=eredmeny
        szamok[osztasind+1]=0
        cmnds[osztasind]=""
print(szamok)
