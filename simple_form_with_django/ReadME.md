# 📄 Django Job Application Form

A simple web application built with **Django** that allows users to submit a job application form. The app collects user details, stores them in a database, and sends a confirmation email upon submission.

---

## 🚀 Features

* 📝 Job application form (name, email, date, occupation)
* 💾 Data stored in database using Django models
* 📧 Email confirmation after submission
* ✅ Success message displayed to user
* 🌐 Multiple pages (Home & About)
* 🎨 Styled with Bootstrap

---

## 🛠️ Technologies Used

* Python
* Django
* HTML / CSS
* Bootstrap

---

## 📁 Project Structure

```
simple_form_with_django/
│
├── manage.py
├── db.sqlite3
├── simple_form_with_django/
│   ├── settings.py
│   ├── urls.py
│
├── app_name/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── about.html
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone <your-repo-url>
cd simple_form_with_django
```

### 2. Create virtual environment

```
python -m venv venv
```

### 3. Activate virtual environment

**Windows:**

```
venv\Scripts\activate
```

**Mac/Linux:**

```
source venv/bin/activate
```

---

### 4. Install dependencies

```
python -m pip install django
```

---

### 5. Run migrations

```
python manage.py migrate
```

---

### 6. Run the development server

```
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

## 📧 Email Configuration (Development)

To print emails in the console instead of sending them, add this to `settings.py`:

```
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

---

## 🧩 URL Routes

| URL       | Description      |
| --------- | ---------------- |
| `/`       | Home (Form Page) |
| `/about/` | About Page       |

---

## 🐞 Common Issues

### ❌ Django not found

Make sure you install Django inside the virtual environment:

```
python -m pip install django
```

---

### ❌ About page not loading

Ensure your `urls.py` contains:

```
path('about/', views.about, name='about')
```

---

## 📌 Future Improvements

* Add form validation errors display
* Store submissions in admin panel
* Add contact page
* Improve UI/UX design
* Deploy to production (Heroku, Vercel, etc.)

---

## 👨‍💻 Author

Your Name

---

## 📜 License

This project is open-source and available under the MIT License.
