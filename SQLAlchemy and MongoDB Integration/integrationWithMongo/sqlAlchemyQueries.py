# schema.py
from sqlAlchemyApplication import *
from sqlalchemy import select
from sqlalchemy import func
from sqlalchemy import desc


# Create an engine
engine = create_engine("sqlite:///AnneTreeDB.db")

# Establish a session
Session = sessionmaker(bind=engine)
session = Session()

# Make queries

print('== Recuperando Clientes com o sobrenome Doe ==\n')
# Example query: Retrieve all customers
stmt = select(Customer).where(Customer.LastName.in_(["Doe"]))
for client in session.scalars(stmt):
    print(client)
print('-'*80)
session.commit()


print('\n== Recuperandoas as categorias das bolsas ==\n')
stmt = (
    select(Product.Name, Category.Name)
    .join(Category)
)
products_with_categories = session.execute(stmt).fetchall()
for product_name, category_name in products_with_categories:
    print(f"Product: {product_name}, Category: {category_name}")

print('-'*80)
session.commit()


print("\n== Recuperando a Bolsas do tipo 'clutch' ==\n")
# Query customers and their order count, showing customers with the highest order count first
# Query products within a specific category
stmt = (
    select(Product, Category.Name)
    .join(Category)
    .where(Category.Name == 'clutch')
)
products_in_category = session.execute(stmt).fetchall()
for product, category_name in products_in_category:
    print(f"Category: {category_name}, Product ID: {product.ProductID}, Name: {product.Name}, Price: {product.Price:.2f}")
print('-'*80)
session.commit()















Base.metadata.drop_all(bind=engine)
session.commit()
# Close the session when done
session.close()



