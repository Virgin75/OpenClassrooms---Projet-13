FROM python:3.8

WORKDIR /app
RUN python3 -m venv env

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN . env/bin/activate && pip3 install -r requirements.txt

COPY . .

#ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:$PORT", "oc_lettings_site.wsgi"]
CMD . env/bin/activate && python3 manage.py runserver 0.0.0.0:$PORT