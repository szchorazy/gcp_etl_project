# GCP Data Engineering project
The aim of this project is to analyze the Supply Chain DataSet used by DataCo Global. 
The supply chain plays a vital role for the company. Understanding which products generate the highest profit, which categories are most frequently ordered, and the reasons behind late deliveries can provide valuable insights. 
This information enables the company to take proactive measures to address these issues effectively.

The analysis of the supply chain data will be conducted using the following technologies and tools:

* Cloud Storage 🪣 to store and manage the supply chain data

* Compute Engine 💽 to host and run the Mage

* Mage 🧙‍♂️ for Extract, Transform, Load (ETL) processes

* BigQuery 🔍 as our data warehouse for storing and querying the transformed supply chain data

* Looker📈 as our business intelligence and data visualization platform

💡Additionally, a key objective of this project is to gain hands-on experience with the Mage tool. 
Since Apache Airflow is widely used and well-known in the industry, I wanted to explore something new, and Mage seemed like a perfect fit for this purpose.

![285978625-6cada155-6df3-4497-8410-ab0d9f4d0b09](https://github.com/user-attachments/assets/8bdb53eb-3ffb-4440-93d0-4684fdfd8539)

# GCS 🪣

Create a new bucket, upload the csv file. Change the permissions of the bucket (permissions -> edit access control -> Fine-grained), edit the access of the csv file to make it publicly available

![Zrzut ekranu 2024-12-11 162927](https://github.com/user-attachments/assets/953c20ce-958b-4675-baca-ec7e92426458)

# Compute Engine 💽

Create a new instance, e.g. Machine type: e2-standard-4

SSH into your VM and run these commands to install Python, pip, wget, pandas, Google Cloud Library, Google Cloud BigQuery library

`sudo apt-get install update`

`sudo apt-get install python3-distutils`

`sudo apt-get install python3-apt`

`sudo apt-get install wget`

`wget https://bootstrap.pypa.io/get-pip.py`

`sudo python3 get-pip.py`

`sudo pip3 install pandas`

`sudo pip3 install google-cloud`

`sudo pip3 install google-cloud-bigquery`

Run `sudo pip3 install mage-ai` to install Mage on your VM.

To start a new Mage project: `mage start supply_chain_de_project` (you will see: `Checking port 6789...` if you restart Mage, the port may change e.g. `Checking port 6790...`)

Create a new firewall rule for the port 6789

![Zrzut ekranu 2024-12-19 200644](https://github.com/user-attachments/assets/a5440a83-5e08-47fd-99d8-6a10b1596f94)

# Mage 🧙
[Mage](https://www.mage.ai/) is a hybrid framework for transforming and integrating data. It combines the best of both worlds: the flexibility of notebooks with the rigor of modular code.

* Extract and synchronize data from 3rd party sources.
* Transform data with real-time and batch pipelines using Python, SQL, and R.
* Load data into your data warehouse or data lake using our pre-built connectors.
* Run, monitor, and orchestrate thousands of pipelines without losing sleep.

Plus hundreds of enterprise-class features, infrastructure innovations, and magical surprises.
## ETL

* Open Mage UI, select `Data loader -> Python -> API`

* Copy URL of your csv file, add it to the Mage code: @data_loader url = ' '

* Run the block, extract the data from GCS

* Transform the data: select `Transformer -> Python -> Generic (no template)`

* Run uber_transformation block

* Select `Data exporter -> Python -> Google BigQuery`

* Go to API & Services on GCP, create a new Service account from the Credentials section, assign the BigQuery Admin role to the SA. Create a new key in JSON format for this SA. Copy and paste the information from your JSON key into the io_config.yaml file.

![Zrzut ekranu 2025-03-05 205738](https://github.com/user-attachments/assets/743fc2c5-8b22-4d62-9cd3-b8f7c52c0996)

* Create a Dataset in BQ, run uber_bigquery_load block. Load all tables to BQ

![Zrzut ekranu 2024-12-19 194608](https://github.com/user-attachments/assets/f022b564-d69c-4447-a8f1-ae820571d624)

![Zrzut ekranu 2024-12-19 195200](https://github.com/user-attachments/assets/d8d5da31-468d-42dc-beb8-0ad13a2eff1f)

All code used for the ETL process in Mage can be found in the "Mage" folder

Create a new `analytics` table by running sql code from `sql_analytics.sql`

# Looker 📈

To finalize the project, create a dashboard using Looker

![Zrzut ekranu 2025-03-05 213018](https://github.com/user-attachments/assets/ac55734a-6efc-4a00-9a1a-b586828159e6)


