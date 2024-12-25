# Django Webpage Project 🌐😷🌿

## Overview 🌐😷🌿
This application constitutes a sophisticated web platform developed using Django, a high-level Python framework, with SQLite as the backend database system. Deployed on Heroku, this project serves as an educational resource dedicated to raising awareness about COVID-19. It encompasses essential information regarding preventative measures, basic remedies, and health recommendations. 🌐😷🌿

## Features 🚀📊🌐
- **Backend Framework**: Utilizes Django to implement robust routing, logic processing, and database integration.
- **Database**: Employs SQLite for lightweight, efficient, and structured data storage.
- **Hosting Platform**: Hosted on Heroku to ensure accessibility and scalability.
- **Content**: Focuses on disseminating actionable and accurate information regarding COVID-19, emphasizing public health and safety. 🚀📊🌐

## Prerequisites 📖🛠️🚀
To set up and execute this project, the following prerequisites must be fulfilled:
- Python 3.8 or newer
- pip (Python package installer)
- Git for version control
- Heroku CLI for seamless application deployment 📖🛠️🚀

## Installation Guide 🔧📃🎡

### Clone the Repository 🔧📃🎡
```bash
$ git clone <repository-url>
$ cd <project-folder>
```

### Create and Activate Virtual Environment 🔄🧔🌐
Establish an isolated environment to manage project dependencies efficiently:
```bash
$ python -m venv env
$ source env/bin/activate   # For Linux/MacOS
$ env\Scripts\activate    # For Windows
```

### Install Dependencies 🌐🔄🛠️
Use pip to install all required libraries and frameworks as specified in the `requirements.txt` file:
```bash
$ pip install -r requirements.txt
```

### Database Setup 🏦🌐📊
Initialize and migrate the database schema to ensure proper functionality:
```bash
$ python manage.py migrate
```

### Run the Application Locally 🏦🌐🔄
Launch the development server to verify proper setup and functionality:
```bash
$ python manage.py runserver
```
Access the application at `http://127.0.0.1:8000/`. 🏦🌐🔄

## Deployment on Heroku 🌐🏦🎡

### Install Heroku CLI 📖🌐🚀
Refer to the [Heroku CLI Documentation](https://devcenter.heroku.com/articles/heroku-cli) to download and configure the CLI for deployment tasks. 📖🌐🚀

### Login to Heroku 🛠️🏦🔄
Authenticate with your Heroku account:
```bash
$ heroku login
```

### Create Heroku App 🏦🔄🌐
Establish a new Heroku application for hosting:
```bash
$ heroku create
```

### Add Heroku Remote Repository 📡🔄🚀
Ensure the Heroku remote repository is linked to your project:
```bash
$ heroku git:remote -a <your-app-name>
```

### Push to Heroku 🏦🔧🎡
Deploy the application to Heroku:
```bash
$ git push heroku main
```

### Set Up Environment Variables 📖🌐🎡
Configure essential environment variables (e.g., set `DEBUG=False` for production):
```bash
$ heroku config:set <ENV_VARIABLE>=<value>
```

### Run Database Migrations on Heroku 🏦🌐📊
Apply database migrations in the Heroku environment:
```bash
$ heroku run python manage.py migrate
```

### Access the App 🏦🌐🛠️
The application will be available at `https://<your-app-name>.herokuapp.com/`. 🏦🌐🛠️

## Project Structure 🌐🎡🛠️
```
project-folder/
|-- app_name/
|   |-- migrations/
|   |-- templates/
|   |-- views.py
|   |-- models.py
|-- project_name/
|   |-- settings.py
|-- db.sqlite3
|-- manage.py
|-- requirements.txt
```

## Technologies Used 🎡🔄🛠️
- **Django**: High-level web development framework
- **SQLite**: Relational database management system
- **Heroku**: Cloud-based application hosting platform 🎡🔄🛠️

## Future Enhancements 📖🚀🌐
- Augment security measures with advanced authentication mechanisms.
- Transition to a scalable database solution such as PostgreSQL.
- Integrate comprehensive unit and integration testing modules to enhance reliability. 📖🚀🌐

## Author 🌐😷🌿
This project was conceptualized and developed by Vijay Kumar. 🌐😷🌿

