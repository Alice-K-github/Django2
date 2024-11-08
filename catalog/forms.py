from django import forms
from .models import Product
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    class Meta:
        # Форма для продукта (создания/редактирования)
        model = Product # Модель (продукт)
        # Включённые в форму элементы модели
        fields = ['name', 'description', 'picture', 'price', 'category', 'created_at', 'updated_at', 'category', 'manufactured_at']

    def __init__(self, *args, **kwargs):
        # Подключение стилизации полей формы
        super(ProductForm, self).__init__(*args, **kwargs)

        # Настройка атрибутов виджета для поля 'name'
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите название продукта'  # Текст подсказки внутри поля
        })

        # Настройка атрибутов виджета для поля 'description'
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите описание продукта'  # Текст подсказки внутри поля
        })

        # Настройка атрибутов виджета для поля 'picture'
        self.fields['picture'].widget.attrs.update({
            'class': 'form-control', # Добавление CSS-класса для стилизации поля
        })

        # Настройка атрибутов виджета для поля 'price'
        self.fields['price'].widget.attrs.update({
            'class': 'form-control', # Добавление CSS-класса для стилизации поля
            'type': 'int' # Указание типа вводимых данных
        })

        # Настройка атрибутов виджета для поля 'category'
        self.fields['category'].widget.attrs.update({
            'class': 'form-control', # Добавление CSS-класса для стилизации поля
        })

        # Настройка атрибутов виджета для поля 'created_at'
        self.fields['created_at'].widget.attrs.update({
            'class': 'form-control', # Добавление CSS-класса для стилизации поля
            'type': 'date', # Указание типа вводимых данных
            'placeholder': '01.01.2000 21:03:22' # Текст подсказки внутри поля
        })

        # Настройка атрибутов виджета для поля 'updated_at'
        self.fields['updated_at'].widget.attrs.update({
            'class': 'form-control', # Добавление CSS-класса для стилизации поля
            'type': 'date', # Указание типа вводимых данных
            'placeholder': '01.01.2000 21:03:22' # Текст подсказки внутри поля
        })

        # Настройка атрибутов виджета для поля 'manufactured_at'
        self.fields['manufactured_at'].widget.attrs.update({
            'class': 'form-control', # Добавление CSS-класса для стилизации поля
            'type': 'date', # Указание типа вводимых данных
            'placeholder': '01.01.2000 21:03:22' # Текст подсказки внутри поля
        })



    def clean_price(self):
        # Валидация для цены
        price = self.cleaned_data.get('price') # Получение значения цены
        if price < 0 :
            raise ValidationError('Цена не должна быть отрицательной.') # Если цена отрицательная - вызывается ошибка валидации
        return price # возвращает значение


    def clean(self):
        # Валидация для всех (нескольких) полей
        cleaned_data = super().clean() # Получаем все значения полей формы
        name = cleaned_data.get('name') # Получаем значение поля названия
        description = cleaned_data.get('description') # Получаем значение поля описания

        if ("казино" or "криптовалюта" or "крипта" or "биржа" or "дешево" or "бесплатно" or "обман" or "полиция" or "радар") in (name or description):
            self.add_error('name', 'В названии\описании нельзя использовать запрещённые слова.') # При наличии запрещённых слов выдаёт ошибку

