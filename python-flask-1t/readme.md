# install flask
Python version 3.x

```
python3 -m pip install flask
python3 app.py
```

localhost:81



Docker file steps
1. python3 version 
2. copied local files app.py and requirements.txt to docker image
3. install flask --> pip install flask --> added in requirements.txt file --> pip install -r requirements.txt
4. run the app

Run the app in container:
    - Make Dockerfile and add steps required for your app to run
    - Build Docker image using Dockerfile
        * docker build -t flask_webapp .
    -  Run the container
        * detached mode and publish
        * docker run -d -p <mac_port>:<container_port> flask_webapp
        * docker run -d -p 82:81 flask_webapp
