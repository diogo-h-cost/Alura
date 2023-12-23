FROM python:3.10 AS test

WORKDIR /app
COPY teste.py /app

FROM alpine
WORKDIR /casa
COPY --from=test /app /casa/
CMD ["python", "teste.py"]
