import smtplib
import pandas as pd
import datetime as dt
import random
import os

# --- 1. إعدادات البريد الإلكتروني ---
MY_EMAIL = "your_email@gmail.com"
MY_PASSWORD = "your_app_password"  # كلمة مرور التطبيقات من جوجل

# --- 2. التحقق من تاريخ اليوم ---
now = dt.datetime.now()
today_tuple = (now.month, now.day)

# --- 3. قراءة ملف البيانات ---
data = pd.read_csv("birthdays.csv")
birthdays_dict = {
    (data_row["month"], data_row["day"]): data_row 
    for (index, data_row) in data.iterrows()
}

# --- 4. التحقق وإرسال الرسالة ---
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    
    # اختيار نموذج رسالة عشوائي
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    
    with open(file_path) as letter_file:
        content = letter_file.read()
        # استبدال الاسم في الرسالة
        final_letter = content.replace("[NAME]", birthday_person["name"])

    # إرسال الإيميل
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{final_letter}"
        )
    print(f"Done! Email sent to {birthday_person['name']}")