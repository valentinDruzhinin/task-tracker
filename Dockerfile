FROM python:3.7-alpine
ADD run.py /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "run.py"]
