from sys import argv

import json

from pyspark.sql.functions import *
from pyspark.sql import Row, SparkSession
import pyspark.sql.types as st

#initialize parametrs
vol = 2000000
k = 0
schema = "Scheme add_info_2.json"
path = "proto.parquet"

#generate the data
#list of receipts atribu
# Add extra comments