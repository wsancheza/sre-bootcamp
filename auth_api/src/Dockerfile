FROM python:3-alpine

# Add your instructions to dockerize the application
# App must run on port 8000

WORKDIR /src
ENV FLASK_APP api.py
ENV FLASK_RUN_HOST 0.0.0.0

COPY * /src/
RUN pip install -r requirements.txt
CMD [ "python", "api.py" ]
