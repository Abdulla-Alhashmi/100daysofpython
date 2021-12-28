#from art import logo
#print(logo)
#the code above is used for replit
print("Welcome to the secret auction program")
bid_dict = []
def secret_bids():
    dict = {}
    dict['name'] = bidder
    dict['bid'] = amount
    bid_dict.append(dict)
cont = 'y'
while cont == 'y':
      bidder = input("What is your name? ")
      amount = int(input("What's your bid? "))
      secret_bids()
      cont = input('Are there any other bidders?\n y/n ')
      #clear() <-- this is to be used in replit
score = [0]     
for i in range(0, len(bid_dict)):
    if bid_dict[i]['bid'] >= score[0]:
        score[0] = i
winner = bid_dict[score[0]]['name']
value = bid_dict[score[0]]['bid']
print(f"the winner is {winner} by bidding {value}")
    
    
    
  
