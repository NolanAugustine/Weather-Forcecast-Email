
import requests
import json
import time
import smtplib
import pyfiglet
import sys
from config import *

#Title Page
def write(text, speed=0.02):
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()

    time.sleep(speed)

  print("") # flush a line



txt = "Python Weather Forecast Email\n"
by_line_raw = 'By: Nolan Augustine'

ascii_banner = pyfiglet.figlet_format(txt, font='slant')
by_line = pyfiglet.figlet_format(by_line_raw, font='small')

write(ascii_banner, speed=0.002)
write(by_line, speed=0.002)


#Api Call
lat = "41.710748"
lon = "-88.242869"
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=imperial" % (lat, lon, api_key)
response = requests.get(url)
data = response.text
parse_json = json.loads(data)
today_weather = parse_json["daily"] [0]

#Today variables
date = today_weather["dt"]
my_time = time.strftime('%m-%d-%y', time.localtime(date))
temp_day = today_weather["temp"] ['day']
temp_night = today_weather["temp"] ['night']
temp_eve = today_weather["temp"] ['eve']
temp_day = today_weather["temp"] ['day']
temp_min = today_weather["temp"] ['min']
temp_max = today_weather["temp"] ['max']
temp_morn = today_weather['temp'] ['morn']
feelslike_morn = today_weather['feels_like'] ['morn']
feelslike_day = today_weather['feels_like'] ['day']
feelslike_eve = today_weather['feels_like'] ['eve']
feelslike_night = today_weather['feels_like'] ['night']
humidity = today_weather['humidity']
wind_speed = today_weather['wind_speed']
pop = today_weather['pop'] 
pop_value = pop * 100

today_output = "Weather for today, " + my_time + ':\n' + 'Morning Temp: ' + str(temp_morn) + 'F' +  '\nMorning Feels Like: ' + str(feelslike_morn) + 'F' + '\nDay Temp: ' + str(temp_day) + 'F' + '\nDay Feels Like: ' + str(feelslike_day) + 'F' + '\nEvening Temp: ' + str(temp_eve) + 'F' + '\nEvening Feels Like: ' + str(feelslike_eve) + 'F' + '\nNight Temp: ' + str(temp_night) +'F' + '\nNight Feels Like: ' + str(feelslike_night) +'F' + '\nHumidity: ' + str(humidity) + '%' + '\nWind Speed: ' + str(wind_speed) + ' MPH' + '\nPercipitation Percentage: ' + str(pop_value) + '%\n'


#tom variables
tom_weather = parse_json["daily"] [1]

tom_date = tom_weather["dt"]
tom_time = time.strftime('%m-%d-%y', time.localtime(tom_date))
tom_my_time = time.strftime('%m-%d-%y', time.localtime(date))
tom_temp_day = tom_weather["temp"] ['day']
tom_temp_night = tom_weather["temp"] ['night']
tom_temp_eve = tom_weather["temp"] ['eve']
tom_temp_day = tom_weather["temp"] ['day']
tom_temp_min = tom_weather["temp"] ['min']
tom_temp_max = tom_weather["temp"] ['max']
tom_temp_morn = tom_weather['temp'] ['morn']
tom_feelslike_morn = tom_weather['feels_like'] ['morn']
tom_feelslike_day = tom_weather['feels_like'] ['day']
tom_feelslike_eve = tom_weather['feels_like'] ['eve']
tom_feelslike_night = tom_weather['feels_like'] ['night']
tom_humidity = tom_weather['humidity']
tom_wind_speed = tom_weather['wind_speed']
tom_pop = tom_weather['pop'] 
tom_pop_value = pop * 100

tom_output = "\nWeather for tommorow, " + tom_time + ':\n' + 'Morning Temp: ' + str(tom_temp_morn) + 'F' +  '\nMorning Feels Like: ' + str(tom_feelslike_morn) + 'F' + '\nDay Temp: ' + str(tom_temp_day) + 'F' + '\nDay Feels Like: ' + str(tom_feelslike_day) + 'F' + '\nEvening Temp: ' + str(tom_temp_eve) + 'F' + '\nEvening Feels Like: ' + str(tom_feelslike_eve) + 'F' + '\nNight Temp: ' + str(tom_temp_night) +'F' + '\nNight Feels Like: ' + str(tom_feelslike_night) +'F' + '\nHumidity: ' + str(tom_humidity) + '%' + '\nWind Speed: ' + str(tom_wind_speed) + ' MPH' + '\nPercipitation Percentage: ' + str(tom_pop_value) + '%'


total_output = str(today_output + tom_output)

#Email 

write('Recipient Email Adress: ')
send_add = input()


SUBJECT = "Daily Weather Forecast"   
TEXT = total_output
 
message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('nolan.python@gmail.com', email_pass)
server.sendmail('nolan.python@gmail.com', send_add, message)
write('Mail was sent')
