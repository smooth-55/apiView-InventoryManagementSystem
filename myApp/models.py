from django.db import models


# Create your models here.


class CommonAttributes(models.Model):
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(CommonAttributes):
    BRAND_CHOICES = [
        ("ZOD", "Zodiac"),
        ("PAN", "Park Avenue"),
        ("NKE", "Nike"),
        ("ADS", "Adidas"),
        ("SPR", "Spykar"),
        ("GSR", "Gstar"),
    ]

    PRODUCT_CATEGORY_CHOICES = [
        ("SE", "Shoes"),
        ("ST", "Shirt"),
        ("PT", "Pant"),
    ]

    image = models.ImageField(upload_to="dynamic_images")
    label = models.CharField(max_length=2, choices=PRODUCT_CATEGORY_CHOICES)
    price = models.FloatField()
    brand = models.CharField(max_length=3, choices=BRAND_CHOICES)
    description = models.TextField()

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        db_table = "product"
        ordering = ["-created_on"]

    def __str__(self):
        return self.label + "-" + self.brand


class Sku(CommonAttributes):
    COLOR_CHOICES = [
        ("RD", "Red"),
        ("WE", "White"),
        ("GY", "Gray"),
        ("YW", "Yellow"),
        ("BK", "Black"),
    ]

    SIZE_CHOICES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
        ("XL", "Extra_Large"),
    ]

    GENDER_CHOICES = [
        ("M", "Mens"),
        ("F", "Womens"),
    ]

    sku_code = models.CharField(max_length=250, null=True, blank=True, unique=True)
    color = models.CharField(max_length=2, choices=COLOR_CHOICES)
    size = models.CharField(max_length=2, choices=SIZE_CHOICES)
    gender_category = models.CharField(max_length=1, choices=GENDER_CHOICES)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sku")

    class Meta:
        verbose_name = "Sku"
        verbose_name_plural = "Skus"
        db_table = "sku"
        ordering = ["-id"]

    def save(self, *args, **kwargs):
        self.sku_code = (
            self.gender_category
            + "-"
            + self.product.label
            + "-"
            + self.product.brand
            + "-"
            + self.color
            + "-"
            + self.size
        )

        if Sku.objects.filter(sku_code=self.sku_code).exists():
            return print("SKU already exists")

        return super(Sku, self).save(*args, **kwargs)

    def __str__(self):
        return self.sku_code


class Batch(CommonAttributes):
    sku = models.ForeignKey(Sku, on_delete=models.CASCADE, related_name="sku")

    class Meta:
        verbose_name = "Batch"
        verbose_name_plural = "Batches"
        db_table = "batch"

    def __str__(self):
        return str(self.created_on)


class Inventory(CommonAttributes):
    remaining_stock = models.PositiveIntegerField(default=1)
    sku = models.OneToOneField(
        Sku, on_delete=models.CASCADE, related_name="inventory_sku"
    )

    class Meta:
        verbose_name = "Inventory"
        verbose_name_plural = "Inventories"
        db_table = "inventory"
        ordering = ["-created_on"]

    def __str__(self):
        return str(self.sku.sku_code) + " : " + str(self.remaining_stock)
