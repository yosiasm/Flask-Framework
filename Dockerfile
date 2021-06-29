FROM python:3.7

# Dockerfile author / maintainer 
LABEL MAINTAINER Yosias Suparno<yosias@qti.co.id> 

RUN mkdir -p /flask-app
WORKDIR /flask-app

# Copy files
COPY ./requirements.txt ./

# Copy folders
COPY . ./src

# Install packages
RUN pip install -r requirements.txt

# Run flask app
EXPOSE 5000

ENV FLASK_APP="src/main.py" FLASK_DEBUG=1 


CMD ["flask", "run", "-h", "0.0.0.0","--cert", "adhoc"]