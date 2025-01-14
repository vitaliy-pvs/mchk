FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /mchk
COPY ./ /mchk
RUN pip install -r requirements.txt