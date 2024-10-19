FROM python:3.11-rc-slim

WORKDIR /app

COPY src ./src/

CMD [ "python", "./src/main.py" ]