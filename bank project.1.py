obal=int(input("enter a bal:"))
ttype=input("enter type:")
tamt=int(input("enter a amount:"))
cbal=0
if ttype=="w" or ttype=="W":
    if tamt>obal:
        print("ins.Fund")
    elif tamt==obal:
        print("Plz.M.M.Bal")
    else:
        cbal=obal-tamt
        print(cbal)
elif ttype=="d" or ttype=="D":
    if tamt>=50000:
        print("Req.PAN")
    else:
        cbal=obal+tamt
        print(cbal)
else:
    print("invalid choice")'''
'''username=input("enter user name:")
password=int(input("enter password:"))
channel=input("enter a ch:")
if username==krishna:
    if password!="1234":
        print("password in correct")
    elif channel==N:
         print("netflix")
    elif channel==A:
         print("aha")
    elif channel==H:
         print("hotstar")
    elif channel==M:
         print("amazon")
    else:
         print("no channel")
else:
   print("username incorrect")
channels={'a','h','w','f'}
username=input("enter user name:")
if username=='krishna':
    if password==(input("enter password:")):
        if channels==(input("enter cha:")):
            if channels(0):
                print("open aha")
            elif channels=='h':
                print("open hotstar")
            elif channels=='w':
                print("open amazon")
            elif channels=='f':
                print("open flipkart")
            else:
                print("the ott not available")
    else:
        print("pass in correct")
        
else:
    print("user name in correct")

        














