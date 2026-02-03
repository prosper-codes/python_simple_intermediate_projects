# Weather Data API 🌦️
```md


A lightweight REST API that provides historical weather data by station, date, and year.

---

## Features

- Retrieve weather data by station and date
- Retrieve all historical data for a station
- Retrieve yearly weather data for a station
- JSON responses
- Simple and fast local setup

---

## Base URL

```

[http://127.0.0.1:5000/api/v1](http://127.0.0.1:5000/api/v1)

```

---

## Endpoints

### Get data for one station on a specific date

```

GET /<station>/<date>

```

**Example**
```

[http://127.0.0.1:5000/api/v1/10/1988-10-25](http://127.0.0.1:5000/api/v1/10/1988-10-25)

```

---

### Get all data for one station

```

GET /<station>

```

**Example**
```

[http://127.0.0.1:5000/api/v1/10](http://127.0.0.1:5000/api/v1/10)

```

---

### Get yearly data for one station

```

GET /yearly/<station>/<year>

```

**Example**
```

[http://127.0.0.1:5000/api/v1/yearly/10/1998](http://127.0.0.1:5000/api/v1/yearly/10/1998)

````

---

## Response Format

All endpoints return JSON.

**Example response**
```json
{
  "station": 10,
  "date": "1988-10-25",
  "temperature": 12.3
}
````

If no data is found, the API returns an empty response or an error message.

---

## Getting Started

### Prerequisites

* Python 3.7+
* pip

### Installation

```bash
git clone https://github.com/your-username/weather-data-api.git
cd weather-data-api
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Open your browser and navigate to:

```
http://127.0.0.1:5000
```

---

## Project Structure

```
weather-data-api/
│
├── app.py
├── data/
├── templates/
│   └── index.html
├── requirements.txt
└── README.md
```

---

## Notes

* Date format must be `YYYY-MM-DD`
* This project is intended for local and educational use
* Ensure the dataset is present before running the app

---

## Future Improvements

* Add proper HTTP status codes
* Input validation and error handling
* Swagger / OpenAPI documentation
* Deploy to a cloud platform

---

## License

This project is licensed under the MIT License.


