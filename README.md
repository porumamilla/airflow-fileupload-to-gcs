# airflow-fileupload-to-gcs
This is a simple airflow project. It is created to demonstrate how to create a DAG in airflow. This simple workflow is 
responsible for taking a json file on local file system and converting to CSV file then uploading to google cloud storage.

## running on docker
To run this airflow project on docker please get this code on your local machine. Go to the project root directory and simply run the following command on your laptop or wherever docker is installed

docker-compose up -d

Once the airflow is up and running on docker and access the application using the URL http://localhost:8080/

Under dags tab please run the dag site-visits-dag 

Once the dag has run please shutdown the server with the following command
docker-compose down

## running on google cloud composer
To run the dag on google cloud composer please copy the 2 python files to dag folder on goolge cloud storage location. And composer should be able to pick up the dag in couple of minutes.



