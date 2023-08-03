FROM okteto/okteto:2.18.0 as okteto

FROM python:3-alpine
WORKDIR /usr/src/app
COPY --from=okteto /usr/local/bin/okteto /usr/local/bin/okteto

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY sleep.py sleep.py

CMD python sleep.py

