FROM python:3.9
RUN mkdir /app && cd /app
WORKDIR /app
COPY requrements.txt .
RUN python3 -m pip3 install pycbrf
COPY . /app
ENTRYPOINT [ "python3", "valut.py" ]