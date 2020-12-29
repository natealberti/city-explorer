# city-explorer
web-service using Flask implementing some APIs

Simple web-service used to find the current weather and timezone of cities around the world. I created this using the Flask framework. To get the weather data, I used "weather API" https://www.weatherapi.com/. You need to create an account and pass the API key through for the service to work. To grab the images of the city, I used the pixabay API https://pixabay.com/api/docs/. You also need to create an account here and get an API key. 

The HTML code is a bit messy, the first time I've really tried using it. The templates folder is what Flask uses to set up the particular endpoits. I passed variables from the APIs to the templates for Flask to use (such as weather, time, etc). 
