import smtplib
import random
import datetime
import pandas as pd
import os
now_str = datetime.datetime.now().strftime("%d/%m")
print(now_str)
ran_num = random.randint(1,3)
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

# 1. Tạo DataFrame từ dữ liệu của bạn
# data = {
#     "Ten": ["Mom", "Dad", "Nhim"],
#     "NgaySinh": ["27/08", "31/05", "18/07"], 
# }
# df = pd.DataFrame(data)
# df.to_csv("ngay_sinh.csv", index=False, encoding="utf-8")
records = pd.read_csv('birthdays.csv').to_dict(orient='records')
# check ngay 
for i in records:
    if i["NgaySinh"] == now_str:
        with open(f"letter_{ran_num}.txt",mode="r") as letter_file:
            letter_file= letter_file.read()
            new_letter = letter_file.replace("[NAME]", i["Ten"])
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL,MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=i["Email"],
                msg=f"Subject:Happy Birthday!\n\n{new_letter}"
            )
# print(records["NgaySinh"])
