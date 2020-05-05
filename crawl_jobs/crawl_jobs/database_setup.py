from decouple import config
from sqlalchemy import create_engine

from crawl_jobs.models import Base

engine = create_engine(config('DATABASE'), echo=True)
Base.metadata.create_all(engine)
