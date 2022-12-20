FROM python:3.9.15-alpine3.16
WORKDIR /app
COPY . . 
RUN "pip3 install -r requirments.txt"
CMD [ "python" ,"http_e.py"]
