FROM python:3.7

COPY requirements.txt /usr/src/python-opencv/requirements.txt

WORKDIR /usr/src/python-opencv

RUN pip install -r requirements.txt

CMD [ "/bin/bash" ]