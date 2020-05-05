from sqlalchemy.orm import sessionmaker

from crawl_jobs.database_setup import engine
from crawl_jobs.models import Job


class CrawlJobsPipeline:

    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()
  
  
    def process_item(self, item, Spider):
        description = item.pop('description')

        jobs = Job(**item, description=' | '.join(description))

        try:
            self.session.add(jobs)
            self.session.commit()
        except:
            self.session.rollback()
