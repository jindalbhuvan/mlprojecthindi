import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql
from sqlalchemy import create_engine

load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv('db')



def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        engine = create_engine('mysql+pymysql://root:19oct2004@localhost:3306/college')
        
        logging.info("Connection Established: %s",engine)
        df=pd.read_sql_query('select * from student',engine)
        print(df.head())

        return df

        pass
    except Exception as ex:
        raise CustomException(ex)

