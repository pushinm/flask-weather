from flask import Flask, render_template, request
import json
import urllib.request as urequest

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
    else:
        # for default name
        city = 'mathura'

    # API KEY
    api = 'c3a7ace3e63db42993bda7945e71278c'

    # SOURCE CONTAINING JSON DATA FROM FROM API
    source = urequest.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api).read()

    list_of_data = json.loads(source)

    data = {
        'country_code': str(list_of_data['sys']['country']),
        'coordinate': str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
        'temp': str(list_of_data['main']['temp']) + 'k',
        'pressure': str(list_of_data['main']['pressure']),
        'humidity': str(list_of_data['main']['humidity']),
    }
    print(data)
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)