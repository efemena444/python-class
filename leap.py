year = (int(input("enter the current year:")))
if (year%4) == 0:
    if (year%100)==0:
        if (year%400)==0:
            print("leap")
        else:
            print("not leap")
    else:
        print("not leap")
else: 
    print("not leap")                
       
                
    
                    
           