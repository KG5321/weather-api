# WeatherAPI

Simple weather API written in Python using FastAPI and OpenWeatherMap API. All requests cached on AWS with S3 and DynamoDB.

_Created for a job interview task._

## Deployment

### Step 1: Create `.env` based on `.env.example`

### Step 2: Build Docker using `docker-compose`
Directly:

```bash
docker-compose up --build
```

or by using `Makefile`:

```bash
make start
```

## Usage

Provide the city name as a query parameter. API returns weather data in JSON format.

### Example Request

```
GET /weather?city=London
```

### Example Response

```json
{
    "coord": {
        "lon": -0.1257,
        "lat": 51.5085
    },
    "weather": [
        {
            "id": 803,
            "main": "Clouds",
            "description": "broken clouds",
            "icon": "04d"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 287.1,
        "feels_like": 286.17,
        "temp_min": 285.98,
        "temp_max": 288.58,
        "pressure": 1024,
        "humidity": 62,
        "sea_level": 1024,
        "grnd_level": 1020
    },
    "visibility": 10000,
    "wind": {
        "speed": 3.09,
        "deg": 320
    },
    "clouds": {
        "all": 75
    },
    "dt": 1727527948,
    "sys": {
        "type": 2,
        "id": 2075535,
        "country": "GB",
        "sunrise": 1727503000,
        "sunset": 1727545520
    },
    "timezone": 3600,
    "id": 2643743,
    "name": "London",
    "cod": 200
}
```
