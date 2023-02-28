from data import db_session
from data.jobs import Jobs
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    info = []
    for el in jobs:
        time = f'{round((el.end_date - el.start_date).total_seconds() / 3600)} hours'
        team_leader = el.team_leader
        info.append([el.job, team_leader, time, el.collaborators, el.is_finished])
    return render_template('work_logs.html', jobs=info)


if __name__ == '__main__':
    db_session.global_init("db/blogs.db")
    app.run(port=8080, host='127.0.0.1')
