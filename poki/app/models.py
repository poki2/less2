from django.db import models
from django.utils.text import slugify

# Create your models here.


class Motherboard(models.Model):
    brand = models.CharField(max_length=255, verbose_name='Бренд')
    model = models.CharField(max_length=255, verbose_name='Модель')
    chipset = models.CharField(max_length=255, verbose_name='Чипсет')
    socket = models.CharField(max_length=50, verbose_name='Сокет')
    price = models.PositiveIntegerField(verbose_name='Цена')
    photo = models.FileField(upload_to='img/', null=True, verbose_name='Фото')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии')



    def __str__(self):
        return f"{self.brand} {self.model}"

    class Meta:
        verbose_name = 'Материнская плата'
        verbose_name_plural = 'Материнские платы'
        get_latest_by = 'id'




# class Processor(models.Model):
#     brand = models.CharField(max_length=255, verbose_name='Бренд')
#     model = models.CharField(max_length=255, verbose_name='Модель')
#     socket = models.CharField(max_length=50, verbose_name='Сокет')
#     cores = models.PositiveIntegerField(verbose_name='Количество ядер')
#     frequency = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Частота (GHz)')
#     cache = models.CharField(max_length=255, blank=True, null=True, verbose_name='Кэш-память')
#     price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
#     in_stock = models.BooleanField(default=True, verbose_name='В наличии')
#
#
#     def __str__(self):
#         return f"{self.brand} {self.model}"
#
#     class Meta:
#         verbose_name = 'Процессор'
#         verbose_name_plural = 'Процессоры'
#
#
# class RAM(models.Model):
#     brand = models.CharField(max_length=255, verbose_name='Бренд')
#     model = models.CharField(max_length=255, verbose_name='Модель')
#     capacity = models.PositiveIntegerField(verbose_name='Объем (ГБ)')
#     speed = models.PositiveIntegerField(verbose_name='Частота (MHz)')
#     type = models.CharField(max_length=50, verbose_name='Тип памяти')
#     price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
#     in_stock = models.BooleanField(default=True, verbose_name='В наличии')
#
#
#     def __str__(self):
#         return f"{self.brand} {self.model}"
#
#     class Meta:
#         verbose_name = 'Оперативная память'
#         verbose_name_plural = 'Оперативная память'
#
#
# class SSD(models.Model):
#     brand = models.CharField(max_length=255, verbose_name='Бренд')
#     model = models.CharField(max_length=255, verbose_name='Модель')
#     capacity = models.PositiveIntegerField(verbose_name='Объем (ГБ)')
#     interface = models.CharField(max_length=50, verbose_name='Интерфейс')
#
#     read_speed = models.PositiveIntegerField(verbose_name='Скорость чтения (MB/s)')
#     write_speed = models.PositiveIntegerField(verbose_name='Скорость записи (MB/s)')
#
#     price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
#     in_stock = models.BooleanField(default=True, verbose_name='В наличии')
#
#
#     def __str__(self):
#         return f"{self.brand} {self.model}"
#
#     class Meta:
#         verbose_name = 'SSD'
#         verbose_name_plural = 'SSD'
#
# class HDD(models.Model):
#     brand = models.CharField(max_length=255, verbose_name='Бренд')
#     model = models.CharField(max_length=255, verbose_name='Модель')
#     capacity = models.PositiveIntegerField(verbose_name='Объем (ГБ/ТБ)')
#     interface = models.CharField(max_length=50, verbose_name='Интерфейс')
#     speed = models.PositiveIntegerField(blank=True, null=True, verbose_name='Скорость вращения (RPM)')
#     price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
#     in_stock = models.BooleanField(default=True, verbose_name='В наличии')
#
#
#     def __str__(self):
#         return f"{self.brand} {self.model}"
#
#     class Meta:
#         verbose_name = 'HDD'
#         verbose_name_plural = 'HDD'
#
# class GraphicsCard(models.Model):
#     brand = models.CharField(max_length=255, verbose_name='Бренд')
#     model = models.CharField(max_length=255, verbose_name='Модель')
#     video_memory = models.PositiveIntegerField(verbose_name='Видеопамять (ГБ)')
#     interface = models.CharField(max_length=50, verbose_name='Интерфейс')
#     cuda_cores = models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество ядер CUDA')
#
#     directx_support = models.CharField(max_length=10, verbose_name='Поддержка DirectX')
#     opengl_support = models.CharField(max_length=10, verbose_name='Поддержка OpenGL')
#
#     price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
#     in_stock = models.BooleanField(default=True, verbose_name='В наличии')
#
#
#     def __str__(self):
#         return f"{self.brand} {self.model}"
#
#     class Meta:
#         verbose_name = 'Видеокарта'
#         verbose_name_plural = 'Видеокарты'
#
# class Cooler(models.Model):
#     brand = models.CharField(max_length=255, verbose_name='Бренд')
#     model = models.CharField(max_length=255, verbose_name='Модель')
#     socket_support = models.CharField(max_length=50, verbose_name='Поддерживаемые сокеты')
#     fan_speed = models.PositiveIntegerField(verbose_name='Скорость вращения вентилятора (RPM)')
#     noise_level = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Уровень шума (дБ)')
#
#     cooler_type = models.CharField(max_length=50, verbose_name='Тип кулера')
#
#     price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
#     in_stock = models.BooleanField(default=True, verbose_name='В наличии')
#
#
#     def __str__(self):
#         return f"{self.brand} {self.model}"
#
#     class Meta:
#         verbose_name = 'Кулер'
#         verbose_name_plural = 'Кулеры'
#
# class PowerSupply(models.Model):
#     brand = models.CharField(max_length=255, verbose_name='Бренд')
#     model = models.CharField(max_length=255, verbose_name='Модель')
#     power_output = models.PositiveIntegerField(verbose_name='Мощность (Вт)')
#     efficiency_rating = models.CharField(max_length=10, verbose_name='Эффективность')
#
#     price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
#     in_stock = models.BooleanField(default=True, verbose_name='В наличии')
#
#
#     def __str__(self):
#         return f"{self.brand} {self.model}"
#
#     class Meta:
#         verbose_name = 'Блок питания'
#         verbose_name_plural = 'Блоки питания'
#
# class ComputerCase(models.Model):
#     brand = models.CharField(max_length=255, verbose_name='Бренд')
#     model = models.CharField(max_length=255, verbose_name='Модель')
#     side_panel = models.CharField(max_length=50, verbose_name='Боковая панель')
#
#     included_fans = models.PositiveIntegerField(verbose_name='Вентиляторы в комплекте')
#
#     drive_bays = models.CharField(max_length=255, verbose_name='Отсеки для накопителей')
#
#     price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
#     in_stock = models.BooleanField(default=True, verbose_name='В наличии')
#
#
#
#
#     def __str__(self):
#         return f"{self.brand} {self.model}"
#
#     class Meta:
#         verbose_name = 'Корпус'
#         verbose_name_plural = 'Корпусы'