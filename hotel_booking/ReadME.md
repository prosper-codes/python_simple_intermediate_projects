
---

# Hotel Booking System

A simple **Python-based hotel booking system** that allows users to book hotels, validate credit cards, and generate reservation tickets.
Data is stored in CSV files (`hotels.csv`, `cards.csv`, `card_security.csv`) for simplicity.

---

## Features

* Check hotel availability
* Book a hotel (updates the CSV file)
* Validate credit card details
* Authenticate secure credit cards with a password
* Generate a reservation ticket for the customer

---

## Requirements

* Python 3.7 or higher
* `pandas` library

Install dependencies using pip:

```bash
pip install pandas
```

---

## CSV File Structure

### `hotels.csv`

| id  | name           | city       | stars | available |
| --- | -------------- | ---------- | ----- | --------- |
| 188 | Snow Palace    | New Delhi  | 5     | yes       |
| 655 | City Break Inn | Porto-Novo | 3     | no        |

* `id` – Hotel ID (string)
* `available` – `"yes"` or `"no"`

---

### `cards.csv`

| number | expiration | cvc | holder     |
| ------ | ---------- | --- | ---------- |
| 1234   | 12/26      | 123 | JOHN SMITH |
| 5678   | 12/28      | 456 | JANE SMITH |

* Card details used for validation.

---

### `card_security.csv`

| number | password |
| ------ | -------- |
| 1234   | mypass   |
| 5678   | pass456  |

* Stores card numbers and passwords for authentication.

---

## How to Run

1. Make sure all CSV files (`hotels.csv`, `cards.csv`, `card_security.csv`) are in the same directory as the script.
2. Run the Python script:

```bash
python main.py
```

3. Follow the prompts:

```
Enter the id of the hotel: 188
Enter the card number: 1234
Enter your name: Alice
```

* If the card is validated and authentication succeeds, the hotel is booked and a **reservation ticket** is displayed.

---

## Example Output

```
Thank you for your reservation!
Here are your booking data:
Name: Alice
Hotel name: Snow Palace
```

---

## Notes

* The program **updates the `hotels.csv` file** to mark hotels as unavailable once booked.
* Credit card validation and authentication are **case-sensitive**.
* Make sure the password in `card_security.csv` matches the input exactly.

---

## Future Improvements

* Add user-friendly input validation
* Support multiple card types
* Implement password hashing for security
* Convert CSV storage to a database for scalability

---



