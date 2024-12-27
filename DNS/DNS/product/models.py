from django.db import models

class Product(models.Model):
    title = models.CharField('Название', max_length=100)
    price = models.IntegerField('Цена')
    description = models.TextField()
    catagory = models.CharField('Категория',
                                 choices=[('Первая', 'Первая'), ('Вторая', 'Вторая'), ('Третья', 'Третья')], max_length=200)
    
    def __str__(self):
        return self.title