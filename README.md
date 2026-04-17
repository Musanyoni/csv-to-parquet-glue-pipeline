# csv-to-parquet-glue-pipeline
## Overview
An end-to-end, production-style data engineering pipeline built on AWS that ingests raw CSV data from Amazon S3, performs scalable transformations using PySpark in AWS Glue, and stores optimized Parquet datasets for efficient querying with Amazon Athena. The pipeline enables fast, serverless analytics and delivers actionable insights through interactive dashboards in Amazon QuickSight.

---

## Architecture
![Architecture Diagram](screenshots/architecture.png)

:

🛠️ AWS Services Used
This project uses a fully serverless AWS stack to build a scalable data pipeline:
Amazon S3 – Stores raw CSV data ,processed Parquet datasets and athena query results.
AWS Glue – Performs ETL using PySpark to transform raw csv data to parquet format.
Glue Data Catalog – Manages table schemas and metadata.
Amazon Athena – Enables SQL-based querying directly on S3.
Amazon QuickSight – Creates interactive dashboards and visualizations
AWS IAM – Controls secure access across services
Amazon CloudWatch – Monitors jobs and logs pipeline activity
Glue Crawlers  – Automatically detects schema and updates the catalog 

---

## Dataset
- **Source:** CSV file containing sales data
- **Columns:**
  - `orderid` - Unique order identifier
  - `customerid` - Unique customer identifier
  - `productid` - Unique product identifier
  - `category` - Product category
  - `quantity` - Number of items ordered
  - `unitprice` - Price per unit
  - `totalprice` - Total order price
  - `date` - Date of order

---

## Steps to Reproduce

### Step 1: Upload Raw  Data to S3
- Create an S3 bucket
- Upload CSV file to `s3://your-bucket/raw_data/` folder

### Step 2: Run AWS Glue ETL Job
- Create a Glue job using the PySpark script in `glue_job/`
- Set source as `s3://your-bucket/raw_data/`
- Set destination as `s3://your-bucket/parquet_data/`
- Run the job to convert CSV to Parquet format

### Step 3: Run Glue Crawler
- Create a Glue crawler pointing to `s3://your-bucket/parquet_data/`
- Run the crawler to catalog the Parquet data
- Verify database and tables appear in Glue Data Catalog

### Step 4: Query Data with Athena
- Open Athena and select your Glue database
- Set query results location to `s3://your-bucket/query_results/`
-Make sure S3 bucket is in the same region with amazon athena
- Run SQL queries to verify and explore the data

### Step 5: Visualise with QuickSight
- Connect QuickSight to Athena
-quicksight and athena should also be in the same region.
- Select your database and table
- Build interactive dashboard with charts and KPIs

---

## Athena Query Examples to check paquet file was loaded in s3 bucket

SELECT *
FROM sales_db.parquet_data
LIMIT 10;


SELECT COUNT(*) AS total_rows
FROM parquet_table;

📈 QuickSight Dashboard
📈 Sales Over Time (Line Chart) showing total revenue (totalprice) across dates
Highlights trends, patterns, and peak sales periods
Supports data-driven insights and performance analysis
Fields:
X-axis: date
Y-axis: totalprice (SUM)





---

## Key Learnings
- How to build an ETL pipeline using AWS Glue and PySpark
- How to store and organise data efficiently in Amazon S3
- How to convert CSV to Parquet for better query performance
- How to query data using Amazon Athena
- How to build interactive dashboards in Amazon QuickSight
- How to manage IAM permissions across AWS services
