p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("enter you comment:")

if((p1 in message)or (p2 in message) or (p3 in message) or (p4 in message)):
    print("this comment is spam")

else:
    print("this comment is not a spam ")