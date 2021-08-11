FROM python:3.9
RUN mkdir /app && cd /app
WORKDIR /app
COPY requrements.txt .
RUN pip3 install -r requrements.txt
COPY . /app
ENTRYPOINT [ "python3.9", "valut.py" ]