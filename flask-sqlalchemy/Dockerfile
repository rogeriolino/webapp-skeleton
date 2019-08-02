FROM python:3-alpine

COPY . .
RUN pip3 install -r requirements.txt

ENV FLASK_APP=src/app.py

CMD [ "python3", "src/app.py" ]