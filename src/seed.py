import pandas as pd
from sqlalchemy import create_engine
conn_string = 'postgresql://localhost/yelp_lunch'
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/ledeprogram/courses/master/foundations/mapping/tilemill/yelp-lunch-nyc.csv')
conn = create_engine(conn_string)
df.to_sql('restaurants', conn, if_exists='replace', index_label = 'id')