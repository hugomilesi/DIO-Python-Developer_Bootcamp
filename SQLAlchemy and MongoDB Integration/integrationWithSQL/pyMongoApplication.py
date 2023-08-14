import datetime
import pymongo

# Conectando a database do pymongo
connection_string = "mongodb+srv://hugo_milesi:anamae22@annetreecluster.gqmyxcf.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(connection_string)

# Criando um database
db = client['AnneTreeDB']
#collection = db.test_collection


# Adicionando Valores no DB

# === clientes ===
customers = db['Customers']

customer_data = [
    {
        "name": "Alice Johnson",
        "email": "alice@gmail.com",
        "address": "456 Elm St, City",
        "phone": "987-654-3210"
    },
    {
        "name": "Bob Smith",
        "email": "bob_j@hotmail.com",
        "address": "789 Oak St, City",
        "phone": "123-456-7890"
    }
]
# submetendo dados do cliente
customer_ids = customers.insert_many(customer_data).inserted_ids

# === Produtos ===
products = db['Products']

product_data = [
    {
        "name": "Bag Thalia",
        "description": "Toda cravejada, com 2 alças diferentes: uma feita de corrente cilíndrica (maior) e outra menor.",
        "price": 129.99,
        "available_colors": ["Black", "Brown", "Red"],
        "stock_quantity": 50
    },
    {
        "name": "Bag olho grego",
        "description": "Bag nuvem é hiper leve, possui alça dourada menor e alça fina preta maior.",
        "price": 79.99,
        "available_colors": ["Gray", "Blue", "Green"],
        "stock_quantity": 30
    }
]
# submetendo dados do produto
product_ids = products.insert_many(product_data).inserted_ids


# === Pedidos ===
orders = db['orders']

order_data = [
    {
        "customer_id": customer_ids[0],
        "products": [
            {"product_id": product_ids[0], "quantity": 2},
            {"product_id": product_ids[1], "quantity": 1}
        ],
        "order_date": datetime.datetime.utcnow(),
        "total_amount": 212.97,
        "status": "Enviado"
    },
    {
        "customer_id": customer_ids[1],
        "products": [
            {"product_id": product_ids[1], "quantity": 3}
        ],
        "order_date": datetime.datetime.utcnow(),
        "total_amount": 240.97,
        "status": "Pendente"
    }
]
#submetendo dados dos pedidos
order_ids = orders.insert_many(order_data).inserted_ids


# == Reviews ==
reviews = db.reviews
review_data = [
    {
        "product_id": product_ids[0],
        "customer_id": customer_ids[0],
        "rating": 5,
        "comment": "Adorei a bolsa! Muito espaçosa."
    },
    {
        "product_id": product_ids[1],
        "customer_id": customer_ids[1],
        "rating": 4,
        "comment": "Perfeita para ir a praia."
    }
]

reviews.insert_many(review_data)
client.close()

