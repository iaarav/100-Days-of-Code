import time
import requests
from datetime import datetime
import smtplib

MY_LAT = 28.973430
MY_LONG = 77.656290
MY_EMAIL = "thecodeteen21@gmail.com"
MY_PASS = ""


def issIsOverhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    diffLat = iss_latitude - MY_LAT
    diffLong = iss_longitude - MY_LONG

    if -5 <= diffLat <= 5 and -5 <= diffLong <= 5:
        return True


def isNightTime():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)

    if isNightTime() and issIsOverhead():
        connection = smtplib.SMTP("smtp.google.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="aarav2008bansal@gmail.com",
            msg="Subject: Look Up!! \n\nThe ISS Space Station is near your place!!"
        )
