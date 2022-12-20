## Setting up Airflow

### Install Airflow
```Bash
# Create Python virtual environment
python3 -m venv env
source env/bin/activate

# Init a Airflow project
export AIRFLOW_HOME=~/airflow-boilerplate

AIRFLOW_VERSION=2.5.0
PYTHON_VERSION="$(python3 --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```


### Init Airflow database, create a user 
```Bash
airflow db init # use sqlite by default

airflow users create --username admin --password 1 --firstname loc --lastname nguyen --role Admin --email lc.nguyendang123@gmail.com

airflow users list

```


### Start Webserver
```Bash
airflow webserver -p 8080
```


### Start Scheduler
```Bash
# Open other terminal
source env/bin/activate
export AIRFLOW_HOME=~/airflow-boilerplate
airflow scheduler
```


### Another way to start Airflow
```Bash
# The Standalone command will initialise the database, make a user,
# and start all components (includes webserver, scheduler).
airflow standalone
```


### View dags list
```Bash
airflow dags list
```


## Setting up MySQL for Metadata
### Install MySQL
```Bash
sudo apt update
sudo apt upgrade
sudo apt install mysql-server
mysql --version
```


### Start MySQL
```Bash
sudo /etc/init.d/mysql start
#or
sudo service mysql start
```


### Find required variables
Enter: `sudo mysql` open the MySQL prompt
```SQL
SHOW DATABASES;

CREATE DATABASE airflow_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'airflow_user' IDENTIFIED BY '1';
GRANT ALL PRIVILEGES ON airflow_db.* TO 'airflow_user';

SELECT user();
SELECT system_user();

SHOW VARIABLES;
SHOW VARIABLES WHERE Variable_name = 'port';
SHOW VARIABLES WHERE Variable_name = 'hostname';

SELECT @@hostname;
SELECT @@port;

-- host: localhost (127.0.0.1)
-- port: 3306
-- database: airflow_db
-- use: airflow_user
-- password: 1
```


### Setting up the Airflow connection to MySQL
Install MySQL packages
```powershell
python3 -m pip install mysql-connector
pip install mysql-connector-python
```


Repalce value of `sql_alchemy_conn` in file `airflow.cfg`
```python
# template
# mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
mysql+mysqlconnector://airflow_user:1@127.0.0.1:3306/airflow_db
```


Restart Airflow UI
```bash
airflow db init # now using MySQL

airflow users create --username admin --password 1 --firstname loc --lastname nguyen --role Admin --email lc.nguyendang123@gmail.com

airflow users list

airflow webserver -p 8080
airflow scheduler
```


## Shutdown dev environment

### Stop Airflow
Press `Ctrl + C` or use following commands
```Bash
lsof -i tcp:8080
kill -9 <PID>
```


### Stop MySQL
```
sudo service mysql stop
```