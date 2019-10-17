FROM python:3.7
ADD . /task-tracker
WORKDIR /task-tracker
RUN pip install -r requirements.txt
CMD python run.py
