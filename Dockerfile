FROM python:3.7-alpine
ADD run.py .
ADD requirements.txt .
RUN pip install -r requirements.txt
CMD ["python", "run.py"]
