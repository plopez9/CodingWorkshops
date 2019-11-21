import pandas as pd

from sqlalchemy import create_engine, select, Table, MetaData

files = "Brazil.csv"

data = pd.read_csv(files, encoding = "ISO-8859-1")

print(data.isnull().values.any())

# engine = create_engine(r"sqlite:///C:\Users\Pedro\Desktop\Programs\Rest-Framework-Workshop\restWorkshop\Brazil.db")
#
# data.to_sql("Fires", con = engine, if_exists= "replace", chunksize = 10)
