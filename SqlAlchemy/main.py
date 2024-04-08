import datetime

from flask import Flask
from data import db_session, users, jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    #app.run()

    J = jobs.Jobs()
    J.team_leader = 1
    J.job = "deployment of residential modules 1 and 2"
    J.work_size = 15
    J.collaborators = "2 3"
    J.start_date = datetime.datetime.now()
    J.is_finished = False

    db_sess = db_session.create_session()
    db_sess.add(J)
    db_sess.commit()




if __name__ == '__main__':
    main()