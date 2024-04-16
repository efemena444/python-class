bidder = {"john":100,"mike":200,"joshua":400,"dean":1000}
highestBidder = max(bidder,key=bidder.get)
highest_bid=bidder[highestBidder]
print(highest_bid)