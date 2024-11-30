FROM python:3.10-slim
EXPOSE 8000
WORKDIR /app/src
COPY src/ ./
RUN pip install pipenv
# RUN pipenv install --system --deploy --ignore-pipfile
RUN pipenv install --system
CMD ["sh", "demo.sh"]