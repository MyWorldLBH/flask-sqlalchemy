import datetime
from forms.user import RegisterForm
from flask import Flask
from flask import render_template, redirect
from data import db_session, users, jobs, news

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")

    @app.route('/register', methods=['GET', 'POST'])
    def reqister():
        form = RegisterForm()
        if form.validate_on_submit():
            if form.password.data != form.password_again.data:
                return render_template('register.html', title='Регистрация',
                                       form=form,
                                       message="Пароли не совпадают")
            db_sess = db_session.create_session()
            if db_sess.query(users.User).filter(users.User.email == form.email.data).first():
                return render_template('register.html', title='Регистрация',
                                       form=form,
                                       message="Такой пользователь уже есть")
            user = users.User(
                name=form.name.data,
                surname=form.surname.data,
                email=form.email.data,
                age=form.age.data,
                position=form.position.data,
                address=form.address.data,
                speciality=form.speciality.data,
            )
            user.set_password(form.password.data)
            db_sess.add(user)
            db_sess.commit()
            return redirect('/login')
        return render_template('register.html', title='Регистрация', form=form)

    @app.route("/")
    def index():
        db_sess = db_session.create_session()
        new = db_sess.query(news.News).filter(news.News.is_private != True)
        return render_template("index.html", news=new)


    # db_sess = db_session.create_session()
    #
    # user = db_sess.query(users.User).filter(users.User.id == 1).first()
    #
    # new = news.News(title="Вторая новость", content="Уже вторая запись!",
    #         user=user, is_private=False)
    # db_sess.add(new)
    # db_sess.commit()
    app.run()

    # J = jobs.Jobs()
    # J.team_leader = 1
    # J.job = "deployment of residential modules 1 and 2"
    # J.work_size = 15
    # J.collaborators = "2 3"
    # J.start_date = datetime.datetime.now()
    # J.is_finished = False
    #
    # db_sess = db_session.create_session()
    # db_sess.add(J)
    # db_sess.commit()





if __name__ == '__main__':
    main()