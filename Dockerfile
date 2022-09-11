FROM python:3.9

WORKDIR './backend'
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY ./server ./server
RUN mkdir ./logs

CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "80"]
