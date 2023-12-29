# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.12.1-slim

EXPOSE 5002

WORKDIR /app
COPY . /app

# Install pip requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:5002", "app:app"]

    
#build a base image >>>>> docker build -t mldockerimg:v1 .
#run the container >>>>>> docker run -dp 8081:5002 -ti --name mlContainer mldockerimg:v1

