from sqlalchemy import *
import datetime
import sqlalchemy
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash  
from .db_session import SqlAlchemyBase

class Jobs(SqlAlchemyBase):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    team_leader = Column(Integer, ForeignKey("users.id"))
    job = Column(String)
    work_size = Column(Integer)
    collaborators = Column(String)
    start_date = Column(DateTime, default=datetime.datetime.now, nullable=True)
    end_date = Column(DateTime, default=datetime.datetime.now, nullable=True)
    is_finished = Column(Boolean)
    user = orm.relationship("User")
