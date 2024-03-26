# 
FROM python:3.9

# 
WORKDIR /app

# 
COPY ./requirements.txt /requirements.txt

# gdal
RUN apt update && apt -y install libgdal-dev


# 
RUN pip install --no-cache-dir --upgrade -r /requirements.txt

# 
COPY ./app /app

# clean
RUN apt clean && rm -rf /var/lib/apt/lists/*

EXPOSE 80

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]