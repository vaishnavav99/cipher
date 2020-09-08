x="n"
a=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

while(x!='y'and x!='Y'):
    def exitt():
        return input("Do u want to exit y/n ?\t")
    
    
    def encode():
        t = input("text \t")
        result=""
        if all(j.isalpha() and j.isspace() for j in t):
            print("invalid text")
            x=exitt()
        else:
            s = int(input("shift \t"))
            T=t.upper()
            l= len(t)
            for i in range (l):
                w=T[i]
                if w==' ':
                    result+=" "
                    continue
                n=a.index(w)
                result+=a[(n+s)%26]
            print("Encoded Result ",result)
            

    def decode():
        t = input("text \t")
        result=""
        if all(j.isalpha() and j.isspace() for j in t):
            print("invalid text")
            
        else:
            s = int(input("shift \t"))
            T=t.upper()
            l= len(t)
            for i in range (l):
                w=T[i]
                if w==' ':
                    result+=" "
                    continue
                n=a.index(w)
                result+=a[(n-s)%26]
            print("Decoded Result ",result)
           

    
    c=input("select \n 1. Encode \n 2. Decode \n \t")
    if(c=="1"):
        encode()
        x=exitt()
    elif (c=='2'):
        decode()
        x=exitt()
    else:
        print("invalid Choice")
    
        
        

    


    