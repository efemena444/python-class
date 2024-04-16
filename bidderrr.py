
def highestbid(bidding):
    biddingrecord = 0
    if biddingrecord >bidding:
       bidding= "break"
    
    






bid ={}
finishedbidding = False
while not finishedbidding:
     name =input("what is your name:")
     bidPrice=int(input("what is the bid:"))
     bid[name]= bidPrice
     otherbidders=input("are they other bidders?:type yes or no")
     if otherbidders == "yes":
         clear()
     elif otherbidders == "no":
         finishedbidding = True
         
             
     


    
    