TOKEN = '5603298774:AAGsGcyym2nbhLmKoWma7pywqQcC9y3srOU'

URL = 'https://api.telegram.org/bot{token}/{method}'

UPDATE_METH = 'getUpdates'
SEND_METH = 'sendMessage'
MY_ID = 202224680

UPDATE_ID_FILE_PATH = 'update_id'

with open(UPDATE_ID_FILE_PATH) as file:
    data = file.readline()
    if data:
        data = int(data)
    UPDATE_ID = data

WEATHER_TOKEN = 'e52e848f35be82df70319d393ce8d8d4'

WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}'
