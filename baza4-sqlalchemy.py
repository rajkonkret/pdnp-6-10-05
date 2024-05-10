# ORM - dostęp do bazy w sposób obiektowy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


# echo=True - logi z bazy danych
engine = create_engine('sqlite:///mydatabase.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
ssesion = Session()

new_user = User(name="Jan Kowalski", age=30)
ssesion.add(new_user)  # INSERT INTO users (name, age) VALUES (?, ?)
ssesion.commit()
ssesion.close()

users = ssesion.query(User).all()  # SELECT users.id AS users_id, users.name AS users_name, users.age AS users_age
for user in users:
    # print(user)
    print(user.name)

# <__main__.User object at 0x000001FC3386F380>
# <__main__.User object at 0x000001FC3386F320>
# Jan Kowalski
# Jan Kowalski
# Jan Kowalski
