
---

## 🌦️ Weather Forecast App

A simple **Streamlit web app** that displays a weather forecast for the next few days using data from the **OpenWeatherMap Forecast API**.
Users can view either **temperature trends** or **sky conditions** (with icons).

---

## 🚀 Features

* Search weather forecast by city name
* Select forecast length (1–5 days)
* View:

  * 📈 Temperature chart (Plotly)
  * ☁️ Sky conditions with weather icons
* Graceful error handling for invalid locations

---

## 🛠️ Technologies Used

* **Python 3**
* **Streamlit** – web interface
* **Plotly** – interactive charts
* **Requests** – API calls
* **OpenWeatherMap API** – weather data

---

## 📁 Project Structure

```
weather_forecast_data_app/
│
├── main.py              # Streamlit frontend
├── backend.py           # API logic
├── images/              # Weather icons
│   ├── clear.png
│   ├── cloud.png
│   ├── rain.png
│   └── snow.png
├── README.md
```

---

## 🔑 API Setup (Required)

This app uses the **OpenWeatherMap 5-Day / 3-Hour Forecast API**.

### 1. Get an API key

* Go to: [https://openweathermap.org/api](https://openweathermap.org/api)
* Create a free account
* Copy your API key

### 2. Add API key to `backend.py`

```python
API_KEY = "YOUR_API_KEY_HERE"
```

---

## 🌐 OpenWeatherMap API Info

**Endpoint used:**

```
https://api.openweathermap.org/data/2.5/forecast
```

**Query parameters:**

* `q` – city name (e.g. `London`)
* `appid` – your API key
* `units=metric` – Celsius temperature

**Example request:**

```
https://api.openweathermap.org/data/2.5/forecast?q=Warsaw&units=metric&appid=YOUR_API_KEY
```

**Important response fields:**

* `list` – forecast data (3-hour intervals)
* `main.temp` – temperature
* `weather[0].main` – sky condition (`Clear`, `Clouds`, `Rain`, etc.)
* `dt_txt` – date and time

---

## ▶️ How to Run the App

### 1. Create virtual environment (optional but recommended)

```bash
python -m venv venv
```

Activate it:

**PowerShell**

```powershell
.\venv\Scripts\Activate.ps1
```

---

### 2. Install dependencies

```bash
pip install streamlit plotly requests
```

---

### 3. Run the app

```bash
streamlit run main.py
```

The app will open in your browser automatically.

---

## 🖼️ Sky Condition Icons

The app maps sky conditions to icons:

```python
images = {
    "Clear": "images/clear.png",
    "Clouds": "images/cloud.png",
    "Rain": "images/rain.png",
    "Snow": "images/snow.png"
}
```

Make sure the images exist in the `images/` folder.

---

## ⚠️ Error Handling

* If an invalid city is entered, the app shows:

```
That place does not exist
```

* Prevents crashes caused by missing API data.

---

## 📌 Notes

* Forecast data is in **3-hour intervals**
* One day ≈ **8 data points**
* Temperatures are displayed in **Celsius**

---

## 📜 License

Free to use for learning and personal projects.

---


