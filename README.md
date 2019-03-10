
# Basic Setup
To run:


Make and enter your virtualenv
``` 
$ virtualenv . 
$ source bin/activate
```


Install dependencies with
``` 
pip install -r requirements.txt 
```


Run the app
```
python app.py
```


It'll be listening by default on http://127.0.0.1:5000


# Using Dockerfile

```
$ docker build . -t spellcheckerapp
$ docker run -d -p 1234:5000 spellcheckerapp
```

It'll be listening on http://127.0.0.1:1234 


