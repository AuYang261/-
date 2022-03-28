FROM python3
WORKDIR /root/ENSS
# RUN python3 -m http.server 5000
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "-m http.server", "5000"]