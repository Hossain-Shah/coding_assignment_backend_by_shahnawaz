# Backend Interview Assignment

## Tools and Frameworks

### Development Environment:

- Python 3.9.5
- Django 4.0.1

## Project Setup for Development

- Install Python 3 if not already installed
    - Download Python 3 for Windows from https://www.python.org/downloads/
    - Extract the .exe file
    - Run the .exe file
    - Open a command prompt and type python
    ```bash
        sudo apt-get install python
    ```
- Clone The Interview Assignment
  ```bash
      git clone https://github.com/Hossain-Shah/coding_assignment_backend_by_shahnawaz.git
  ```
- Install the requirements using the command:
  ```bash
      pip install -r requirements.txt
  ```
- Run the development server using the command
  ```bash
    python manage.py runserver
  ```
- To create super user run the command
  ```bash
    python manage.py createsuperuser
  ```
- To migrate database run the command
  ```bash
    python manage.py makemigrations
    python manage.py migrate
  ```
