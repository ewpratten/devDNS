from alpine:3.10

copy . /usr/src/app/

workdir /usr/src/app/

run apk add --no-cache py3-pip
run pip3 install -r requirements.txt

cmd ["python3", "main.py"]

