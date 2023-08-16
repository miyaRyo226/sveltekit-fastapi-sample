from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine
from sqlalchemy_utils import database_exists, create_database

class Movies(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    genre: str
    sensitive: Optional[bool] = False


movie_1 = Movies(name="Fight Club", genre="Thriller",sensitive=True)

engine = create_engine("postgresql://postgres:postgres@database:5432/testdb")
if not database_exists(engine.url):
    create_database(engine.url)

SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    session.add(movie_1)
    session.commit()