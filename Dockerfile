FROM python:3.9

RUN mkdir app
RUN cd app

RUN python3 -m pip install pymongo

WORKDIR /app/

COPY main.py /app/main.py

RUN ls -la

CMD ["python", "main.py"]

EXPOSE 8000
