from django.shortcuts import render
from orders.models import Order, ProductInOrder, ProductInBasket, Call_Me
from orders.forms import CheckoutContactForm
from products.models import Product_Image
from shadow.models import Log_In_Site, Eye

from main.models import Footer

from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import redirect, reverse

import smtplib
from smtplib import SMTPAuthenticationError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def checkout(request):
    session_key = request.session.session_key
# A record of data about the visit of web-site is beginning
    session_key = request.session.session_key
    # Checking for being of record in the base of the sessions key is beginning
    if Log_In_Site.objects.filter(session_key=session_key).count():
        # Record in the base of mark in track is beginning
        find_max = Eye.objects.filter(session_key=session_key)
        max_id_in = 0
        for find_single in find_max:
            if max_id_in < int(find_single.id):
                max_id_in = int(find_single.id)
        page_max_many = Eye.objects.filter(session_key=session_key, page="Корзина", id=max_id_in)
        if page_max_many.count() != 0:
            for page_max in page_max_many:
                pass
            if page_max.page == "Корзина":
                Eye.objects.get(session_key=session_key, page="Корзина", id=max_id_in).delete()
        Eye.objects.create(session_key=session_key,
                           page="Корзина",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key))
        # Record in the base of mark in track is an end
    else:
        # Record in the base of being of FTU on a web-site and creation of mark of his location - beginning
        Log_In_Site.objects.create(session_key=session_key, leng="rus")
        Eye.objects.create(session_key=session_key,
                           page="Корзина",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key, leng="rus"))
        # Record in the base of being of FTU on a web-site and creation of mark of his location - end
    # Checking for being of record in the base of the sessions key is an end
    # A record of data about the visit of web-site is an end

    # The signal processing on switching of language is beginning
    data = request.POST
    if data.get("submit") == "ukr":
        Log_In_Site.objects.filter(session_key=session_key).update(leng="ukr")
        return redirect('checkout_ukr')
    # The signal processing on switching of language is an end
    all_info_footer = Footer.objects.filter(is_active=True)
# Preparation of list for opening of windows is beginning
    products_in_bascet = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    for prod in products_in_bascet:
        pass
    dict_vendor_code_product = dict()
    list_vendor_code_product = list()
    for product_in in products_in_bascet:
        only_product = product_in.product
        img_for_web = Product_Image.objects.get(product=only_product)
        id_in = only_product.id
        vendor_code_product = only_product.vendor_code_product
        vendor_code_product_re = "#" + str(vendor_code_product)
        dict_vendor_code_product = {"only_product": only_product,
                                    "img_for_web": img_for_web,
                                    "vendor_code_product": vendor_code_product,
                                    "vendor_code_product_re": vendor_code_product_re}
        list_vendor_code_product.append(dict_vendor_code_product)
# Preparation of list for opening of windows is an end
    imgs_products_in_bascet = Product_Image.objects.filter(is_active=True, is_main=True)
    form = CheckoutContactForm(request.POST or None)
    if request.POST:
        if form.is_valid:
            data = request.POST
            list_result = []
            for name, value in data.items():
                if name.startswith("product_in_bascet_"):
                    products_in_bascet_id = name.split("product_in_bascet_")[1]
                    product_in_basket = ProductInBasket.objects.get(id=products_in_bascet_id, is_active=True)
                    product_in_basket.nmb = int(value)
                    product_in_basket.save(force_update=True)
            for name_d, value_d in data.items():
                if name_d.startswith("product_is_delet_"):
                    products_in_bascet_no_active = name_d.split("product_is_delet_")[1]
                    product_in_basket = ProductInBasket.objects.get(id=products_in_bascet_no_active, is_active=True)
                    product_in_basket.nmb = False
                    product_in_basket.delete()
            products_in_bascet = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    products_in_bascet = ProductInBasket.objects.filter(session_key=session_key, is_active=True)

    return render(request, 'orders/checkout.html', locals())


def checkout_ukr(request):
    # A record of data about the visit of web-site is beginning
    session_key = request.session.session_key
    # Checking for being of record in the base of the sessions key is beginning
    if Log_In_Site.objects.filter(session_key=session_key).count():
        # Record in the base of mark in track is beginning
        find_max = Eye.objects.filter(session_key=session_key)
        max_id_in = 0
        for find_single in find_max:
            if max_id_in < int(find_single.id):
                max_id_in = int(find_single.id)
        page_max_many = Eye.objects.filter(session_key=session_key, page="Корзина", id=max_id_in)
        if page_max_many.count() != 0:
            for page_max in page_max_many:
                pass
            if page_max.page == "Корзина":
                Eye.objects.get(session_key=session_key, page="Корзина", id=max_id_in).delete()
        Eye.objects.create(session_key=session_key,
                           page="Корзина",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key))
        # Record in the base of mark in track is an end
    else:
        # Record in the base of being of FTU on a web-site and creation of mark of his location - beginning
        Log_In_Site.objects.create(session_key=session_key, leng="rus")
        Eye.objects.create(session_key=session_key,
                           page="Корзина",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key, leng="rus"))
        # Record in the base of being of FTU on a web-site and creation of mark of his location - end
    # Checking for being of record in the base of the sessions key is an end
    # A record of data about the visit of web-site is an end
    # The signal processing on switching of language is beginning
    data = request.POST
    if data.get("submit") == "rus":
        Log_In_Site.objects.filter(session_key=session_key).update(leng="rus")
        return redirect('checkout')
    # The signal processing on switching of language is an end
    products_in_bascet = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    imgs_products_in_bascet = Product_Image.objects.filter(is_active=True, is_main=True)
    form = CheckoutContactForm(request.POST or None)
    if request.POST:
        if form.is_valid:
            data = request.POST
            list_result = []
            for name, value in data.items():
                if name.startswith("product_in_bascet_"):
                    products_in_bascet_id = name.split("product_in_bascet_")[1]
                    product_in_basket = ProductInBasket.objects.get(id=products_in_bascet_id, is_active=True)
                    product_in_basket.nmb = int(value)
                    product_in_basket.save(force_update=True)
            for name_d, value_d in data.items():
                if name_d.startswith("product_is_delet_"):
                    products_in_bascet_no_active = name_d.split("product_is_delet_")[1]
                    product_in_basket = ProductInBasket.objects.get(id=products_in_bascet_no_active, is_active=True)
                    product_in_basket.nmb = False
                    product_in_basket.delete()

    return render(request, 'orders/checkout_ukr.html', locals())


def checkout_order(request):
    all_info_footer = Footer.objects.filter(is_active=True)
    # A record of data about the visit of web-site is beginning
    session_key = request.session.session_key
    # Checking for being of record in the base of the sessions key is beginning
    if Log_In_Site.objects.filter(session_key=session_key).count():
        # Record in the base of mark in track is beginning
        find_max = Eye.objects.filter(session_key=session_key)
        max_id_in = 0
        for find_single in find_max:
            if max_id_in < int(find_single.id):
                max_id_in = int(find_single.id)
        page_max_many = Eye.objects.filter(session_key=session_key, page="Оформление ордера", id=max_id_in)
        if page_max_many.count() != 0:
            for page_max in page_max_many:
                pass
            if page_max.page == "Оформление ордера":
                Eye.objects.get(session_key=session_key, page="Оформление ордера", id=max_id_in).delete()

        Eye.objects.create(session_key=session_key,
                           page="Оформление ордера",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key))
        # Record in the base of mark in track is an end
    else:
        # Record in the base of being of FTU on a web-site and creation of mark of his location - beginning
        Log_In_Site.objects.create(session_key=session_key, leng="rus")
        Eye.objects.create(session_key=session_key,
                           page="Оформление ордера",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key, leng="rus"))
        # Record in the base of being of FTU on a web-site and creation of mark of his location - end
    # Checking for being of record in the base of the sessions key is an end
    # A record of data about the visit of web-site is an end
    # The signal processing on switching of language is beginning
    data = request.POST
    if data.get("submit") == "ukr":
        Log_In_Site.objects.filter(session_key=session_key).update(leng="ukr")
        return redirect('checkout_order_ukr')
    # The signal processing on switching of language is end
    products_in_bascet = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    imgs_products_in_bascet = Product_Image.objects.filter(is_active=True, is_main=True)
    form = CheckoutContactForm(request.POST or None)
    if request.POST:
        if form.is_valid:
            data = request.POST
            name = data.get("name")
            email = data.get("email")
            phone = data.get("phone")
            adress = data.get("adress")
            comment = data.get("comment")
            order = Order.objects.create(customer_name=name, customer_email=email, customer_phone=phone,
                                         customer_address=adress, comments=comment, status_id=1, session_key=session_key)

            text_for_send_boss = "Номер ордера заказа: " + str(order.id) + " ."
            text_for_send_boss = text_for_send_boss + "Перечень товаров, заказанных в нашем магазине."
            for product_in_bascet in products_in_bascet:
                text_for_send_boss = text_for_send_boss + str(product_in_bascet.product.name_product) + " - " + str(product_in_bascet.nmb) + ". "

            text_for_send_boss = text_for_send_boss + "ФИО покупателя - " + str(name) + ". "
            text_for_send_boss = text_for_send_boss + "Email покупателя - " + str(email) + ". "
            text_for_send_boss = text_for_send_boss + "Телефон покупателя - " + str(phone) + ". "
            text_for_send_boss = text_for_send_boss + "Адрес покупателя - " + str(adress) + ". "
            text_for_send_boss = text_for_send_boss + "Комментарий покупателя - " + str(comment) + ". "
            print(text_for_send_boss)


            text_for_send_purches = "Номер ордера заказа: " + str(order.id) + ". "
            text_for_send_purches = text_for_send_purches + "Перечень товаров, заказанных в нашем магазине."
            for product_in_bascet in products_in_bascet:
                text_for_send_purches = text_for_send_purches + str(product_in_bascet.product.name_product) + " - " + str(
                    product_in_bascet.nmb) + ". "

            text_for_send_purches = text_for_send_purches + "ФИО - " + str(name) + ". "
            text_for_send_purches = text_for_send_purches + "Email - " + str(email) + ". "
            text_for_send_purches = text_for_send_purches + "Телефон - " + str(phone) + ". "
            text_for_send_purches = text_for_send_purches + "Адрес - " + str(adress) + ". "
            text_for_send_purches = text_for_send_purches + "Комментарий - " + str(comment) + ". "
            text_for_send_purches = text_for_send_purches + "Наш менеджер в ближайшее время свяжется для дальнейшего согласования по приобретению товара. "
            text_for_send_purches = text_for_send_purches + "Благодарим Вас за выбор нашего Интернет Магазина. "
            text_for_send_purches = text_for_send_purches + "С уважением, Администрация интернет-магазина CERAMA CASA."
            print(text_for_send_purches)

            email_us = "shop.cerama.casa.orders@gmail.com"
            password = '12345678qwe'
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email_us, password)
            msg = MIMEMultipart()
            msg['From'] = email_us
            msg['To'] = "bestmen911@gmail.com"
            msg['Subject'] = "New order"
            text = "Регистрация нового заказа (CERAMO CASA)"
            text = text_for_send_boss
            msg.attach(MIMEText(text))
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            server.quit()

            email_us = "shop.cerama.casa.orders@gmail.com"
            password = '12345678qwe'
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email_us, password)
            msg = MIMEMultipart()
            msg['From'] = email_us
            msg['To'] = email
            msg['Subject'] = "Вами создан заказ в нашем магазине CERAMO CASA"
            text = text_for_send_purches
            msg.attach(MIMEText(text))
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            server.quit()

            list_result = []
            for product_in_bascet in products_in_bascet:
                ProductInOrder.objects.create(product=product_in_bascet.product, nmb=product_in_bascet.nmb, order=order,
                                              session_key=session_key)
            for product_in_bascet in products_in_bascet:
                product_in_bascet.delete()

        return redirect(checkout_end)

    return render(request, 'orders/checkout_order.html', locals())


def checkout_order_ukr(request):
    # A record of data about the visit of web-site is beginning
    session_key = request.session.session_key
    # Checking for being of record in the base of the sessions key is beginning
    if Log_In_Site.objects.filter(session_key=session_key).count():
        # Record in the base of mark in track is beginning
        find_max = Eye.objects.filter(session_key=session_key)
        max_id_in = 0
        for find_single in find_max:
            if max_id_in < int(find_single.id):
                max_id_in = int(find_single.id)
        page_max_many = Eye.objects.filter(session_key=session_key, page="Оформление ордера", id=max_id_in)
        if page_max_many.count() != 0:
            for page_max in page_max_many:
                pass
            if page_max.page == "Оформление ордера":
                Eye.objects.get(session_key=session_key, page="Оформление ордера", id=max_id_in).delete()

        Eye.objects.create(session_key=session_key,
                           page="Оформление ордера",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key))
        # Record in the base of mark in track is an end
    else:
        # Record in the base of being of FTU on a web-site and creation of mark of his location - beginning
        Log_In_Site.objects.create(session_key=session_key, leng="rus")
        Eye.objects.create(session_key=session_key,
                           page="Оформление ордера",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key, leng="rus"))
        # Record in the base of being of FTU on a web-site and creation of mark of his location - end
    # Checking for being of record in the base of the sessions key is an end
    # A record of data about the visit of web-site is an end
    # The signal processing on switching of language is beginning
    data = request.POST
    if data.get("submit") == "rus":
        Log_In_Site.objects.filter(session_key=session_key).update(leng="rus")
        return redirect('checkout_order')
    # The signal processing on switching of language is end
    products_in_bascet = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    imgs_products_in_bascet = Product_Image.objects.filter(is_active=True, is_main=True)
    form = CheckoutContactForm(request.POST or None)
    if request.POST:
        if form.is_valid:
            data = request.POST
            name = data.get("name")
            email = data.get("email")
            phone = data.get("phone")
            adress = data.get("adress")
            comment = data.get("comment")
            order = Order.objects.create(customer_name=name, customer_email=email, customer_phone=phone,
                                         customer_address=adress, comments=comment, status_id=1, session_key=session_key)
            list_result = []
            for product_in_bascet in products_in_bascet:
                ProductInOrder.objects.create(product=product_in_bascet.product, nmb=product_in_bascet.nmb, order=order,
                                              session_key=session_key)
            for product_in_bascet in products_in_bascet:
                product_in_bascet.delete()
        return redirect(checkout_end)

    return render(request, 'orders/checkout_order_ukr.html', locals())


def checkout_end(request):
    all_info_footer = Footer.objects.filter(is_active=True)
    # A record of data about the visit of web-site is beginning
    session_key = request.session.session_key
    # Checking for being of record in the base of the sessions key is beginning
    if Log_In_Site.objects.filter(session_key=session_key).count():
        # Record in the base of mark in track is beginning
        find_max = Eye.objects.filter(session_key=session_key)
        max_id_in = 0
        for find_single in find_max:
            if max_id_in < int(find_single.id):
                max_id_in = int(find_single.id)
        page_max_many = Eye.objects.filter(session_key=session_key, page="Окончание оформления ордера", id=max_id_in)
        if page_max_many.count() != 0:
            for page_max in page_max_many:
                pass
            if page_max.page == "Окончание оформления ордера":
                Eye.objects.get(session_key=session_key, page="Окончание оформления ордера", id=max_id_in).delete()
        Eye.objects.create(session_key=session_key,
                           page="Окончание оформления ордера",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key))
        # Record in the base of mark in track is an end
    else:
        # Record in the base of being of FTU on a web-site and creation of mark of his location - beginning
        Log_In_Site.objects.create(session_key=session_key, leng="rus")
        Eye.objects.create(session_key=session_key,
                           page="Окончание оформления ордера",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key, leng="rus"))
        # Record in the base of being of FTU on a web-site and creation of mark of his location - end
    # Checking for being of record in the base of the sessions key is an end
    # A record of data about the visit of web-site is an end
    # The signal processing on switching of language is beginning
    data = request.POST
    if data.get("submit") == "ukr":
        Log_In_Site.objects.filter(session_key=session_key).update(leng="ukr")
        return redirect('checkout_end_ukr')
    # The signal processing on switching of language is end
    products_in_orders = ProductInOrder.objects.filter(session_key=session_key)
    max_num_order = 0
    for products_in_order in products_in_orders:
        reserv = products_in_order.order.id
        if int(reserv) > int(max_num_order):
            max_num_order = int(reserv)
    products_in_orders = ProductInOrder.objects.filter(session_key=session_key, order__id=max_num_order)

    return render(request, 'orders/checkout_end.html', locals())


def checkout_end_ukr(request):
    # A record of data about the visit of web-site is beginning
    session_key = request.session.session_key
    # Checking for being of record in the base of the sessions key is beginning
    if Log_In_Site.objects.filter(session_key=session_key).count():
        # Record in the base of mark in track is beginning
        find_max = Eye.objects.filter(session_key=session_key)
        max_id_in = 0
        for find_single in find_max:
            if max_id_in < int(find_single.id):
                max_id_in = int(find_single.id)
        page_max_many = Eye.objects.filter(session_key=session_key, page="Окончание оформления ордера", id=max_id_in)
        if page_max_many.count() != 0:
            for page_max in page_max_many:
                pass
            if page_max.page == "Окончание оформления ордера":
                Eye.objects.get(session_key=session_key, page="Окончание оформления ордера", id=max_id_in).delete()

        Eye.objects.create(session_key=session_key,
                           page="Окончание оформления ордера",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key))
        # Record in the base of mark in track is an end
    else:
        # Record in the base of being of FTU on a web-site and creation of mark of his location - beginning
        Log_In_Site.objects.create(session_key=session_key, leng="rus")
        Eye.objects.create(session_key=session_key,
                           page="Окончание оформления ордера",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key, leng="rus"))
        # Record in the base of being of FTU on a web-site and creation of mark of his location - end
    # Checking for being of record in the base of the sessions key is an end
    # A record of data about the visit of web-site is an end
    # The signal processing on switching of language is beginning
    data = request.POST
    if data.get("submit") == "rus":
        Log_In_Site.objects.filter(session_key=session_key).update(leng="rus")
        return redirect('checkout_end')
    # The signal processing on switching of language is end
    products_in_orders = ProductInOrder.objects.filter(session_key=session_key)

    return render(request, 'orders/checkout_end_ukr.html', locals())


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    product_id = data.get('product_id')
    nmb = data.get('nmb')
    csrfmiddlewaretoken = data.get('csrfmiddlewaretoken')
    if product_id != None and nmb != None and csrfmiddlewaretoken != None:
        new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id,
                                                                     defaults={"nmb": nmb})
        if not created:
            new_product.nmb += int(nmb)
            new_product.save(force_update=True)

        product_total_nmb = ProductInBasket.objects.filter(session_key=session_key, is_active=True).count()
        return_dict['product_total_nmb'] = product_total_nmb
    else:
        pass

    return JsonResponse(return_dict)


def phone_adding(request):
    data = request.GET
    send_name = data.get('name')
    send_phone = data.get('phone')
    Call_Me.objects.create(call_me_name=send_name, call_me_phone=send_phone)

    email_us = "shop.phone.cerama.casa@gmail.com"
    password = '12345678qwe'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_us, password)
    msg = MIMEMultipart()
    msg['From'] = email_us
    msg['To'] = "bestmen911@gmail.com"
    msg['Subject'] = "Сообщение - перезвони мне."
    text = "ФИО - " + str(send_name) + ". " + "Контактный телефон - " + str(send_phone) + ". "
    msg.attach(MIMEText(text))
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

    return redirect(reverse('main'))
