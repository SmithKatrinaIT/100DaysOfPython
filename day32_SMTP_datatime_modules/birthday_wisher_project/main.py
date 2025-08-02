import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime as dt
import pandas
import random

contents = ""

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# use Pandas to read csv file into a dataframe
data = pandas.read_csv("birthdays.csv")

# create birthday dictionary from 'data' using dictionary comprehension
# Syntax:  new_dict = {new_key:new_value for (index, data_row) in data.iterrows()}
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

# email address and password
email = "python3.100days@gmail.com"
password = "chzv hgzr xwqc cziv"
msg_subject = "Happy Birthday Wisher App"
# msg = MIMEMultipart()
# msg['From'] = email
# msg['To'] = email
# msg['Subject'] = msg_subject


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if today_tuple in birthday_dict:
	birthday_person = birthday_dict[today_tuple]
	file_path = f'./letter_templates/letter_{random.randint(1,3)}.txt'

	with open(file_path) as file:   # OPEN & READ THE FILE
		contents = file.read()
		contents = contents.replace("[NAME]",  birthday_person["name"])

	# 4. Send the letter generated in step 3 to that person's email address.
	#msg.attach(MIMEText(contents, 'plain'))


	# the object used to connect to smtp server
	with smtplib.SMTP("smtp.gmail.com", 587) as connection:

		# method of sending email securely - encrypted
		connection.starttls()

		# login to email
		connection.login(user=email, password=password)

		#convert_msg_to_string = msg.as_string()
		#convert_msg_to_string = contents

		# send email
		connection.sendmail(from_addr=email, to_addrs=email,msg=f'Subject: {msg_subject}\n\n{contents}')
		print("Email sent successfully")

