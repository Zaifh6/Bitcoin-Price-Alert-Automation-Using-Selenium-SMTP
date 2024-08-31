# Bitcoin Price Alert System Using Selenium & SMTP

![Bitcoin Price Alert](https://github.com/user-attachments/assets/f69d28c6-c049-435d-a831-d95c7efef7b7)
![Price Alert Example](https://github.com/user-attachments/assets/0cae66de-a66f-4ad7-b073-d9d2cd0decdc)

## About The Project

The Bitcoin Price Alert System is a practical application built using Python. It leverages the `selenium` library to monitor real-time Bitcoin prices on CoinMarketCap and sends email alerts using `smtplib` when significant price changes are detected. This project demonstrates the integration of web scraping and email communication to keep users informed about important cryptocurrency market movements.

### Features

- Real-time Bitcoin price monitoring using Selenium
- Email alerts sent via SMTP when the Bitcoin price increases or decreases significantly
- Easy-to-customize thresholds for price alerts
- Clear and concise email notifications with relevant market information

### Built With

* **Python** – The programming language used to implement the core functionality.
* **Selenium** – For automating web browser interactions to scrape Bitcoin price data from CoinMarketCap.
* **SMTP** – For sending email alerts about Bitcoin price changes.
* **EmailMessage** – Part of the `email` module for creating well-encoded email messages with UTF-8 support.

## Getting Started

To get this Bitcoin Price Alert System up and running locally, follow these steps:

### Prerequisites

1. **Python:** Ensure Python is installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).
2. **Python Libraries:** Install the required libraries using pip:
- Selenium
- time
- Email
- SMTP
