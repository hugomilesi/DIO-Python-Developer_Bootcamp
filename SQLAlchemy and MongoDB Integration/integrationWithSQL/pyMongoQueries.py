import datetime
import pymongo
from pprint import pprint

# Conectando a database do pymongo
connection_string = "mongodb+srv://hugo_milesi:anamae22@annetreecluster.gqmyxcf.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(connection_string)
db = client['AnneTreeDB']

# Query 1
customers = db['Customers']
email_to_find = "alice@gmail.com"
query = {"email": email_to_find}
found_customers = customers.find(query)

print("\nRecuperando informações de produtos pelo email: ", email_to_find, '\n')
for customer in found_customers:
    pprint(customer)
    print("-------------------------")


# Query 2
orders = db['orders']
query = {"total_amount": {"$gt": 220.0}}
selected_orders = orders.find(query)

print('Recuperando o total de compras maiores que R$220', '\n')
for order in selected_orders:
    pprint(order)
    print("-------------------------")


# Query 3: Find reviews with a rating of 5 ===
print("Reviews com nota 5\n")
reviews = db['reviews']
query = {"rating": 5}
high_rated_reviews = reviews.find(query)

for review in high_rated_reviews:
    pprint(review)
    print("-------------------------")

# Query 4
customers = db['Customers']
name_to_find = "Bob Smith"  # Replace with the specific name you're searching for
query = {"name": name_to_find}
found_customers = customers.find(query)

print("Cliente com o nome de:", name_to_find, '\n')
for customer in found_customers:
    pprint(customer)
    print("-------------------------")


client.close()
