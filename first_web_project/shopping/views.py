from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import *
from django.urls import reverse
from .forms import *


# Create your views here.

def go_home(request):
    data = Wheel.objects.all()
    nav_list = Nav.objects.all()
    must_buy_list = MustBuy.objects.all()
    shop = Shop.objects.all()
    main_list = MainShow.objects.all()
    shop1 = shop[0]
    shop2 = shop[1:3]
    shop3 = shop[3:7]
    shop4 = shop[7:11]
    title = '主页'
    return render(request, 'shop/home.html', locals())


def market(request, categoryid, childcid, sortid):
    # 侧边栏和分类栏数据
    foodtypes = FoodTypes.objects.all()
    title = "闪送超市"
    # http://127.0.0.1:8000/market/104749/0/0/
    # http://127.0.0.1:8000/market/categoryid/childcid/sortid/
    # 判断 是否是全部类型
    if childcid == '0':  # 是全部类型
        product_list = Goods.objects.filter(categoryid=categoryid)
    else:  # 因为点击侧边栏时  传入的参数  侧边栏的参数值  和 对应的全部类型的参数  如何排序的参数 只是0
        product_list = Goods.objects.filter(categoryid=categoryid, childcid=childcid)
    # 加入全部类型下拉 的选项
    group = foodtypes.get(typeid=categoryid)
    child_name = group.childtypenames
    array = child_name.split('#')
    child_list = []
    for str1 in array:
        array2 = str1.split(':')
        obj = {'childName': array2[0], 'childId': array2[1]}
        child_list.append(obj)
    # 判断 排序的参数
    if sortid == "1":
        product_list = product_list.order_by('productnum')
    elif sortid == '2':
        product_list = product_list.order_by('price')
    elif sortid == '3':
        product_list = product_list.order_by('-price')
    user_name = request.session.get('username')
    if user_name:
        for good in product_list:
            user_id = UserModel.objects.get(username=user_name).id
            carts = CartGoods.objects.filter(productid=good.productid, userid=user_id).first()
            if carts:
                good.cart_num = carts.productnum
            else:
                good.cart_num = 0
    return render(request, 'shop/market.html', locals())


def register(request):
    if request.method == 'POST':
        username = request.POST['userAccount']
        password = request.POST['userPass']
        telephone = request.POST['userPhone']
        address = request.POST['userAdderss']
        img = request.FILES.get('userImg')
        UserModel.objects.create(username=username, password=password, telephone=telephone, address=address, img=img)
        return redirect(reverse('shop:login'))
    else:
        title = "注册"
        return render(request, 'shop/register.html', locals())


def login(request):
    if request.method == 'GET':
        form = LoginForm()
        title = "登录"
        return render(request, 'shop/login.html', locals())
    else:
        reg_form = LoginForm(request.POST)
        if reg_form.is_valid():
            name = reg_form.cleaned_data['username']
            data = UserModel.objects.get(username=name)
            password = reg_form.cleaned_data['password']
            if data and data.password == password:
                request.session['username'] = name
                request.session['url'] = '/static/mdeia/' + data.img.url
                return redirect(reverse('shop:mine'))
            else:
                script = 'alert'
                wrong = '账号或密码错误'
                form = LoginForm()
                return render(request, 'shop/login.html', locals())


def mine(request):
    name = request.session.get('username')
    if name:
        username = name
        url = request.session.get('url')
        title = name
    else:
        username = '登录'
        title = "登录"
    return render(request, 'shop/mine.html', locals())


def logout(request):
    del request.session['username']
    del request.session['url']
    return redirect(reverse('shop:mine'))


def username(request):
    name = request.GET.get('arg')
    if not UserModel.objects.filter(username=name):
        return JsonResponse({'error': '该用户名可用', 'value': 1})
    else:
        return JsonResponse({'error': '该用户名不可用', 'value': 0})


def cart(request):
    if request.session.get('username'):
        user = UserModel.objects.get(username=request.session.get('username'))
        cartslist = CartGoods.objects.all()
        for i in cartslist:
            if not i.ischose:
                true_Flag = False
                break
        else:
            true_Flag = True
        return render(request, 'shop/cart.html', locals())
    else:
        return redirect(reverse('shop:login'))


def sub(request):
    user_name = request.session.get('username')
    product_id = request.GET.get('product_id')
    # user_id = UserModel.objects.get(username=user_name).id
    if user_name:
        if not CartGoods.objects.filter(productid=product_id):
            return JsonResponse({'error': '该商品购物车没有'})
        else:
            cart1 = CartGoods.objects.filter(productid=product_id).first()
            if int(cart1.productnum) == 1:
                cart1.delete()
                return JsonResponse({'value': '0'})
            else:
                cart1.productnum = str(int(cart1.productnum) - 1)
                cart1.save()
                return JsonResponse({'value': cart1.productnum})
    else:
        return JsonResponse({'error': '未登录'})


def add(request):
    product_id = request.GET.get('product_id')
    user_name = request.session.get('username')
    if user_name:
        if not CartGoods.objects.filter(productid=product_id):
            user_id = UserModel.objects.get(username=user_name).id
            goods = Goods.objects.filter(productid=product_id).first()
            CartGoods.objects.create(productid=product_id, productimg=goods.productimg, productprice=goods.price,
                                     productnum='1', userid=user_id)
            return JsonResponse({'value': '1'})
        else:
            cart1 = CartGoods.objects.filter(productid=product_id).first()
            cart1.productnum = str(int(cart1.productnum) + 1)
            cart1.save()
            return JsonResponse({'value': cart1.productnum})
    else:
        return JsonResponse({'error': '未登录'})


def cart_add(request):
    pro_id = request.GET.get('product_id')
    user_name = request.session.get('username')
    if user_name:
        cart1 = CartGoods.objects.filter(productid=pro_id).first()
        cart1.productnum = str(int(cart1.productnum) + 1)
        cart1.save()
        return JsonResponse({'value': cart1.productnum})
    else:
        return JsonResponse({'error': '未登录'})


def cart_sub(request):
    pro_id = request.GET.get('product_id')
    user_name = request.session.get('username')
    if user_name:
        cart1 = CartGoods.objects.filter(productid=pro_id).first()
        if cart1.productnum == '1':
            cart1.delete()
            return JsonResponse({'value': '0'})
        else:
            cart1.productnum = str(int(cart1.productnum) - 1)
            cart1.save()
            return JsonResponse({'value': cart1.productnum})
    else:
        return JsonResponse({'error': '未登录'})


def click(request):
    pro_id = request.GET.get('product_id')
    cart1 = CartGoods.objects.filter(productid=pro_id).first()
    if cart1.ischose:
        cart1.ischose = False
        cart1.save()
        return JsonResponse({'state': 'False'})
    else:
        cart1.ischose = True
        cart1.save()
        return JsonResponse({'state': 'True'})


def all_click(request):
    state = request.GET.get('state')
    carts = CartGoods.objects.all()
    print(state)
    if state == 'False':
        for i in carts:
            i.ischose = True
            i.save()
        return JsonResponse({'state': 'True'})
    else:
        for i in carts:
            i.ischose = False
            i.save()
        return JsonResponse({'state': 'False'})


