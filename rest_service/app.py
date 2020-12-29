from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

###home page
@app.route('/')
def home():
    #arbitrary "home" image
    img_source = 'http://thewowstyle.com/wp-content/uploads/2015/02/luxury-home.jpg'
    return render_template('home.html', source=img_source)

###page for getting info on weather
@app.route('/weather')
def weather():
    location = request.args.get('location')

    # connecting to apis #
    #weather api
    weatherkey = ''
    weatherresponse = requests.get(f'http://api.weatherapi.com/v1/current.json?key={weatherkey}&q={location}')
    j = json.loads(weatherresponse.text)
    #pixabay api
    pixkey = ''
    pixresponse = requests.get(f'https://pixabay.com/api/?key={pixkey}&q={location}')
    pixjson = json.loads(pixresponse.text)

    #getting data from json response
    img_source = j['current']['condition']['icon']
    description = j['current']['condition']['text']
    region = j['location']['region']
    #if region !exist, country is provided
    if(region==''):
        region = j['location']['country']
    temp_f = j['current']['temp_f']
    temp_c = j['current']['temp_c']
    time = j['location']['localtime']
    try:
        image = pixjson['hits'][0]['largeImageURL']
    except IndexError:
        image = ''
    #returning HTML template with variables plugged in
    return render_template('weather.html',
                            source=img_source,
                            loc=str(location).upper(),
                            region=str(region).upper(),
                            temp_f=temp_f,
                            temp_c=temp_c,
                            desc=description,
                            image=image,
                            time=time,)

###page for getting info on time/timezones
@app.route('/time')
def time():
    location = request.args.get('location')

    # connecting to apis #
    #weather api
    weatherkey = ''
    weatherresponse = requests.get(f'http://api.weatherapi.com/v1/timezone.json?key={weatherkey}&q={location}')
    j = json.loads(weatherresponse.text)
    #pixabay api
    pixkey = ''
    pixresponse = requests.get(f'https://pixabay.com/api/?key={pixkey}&q={location}')
    pixjson = json.loads(pixresponse.text)

    #getting data from json response
    localtime = j['location']['localtime']
    timezone = j['location']['tz_id']
    region = j['location']['region']
    #if outside of US, region is assigned to country
    if(region==''):
        region = j['location']['country']
    try:
        image = pixjson['hits'][0]['largeImageURL']
    except IndexError:
        image = ''
    # returning HTML template with variables plugged in
    return render_template('time.html',
                           loc=str(location).upper(),
                           region=str(region).upper(),
                           localtime=localtime,
                           timezone=timezone,
                           image=image)

###testing endpoint
@app.route('/secret')
def secret():
    return '<img src="https://www.to-hawaii.com/kauai/beaches/images/secretbeach/secret_beach.jpg" align="center">'

if __name__ == '__main__':
    app.run()