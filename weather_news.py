#импортируем Flask и библиотеку Request
from flask import Flask, render_template, request
import requests

#создауем объект класса Flask
app = Flask(__name__)

#формируем путь и методы GET и POST
@app.route('/', methods=['GET', 'POST'])
#создаем функцию с переменной weather, где мы будем сохранять погоду
def weather():
   weather = None
   # формируем условия для проверки метода
   if request.method == 'POST':
       # этот определенный город мы будем брать для запроса API
       city = request.form['city']
       #прописываем переменную, куда будет сохраняться результат и функцию weather с указанием города, который берем из формы
       weather = get_weather(city)
       #передаем информацию о погоде в index.html
   return render_template("weather_news.html", weather=weather)

#в функции прописываем город, который мы будем вводить в форме
def get_weather(city):
   api_key = "945fdp30aac0b74f3de52069536499d8"
   #адрес, по которомы мы будем отправлять запрос
   url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
   #для получения результата нам понадобится модуль requests
   response = requests.get(url)
   #прописываем формат возврата результата
   return response.json()

#прописываем запуск
if __name__ == '__main__':
   app.run(debug=True)