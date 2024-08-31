# importing all the libraries neede
from email.message import EmailMessage
from smtplib import SMTP
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# adding personal info
my_email = "YOUR_EMAIL"
password = "APP_PASSWORD"  # Use an App Password if 2FA is enabled

# creating a class
class Currency():
    def __init__(self):
        
        # basic selenium setup which will open the page
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get("https://coinmarketcap.com/")

    # fetch the bitcoin currency    
    def currency_update(self):
        time.sleep(3)
        bitcoin_element = self.driver.find_element(By.XPATH,
                                           '//*[@id="__next"]/div[2]/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[1]/td[4]/div/span')
        return bitcoin_element.text

    # send email method
    def send_up_email(self):
        msg = EmailMessage()
        msg.set_content("""We want to inform you that Bitcoin has experienced a notable increase in price recently. This movement could have significant implications for your investment strategy and market outlook.
Please review your portfolio and consider any necessary adjustments based on this development. For detailed analysis and up-to-date information, we recommend checking your preferred financial news sources or trading platforms.
If you have any questions or need further assistance, feel free to reach out.""")
        msg["Subject"] = "🚀 Alert: Bitcoin Price Has Increased!"
        msg["From"] = my_email
        msg["To"] = "EMAIL TO SEND THE MESSAGE"

        with SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.send_message(msg)
            print("Email sent successfully!")

    def send_down_email(self):
        msg = EmailMessage()
        msg.set_content("""We want to inform you that Bitcoin has recently experienced a decline in price. This drop could impact your investment strategy and market positions.
We recommend reviewing your portfolio and considering any necessary adjustments. For detailed information and analysis, please consult your preferred financial news sources or trading platforms.
If you need further assistance or have any questions, please feel free to reach out.""")
        msg["Subject"] = "📉 Alert: Bitcoin Price Has Decreased"
        msg["From"] = my_email
        msg["To"] = "EMAIL TO SEND THE MESSAGE"

        with SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.send_message(msg)
            print("Email sent successfully!")

# creating a bot object
bot = Currency()
# data cleaning
bitcoin_price_str = bot.currency_update()
bitcoin_price_str = bitcoin_price_str.strip("$")
bitcoin_price_str_clean = bitcoin_price_str.replace(",", "")
bitcoin_price_float = float(bitcoin_price_str_clean)
bitcoin_price = int(bitcoin_price_float)
print(bitcoin_price)

# custom conditions on when to send email
# we can also customize these conditions so that we only get weekly updates
if bitcoin_price > 60000:
    bot.send_up_email()
elif bitcoin_price < 60000:
    bot.send_down_email()
