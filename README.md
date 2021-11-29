# Tasker: A Simple fully djnago web application to manage tasks
Click here to see the [tasker demo](https://wiki-task.herokuapp.com/)

# Local project setup
   ```
   for more information on pre-requisite for mysqlclient, visit this page: (https://pypi.org/project/mysqlclient/)

1. Use anaconda / virtualenv for setting up this project

2. Install pip requirements
   ```
   pip install -r requirements.txt
   ```
3. Setup your database credentials and SITE_URL in settings.py file available inside ### pydjango_ci_integration folder

4. Once you have setup your database, Open command prompt pointing to the Root of the project directory and run following command to create application default database
   ```
   (virtualenv / conda environment) > python manage.py migrate
   
   (virtualenv / conda environment) > python manage.py createsuperuser
   ```
5. Once all of the above command run sucessfully, We are ready to go. Start server by executing command
   ```
   (virtualenv / conda environment) > python manage.py runserver 127.0.0.1:8732
   ```
  and visit the web browser with 'http://127.0.0.1:8732'
  
## Environment variables

The following environment variables can be set to override defaults:

- `SECRET_KEY`: Django [secret key](https://docs.djangoproject.com/en/2.2/ref/settings/#secret-key).
- `DATABASE_URL`: The target database slug.
   
