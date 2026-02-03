# Simple Thesarus Flask Dictionary API

A simple Flask-based REST API that serves word definitions from a CSV file. The app also includes a basic home page.

---

## Features

* 🔎 Look up word definitions via a REST endpoint
* 📄 Data source backed by a CSV file (`dictionary.csv`)
* 🧩 Simple Flask app structure
* 🧪 Runs in debug mode for easy development

---

## Project Structure

```
.
├── app.py
├── data/
│   └── dictionary.csv
├── templates/
│   └── home.html
└── README.md
```

---

## Requirements

* Python 3.8+
* Flask
* pandas

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/prosper-codes/python_simple_intermediate_projects.git
   cd simple_Thesarus_APi
   ```

2. **Create and activate a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

3. **Install dependencies**

   ```bash
   pip install flask pandas
   ```

---

## Data Format

The CSV file should be located at:

```
data/dictionary.csv
```

Expected columns:

| word  | definition                  |
| ----- | --------------------------- |
| apple | A fruit that grows on trees |

---

## Running the App

Start the Flask development server:

```bash
python app.py
```

The app will run at:

```
http://127.0.0.1:5002/
```

---

## API Usage

### Get Word Definition

**Endpoint:**

```
GET /api/v1/<word>/
```

**Example:**

```
http://127.0.0.1:5002/api/v1/apple/
```

**Response:**

```json
{
  "word": "apple",
  "definition": "A fruit that grows on trees"
}
```

---

## Home Page

Visiting the root URL renders a template:

```
GET /
```

This loads `templates/home.html`.

---

## Notes & Improvements

* Currently, word lookup is **case-sensitive**
* No error handling for missing words (returns `NaN`)
* Could be extended with:

  * Case-insensitive search
  * 404 handling for missing words
  * JSON error messages
  * Docker support

---

## License

This project is open-source and free to use for learning and experimentation.
