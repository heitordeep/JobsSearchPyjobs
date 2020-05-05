from sqlalchemy import create_engine
from crawl_jobs.models import Base
from decouple import config


engine = create_engine(config("DATABASE"), echo=False)
Base.metadata.create_all(engine)
