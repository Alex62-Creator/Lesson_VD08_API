#Импортируем библиотеки и модули
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional

#Импортируем модель User из нашего модуля
from app.models import User

#Создаём класс RegistrationForm, который будет создавать форму регистрации
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    #Создаём функцию для проверки уникальности имени пользователя
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Такое имя уже существует.')

    #Создаём функцию для проверки уникальности почты
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Такая почта уже используется.')

#Создаём класс LoginForm, который будет создавать форму входа зарегистрированных пользователей
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Запомни меня')
    submit = SubmitField('Login')

#Создаём класс ModifyForm, который будет создавать форму регистрации
class ModifyForm(FlaskForm):
    username = StringField('New Username', validators=[Optional(), Length(min=2, max=20)])
    email = StringField('New Email', validators=[Optional(), Email()])
    password = PasswordField('New Password', validators=[Optional()])
    confirm_password = PasswordField('Confirm Password', validators=[Optional(), EqualTo('password')])
    submit = SubmitField('Submit')

    #Создаём функцию для проверки уникальности имени пользователя
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Такое имя уже существует.')

    #Создаём функцию для проверки уникальности почты
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Такая почта уже используется.')