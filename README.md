# Exercise 1
Create Dockerfile for building image for the getweather program you’ve written.
Then build and run the image

## 1.1 Install and configure Docker

### To install and enable loging run command:
```
$ ansible-playbook -i "localhost," -c local site.yml
```

## 1.2 Write a weather reporting program

### To get weather we use pyowm library(A Python wrapper around OpenWeatherMap web APIs), to install it run command:
```python
$ pip install pyowm
```
### To make the program work you must have env variables set for OWM_API_KEY and OWM_CITY, to do so you can run:

```bash
$ export OWM_API_KEY='xxxx'
```
```bash
$ export OWM_CITY='xxxx'
```

### To get the weather for selected city run:
```
$ python3 getweather.py
```
## 1.3 Dockerize and run the program

### To build the docker image run:

```
$ docker build --rm -t "getweather:dev" .
```

### To run the image run:
```
$ docker run --rm --name weatherreporting --env OWM_CITY="xxxx" --env OWM_API_KEY="xxxx" getweather:dev
```