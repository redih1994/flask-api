# Weather Data API

This Flask API provides weather data for different stations. It allows users to retrieve temperature data for specific stations and dates, as well as access data for all dates and a particular year for a given station. The data is read from text files and served through the API endpoints.

## API Endpoints

- `GET /` - Home page that displays weather data in an HTML table format.
- `GET /api/v1/<station>/<date>` - Retrieves the temperature for a specific station and date.
- `GET /api/v1/<station>` - Retrieves all weather data for a specific station.
- `GET /api/v1/annual/<station>/<year>` - Retrieves weather data for a specific station and year.

## Usage

1. Make sure you have Python and Flask installed.
2. Run the `app.py` script to start the Flask server.
3. Open your browser and navigate to `http://127.0.0.1:5011` to view the home page and weather data table.
4. Use the provided URLs to access specific weather data through the API endpoints.

## Dependencies

- Flask
- pandas

You can install the required dependencies using `pip`:


        pip install Flask pandas 
        or
        pip install requirements.txt



## Data Source
    The weather data is sourced from the European Climate Assessment & Dataset (ECA&D) and contains daily surface air temperature readings for various stations in Europe.

    The stations.txt file in the data_small directory provides information about the stations, including their identifiers, names, country codes, latitude, longitude, and elevation.


## Acknowledgments
        The weather data used in this project is provided by the European Climate Assessment & Dataset (ECA&D). We acknowledge their contribution to climate research and making the data freely available.