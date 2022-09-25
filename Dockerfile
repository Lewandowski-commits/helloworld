
FROM python:3.10

ENV DASH_DEBUG_MODE False
COPY . /
COPY ./app /app
RUN set -ex && \
    pip install -r app/requirements.txt
EXPOSE 8050
CMD ["python", "-m", "flask", "run"]