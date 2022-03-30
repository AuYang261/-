FROM python:3.9
WORKDIR /ENSS
#RUN echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster main contrib non-free" >> /etc/apt/sources.list \
#    && echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-updates main contrib non-free" >> /etc/apt/sources.list \
#    && echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ buster-backports main contrib non-free" >> /etc/apt/sources.list \
#    && echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian-security buster/updates main contrib non-free" >> /etc/apt/sources.list \
#    && apt-get upgrade \
#    && apt-get update \
#    && apt-get install build-essential python3-dev
COPY . .
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirement.txt
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
