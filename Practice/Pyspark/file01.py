from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DataExplorers").getOrCreate()
print(spark)