#импортируем Flask и библиотеку Request
from flask import Flask, render_template, request
import requests

#создауем объект класса Flask
app = Flask(__name__)

#формируем путь и методы GET и POST
@app.route('/', methods=['GET', 'POST'])
#создаем функцию с переменной weather, где мы будем сохранять погоду
def weather_news():
   weather = None
   news = None
   # формируем условия для проверки метода
   if request.method == 'POST':
       # этот определенный город мы будем брать для запроса API
       city = request.form['city']
       #прописываем переменную, куда будет сохраняться результат и функцию weather с указанием города, который берем из формы
       weather = get_weather(city)
       # прописываем переменную, куда будет сохраняться результат запроса новостей
       news = get_news()
       #передаем информацию о погоде в index.html
   return render_template("weather_news.html", weather=weather, news=news)

#в функции прописываем город, который мы будем вводить в форме
def get_weather(city):
   api_key = "your api key"
   #адрес, по которомы мы будем отправлять запрос
   url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
   #для получения результата нам понадобится модуль requests
   response = requests.get(url)
   #прописываем формат возврата результата
   return response.json()

def get_news():
   api_key = "your api key"
   # адрес, по которомы мы будем отправлять запрос
   url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
   # для получения результата нам понадобится модуль requests
   response = requests.get(url)
   # прописываем формат возврата результата
   return response.json().get('articles', [])

#прописываем запуск
if __name__ == '__main__':
   app.run(debug=True)