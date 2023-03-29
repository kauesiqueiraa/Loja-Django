from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.utils.html import mark_safe


class Category(models.Model):
    title = models.CharField(max_length=180)
    image = models.ImageField(upload_to="cat_imgs/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categoria'

    def image_tag_path(self):
        return mark_safe('<img src="%s" width="80" height= "60" />' % (self.image.url))


class Color(models.Model):
    title = models.CharField(max_length=100)
    color_codigo = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Cor'
        verbose_name_plural = 'Cores'

    def color_tag_path(self):
        return mark_safe('<div style="width:40px; height:40px; background:%s" ></div>' % (self.color_codigo))


class Size(models.Model):
    title = models.CharField(max_length=180)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tamanho'
        verbose_name_plural = 'Tamanhos'


class Marca(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="marca_imgs/")

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="product_imgs/")
    slug = models.CharField(max_length=400)
    detail = models.TextField()
    specs = models.TextField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'


class Banner(models.Model):
    img = models.CharField(max_length=250)
    alt_text = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = '1. Banners'


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.product.title
