
---

# 🧪 Selenium Automation – Login & Contact Form Test

## 📌 Project Description

This project automates:

1. Logging into the Practice Test Automation website
2. Navigating to the Contact page
3. Filling out and submitting the contact form

The automation is built using:

* 🐍 Python
* 🌐 Selenium WebDriver
* 🚗 ChromeDriver (managed automatically with webdriver-manager)

The test site used is:

* Login Page: [https://practicetestautomation.com/practice-test-login/](https://practicetestautomation.com/practice-test-login/)
* Contact Page: [https://practicetestautomation.com/contact/](https://practicetestautomation.com/contact/)

---

## ⚙️ Technologies Used

* Python 3.x
* Selenium
* WebDriver Manager
* Google Chrome

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/prosper-codes/python_simple_intermediate_projects.git
cd browser-automation-selenium
```

### 2️⃣ Install dependencies

```bash
pip install selenium
pip install webdriver-manager
```

---

## ▶️ How to Run

Run the Python script:

```bash
python main.py
```

The script will:

* Open Chrome
* Log in using valid credentials
* Navigate to the Contact page
* Fill out the form
* Submit the form
* Wait for user input before closing

---

## 🔐 Login Credentials Used

```
Username: student
Password: Password123
```

---

## 🧠 What This Project Demonstrates

* Explicit waits using `WebDriverWait`
* Element location using `By.ID`
* Form automation
* Page navigation
* Basic Selenium best practices
* ChromeDriver automatic version management

---

## 📂 Project Structure

```
project-folder/
│
├── chromedriver-win64
└── main.py
└── README.md
```

---

## 🚀 Example Code Snippet

```python
username = wait.until(
    Exc.visibility_of_element_located((By.ID, "username"))
)
username.send_keys("student")
```

---

## 🏁 Future Improvements

* Add assertions for verification
* Convert to pytest framework
* Implement Page Object Model (POM)
* Add headless execution mode
* Add logging and reporting

---


