
---

# Tour Scraper & Email Notifier (Python)

This project is a **Python web scraper** that checks for new tour events from a website, stores them in an **SQLite database**, and sends an **email notification** when a new tour is detected.

---

## 🚀 Features

* Scrapes tour data from a live website
* Extracts tour details using `selectorlib`
* Stores tours in an SQLite database (`data.db`)
* Prevents duplicate tour entries
* Sends an email alert when a new tour is found
* Runs continuously in a loop

---

## 🧰 Technologies Used

* Python 3
* `requests`
* `selectorlib`
* `sqlite3`
* `smtplib`
* `email.message`

---

## 📦 Project Structure

```
project/
│
├── main.py
├── extract.yaml
├── data.db
└── README.md
```

---

## 🛠️ Database Schema

Make sure your SQLite database has this table before running the script:

```sql
CREATE TABLE events (
    band TEXT,
    city TEXT,
    date TEXT
);
```

---

## ⚙️ Setup Instructions

### 1. Install Required Packages

```bash
pip install requests selectorlib
```

### 2. Configure Email Credentials

Edit these variables in the script:

```python
SENDER = "your_email@gmail.com"
PASSWORD = "your_email_app_password"
RECEIVER = "receiver_email@gmail.com"
```

⚠️ **Important:**
Use a **Gmail App Password**, not your regular Gmail password.

---

### 3. Configure `extract.yaml`

Example `extract.yaml` file:

```yaml
tours:
  css: "div#content"
  type: Text
```

(Adjust selectors based on the website structure.)

---

## ▶️ How It Works

1. The script scrapes the tours webpage
2. Extracts tour information (band, city, date)
3. Checks if the tour already exists in the database
4. If it’s new:

   * Saves it to SQLite
   * Sends an email notification
5. Repeats continuously in a loop

---

## ▶️ Run the Script

```bash
python main.py
```

Output example:

```
Tigers, Tiger City, 2088.10.14
Email was sent
```

---

## 📝 Notes

* The script runs indefinitely using `while True`
* You may want to add `time.sleep()` to avoid excessive requests
* Make sure `data.db` exists in the project directory
* The extracted tour string must follow this format:

```
Band Name, City Name, YYYY.MM.DD
```

---

## 🔒 Security Tip

Never hard-code real passwords in production.
Use environment variables or a `.env` file instead.

---

## 📌 Future Improvements

* Add scheduling with `cron` or `schedule`
* Store timestamps
* Improve error handling
* Switch to PostgreSQL or MySQL
* Parse multiple tours instead of one

---



