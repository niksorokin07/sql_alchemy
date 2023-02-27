from data.users import User
from data.jobs import Jobs

import data.db_session as db_session


db_session.global_init("db/blogs.db")
dbs = db_session.create_session()


jobs = Jobs()
user = dbs.query(User).filter(User.position == 'captain').first()
jobs.team_leader = user.id
jobs.job = 'deployment of residential modules 1 and 2'
jobs.work_size = 15
jobs.collaborators = '2, 3'
jobs.is_finished = False
dbs.add(jobs)


dbs.commit()
