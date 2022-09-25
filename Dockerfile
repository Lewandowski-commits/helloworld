
FROM python:3.8

ENV DASH_DEBUG_MODE False
COPY . /
COPY ./app /app
RUN set -ex && \
    pip install -r app/requirements.txt
EXPOSE 5000
CMD ["python", "wsgi.py"]