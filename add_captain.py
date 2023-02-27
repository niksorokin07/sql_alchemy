from data.users import User

import data.db_session as db_session


db_session.global_init("db/blogs.db")
dbs = db_session.create_session()


user = User()
user.surname = "Scott"
user.name = "Ridley"
user.age = 21
user.position = "captain"
user.speciality = "research engineer"
user.address = "module_1"
user.email = "scott_chief@mars.org"
user.hashed_password = "cap"
dbs.add(user)


user = User()
user.surname = "Joan"
user.name = "Rowling"
user.age = 29
user.position = "trainee"
user.speciality = "doctor"
user.address = "module_1"
user.email = "joan.rowling@mars.org"
user.hashed_password = "Joan29"
dbs.add(user)


user = User()
user.surname = "Tom"
user.name = "Cruise"
user.age = 25
user.position = "middle"
user.speciality = "research engineer"
user.address = "module_1"
user.email = "tom.cruise@mars.org"
user.hashed_password = "25cruise"
dbs.add(user)


user = User()
user.surname = "Mathew"
user.name = "Peterson"
user.age = 22
user.position = "trainee"
user.speciality = "research engineer"
user.address = "module_1"
user.email = "mathew.peterson@mars.org"
user.hashed_password = "Mathew22"
dbs.add(user)


dbs.commit()
