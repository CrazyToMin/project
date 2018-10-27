from django.db import models


# Create your models here.

# 轮播图
class Wheel(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=10)

    class Meta:
        db_table = "wheel"


# 导航栏
class Nav(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=10)

    class Meta:
        db_table = "nav"


# 导航栏下的轮播
class MustBuy(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=10)

    class Meta:
        db_table = "mustbuy"


#
class Shop(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=10)

    class Meta:
        db_table = "shop"


class MainShow(models.Model):
    trackid = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    img = models.CharField(max_length=200)
    categoryid = models.CharField(max_length=10)
    brandname = models.CharField(max_length=20)

    img1 = models.CharField(max_length=200)
    childcid1 = models.CharField(max_length=10)
    productid1 = models.CharField(max_length=10)
    longname1 = models.CharField(max_length=50)
    price1 = models.CharField(max_length=10)
    marketprice1 = models.CharField(max_length=10)

    img2 = models.CharField(max_length=200)
    childcid2 = models.CharField(max_length=10)
    productid2 = models.CharField(max_length=10)
    longname2 = models.CharField(max_length=50)
    price2 = models.CharField(max_length=10)
    marketprice2 = models.CharField(max_length=10)

    img3 = models.CharField(max_length=200)
    childcid3 = models.CharField(max_length=10)
    productid3 = models.CharField(max_length=10)
    longname3 = models.CharField(max_length=50)
    price3 = models.CharField(max_length=10)
    marketprice3 = models.CharField(max_length=10)

    class Meta:
        db_table = "mainshow"


# 侧边栏
class FoodTypes(models.Model):
    typeid = models.CharField(max_length=10)
    typename = models.CharField(max_length=20)
    typesort = models.IntegerField(max_length=11)
    childtypenames = models.CharField(max_length=150)

    class Meta:
        db_table = "foodtypes"


# 商品
class Goods(models.Model):
    productid = models.CharField(max_length=10)  # 商品id
    productimg = models.CharField(max_length=150)  # 商品图片
    productname = models.CharField(max_length=50)  # 商品名称
    productlongname = models.CharField(max_length=100)  # 商品长名称
    isxf = models.NullBooleanField(default=False)  # 是否精选
    pmdesc = models.CharField(max_length=10)  # 是否买一赠一
    specifics = models.CharField(max_length=20)  # 规格
    price = models.FloatField(max_length=10)  # 价格
    marketprice = models.CharField(max_length=10)  # 超市价格
    categoryid = models.CharField(max_length=10)  # 组id
    childcid = models.CharField(max_length=10)  # 子类组id
    childcidname = models.CharField(max_length=10)  # 子类组名称
    dealerid = models.CharField(max_length=10)  # 详情页id
    storenums = models.IntegerField()  # 库存
    productnum = models.IntegerField()  # 销量

    class Meta:
        db_table = "goods"


class UserModel(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    img = models.ImageField(upload_to='icons')

    class Meta:
        db_table = "user"


class CartGoods(models.Model):
    productid = models.CharField(max_length=20)
    productimg = models.CharField(max_length=150)
    productprice = models.CharField(max_length=10)
    productnum = models.CharField(max_length=10)
    userid = models.CharField(max_length=20)
    ischose = models.BooleanField(default=False)

    class Meta:
        db_table = 'cart'


