FROM python:3.9-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /mchk
COPY . .
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:80"]