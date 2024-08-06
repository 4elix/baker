from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя категории')
    image = models.ImageField(upload_to='image/categories/', verbose_name='Картинка категории')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['pk']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Products(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    price = models.IntegerField(default=0, verbose_name='Стоимость')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание на детальную страницу')
    quantity = models.IntegerField(default=0, verbose_name='Количество')
    slug = models.SlugField(max_length=255, verbose_name='ссылка до продукта')

    def __str__(self):
        return self.title

    def get_first_image(self):
        photo = self.product_image.all().first()
        if photo is not None:
            return photo.image.url
        else:
            return 'https://kartinkof.club/uploads/posts/2022-06/1655949284_11-kartinkof-club-p-kartinki-s-nadpisyu-net-ya-s-gorla-12.jpg'

    def get_list_image(self):
        try:
            photo = self.product_iamge.all()
            return photo
        except:
            return '-'

    class Meta:
        ordering = ['pk']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ProductGallery(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_image')
    image = models.ImageField(upload_to=f'image/product/', blank=True, null=True)


class Worker(models.Model):
    CHOICES_POSITION = [
        ('с', 'Стажер'),
        ('к', 'Кондитер'),
        ('п', 'Пекарь'),
        ('гп', 'Главный пекарь')
    ]
    full_name = models.CharField(max_length=255, verbose_name='ФИО работника')
    years_experience = models.IntegerField(default=0, verbose_name='Годы опыта')
    image = models.ImageField(upload_to='image/team/', verbose_name='Фото работника')
    position = models.CharField(max_length=2, choices=CHOICES_POSITION, default='c', verbose_name='Должность')
    facebook = models.CharField(max_length=200, verbose_name='Ссылка на facebook')
    twitter_x = models.CharField(max_length=200, verbose_name='Ссылка на twitter')
    instagram = models.CharField(max_length=200, verbose_name='Ссылка на instagram')

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['pk']
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
