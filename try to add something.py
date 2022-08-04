# Databricks notebook source
info = dbutils.widgets.get("info")
# info = {"qwe": "ewq"}

# COMMAND ----------

from pymongo import MongoClient
connectionString= "mongodb+srv://scofield1210:0MlW0YYxMGZGDI0a@test-cluster.h0y0u.gcp.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connectionString)
db = client['sample_airbnb']

# COMMAND ----------

from datetime import datetime

db['test_insert'].insert_one({'info': info, 'time': datetime.now(), 'trial': True})

# COMMAND ----------



# COMMAND ----------


