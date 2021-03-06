FROM python:3.7
RUN apt-get update \
    && apt-get install -y --no-install-recommends
WORKDIR /usr/scr/app
copy requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

EXPOSE 5000
CMD ["python", "app.py"]

