FROM python:3.6
RUN apt-get update \
&&apt-get install python3
WORKDIR /root/ENSS
# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt
# RUN pip install http
COPY . .
CMD ["python3", "-m", "http.server", "8081"]
