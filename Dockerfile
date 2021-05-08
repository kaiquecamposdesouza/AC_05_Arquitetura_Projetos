FROM python:3.8
RUN pip install flask
RUN pip install psycopg2
RUM mkdir templates
RUN mkdir static
COPY controler.py /controler.py
COPY templates/*  /templates/
COPY static/*  /static/
RUN chmod -R a+rwx static
RUN chmod -R a+rwx templates
CMD ["python","controler.py"]
