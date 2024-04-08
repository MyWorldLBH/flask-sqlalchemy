import datetime

from flask import Flask
from data import db_session, users

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    #app.run()

    user = users.User()
    user.name = "Ridley"
    user.surname = "Scott"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineera"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "chelovechishefromzapad".__hash__()

    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()




if __name__ == '__main__':
    main()