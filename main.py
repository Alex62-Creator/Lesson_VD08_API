import requests
api_url = 'https://api.api-ninjas.com/v1/quotes'
response = requests.get(api_url, headers={'X-Api-Key': 'QxBNBiZt7JqAZQZrIEXCKA==Fh4x99LAfgx7Dqvm'})
if response.status_code == requests.codes.ok:
    print(f"Цитата: {response.json()}")
else:
    print("Error:", response.status_code, response.text)


##Импортируем объект Flask
from app import app

#Запускаем приложение
if __name__ == '__main__':
    app.run(debug=True)


Models

#Импортируем библиотеки
from app import db, login_manager
from flask_login import UserMixin # Этот класс даёт возможность работать с пользователем

#Создаём декоратор, который сообщает Flask, что функция будет использоваться для загрузки пользователя по его ID
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) # Эта строчка будет отправлять в БД запрос для поиска определённого юзера по его ID

#Создаём класс User
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):  # Функция, чтобы представить информацию о пользователе в виде одной строки
        return f'User: {self.username}, email: {self.emai}'