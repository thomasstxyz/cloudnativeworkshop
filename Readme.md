
# Cloud Native Basic Camp mit Thomas Schuetz

DevOps ist keine Technologie, es ist eine Kultur.

Heroku https://www.heroku.com/
Eine Applikation sollte nie mehr als 5 Sekunden zum Hochfahren brauchen.


https://12factor.net/


## Demo

Follow below steps to get the web app running locally.

### Build container image

```bash
docker build -t flaskapp .
```
### Run container image

```bash
docker run -it -e APP_TEXT='world!!' -p 8080:8080 flaskapp
```


## Initial Python Dev Setup

Create Python virtual environment

```bash
python3 -m venv venv

source venv/bin/activate

pip install flask

pip freeze > requirements.txt
```
