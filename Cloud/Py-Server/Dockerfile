FROM python:3.9
# WORKDIR .
# RUN apt-get update \
#     &&apt-get install python3
RUN apt-get update
COPY . .
RUN pip3 install -r requirements.txt
CMD ["flask", "run", "--host=0.0.0.0:8081"]
