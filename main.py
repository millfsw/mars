from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config["SECRET_KEY"] = "yandexlyceum_secret_key"


def main():
    db_session.global_init("db/mars.db")
    session = db_session.create_session()
    print(list(session.query(User)))
    # user1 = User()
    # user1.surname = "Scott"
    # user1.name = "Ridley"
    # user1.age = "21"
    # user1.position = "captain"
    # user1.speciality = "research engineer"
    # user1.addres = "module_1"
    # user1.email = "scott_chief@mars.org"
    # user1.hashed_password = "asdfg"
    # session.add(user1)

    # user2 = User()
    # user2.surname = "Brown"
    # user2.name = "Jons"
    # user2.age = "22"
    # user2.position = "assistant"
    # user2.speciality = "help members"
    # user2.addres = "module_1"
    # user2.email = "brown35@mars.org"
    # user2.hashed_password = "hjklo"
    # session.add(user2)

    # user3 = User()
    # user3.surname = "Smith"
    # user3.name = "Michael"
    # user3.age = "23"
    # user3.position = "pilot"
    # user3.speciality = "flies into space"
    # user3.addres = "module_1"
    # user3.email = "smithmary46@mars.org"
    # user3.hashed_password = "qwery"
    # session.add(user3)

    session.commit()
    # app.run()


if __name__ == "__main__":
    main()
