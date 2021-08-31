# Web Application for ML Prediction Models.

Techstack: 

Python flask,numpy,pandas,joblib

Web:bootstrap2

## Introduction

What will be my predicted feet size given my data?
What will be my predicted calorie consumption given my data ?

People always have questions and expect answers from various online predictive calculators. This template structures an online machine that enables prediction with user-entered data. Developers can cooperate the framework with any machine learning models so long as the model was trained over stuctured table data. In order to help all users to effortlessly deploy the server, a guide over how to deploy this Flask Application over Ubuntu VPS is attached  


An Example for this framework: http://zhuformula.com/
This website for calculating post surgury eye sight has already help patients with more than 10k calculations in last 6 months 

## Installation&Local Testing

Clone the whole project.
Make Sure every package in requirements.txt is installed
python3 __init__.py

## Server Setup

VPS: Ubuntu 16.04 x64

Firstly use ssh to connect to your server


```
ssh root@123.123.123.123
Password:
```

enter password 

```
cd /var/www 
sudo mkdir FlaskApp
cd FlaskApp
sudo mkdir FlaskApp
cd FlaskApp
```
Then upload all the files to the current folder, soi that it looks like
```
|----FlaskApp
|---------FlaskApp
|--------------__init__.py
|--------------templates
...
```
Install pip and test run 
```
sudo apt-get install python-pip
sudo pip install Flask
sudo python __init__.py 
```
Configure the Virtual Host 

```
sudo nano /etc/apache2/sites-available/FlaskApp.conf
```
configure the FlaskApp.conf to be
```
<VirtualHost *:80>
		ServerName mywebsite.com
		ServerAdmin admin@mywebsite.com
		WSGIScriptAlias / /var/www/FlaskApp/flaskapp.wsgi
		<Directory /var/www/FlaskApp/FlaskApp/>
			Order allow,deny
			Allow from all
		</Directory>
		Alias /static /var/www/FlaskApp/FlaskApp/static
		<Directory /var/www/FlaskApp/FlaskApp/static/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```
Enable the virtual host with
```
sudo a2ensite FlaskApp
```
```
#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FlaskApp/")

from FlaskApp import app as application
application.secret_key = 'Add your secret key'
```
Now your directory structure should look like this:
```
|--------FlaskApp
|----------------FlaskApp
|-----------------------static
|-----------------------templates
|-----------------------venv
|-----------------------__init__.py
|----------------flaskapp.wsgi
```

## Run
```
sudo service apache2 restart 
```

## Debugging

If error occurs as Internal Server Error, that means parts of your flask application is bugging, you should check out the error log using the following.  

```
cd /var/log/apache2/error.log
```

