# 🍽 Django Restaurant Menu App

A simple Django web application for managing and displaying a restaurant menu.
Users can view meals, see details, and manage menu items through the admin panel.

---

## 🚀 Features

* 📋 Display all menu items on the homepage
* 🍲 Categorize meals (Starters, Salads, Main Dishes, Desserts)
* 🔍 View detailed information about each item
* 🛠 Admin panel for managing menu items
* ✅ Availability status (Available / Unavailable)

---

## 🧱 Tech Stack

* Python
* Django
* HTML / CSS

---

## 📁 Project Structure

```
project/
│
├── app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   ├── index.html
│   │   └── menu_item_details.html
│
├── manage.py
└── db.sqlite3
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Create virtual environment

```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```
pip install django
```

### 4. Apply migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 5. Create superuser (for admin panel)

```
python manage.py createsuperuser
```

### 6. Run the server

```
python manage.py runserver
```

---

## 🌐 Usage

* Open in browser:
  `http://127.0.0.1:8000/` → View menu

* Admin panel:
  `http://127.0.0.1:8000/admin/` → Manage items

---

## 🗂 Models Overview

### Item Model

* `meal` – Name of the dish
* `description` – Description of the meal
* `price` – Price of the item
* `meal_type` – Category (Starters, Salads, etc.)
* `author` – User who created the item
* `status` – Availability (Available / Unavailable)
* `date_created` – Created timestamp
* `date_updated` – Updated timestamp

---

## 💡 Future Improvements

* 🖼 Add images for menu items
* 🔍 Search and filter functionality
* 🛒 Ordering system
* ⭐ Ratings & reviews
* 📱 Responsive design with Bootstrap

---

## 📄 License

This project is open-source and available under the MIT License.

---


