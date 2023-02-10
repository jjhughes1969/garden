FROM python:3.7
WORKDIR /app
RUN pip3 install spacy
RUN python3 -m spacy download en_core_web_sm
COPY . /app
CMD python3 garden.py

