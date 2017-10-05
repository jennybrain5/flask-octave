FROM octave1:latest
MAINTAINER Jenniffer Guerrero "jenniffer.guerrero@correounivalle.edu.co"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install requests
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]