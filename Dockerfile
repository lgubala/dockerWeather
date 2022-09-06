FROM python:3.8.10
COPY getweather.py ./
RUN pip install pyowm
CMD ["python","./getweather.py"]