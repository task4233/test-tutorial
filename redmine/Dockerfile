FROM python3

RUN pip install locustio

WORKDIR /locust
COPY ./locustfile.py .
COPY ./run.sh .

ENTRYPOINT ["./run.sh"]