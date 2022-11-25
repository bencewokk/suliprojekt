x=1
a=1
szamosz1=int(input("elso oszto"))
szamosz2=int(input("masodik oszto"))
osztando=int(input("range"))
while x!=osztando:
    e=0
    #print (x)
    y=x/szamosz1
    z=x/szamosz2
    #print (y)
    b=(y.is_integer())
    d=(z.is_integer())
    if b==True:
        print ("a(z)", a,"." , szamosz1 ,"al/el oszthato szam:",x)
        a=a+1
        e=1
        if d==True:
            print("               es", szamosz2 ,"val/vel is")
    if e==1:
        print("")
    x=x+1
    
    
    
    
    
