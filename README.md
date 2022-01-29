# Flask-Headless-CMS
A Headless Content Management System built in Flask

[![Python application](https://github.com/Dev-Elie/Flask-Headless-CMS/actions/workflows/python-app.yml/badge.svg)](https://github.com/Dev-Elie/Flask-Headless-CMS/actions/workflows/python-app.yml)

## Set up & Installation.

### 1 .Clone/Fork the git repo and create an environment 
                    
**Windows**
          
```bash
git clone https://github.com/Dev-Elie/Flask-Headless-CMS.git
cd Flask-Headless-CMS
py -3 -m venv venv

```
          
**macOS/Linux**
          
```bash
git clone https://github.com/Dev-Elie/Flask-Headless-CMS.git
cd Flask-Headless-CMS
python3 -m venv venv

```

### 2 .Activate the environment
          
**Windows** 

```venv\Scripts\activate```
          
**macOS/Linux**

```. venv/bin/activate```
or
```source venv/bin/activate```

### 3 .Install the requirements

Applies for windows/macOS/Linux

```
cd cms
pip install -r requirements.txt
```
### 4. Add a .env file

Create a ".env" file with the contents below. Make sure to include your actual environment variables.

```
SECRET_KEY=
DB_NAME=
TEST_DB_NAME=
DB_HOSTNAME=localhost
DB_USER=
DB_PASSWORD=
DB_PORT=
```

### 5. Run the application 

**For linux and macOS**
Make the run file executable by running the code

```chmod 777 run```

Then start the application by executing the run file

```./run```

**On windows**
```
set FLASK_APP=app
flask run
```
## Running tests

Navigate to the root of the directory,then execute

`pytest -v`

<br>
Explore more on pytest [here](https://docs.pytest.org/en/6.2.x/)
</br>
<div align="center"><h1>Follow me on Twitter</h1></div>
<p align="center"> <a href="https://twitter.com/dev_elie" target="blank"><img src="https://img.shields.io/twitter/follow/dev_elie?logo=twitter&style=for-the-badge" alt="dev_elie" /></a> </p>



