FROM python:3.6

RUN mkdir pairwise-testing

COPY ./ /pairwise-testing

WORKDIR /pairwise-testing

RUN pip install -r requirements.txt

EXPOSE 8000

WORKDIR /pairwise-testing/generate_my_pairs

RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
