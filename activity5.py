
# ================STUDENT DETAILS==============
# Web Applications
# Kabba Bangura
# Date: 2022, 12, 7
# /Working with JSON /Dictionaries and Application Programming interfaces

# Completed Python program as defined in the attached file: 3900 Activity 5 Working with API’s and JSON -sv.pdfDownload 3900 Activity 5 Working with API’s and JSON -sv.pdf

from datetime import datetime
import requests
import pytemperature
import sys


def main():
    api_start = "https://api.openweathermap.org/data/2.5/weather?q="
    api_key = '&appid=146e28701aae5676a191025afebeecf3'
    now = datetime.now()
    day_date = now.strftime('%A,%B %d, %Y')
    print('ISQA 3900 Open Weather API')
    print(day_date)
    filename = input('\nEnter the output filename: ')
    try:
        myfile = open(filename, 'w')

    except:
        print('Unable to open file '+filename +
              "\n Data will not be save to a file")
    choice = 'y'
    while choice.lower() == 'y':
        # input city and county code
        city = input('Enter city: ')
        print('Use ISO letter county code like: https://countrycode.org/')
        country = input("Enter country code: ")
        # app configures url to generate json data
        try:
            url = api_start+city+','+country+api_key
            json_data = requests.get(url).json()

            # getting weather data from json
            weather_description = json_data['weather'][0]['description']
            temperature = pytemperature.k2f(json_data['main']['temp'])
            pressure = json_data['main']['pressure']
            humidity = json_data['main']['humidity']
            print('The weather Report for: ' +
                  city + ' in ' + country + ' is: ')
            print('\tCurrent conditions: ', weather_description)
            print('\tCurrent Temperature in Fahrenheit: ', temperature)

            print('\tCurrent Pressure in hpa: ', pressure)

            print('\tCurrent Humidity: ', humidity, '%')
            choice = input('Continue(y/n)?: ')
            print()

        except KeyError as e:
            print('An Error occured while matching the key ', e)

    if myfile:
        myfile.close()
    print('Thank you- Goodbye ')


if __name__ == '__main__':
    main()
