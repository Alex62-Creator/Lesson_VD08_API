#Импортируем библиотеки и модули
from flask import render_template, request, redirect, url_for
import requests
from translate import Translator
from app import app

#Инициализируем пустой список для хранения цитат
quotes = []

#Создаём маршрут для страницы нашего приложения
@app.route('/', methods=["GET", "POST"])
def index():
    #Проверяем был ли запрос на цитату
    if request.method == 'POST':
        #Получаем рандомную цитату в формате JSON
        quote_json = get_quote()
        #Выделяем текст цитаты и переводим на русский
        quote = translate_to_rus(quote_json[0]['quote'])
        # Выделяем автора
        author = quote_json[0]['author']
        # Выделяем категорию цитаты и переводим на русский
        category = translate_to_rus(quote_json[0]['category'])
        #Добавляем в список цитат
        quotes.append({'quote': quote, 'author': author, 'category': category})
        #Используем для обновления страницы и предотвращения повторной отправки формы.
        return redirect(url_for('index'))
    #Передаем список с цитатами в index.html
    return render_template('index.html', quotes=quotes)

#Функция получения цитаты с сайта api.api-ninjas.com с использованием API
def get_quote():
    #URL необходимой страницы
    url = 'https://api.api-ninjas.com/v1/quotes'
    #API-ключ
    api_key = 'your api-key'
    #Запрос к сайту
    response = requests.get(url, headers={'X-Api-Key': api_key})
    #Если запрос выполнен успешно, возвращаем цитату в формате JSON
    if response.status_code == requests.codes.ok:
        return response.json()

# Создаём функцию, которая будет переводить на русский
def translate_to_rus(text):
    # Создаём объект Translator
    translator = Translator(to_lang="ru")
    # Переводим
    result = translator.translate(text)
    # Возвращаем результат перевода
    return result

