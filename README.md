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

Follow the steps below to set up the project on your local machine .


### 1. **Clone the repository**:
Clone the project repository to your local machine using the following command:

   
     git clone git@github.com:Samiha128/Academic-Patent.git
     cd Academic-Patent
    
### 2.**Start the Docker Containers**:
Navigate to the project directory and run the following command to bring up the Docker containers in detached mode:

    docker-compose up -d
### 3.Launch the Development Container



## Architecture
![Architecture](./images/architecture.png)

## contact

Feel free to contribute to this project by opening issues or submitting pull requests. Your input is welcome!

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/samiha-el-mansouri-27505b250/)


