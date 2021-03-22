FROM python:3.8
LABEL Name=default maintainer="Checkout container assessment" Version=1.0.0

COPY ./app /consumer_store/app
COPY ./main.py /consumer_store/main.py

COPY ./app/main/configuration/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR ./consumer_store

RUN echo "--------------------- Finish ---------------------"

ENTRYPOINT [ "/entrypoint.sh" ]
