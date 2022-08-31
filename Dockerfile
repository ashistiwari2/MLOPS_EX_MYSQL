#
FROM python:3.9

#
WORKDIR /usr/src/application

#
COPY requirements.txt ./

#
RUN pip install --no-cache-dir --upgrade -r requirements.txt

#
COPY . .

#
CMD ["uvicorn", "Logistic_api.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8008"]
#COPY ./requirements.txt /code/requirements.txt
# RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
# COPY ./app /code/app

