from sqlalchemy import create_engine, Column, Integer, String, Float, Text, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import declarative_base
import datetime

# Define the schema using SQLAlchemy
Base = declarative_base()

class Customer(Base):
    __tablename__ = 'Customers'

    CustomerID = Column(Integer, primary_key=True, autoincrement=True)
    FirstName = Column(String(40))
    LastName = Column(String(40))
    Email = Column(String(40))
    Address = Column(String(150))

    orders = relationship('Order', back_populates='customer')

    def __repr__(self):
        return f"Customer(CustomerID={self.CustomerID}, FirstName='{self.FirstName}', LastName='{self.LastName}', Email='{self.Email}', Address='{self.Address}')"


class Category(Base):
    __tablename__ = 'Categories'

    CategoryID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(40))

    products = relationship("Product", back_populates="category")

    def __repr__(self):
        return f"Category(CategoryID={self.CategoryID}, Name='{self.Name}')"

class Product(Base):
    __tablename__ = 'Products'

    ProductID = Column(Integer, primary_key=True, autoincrement=True)
    CategoryID = Column(Integer, ForeignKey('Categories.CategoryID'))
    Name = Column(String(40))
    Description = Column(Text(200))
    Price = Column(Float)

    category = relationship("Category", back_populates="products")
    order_items = relationship("OrderItem", back_populates="product")

    def __repr__(self):
        return f"Product(ProductID={self.ProductID}, Name='{self.Name}', Price={self.Price})"


class Order(Base):
    __tablename__ = 'Orders'

    OrderID = Column(Integer, primary_key=True, autoincrement=True)
    CustomerID = Column(Integer, ForeignKey('Customers.CustomerID'))
    OrderDate = Column(DateTime)
    TotalAmount = Column(Float)

    customer = relationship("Customer", back_populates='orders')
    order_items = relationship('OrderItem', back_populates='order')

    def __repr__(self):
        return f"Order(OrderID={self.OrderID}, TotalAmount={self.TotalAmount}, OrderDate='{self.OrderDate}')"


class OrderItem(Base):
    __tablename__ = 'OrderItems'

    OrderItemID = Column(Integer, primary_key=True, autoincrement=True)
    OrderID = Column(Integer, ForeignKey('Orders.OrderID'))
    ProductID = Column(Integer, ForeignKey('Products.ProductID'))
    Quantity = Column(Integer)
    Subtotal = Column(Float)

    order = relationship("Order", back_populates='order_items')
    product = relationship('Product', back_populates='order_items')

    def __repr__(self):
        return f"OrderItem(OrderItemID={self.OrderItemID}, Quantity={self.Quantity}, Subtotal={self.Subtotal})"


# Establish a connection to the database
engine = create_engine("sqlite:///AnneTreeDB.db")

# Create the tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Adicionando Clientes
customer1 = Customer(FirstName="John",
                     LastName="Doe",
                     Email="john@gmail.com",
                     Address="Estrada do pau-ferro 65")

customer2 = Customer(FirstName='jane',
                     LastName='Doe',
                     Email='jane_d@gmail.com',
                     Address='Largo do Machado 45')

# Categorias
category1 = Category(Name="clutch")
category2 = Category(Name='Basket Bag')
category3 = Category(Name='Cross Body Bag')

# Adicionando Produtos
product1 = Product(CategoryID=3, Name="Bag Thalia",
                   Description="Toda cravejada, com 2 alças diferentes: uma feita de corrente cilíndrica (maior) e outra menor.",
                   Price=129.99)

product2 = Product(CategoryID=2, Name="Bag Olho Grego",
                   Description="Bag nuvem é hiper leve, possui alça dourada menor e alça fina preta maior.",
                   Price=79.99)

product3 = Product(CategoryID=1, Name="Bag Ruby",
                   Description="Bag metalassê, com detalhes prateados, possui alça ajustável", Price=99.90)

# Criando Pedidos
order1 = Order(CustomerID=1,
               OrderDate=datetime.datetime(2023,8, 14),
               TotalAmount=129.99)

order2 = Order(CustomerID=2,
               OrderDate=datetime.datetime(2023,10,7),
               TotalAmount=179.99)



# Criando detalhes dos pedidos
order_item1 = OrderItem(OrderID=1,
                        ProductID=1,
                        Quantity=1,
                        Subtotal=129.99)

order_item2 = OrderItem(OrderID=2,
                        ProductID=3,
                        Quantity=2,
                        Subtotal=199.80)


session.add_all([customer1, customer2,
                 category1, category2, category3,
                 product1, product2, product3,
                 order1, order2,
                 order_item1, order_item2])
session.commit()



#Base.metadata.drop_all(bind=engine)
#session.commit()

session.close()
