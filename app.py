from flask import Flask, render_template, request
from weather import get_weather

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather, temp_city, icon = None, None, None
    if request.method == 'POST':
        location = request.form['locationName']
        weather, temp_city, icon  = get_weather(location)
        print(weather)
        print(temp_city)
        print(icon)

    return render_template('index.html', weather=weather, temp_city=temp_city, icon=icon )

if __name__ == '__main__':
    app.run(debug=True)



