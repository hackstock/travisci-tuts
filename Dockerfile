FROM python:latest
WORKDIR /travisapp
COPY . /travisapp
RUN pip install -r requirements.txt
CMD ["python3","app.py"]