FROM python:3.9
RUN mkdir /app && cd /app
WORKDIR /app
RUN python3 -m pip install pycbrf
COPY . /app
ENTRYPOINT [ "python3", "valut.py" ]