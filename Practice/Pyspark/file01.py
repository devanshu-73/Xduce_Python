import findspark
findspark.init()
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("CSV Reader") \
    .getOrCreate()

df = spark.read.csv('dataset.csv',header = True, inferSchema = True)

df.show()