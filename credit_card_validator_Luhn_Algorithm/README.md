💳 Credit Card Validator (Luhn Algorithm)

A simple Python program to validate credit and debit card numbers using the Luhn Algorithm.

📌 About

The Luhn Algorithm is a checksum formula used to validate card numbers and detect common input errors.
This project implements an optimized and readable version with basic input validation.

⚙️ Features

Validates card numbers using the Luhn algorithm

Supports card numbers with spaces or dashes

Checks for valid length (13–19 digits)

Rejects invalid or non-numeric input

Single-pass optimized logic

🧠 How the Algorithm Works

Remove spaces and dashes from the input

Starting from the correct position, double every second digit

If the doubled value is greater than 9, subtract 9

Add all digits together

If the total is divisible by 10, the card number is valid

🧪 Example

Input

5610591081018250

Output

This card is valid

▶️ Usage

Clone the repository:

git clone https://github.com/prosper-codes/python_simple_intermediate.git
cd card-validator

Run the script:

python card_validator.py

Enter the card number when prompted.

🧩 Core Logic
if idx % 2 == 0:
n \*= 2
if n > 9:
n -= 9

Doubles selected digits

Converts two-digit results into a single digit

Ensures accurate checksum calculation

📂 Project Structure
card-validator/
│── card_validator.py
│── README.md
