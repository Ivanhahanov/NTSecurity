FROM python:3.8-alpine
MAINTAINER Ivan Hahanov 'hahanov.i@explabs.ru'
RUN pip install fastapi uvicorn pytest redis
RUN pip install docker
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apk add --update docker openrc
RUN rc-update add docker boot
EXPOSE 80
COPY app /app
CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "80", "--reload"]