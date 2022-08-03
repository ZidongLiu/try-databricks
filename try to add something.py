# Databricks notebook source
from src.helpers import get_sum_from_1_to_10000

# COMMAND ----------

test_rdd = sc.parallelize(range(10000))

# COMMAND ----------

test_rdd.map(get_sum_from_1_to_10000).first()

# COMMAND ----------

1 + 1 == 3

# COMMAND ----------

1 + 2

# COMMAND ----------


