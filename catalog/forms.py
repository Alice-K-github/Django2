from django import forms
from .models import Product
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'picture', 'price', 'category', 'created_at', 'updated_at', 'category', 'manufactured_at']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        # Настройка атрибутов виджета для поля 'name'
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите название продукта'  # Текст подсказки внутри поля
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите описание продукта'  # Текст подсказки внутри поля
        })

        self.fields['picture'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'type': 'int'
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['created_at'].widget.attrs.update({
            'class': 'form-control',
            'type': 'date',
            'placeholder': '01.01.2000 21:03:22'
        })

        self.fields['updated_at'].widget.attrs.update({
            'class': 'form-control',
            'type': 'date',
            'placeholder': '01.01.2000 21:03:22'
        })

        self.fields['manufactured_at'].widget.attrs.update({
            'class': 'form-control',
            'type': 'date',
            'placeholder': '01.01.2000 21:03:22'
        })



    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0 :
            raise ValidationError('Цена не должна быть отрицательной.')
        return price


    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        if ("казино" or "криптовалюта" or "крипта" or "биржа" or "дешево" or "бесплатно" or "обман" or "полиция" or "радар") in (name or description):
            self.add_error('name', 'В названии\описании нельзя использовать запрещённые слова.')

