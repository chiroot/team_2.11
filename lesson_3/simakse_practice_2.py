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

#read the parametrs
if len (argv) > 1:
    vol = int(argv[1])
    k = int(argv[2])
    schema = argv[3]
    path = argv[4]


#generate the data
#list of receipts atributes