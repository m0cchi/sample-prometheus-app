FROM python:3.12.5

ADD app.py /usr/share/app/
ADD requirements.txt /usr/share/app/

WORKDIR /usr/share/app/

RUN pip install -r requirements.txt

CMD python app.py

