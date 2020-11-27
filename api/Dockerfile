FROM python:3.8-slim

WORKDIR /home/api

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

ADD . /home/api/api

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
