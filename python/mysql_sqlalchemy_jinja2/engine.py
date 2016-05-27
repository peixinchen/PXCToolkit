from sqlalchemy import create_engine
import settings


engine = create_engine('{driver}://{user}:{password}@{host}:{port}/{instance}?charset=utf8'.format(
    **settings.DB
), echo=True)
