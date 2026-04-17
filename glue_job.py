import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import trim, col, to_date
from pyspark.sql.types import StringType

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("s3://musa-data-pipeline-demo/raw-data/sales_data_5MB.csv")

df = df.withColumn("Date", to_date(col("Date"), "yyyy-MM-dd"))

for field in df.schema.fields:
    if isinstance(field.dataType, StringType):
        df = df.withColumn(field.name, trim(col(field.name)))

df.write \
  .mode("overwrite") \
  .parquet("s3://musa-data-pipeline-demo/processed-data/sales/")

job.commit()
