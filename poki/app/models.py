from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify

# Create your models here.






# class CustomUser(AbstractUser):
#     username = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=255)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []


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



    def get_component_info(self):
        return f"Материнская плата: {self.brand} {self.model}, Чипсет: {self.chipset}, Сокет: {self.socket}, Цена: {self.price}$"


    class Meta:
        verbose_name = 'Материнская плата'
        verbose_name_plural = 'Материнские платы'




class Processor(models.Model):
    brand = models.CharField(max_length=255, verbose_name='Бренд')
    model = models.CharField(max_length=255, verbose_name='Модель')
    socket = models.CharField(max_length=50, verbose_name='Сокет')
    cores = models.PositiveIntegerField(verbose_name='Количество ядер')
    frequency = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Частота (GHz)')
    cache = models.CharField(max_length=255, blank=True, null=True, verbose_name='Кэш-память')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии')


    def __str__(self):
        return f"{self.brand} {self.model}"

    class Meta:
        verbose_name = 'Процессор'
        verbose_name_plural = 'Процессоры'

    def get_component_info(self):
        return f"Процессор: {self.brand} {self.model}, Сокет: {self.socket}, Количество ядер: {self.cores}, Частота: {self.frequency} GHz, Цена: {self.price}$"




class RAM(models.Model):
    brand = models.CharField(max_length=255, verbose_name='Бренд')
    model = models.CharField(max_length=255, verbose_name='Модель')
    capacity = models.PositiveIntegerField(verbose_name='Объем (ГБ)')
    speed = models.PositiveIntegerField(verbose_name='Частота (MHz)')
    type = models.CharField(max_length=50, verbose_name='Тип памяти')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии')


    def __str__(self):
        return f"{self.brand} {self.model}"

    class Meta:
        verbose_name = 'Оперативная память'
        verbose_name_plural = 'Оперативная память'


    def get_component_info(self):
        return f"Оперативная память: {self.brand} {self.model}, Объем: {self.capacity} ГБ, Частота: {self.speed} MHz, Цена: {self.price}$"



class SSD(models.Model):
    brand = models.CharField(max_length=255, verbose_name='Бренд')
    model = models.CharField(max_length=255, verbose_name='Модель')
    capacity = models.PositiveIntegerField(verbose_name='Объем (ГБ)')
    interface = models.CharField(max_length=50, verbose_name='Интерфейс')

    read_speed = models.PositiveIntegerField(verbose_name='Скорость чтения (MB/s)')
    write_speed = models.PositiveIntegerField(verbose_name='Скорость записи (MB/s)')

    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии')


    def __str__(self):
        return f"{self.brand} {self.model}"

    class Meta:
        verbose_name = 'SSD'
        verbose_name_plural = 'SSD'


    def get_component_info(self):
        return f"SSD: {self.brand} {self.model}, Объем: {self.capacity} ГБ, Интерфейс: {self.interface}, Скорость чтения/записи: {self.read_speed}/{self.write_speed} MB/s, Цена: {self.price}$"


class HDD(models.Model):
    brand = models.CharField(max_length=255, verbose_name='Бренд')
    model = models.CharField(max_length=255, verbose_name='Модель')
    capacity = models.PositiveIntegerField(verbose_name='Объем (ГБ/ТБ)')
    interface = models.CharField(max_length=50, verbose_name='Интерфейс')
    speed = models.PositiveIntegerField(blank=True, null=True, verbose_name='Скорость вращения (RPM)')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии')


    def __str__(self):
        return f"{self.brand} {self.model}"

    class Meta:
        verbose_name = 'HDD'
        verbose_name_plural = 'HDD'


    def get_component_info(self):
        return f"HDD: {self.brand} {self.model}, Объем: {self.capacity} ГБ/ТБ, Интерфейс: {self.interface}, Скорость вращения: {self.speed} RPM, Цена: {self.price}$"


class GraphicsCard(models.Model):
    brand = models.CharField(max_length=255, verbose_name='Бренд')
    model = models.CharField(max_length=255, verbose_name='Модель')
    video_memory = models.PositiveIntegerField(verbose_name='Видеопамять (ГБ)')
    interface = models.CharField(max_length=50, verbose_name='Интерфейс')
    cuda_cores = models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество ядер CUDA')

    directx_support = models.CharField(max_length=10, verbose_name='Поддержка DirectX')
    opengl_support = models.CharField(max_length=10, verbose_name='Поддержка OpenGL')

    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии')


    def __str__(self):
        return f"{self.brand} {self.model}"

    class Meta:
        verbose_name = 'Видеокарта'
        verbose_name_plural = 'Видеокарты'


    def get_component_info(self):
        return f"Видеокарта: {self.brand} {self.model}, Видеопамять: {self.video_memory} ГБ, Интерфейс: {self.interface}, Количество ядер CUDA: {self.cuda_cores}, Цена: {self.price}$"


class Cooler(models.Model):
    brand = models.CharField(max_length=255, verbose_name='Бренд')
    model = models.CharField(max_length=255, verbose_name='Модель')
    socket_support = models.CharField(max_length=50, verbose_name='Поддерживаемые сокеты')
    fan_speed = models.PositiveIntegerField(verbose_name='Скорость вращения вентилятора (RPM)')
    noise_level = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Уровень шума (дБ)')

    cooler_type = models.CharField(max_length=50, verbose_name='Тип кулера')

    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии')


    def __str__(self):
        return f"{self.brand} {self.model}"

    class Meta:
        verbose_name = 'Кулер'
        verbose_name_plural = 'Кулеры'

    def get_component_info(self):
        return f"Кулер: {self.brand} {self.model}, Поддерживаемые сокеты: {self.socket_support}, Скорость вращения вентилятора: {self.fan_speed} RPM, Уровень шума: {self.noise_level} дБ, Цена: {self.price}$"


class PowerSupply(models.Model):
    brand = models.CharField(max_length=255, verbose_name='Бренд')
    model = models.CharField(max_length=255, verbose_name='Модель')
    power_output = models.PositiveIntegerField(verbose_name='Мощность (Вт)')
    efficiency_rating = models.CharField(max_length=10, verbose_name='Эффективность')

    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии')


    def __str__(self):
        return f"{self.brand} {self.model}"

    class Meta:
        verbose_name = 'Блок питания'
        verbose_name_plural = 'Блоки питания'

    def get_component_info(self):
        return f"Блок питания: {self.brand} {self.model}, Мощность: {self.power_output} Вт, Эффективность: {self.efficiency_rating}, Цена: {self.price}$"




class ComputerCase(models.Model):
    brand = models.CharField(max_length=255, verbose_name='Бренд')
    model = models.CharField(max_length=255, verbose_name='Модель')
    side_panel = models.CharField(max_length=50, verbose_name='Боковая панель')

    included_fans = models.PositiveIntegerField(verbose_name='Вентиляторы в комплекте')

    drive_bays = models.CharField(max_length=255, verbose_name='Отсеки для накопителей')

    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии')




    def __str__(self):
        return f"{self.brand} {self.model}"

    class Meta:
        verbose_name = 'Корпус'
        verbose_name_plural = 'Корпусы'
    def get_component_info(self):
        return f"Корпус: {self.brand} {self.model}, Боковая панель: {self.side_panel}, Вентиляторы в комплекте: {self.included_fans}, Отсеки для накопителей: {self.drive_bays}, Цена: {self.price}$"