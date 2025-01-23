# Academic Patent Analysis Architecture

## Table of Contents 📋
- [Overview](#overview)
- [Installation](#installation)
- [Architecture](#architecture)
- [Contact](#contact)

---

## 🚀 Overview

The goal of this project is to analyze academic patents extracted from Scopus via a Kafka producer, with the data stored in MinIO. The architecture follows a Medallion model, with data transformations performed through a Spark cluster consisting of one Spark master and two worker nodes. The transformations are executed within an integrated JupyterLab environment in Docker. After the transformation, the data is stored in MinIO in the form of Parquet files. Finally, the transformed data is transferred to ClickHouse, and dashboards are created using Power BI.

### Key Features:
- **MinIO Storage**: Raw data is stored in MinIO, an object storage service, for secure and scalable management.
- **Spark Cluster**: Data transformation is handled by a Spark cluster with one master node and two worker nodes, ensuring distributed processing for large datasets.
- **Kafka Integration**: Data is extracted from Scopus using a Kafka producer, enabling efficient and scalable data streaming.
- **JupyterLab Integration**: Data transformations are performed interactively within JupyterLab, integrated in a Docker environment, offering flexibility and ease of use.
- **ClickHouse Integration**: Transformed data is loaded into ClickHouse for fast, scalable analytics.
- **Power BI Dashboards**: Data visualizations and interactive dashboards are created using Power BI, enabling insights and reporting.


---


## ⚙️ Installation

Follow the steps below to set up the project on your local machine or AWS environment.



### 1. **Clone the repository**:
Clone the project repository to your local machine using the following command:

     ```bash
     git clone git@github.com:Samiha128/Academic-Patent.git
     cd Academic-Patent

### 2. Set up AWS services:
   This project leverages several AWS services. Here's how to set them up:
   
#### EC2 Instance Setup:

  Create an EC2 instance:
  Launch an EC2 instance in your desired AWS region (preferably t2.micro for Free Tier usage).
#### Connect to your EC2 instance:

Use SSH to connect to your instance:

    ```bash
      ssh -i "path/to/your/file.pem" ec2-user@<your-ec2-public-ip>
      


#### Installing Kafka on EC2

1. **Download and extract Kafka**:

    ```bash
    wget https://archive.apache.org/dist/kafka/3.6.1/kafka_2.12-3.6.1.tgz
    tar -xvf kafka_2.12-3.6.1.tgz
    cd kafka_2.12-3.6.1
    ```

2. **Install Java** (Kafka requires Java 17 or above):

    ```bash
    sudo yum install java-17-amazon-corretto
    java -version
    ```

3.**Starting Zookeeper and Kafka:**
  ```bash
       bin/zookeeper-server-start.sh config/zookeeper.properties

  ```
In a new terminal session, start the Kafka server:
  ```bash
       export KAFKA_HEAP_OPTS="-Xmx256M -Xms128M"
       cd kafka_2.12-3.6.1
       bin/kafka-server-start.sh config/server.properties


  ```
Note: You may need to modify the server.properties file to set your EC2's public IP address. 
   ```bash
       sudo nano config/server.properties

  ```
Change the line for ADVERTISED_LISTENERS to your EC2 instance's public IP address:

```bash
      ADVERTISED_LISTENERS=PLAINTEXT://your-ec2-public-ip:9092
  ```
4.**Creating a Kafka Topic:**

In a new terminal session, create a Kafka topic for stock market data:
```bash
      cd kafka_2.12-3.6.1
     bin/kafka-topics.sh --create --topic stock_market_data --bootstrap-server your-ec2-public-ip:9092 --replication-factor 1 --partitions 1

  ```
5.**Starting Producer and Consumer:**
Start a producer to simulate sending stock market data:
```bash
     bin/kafka-console-producer.sh --topic stock_market_data --bootstrap-server your-ec2-public-ip:9092

  ```
Start a consumer to listen to the topic:
```bash
     bin/kafka-console-consumer.sh --topic stock_market_data --bootstrap-server your-ec2-public-ip:9092

  ```
**Create an S3 Bucket**

**AWS Glue Crawler Setup**

1.Create a Glue Crawler

2.Create a Glue Database

**Set up Athena**

## Architecture
![Architecture](./images/architecture.png)

## contact

Feel free to contribute to this project by opening issues or submitting pull requests. Your input is welcome!

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/samiha-el-mansouri-27505b250/)


