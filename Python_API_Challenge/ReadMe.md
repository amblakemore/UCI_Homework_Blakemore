# What's the Weather Like?


Whether financial, political, or social -- data's true power lies in its ability to answer questions definitively. So let's take what you've learned about Python requests, APIs, and JSON traversals to answer a fundamental question: "What's the weather like as we approach the equator?"
Now, we know what you may be thinking: "Duh. It gets hotter..."
But, if pressed, how would you prove it?

### WeatherPy
We've created a Python script to visualize the weather of 500+ cities across the world of varying distance from the equator. We've accomplished this by using the Citipy library and the OpenWeatherMap API. After we've created a DataFrame to analyze our data, we've created a series of scatter plots to showcase the relationships between: 
            - Temperature vs Latitude
            - Humidity vs Latitude
            - Cloudiness vs Latitude
            - Wind speed vs Latitude
            
![Alt text](/Python_API_Challenge/WeatherPy/Images/CityLatitudevsWindSpeed.png?raw=true "Optional Title")            
            
### VacationPy
Using the information from our WeatherPy data set, we're planning a vacation! We use the jupyter-gmaps and Google Places API to create a heat map for humidity for every city from the WeatherPy portion and then plotting the hotels.

![Alt text](/Python_API_Challenge/VacationPy/screenshot.png?raw=true "Optional Title")  
