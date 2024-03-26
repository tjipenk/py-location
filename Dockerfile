# 
FROM python:3.9

# 
WORKDIR /app

# 
COPY ./requirements.txt /requirements.txt

# gdal
RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin

# 
RUN pip install --no-cache-dir --upgrade -r /requirements.txt

# 
COPY ./app /app

# clean
RUN apt clean && rm -rf /var/lib/apt/lists/*

EXPOSE 8000

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]