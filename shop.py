import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
#########################################################
'''
fil = open("data.txt",'r')

data = fil.read()
dataset=[]
data = data.split(',')
for values in data:
    dataset.append(values.strip('\n'))


'''
dataset=[["Bread", "Milk", "Beer"],
 ["Bread", "Diapers", "Eggs"],
 ["Milk", "Diapers", "Beer", "Cola"],
 ["Bread", "Milk", "Diapers", "Beer"],
 ["Bread", "Milk", "Cola"]]

#########################################################
te=TransactionEncoder()
te=te.fit(dataset)           # Reads unique values 
te_ary=te.transform(dataset) # Converts array into a matrx
df=pd.DataFrame(te_ary, columns=te.columns_)

#########################################################
frequent_items=apriori(df,min_support=0.6,use_colnames=True)
frequent_items
rules = association_rules(frequent_items,
                         metric= 'confidence',
                        min_threshold=0.5)
#########################################################
# Shopping Part
def item():
  print("Items available are-", available)
  print("Your cart contains",cart)
  buy=input("What do you want to buy? \nItem:")
  buy=buy.title()
  shop(buy)
  print("--------------------------------")


def shop(buy):
    if buy in available:
        cart.append(buy)
        available.remove(buy)
        print(buy+" is added to the list")
        cartitem=[buy]
        rec=[list(x) for x in rules[rules['antecedants'].apply(lambda x: set(cartitem).issubset(set(x)))]['consequents']]
        for values in rec:
            for value in values:
                if value in cart:
                    rec.remove(values)
        print(rec)
        print("Recommended:",rec)
    elif buy in cart:
      print("Item already in cart!")
      item()
    elif buy =='Exit':
        want_to_buy = False
        print("You bought ",cart)
        exit()
        
    else:
        print("Item not in list")
        item()

available= ['Diapers', 'Milk', 'Cola', 'Bread', 'Beer', 'Eggs']
cart=[]
want_to_buy=True
while(want_to_buy==True):
    item()    
    if available==[]:
        print("You have bought the whole shop!!")
        want_to_buy=False