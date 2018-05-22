from django.db import models

# Create your models here.

class Manufacturer_Country(models.Model):
    name_manufacturer_country = models.CharField(max_length=64, blank=True, null=True, default=None)
    name_manufacturer_country_ukr = models.CharField(max_length=64, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.name_manufacturer_country

    class Meta:
        verbose_name = 'Manufacturer_Country (Страна производитель)'
        verbose_name_plural = 'Manufacturer_Countrys (Страны призводителей)'


class Manufacturer(models.Model):
    name_manufacturer = models.CharField(max_length=64, blank=True, null=True, default=None)
    image_logo_manufacturer = models.ImageField(upload_to='manufacturer_images_logo/')
    manufacturer_country = models.ForeignKey(Manufacturer_Country, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active = models.BooleanField(default=True)

    description_manufacturer = models.TextField(blank=True, null=True, default=None)
    description_manufacturer_ukr = models.TextField(blank=True, null=True, default=None)
    short_description_manufacturer = models.TextField(blank=True, null=True, default=None)
    short_description_manufacturer_ukr = models.TextField(blank=True, null=True, default=None)

    title = models.CharField(max_length=320, blank=True, null=True, default=None)
    keyword = models.CharField(max_length=512, blank=True, null=True, default=None)
    description = models.CharField(max_length=512, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.name_manufacturer

    class Meta:
        verbose_name = 'Manufacturer (Производитель)'
        verbose_name_plural = 'Manufacturers (Производители)'


class Manufacturer_Image(models.Model):
    name_manufacturer = models.ForeignKey(Manufacturer, blank=True, null=True, default=None)
    image_manufacturer = models.ImageField(upload_to='manufacturer_images/')
    is_active_manufacturer = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Manufacturer_Image (Изображение в производителе)'
        verbose_name_plural = 'Manufacturer_Images (Изображения в производителе)'


class Price_Group(models.Model):
    name_price_group = models.CharField(max_length=64, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.name_price_group

    class Meta:
        verbose_name = 'Price_Group (Ценовая группв)'
        verbose_name_plural = 'Price_Groups (Ценовые группы)'


class Availability(models.Model):
    name_availability = models.CharField(max_length=64, blank=True, null=True, default=None)
    name_availability_ukr = models.CharField(max_length=64, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.name_availability

    class Meta:
        verbose_name = 'Availability (Наличие)'
        verbose_name_plural = 'Availabilitys (Наличие)'


class Collection_Search_NHS(models.Model):
    name_collection_nhs = models.CharField(max_length=64, blank=True, null=True, default=None)
    name_collection_nhs_ukr = models.CharField(max_length=64, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.name_collection_nhs

    class Meta:
        verbose_name = 'Collection_Search_NHS (Новинка_Хит_Распродажа)'
        verbose_name_plural = 'Collection_Search_NHSs (Новинка_Хит_Распродажа)'


class Collection(models.Model):
    id_patch = models.CharField(max_length=30, null=True, default=None)
    is_active_collection = models.BooleanField(default=True)
    is_view_main = models.BooleanField(default=False)
    name_collection = models.CharField(max_length=64, blank=True, null=True, default=None)
    manufacturer_collection = models.ForeignKey(Manufacturer, blank=True, null=True, default=None)
    availability_collection = models.ForeignKey(Availability, blank=True, null=True, default=None)
    price_group_collection = models.ForeignKey(Price_Group, blank=True, null=True, default=None)
    name_collection_nhs = models.ForeignKey(Collection_Search_NHS, blank=True, null=True, default=None)

    price_download = models.FileField(upload_to='price_download/', null=True, default=None)
    image_collection_mini = models.ImageField(upload_to='collection_images_mini/', null=True, default=None)

    description_collection_mini = models.CharField(max_length=140, blank=True, null=True, default=None)
    description_collection_mini_ukr = models.CharField(max_length=140, blank=True, null=True, default=None)

    description_collection = models.TextField(blank=True, null=True, default=None)
    description_collection_ukr = models.TextField(blank=True, null=True, default=None)
    short_description_collection = models.TextField(blank=True, null=True, default=None)
    short_description_collection_ukr = models.TextField(blank=True, null=True, default=None)

    title = models.CharField(max_length=320, blank=True, null=True, default=None)
    title_ukr = models.CharField(max_length=320, blank=True, null=True, default=None)
    keyword = models.CharField(max_length=512, blank=True, null=True, default=None)
    keyword_ukr = models.CharField(max_length=512, blank=True, null=True, default=None)
    description = models.CharField(max_length=512, blank=True, null=True, default=None)
    description_ukr = models.CharField(max_length=512, blank=True, null=True, default=None)


    def __str__(self):
        return "%s" % self.name_collection

    class Meta:
        verbose_name = 'Collection (Коллекция)'
        verbose_name_plural = 'Collections (Коллекции)'


class Collection_Image(models.Model):
    name_collection = models.ForeignKey(Collection, blank=True, null=True, default=None)
    image_collection = models.ImageField(upload_to='collection_images/')
    is_main_collection = models.BooleanField(default=False)
    is_active_collection = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Collection_Image (Изображение в коллекции)'
        verbose_name_plural = 'Collection_Images (Изображения в коллекциях)'


class Collection_Application_For_Search(models.Model):
    name_collection = models.ForeignKey(Collection, blank=True, null=True, default=None)
    collection_application_is_active = models.BooleanField(default=True)
    collection_application_bathrooms = models.BooleanField(default=False)  # Для ванных комнат
    collection_application_floor = models.BooleanField(default=False)  # Для кухни / Напольная плитка
    collection_application_apron = models.BooleanField(default=False)  # Для кухни / Фартук
    collection_application_outdoor = models.BooleanField(default=False)  # Для уличного применения
    collection_application_residential = models.BooleanField(default=False)  # Жилой интерьер
    collection_application_projects = models.BooleanField(default=False)  # Общественные интерьеры / Проекты



    def __str__(self):
        return "%s" % self.name_collection

    class Meta:
        verbose_name = 'Collection_Application_Search (Применение)'
        verbose_name_plural = 'Collection_Application_Search (Применения)'


class Collection_Type_Material_For_Search(models.Model):
    name_collection_type_material = models.ForeignKey(Collection, blank=True, null=True, default=None)
    collection_type_material_is_active = models.BooleanField(default=True)
    collection_type_material_grout = models.BooleanField(default=False)  # Затирка / Клей / Строительная химия
    collection_type_material_ceramic = models.BooleanField(default=False)  # Керамическая плитка
    collection_type_material_porcelain = models.BooleanField(default=False)  # Керамогранит
    collection_type_material_clinker = models.BooleanField(default=False)  # Клинкерная плитка
    collection_type_material_natural = models.BooleanField(default=False)  # Натуральный камень
    collection_type_material_leveling = models.BooleanField(default=False)  # Система выравнивания плитки
    collection_type_material_glass = models.BooleanField(default=False)  # Стеклянная мозаика
    collection_type_material_steps = models.BooleanField(default=False)  # Ступени

    def __str__(self):
        return "%s" % self.name_collection_type_material

    class Meta:
        verbose_name = 'Collection_Type_Material_Search (Тип материала)'
        verbose_name_plural = 'Collection_Type_Material_Search (Типы материалов)'


class Collection_Texturer_For_Search(models.Model):
    name_texturer_collection = models.ForeignKey(Collection, blank=True, null=True, default=None)
    collection_texturer_is_active = models.BooleanField(default=True)
    collection_texturer_3d = models.BooleanField(default=False)  # 3D / Трехмерная
    collection_texturer_art = models.BooleanField(default=False)  # Арт
    collection_texturer_concrete = models.BooleanField(default=False)  # Бетон / Цемент / Штукатурка
    collection_texturer_geometrical = models.BooleanField(default=False)  # Геометрический рисунок
    collection_texturer_damaskato = models.BooleanField(default=False)  # Дамаскато / Вензеля
    collection_texturer_wood = models.BooleanField(default=False)  # Дерево / Керамический паркет
    collection_texturer_imitationbrick = models.BooleanField(default=False)  # Имитация кирпичной кладки
    collection_texturer_imitationskin = models.BooleanField(default=False)  # Имитация кожи
    collection_texturer_rock = models.BooleanField(default=False)  # Камень
    collection_texturer_cotto = models.BooleanField(default=False)  # Котто /  имитация
    collection_texturer_crackle = models.BooleanField(default=False)  # Кракле
    collection_texturer_metal = models.BooleanField(default=False)  # Металл
    collection_texturer_monocolor = models.BooleanField(default=False)  # Моноколор
    collection_texturer_marble = models.BooleanField(default=False)  # Мрамор
    collection_texturer_onyx = models.BooleanField(default=False)  # Оникс
    collection_texturer_patchwork = models.BooleanField(default=False)  # Патчворк
    collection_texturer_cloth = models.BooleanField(default=False)  # Ткань
    collection_texturer_travertine = models.BooleanField(default=False)  # Травертин
    collection_texturer_flowers = models.BooleanField(default=False)  # Цветы / Растения
    collection_texturer_ethnic = models.BooleanField(default=False)  # Этнический рисунок

    def __str__(self):
        return "%s" % self.name_texturer_collection

    class Meta:
        verbose_name = 'Collection_Texturer_For_Search (Текстура)'
        verbose_name_plural = 'Collection_Texturer_For_Search (Текстуры)'


class Collection_Facturer_For_Search(models.Model):
    name_facturer_collection = models.ForeignKey(Collection, blank=True, null=True, default=None)
    collection_facturer_is_active = models.BooleanField(default=True)
    collection_stile_glossy = models.BooleanField(default=False)  # Глянцевая / Настенная
    collection_stile_matte = models.BooleanField(default=False)  # Матовая
    collection_stile_polished = models.BooleanField(default=False)  # Полированная
    collection_stile_polopolarized = models.BooleanField(default=False)  # Полуполированная / Лапатированная
    collection_stile_satin = models.BooleanField(default=False)  # Сатинированная
    collection_stile_aged = models.BooleanField(default=False)  # Состаренная / Рустичная
    collection_stile_structured = models.BooleanField(default=False)  # Структурированная / Рельефная


    def __str__(self):
        return "%s" % self.name_facturer_collection

    class Meta:
        verbose_name = 'Collection_Facturer_For_Search (Фактура)'
        verbose_name_plural = 'Collection_Facturer_For_Search (Фактуры)'


class Collection_Style_For_Search(models.Model):
    name_style_collection = models.ForeignKey(Collection, blank=True, null=True, default=None)
    collection_stile_is_active = models.BooleanField(default=True)
    collection_stile_vintage = models.BooleanField(default=False)  # винтаж
    collection_stile_classic = models.BooleanField(default=False)  # классика
    collection_stile_modern = models.BooleanField(default=False)  # современный

    def __str__(self):
        return "%s" % self.name_style_collection

    class Meta:
        verbose_name = 'Collection_Style_For_Search (Стиль)'
        verbose_name_plural = 'Collection_Style_For_Search (Стили)'


class Collection_Floor_For_Search(models.Model):
    name_floor_collection = models.ForeignKey(Collection, blank=True, null=True, default=None)
    collection_floor_is_active = models.BooleanField(default=True)
    collection_floor_floor = models.BooleanField(default=False)  # для пола
    collection_floor_wall = models.BooleanField(default=False)  # для стен
    collection_floor_universal = models.BooleanField(default=False)  # универсальная

    def __str__(self):
        return "%s" % self.name_floor_collection

    class Meta:
        verbose_name = 'Collection_Floor_For_Search (Настенная/Напольная)'
        verbose_name_plural = 'Collection_Floor_For_Search (Настенная/Напольная)'


class Collection_Colour_For_Search(models.Model):
    name_colour_collection = models.ForeignKey(Collection, blank=True, null=True, default=None)
    collection_colour_is_active = models.BooleanField(default=True)
    collection_colour_beige = models.BooleanField(default=False)  # бежевый
    collection_colour_white = models.BooleanField(default=False)  # белый
    collection_colour_burgundy = models.BooleanField(default=False)  # бордовый
    collection_colour_blue = models.BooleanField(default=False)  # голубой
    collection_colour_yellow = models.BooleanField(default=False)  # желтый
    collection_colour_green = models.BooleanField(default=False)  # зеленый
    collection_colour_gold = models.BooleanField(default=False)  # золотой
    collection_colour_brown = models.BooleanField(default=False)  # коричневый
    collection_colour_red = models.BooleanField(default=False)  # красный
    collection_colour_multicolor = models.BooleanField(default=False)  # мультиколор
    collection_colour_orange = models.BooleanField(default=False)  # оранжевый
    collection_colour_pink = models.BooleanField(default=False)  # розовый
    collection_colour_silver_platinum = models.BooleanField(default=False)  # серебряный/платина
    collection_colour_silver_grey = models.BooleanField(default=False)  # серый
    collection_colour_silver_darkblue = models.BooleanField(default=False)  # синий
    collection_colour_silver_lilac = models.BooleanField(default=False)  # сиреневый
    collection_colour_silver_black = models.BooleanField(default=False)  # черный

    def __str__(self):
        return "%s" % self.name_colour_collection

    class Meta:
        verbose_name = 'Collection_Colour_For_Search (Цвет)'
        verbose_name_plural = 'Collection_Colour_For_Search (Цвета)'


class Size(models.Model):
    name_size = models.CharField(max_length=25, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.name_size

    class Meta:
        verbose_name = 'Size (Размер)'
        verbose_name_plural = 'Sizes (Размеры)'


class Product_Type(models.Model):
    name_product_type = models.CharField(max_length=128, blank=True, null=True, default=None)
    name_product_type_ukr = models.CharField(max_length=128, blank=True, null=True, default=None)
    yacor = models.CharField(max_length=128, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.name_product_type

    class Meta:
        verbose_name = 'Product_Type (Тип продукта)'
        verbose_name_plural = 'Product_Type (Типы продуктов)'


class Product(models.Model):
    name_product = models.CharField(max_length=64, blank=True, null=True, default=None)
    # id_for_open_box = models.CharField(max_length=30, null=True, default=None)
    # for_open_box = models.CharField(max_length=30, null=True, default=None)

    collection_product = models.ForeignKey(Collection, blank=True, null=True, default=None)
    size_product = models.ForeignKey(Size, blank=True, null=True, default=None)
    vendor_code_product = models.CharField(max_length=20, blank=True, null=True, default=None)
    product_type_product = models.ForeignKey(Product_Type, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    data_target = models.CharField(max_length=20, blank=True, null=True, default=None)

    title = models.CharField(max_length=320, blank=True, null=True, default=None)
    title_ukr = models.CharField(max_length=320, blank=True, null=True, default=None)
    keyword = models.CharField(max_length=512, blank=True, null=True, default=None)
    keyword_ukr = models.CharField(max_length=512, blank=True, null=True, default=None)
    description = models.CharField(max_length=512, blank=True, null=True, default=None)
    description_ukr = models.CharField(max_length=512, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.name_product

    class Meta:
        verbose_name = 'Product (Продукт)'
        verbose_name_plural = 'Products (Продукты)'


class Product_Image(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='products_images/')
    image_mini = models.ImageField(upload_to='products_images_mini/', null=True, default=None)
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Product_Image (Изображение продукта)'
        verbose_name_plural = 'Product_Images (Изображения продуктов)'
