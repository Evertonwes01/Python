from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import Column, select, func
from sqlalchemy import inspect
from sqlalchemy import create_engine
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"
    # atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    # criando relacionamento entre as classes
    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(50), nullable=False)
    id_user = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    # criando relacionamento
    user = relationship(
        "User", back_populates="address"
    )

    def __repr__(self):
        return f"Address(id={self.id}, email_address={self.email_address})"


print(User.__tablename__)
print(Address.__tablename__)

# conexão com banco de dados
engine = create_engine("sqlite://")

# criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

# investiga o esquema de banco de dados
insp = inspect(engine)
# Retorna True se encontrar a tabela chamada "user_account" e False se não encontrar a tabela
print(insp.has_table("user_account"))
# Retorna as tabelas que existem no banco
print(insp.get_table_names())
# Retorna o nome (esquema) do banco de dados
print(insp.default_schema_name)

# criando os usuarios
with Session(engine) as session:
    juliana = User(
        name='juliana',
        fullname='Juliana Mascarenhas',
        address=[Address(email_address='juliana.m@gmail.com')]
    )

    sandy = User(
        name='sandy',
        fullname='Sandy Cardoso',
        address=[Address(email_address='sandycardoso@gmail.com'),
                 Address(email_address='sandyca001@hotmail.com')]
    )

    patrick = User(name='patrick', fullname='patrick Cardoso')

    # enviando para o BD (persistência de dados)
    session.add_all([juliana, sandy, patrick])

    session.commit()

stmt = select(User).where(User.name.in_(['juliana','sandy','patrick']))
print('=' * 100)
print('\nRecuperando usuários a partir de condição de filtragem:\n')
for user in session.scalars(stmt):
    print(user)

stmt_address = select(Address).where(Address.id_user.in_([2]))
print('=' * 100)
print('\nRecuperando os endereços de email de Sandy:\n')
for address in session.scalars(stmt_address):
    print(address)

stmt_order = select(User).order_by(User.fullname.desc())
print('\nRecuperando info de maneira ordenada\n')
for result in session.scalars(stmt_order):
    print(result)

stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)
print('\n')
for result in session.scalars(stmt_join):
    print(result)

# print(select(User.fullname, Address.email_address).join_from(Address, User))

connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
print("\nExecuntando apartir da connection\n")
for result in results:
    print(result)

stmt_count = select(func.count('*')).select_from(User)
print("\nTotal de instâncias em User\n")
for result in session.scalars(stmt_count):
    print(result)

#encerrando a session
session.close()
