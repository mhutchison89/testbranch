FROM python:3.6-slim

COPY . /AWSEC2

WORKDIR /AWSEC2

RUN pip install --no-cache-dir -r requirements.txt

RUN ["pytest", "-v", "code/test.py"]

CMD tail -f /dev/null