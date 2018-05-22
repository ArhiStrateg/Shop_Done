from django.shortcuts import render, render_to_response
from main.models import Search_Low_Addition, For_Main, For_IMG_Main, Projects_Materials, Contscts, Search_For_Project, \
    Diler_Otdel, \
    Diler_Otdel_Сonttacts, Search_Diller_Otdel, Company, Footer, Search_Search, Search_Manafactory, \
    Search_Manafactory_Single, \
    Zakaz, User_Login
from products.models import Manufacturer, Collection_Image, Collection_Search_NHS, Collection_Application_For_Search, \
    Collection_Style_For_Search, \
    Manufacturer_Country, Collection_Type_Material_For_Search, Collection_Floor_For_Search, Availability, \
    Collection_Texturer_For_Search, \
    Size, Price_Group, Collection_Facturer_For_Search, Collection, Product_Image, Collection_Colour_For_Search, \
    Product_Type, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from main.forms import Login_Form
from django.core.urlresolvers import reverse
from shadow.models import Statistic_Find_Simple, Statistic_Find_Bloc, Eye, Log_In_Site

from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout

from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest


def robots(request):
    return render_to_response('robots.txt', content_type='text/plain')


def sitemap(request):
    return render_to_response('sitemap.html')
    # return render_to_response('sitemap.html', content_type='text/plain')


def zakaz(request):
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
        page_max_many = Eye.objects.filter(session_key=session_key, page="Заказ/Оплата/Доставка", id=max_id_in)
        if page_max_many.count() != 0:
            for page_max in page_max_many:
                pass
            if page_max.page == "Заказ/Оплата/Доставка":
                Eye.objects.get(session_key=session_key, page="Заказ/Оплата/Доставка", id=max_id_in).delete()

        Eye.objects.create(session_key=session_key,
                           page="Заказ/Оплата/Доставка",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key))
        # Record in the base of mark in track is an end
    else:
        # Record in the base of being of FTU on a web-site and creation of mark of his location - beginning
        Log_In_Site.objects.create(session_key=session_key, leng="rus")
        Eye.objects.create(session_key=session_key,
                           page="Заказ/Оплата/Доставка",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key, leng="rus"))
        # Record in the base of being of FTU on a web-site and creation of mark of his location - end
    # Checking for being of record in the base of the sessions key is an end
    # A record of data about the visit of web-site is an end

    # The signal processing on switching of language is beginning
    data = request.POST

    if data.get("submit") == "ukr":
        Log_In_Site.objects.filter(session_key=session_key).update(leng="ukr")
        return redirect('zakaz_ukr')
    # The signal processing on switching of language is an end

    all_info_footer = Footer.objects.filter(is_active=True)
    all_info_contacts = Contscts.objects.filter(is_active=True)
    all_info_zakaz = Zakaz.objects.filter(is_active=True)

    for zakaz_info in all_info_zakaz:
        pass

    return render(request, 'main/zakaz.html', locals())


def zakaz_ukr(request):
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
        page_max_many = Eye.objects.filter(session_key=session_key, page="Заказ/Оплата/Доставка", id=max_id_in)
        if page_max_many.count() != 0:
            for page_max in page_max_many:
                pass
            if page_max.page == "Заказ/Оплата/Доставка":
                Eye.objects.get(session_key=session_key, page="Заказ/Оплата/Доставка", id=max_id_in).delete()

        Eye.objects.create(session_key=session_key,
                           page="Заказ/Оплата/Доставка",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key))
        # Record in the base of mark in track is an end
    else:
        # Record in the base of being of FTU on a web-site and creation of mark of his location - beginning
        Log_In_Site.objects.create(session_key=session_key, leng="rus")
        Eye.objects.create(session_key=session_key,
                           page="Заказ/Оплата/Доставка",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key, leng="rus"))
        # Record in the base of being of FTU on a web-site and creation of mark of his location - end
    # Checking for being of record in the base of the sessions key is an end
    # A record of data about the visit of web-site is an end

    # The signal processing on switching of language is beginning
    data = request.POST
    if data.get("submit") == "rus":
        Log_In_Site.objects.filter(session_key=session_key).update(leng="rus")
        return redirect('zakaz')
    # The signal processing on switching of language is end

    all_info_footer = Footer.objects.filter(is_active=True)
    all_info_contacts = Contscts.objects.filter(is_active=True)
    all_info_zakaz = Zakaz.objects.filter(is_active=True)
    for zakaz_info in all_info_zakaz:
        pass

    return render(request, 'main/zakaz_ukr.html', locals())


def company(request):
    # A record of data about the visit of web-site is beginning
    session_key = request.session.session_key
    # Checking for being of record in the base of the sessions key is beginning
    if Log_In_Site.objects.filter(session_key=session_key).count():
        #  Record in the base of mark in track is beginning
        find_max = Eye.objects.filter(session_key=session_key)
        max_id_in = 0
        for find_single in find_max:
            if max_id_in < int(find_single.id):
                max_id_in = int(find_single.id)
        page_max_many = Eye.objects.filter(session_key=session_key, page="О компании", id=max_id_in)
        if page_max_many.count() != 0:
            for page_max in page_max_many:
                pass
            if page_max.page == "О компании":
                Eye.objects.get(session_key=session_key, page="О компании", id=max_id_in).delete()

        Eye.objects.create(session_key=session_key,
                           page="О компании",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key))
        # Record in the base of mark in track is an end
    else:
        # Record in the base of being of FTU on a web-site and creation of mark of his location - beginning
        Log_In_Site.objects.create(session_key=session_key, leng="rus")
        Eye.objects.create(session_key=session_key,
                           page="О компании",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key, leng="rus"))
        # Record in the base of being of FTU on a web-site and creation of mark of his location - end
    # Checking for being of record in the base of the sessions key is an end
    # A record of data about the visit of web-site is an end

    # The signal processing on switching of language is beginning
    data = request.POST
    if data.get("submit") == "ukr":
        Log_In_Site.objects.filter(session_key=session_key).update(leng="ukr")
        return redirect('company_ukr')
    # The signal processing on switching of language is end

    all_info_company = Company.objects.filter(is_active=True)
    all_info_contacts = Contscts.objects.filter(is_active=True)
    all_info_footer = Footer.objects.filter(is_active=True)

    for compan_info in all_info_company:
        pass

    return render(request, 'main/company.html', locals())


def company_ukr(request):
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
        page_max_many = Eye.objects.filter(session_key=session_key, page="О компании", id=max_id_in)
        if page_max_many.count() != 0:
            for page_max in page_max_many:
                pass
            if page_max.page == "О компании":
                Eye.objects.get(session_key=session_key, page="О компании", id=max_id_in).delete()

        Eye.objects.create(session_key=session_key,
                           page="О компании",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key))
        # Record in the base of mark in track is an end
    else:
        # Record in the base of being of FTU on a web-site and creation of mark of his location - beginning
        Log_In_Site.objects.create(session_key=session_key, leng="ukr")
        Eye.objects.create(session_key=session_key,
                           page="О компании",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key, leng="ukr"))
        # Record in the base of being of FTU on a web-site and creation of mark of his location - end
    # Checking for being of record in the base of the sessions key is an end
    # A record of data about the visit of web-site is an end

    # The signal processing on switching of language is beginning
    data = request.POST
    if data.get("submit") == "rus":
        Log_In_Site.objects.filter(session_key=session_key).update(leng="rus")
        return redirect('company')
    # The signal processing on switching of language is end

    all_info_company = Company.objects.filter(is_active=True)
    all_info_contacts = Contscts.objects.filter(is_active=True)
    all_info_footer = Footer.objects.filter(is_active=True)

    for compan_info in all_info_company:
        pass

    return render(request, 'main/company_ukr.html', locals())


def contacts(request):
    # A record of data about the visit of web-site is beginning
    session_key = request.session.session_key
    # Checking for being of record in the base of the sessions key is beginning
    if Log_In_Site.objects.filter(session_key=session_key).count():
        #  Record in the base of mark in track is beginning
        find_max = Eye.objects.filter(session_key=session_key)
        max_id_in = 0
        for find_single in find_max:
            if max_id_in < int(find_single.id):
                max_id_in = int(find_single.id)
        page_max_many = Eye.objects.filter(session_key=session_key, page="Контакты", id=max_id_in)
        if page_max_many.count() != 0:
            for page_max in page_max_many:
                pass
            if page_max.page == "Контакты":
                Eye.objects.get(session_key=session_key, page="Контакты", id=max_id_in).delete()

        Eye.objects.create(session_key=session_key,
                           page="Контакты",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key))
        #  Record in the base of mark in track is an end
    else:
        #  Record in the base of being of FTU on a web-site and creation of mark of his location - beginning
        Log_In_Site.objects.create(session_key=session_key, leng="rus")
        Eye.objects.create(session_key=session_key,
                           page="Контакты",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key, leng="rus"))
        #  Record in the base of being of FTU on a web-site and creation of mark of his location - end
        # Checking for being of record in the base of the sessions key is an end
        #  A record of data about the visit of web-site is an end

    #  The signal processing on switching of language is beginning
    data = request.POST

    if data.get("submit") == "ukr":
        Log_In_Site.objects.filter(session_key=session_key).update(leng="ukr")
        return redirect('contacts_ukr')
    # The signal processing on switching of language is end

    all_info_footer = Footer.objects.filter(is_active=True)
    all_info_contacts = Contscts.objects.filter(is_active=True)

    for contacts_info in all_info_contacts:
        pass

    return render(request, 'main/contacts.html', locals())


def contacts_ukr(request):
    #  A record of data about the visit of web-site is beginning
    session_key = request.session.session_key
    # Checking for being of record in the base of the sessions key is beginning
    if Log_In_Site.objects.filter(session_key=session_key).count():
        #  Record in the base of mark in track is beginning
        find_max = Eye.objects.filter(session_key=session_key)
        max_id_in = 0
        for find_single in find_max:
            if max_id_in < int(find_single.id):
                max_id_in = int(find_single.id)
        page_max_many = Eye.objects.filter(session_key=session_key, page="Контакты", id=max_id_in)
        if page_max_many.count() != 0:
            for page_max in page_max_many:
                pass
            if page_max.page == "Контакты":
                Eye.objects.get(session_key=session_key, page="Контакты", id=max_id_in).delete()

        Eye.objects.create(session_key=session_key,
                           page="Контакты",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key))
        #  Record in the base of mark in track is an end
    else:
        #  Record in the base of being of FTU on a web-site and creation of mark of his location - beginning
        Log_In_Site.objects.create(session_key=session_key, leng="rus")
        Eye.objects.create(session_key=session_key,
                           page="Контакты",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key, leng="rus"))
        #  Record in the base of being of FTU on a web-site and creation of mark of his location - end
        # Checking for being of record in the base of the sessions key is an end
        #  A record of data about the visit of web-site is an end

    #  The signal processing on switching of language is beginning
    data = request.POST
    if data.get("submit") == "rus":
        Log_In_Site.objects.filter(session_key=session_key).update(leng="rus")
        return redirect('contacts')
    # The signal processing on switching of language is end

    all_info_footer = Footer.objects.filter(is_active=True)
    all_info_contacts = Contscts.objects.filter(is_active=True)

    for contacts_info in all_info_contacts:
        pass

    return render(request, 'main/contacts_ukr.html', locals())


def diler_otdel(request):
    #  A record of data about the visit of web-site is beginning
    session_key = request.session.session_key
    # Checking for being of record in the base of the sessions key is beginning
    if Log_In_Site.objects.filter(session_key=session_key).count():
        #  Record in the base of mark in track is beginning
        find_max = Eye.objects.filter(session_key=session_key)
        max_id_in = 0
        for find_single in find_max:
            if max_id_in < int(find_single.id):
                max_id_in = int(find_single.id)
        page_max_many = Eye.objects.filter(session_key=session_key, page="Дилерский отдел", id=max_id_in)
        if page_max_many.count() != 0:
            for page_max in page_max_many:
                pass
            if page_max.page == "Дилерский отдел":
                Eye.objects.get(session_key=session_key, page="Дилерский отдел", id=max_id_in).delete()

        Eye.objects.create(session_key=session_key,
                           page="Дилерский отдел",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key))
        # Record in the base of mark in track is an end
    else:
        #  Record in the base of being of FTU on a web-site and creation of mark of his location - beginning
        Log_In_Site.objects.create(session_key=session_key, leng="rus")
        Eye.objects.create(session_key=session_key,
                           page="Дилерский отдел",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key, leng="rus"))
        #  Record in the base of being of FTU on a web-site and creation of mark of his location - end
        # Checking for being of record in the base of the sessions key is an end
        #  A record of data about the visit of web-site is an end

    all_info_footer = Footer.objects.filter(is_active=True)
    all_info_diler_otdel = Diler_Otdel.objects.filter(is_active=True)
    all_info_contscts = Diler_Otdel_Сonttacts.objects.filter(is_active=True)

    all_info = Diler_Otdel.objects.filter(is_active=True)

    for diler_otdelt_info in all_info:
        pass

    view_all_help = False  # Marker for the show of information about a search (changes a value in the end)

    response_view = False

    list_manafactory = ["ADEX", "AMADIS", "ARGENTA", "ATLANTIC TILES", "ATLAS CONCORDE", "ATLAS CONCORDE RUSSIA",
                        "CERACASA",
                        "CERAMICA RIBESALBES", "CICOGRES", "CIFRE", "DUAL GRES", "EQUIPE", "ESTIMA/ЭСТИМА", "GAYAFORES",
                        "GRAZIA CERAMICHE",
                        "IBERO", "KERRANOVA/КЕРРАНОВА", "PANARIA", "REX CERAMICHE", "SALONI", "SETTECENTO"]
    manafacturer_search_hight = Manufacturer.objects.filter(is_active=True, name_manufacturer__in=list_manafactory)

    # Collection on the base of COUNTRIES in accordance with the list of list_manafactory
    country = []
    for sear_country in manafacturer_search_hight:
        country.append(sear_country.manufacturer_country.name_manufacturer_country)
    country = Manufacturer_Country.objects.filter(name_manufacturer_country__in=country)

    # Collection on the base of PRICE GROUP in accordance with the list of list_manafactory
    price_ava = Collection_Image.objects.filter(is_main_collection=True, is_active_collection=True,
                                                name_collection__manufacturer_collection__name_manufacturer__in=list_manafactory)
    list_prise_ava = []
    for list_prise_ava_singl in price_ava:
        list_prise_ava.append(list_prise_ava_singl.name_collection.price_group_collection.name_price_group)
    price = Price_Group.objects.filter(name_price_group__in=list_prise_ava)

    resilt_collections_images = Collection_Image.objects.filter(is_active_collection=True, is_main_collection=True,
                                                                name_collection__is_active_collection=True,
                                                                name_collection__manufacturer_collection__name_manufacturer__in=list_manafactory)

    request_get_manafacturer = request.GET.getlist('manafacturer')
    request_get_country = request.GET.getlist('country')
    request_get_price = request.GET.getlist('price')
    request_get_cancel = request.GET.getlist('cancel')
    request_get_find = request.GET.getlist('find')

    if 'Искать' in request_get_find:
        result_search = []
        list_search = []
        result = []
        if request_get_manafacturer != []:
            for data_m in request_get_manafacturer:
                data_for_search = Collection.objects.filter(is_active_collection=True,
                                                            manufacturer_collection__id=data_m)
                if data_for_search.exists():
                    list_search.append(data_for_search)
            for in_list in list_search:
                in_list_re = in_list.values()
                for zipis in in_list_re:
                    result.append(zipis["id"])
            result = set(result)
            result_search.append(result)

        result = []
        if request_get_country != []:
            for data_m in request_get_country:
                data_for_search = Collection.objects.filter(is_active_collection=True,
                                                            manufacturer_collection__manufacturer_country__id=data_m)
                if data_for_search.exists():
                    list_search.append(data_for_search)
            for in_list in list_search:
                in_list_re = in_list.values()
                for zip in in_list_re:
                    result.append(zip["id"])
            result = set(result)
            result_search.append(result)

        result = []
        if request_get_price != []:
            for data_m in request_get_price:
                data_for_search = Collection.objects.filter(is_active_collection=True,
                                                            price_group_collection__id=data_m)
                if data_for_search.exists():
                    list_search.append(data_for_search)
            for in_list in list_search:
                in_list_re = in_list.values()
                for zip in in_list_re:
                    result.append(zip["id"])
            result = set(result)
            result_search.append(result)

        result_all = []
        for alfa in result_search:
            for betta in alfa:
                result_all.append(betta)

        list_only = []

        len_resu = len(result_search)  # We get length result_search - list with the corteges of ID of collections

        for list_resu_only in result_all:  # We pass on result_all - incorporated ID from all positions of queries on a search
            if result_all.count(
                    list_resu_only) == len_resu and list_resu_only not in list_only:  # We check every element for an amount equal to all queries, if it is equal to all queries that it necessary ID
                list_only.append(list_resu_only)

        result_all = list_only

        resilt_collections = Collection.objects.filter(is_active_collection=True, id__in=result_all)
        resilt_collections_images = Collection_Image.objects.filter(is_active_collection=True, is_main_collection=True,
                                                                    name_collection__is_active_collection=True,
                                                                    name_collection__id__in=result_all,
                                                                    name_collection__manufacturer_collection__name_manufacturer__in=list_manafactory)

        # Stock a block in the base of result of search of collections coming from a sectional search is beginning
        # A Subblock collecting data from the result of sectional search is beginning
        collections_single_diller_otdel = Collection.objects.filter(id__in=result_all,
                                                                    manufacturer_collection__name_manufacturer__in=list_manafactory)
        list_collection = []
        list_statistica = []
        for collection_single_diller_otdel in collections_single_diller_otdel:
            list_collection.append(collection_single_diller_otdel.id)
        # A Subblock collecting data from the result of sectional search is an end

        # A Subblock collecting data from all base of queries of sectional search on the sessions key and page is beginning
        if Collection.objects.filter(id__in=result_all,
                                     manufacturer_collection__name_manufacturer__in=list_manafactory).exists():
            all_statistica = Statistic_Find_Bloc.objects.filter(session_key=session_key, page="diler_otdel")
            for statistica in all_statistica:
                list_statistica.append(statistica.collection)
        # A Subblock collecting data from all base of queries of sectional search on the sessions key and page is an end

        #  Subblock of record in case of absence of result of sectional search in a base is beginning
        if str(list_collection) not in list_statistica and len(str(list_collection)) > 2:
            Statistic_Find_Bloc.objects.create(session_key=session_key, collection=list_collection,
                                               page="diler_otdel")
        # Subblock of record in case of absence of result of sectional search in a base is an end
        # Stock a block in the base of result of search of collections coming from a sectional search is an end

        # Checking for a presence as a result of retrieval of data
        if resilt_collections_images.exists() == True:
            response_view = True
            # Receipt of way at the query of search
            response = str(request.get_full_path())
            # Transformation of line to the query and receipt of necessary remain of way for adding to pagginator
            response = response.replace("/diler_otdel/", "")
            create_base = Search_Diller_Otdel.objects.filter(session_key=session_key)

            if "page" not in response:
                if create_base.exists() == True:
                    Search_Diller_Otdel.objects.filter(session_key=session_key).update(response=response,
                                                                                       request_get_manafacturer=request_get_manafacturer,
                                                                                       request_get_price=request_get_price,
                                                                                       request_get_country=request_get_country)
                if create_base.exists() == False:
                    Search_Diller_Otdel.objects.create(session_key=session_key, response=response,
                                                       request_get_manafacturer=request_get_manafacturer,
                                                       request_get_price=request_get_price,
                                                       request_get_country=request_get_country)
                    Search_Manafactory.objects.filter(session_key=session_key).delete()
                    Search_Manafactory_Single.objects.filter(session_key=session_key).delete()
                    Search_For_Project.objects.filter(session_key=session_key).delete()
                    Search_Low_Addition.objects.filter(session_key=session_key).delete()
                    Search_Search.objects.filter(session_key=session_key).delete()

                    # Checking for absence as a result of retrieval of data

        if resilt_collections_images.exists() == False:
            response_view = False
            resilt_collections_images = Collection_Image.objects.filter(is_active_collection=True,
                                                                        is_main_collection=True,
                                                                        name_collection__is_active_collection=True,
                                                                        name_collection__manufacturer_collection__name_manufacturer__in=list_manafactory)

        response_for_search = Search_Diller_Otdel.objects.filter(session_key=session_key)
        for response_for_web in response_for_search:
            pass

    if 'Сбросить фильтр поиска' in request_get_cancel:
        response_view = False
        resilt_collections_images = Collection_Image.objects.filter(is_active_collection=True, is_main_collection=True,
                                                                    name_collection__is_active_collection=True,
                                                                    name_collection__manufacturer_collection__name_manufacturer__in=list_manafactory)
        delete_base = Search_Diller_Otdel.objects.filter(session_key=session_key)
        if delete_base.exists() == True:
            delete_base.delete()
        if delete_base.exists() == False:
            pass

    # Preparation to paggination
    resilt_collections_images = resilt_collections_images.order_by('id')
    # Paggination of page is beginning
    paginator = Paginator(resilt_collections_images, 4)
    page = request.GET.get('page')

    try:
        resilt_collections_images = paginator.page(page)
    except PageNotAnInteger:
        resilt_collections_images = paginator.page(1)
    except EmptyPage:
        resilt_collections_images = paginator.page(paginator.num_pages)
    # Paggination of page is an end

    if request_get_manafacturer != []:
        for info_sig in Search_Diller_Otdel.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_manafacturer = True  # Marker of display of information about a search
            str_manafacturer = str(
                info_sig.request_get_manafacturer)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_manafacturer)
            srez = str_manafacturer[2:len_str - 2]  # We produce the cut of line of dellet from []
            info_manafacturer_veb = srez.split("', '")  # Line feed in the list of values of ID
            info_manafacturer_veb = Manufacturer.objects.filter(
                id__in=info_manafacturer_veb)  # Receipt of query from a base in accordance with a list

    if request_get_country != []:
        for info_sig in Search_Diller_Otdel.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_country = True  # Marker of display of information about a search
            str_country = str(
                info_sig.request_get_country)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_country)
            srez = str_country[2:len_str - 2]  # We produce the cut of line of delet from []
            info_country_veb = srez.split("', '")  # Line feed in the list of values of ID
            info_country_veb = Manufacturer_Country.objects.filter(
                id__in=info_country_veb)  # Receipt of query from a base in accordance with a list

    if request_get_price != []:
        for info_sig in Search_Diller_Otdel.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_price = True  # Marker of display of information about a search
            str_price = str(
                info_sig.request_get_price)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_price)
            srez = str_price[2:len_str - 2]  # We produce the cut of line of delet from []
            info_price_veb = srez.split("', '")  # Line feed in the list of values of ID
            info_price_veb = Price_Group.objects.filter(
                id__in=info_price_veb)  # Receipt of query from a base in accordance with a list

    return render(request, 'main/diler_otdel.html', locals())


def projects_materials(request):
    #  A record of data about the visit of web-site is beginning
    session_key = request.session.session_key
    # Checking for being of record in the base of the sessions key is beginning
    if Log_In_Site.objects.filter(session_key=session_key).count():
        #  Record in the base of mark in track is beginning
        find_max = Eye.objects.filter(session_key=session_key)
        max_id_in = 0
        for find_single in find_max:
            if max_id_in < int(find_single.id):
                max_id_in = int(find_single.id)
        page_max_many = Eye.objects.filter(session_key=session_key, page="Проектные материалы", id=max_id_in)
        if page_max_many.count() != 0:
            for page_max in page_max_many:
                pass
            if page_max.page == "Проектные материалы":
                Eye.objects.get(session_key=session_key, page="Проектные материалы", id=max_id_in).delete()

        Eye.objects.create(session_key=session_key,
                           page="Проектные материалы",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key))
        #  Record in the base of mark in track is an end
    else:
        #  Record in the base of being of FTU on a web-site and creation of mark of his location - beginning
        Log_In_Site.objects.create(session_key=session_key, leng="rus")
        Eye.objects.create(session_key=session_key,
                           page="Проектные материалы",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key, leng="rus"))
        #  Record in the base of being of FTU on a web-site and creation of mark of his location - end
        # Checking for being of record in the base of the sessions key is an end
        #  A record of data about the visit of web-site is an end

    #  The signal processing on switching of language is beginning
    data = request.POST
    if data.get("submit") == "ukr":
        Log_In_Site.objects.filter(session_key=session_key).update(leng="ukr")
        return redirect('projects_materials_ukr')
    # The signal processing on switching of language is beginning

    all_info_footer = Footer.objects.filter(is_active=True)
    all_info_project_material = Projects_Materials.objects.filter(is_active=True)

    all_info_project = Projects_Materials.objects.filter(is_active=True)

    for project_info in all_info_project:
        pass

    view_all_help = False  # Marker for the show of information about a search (changes a value in the end)

    response_view = False

    list_manafactory = ["ATLAS CONCORDE", "ATLAS CONCORDE RUSSIA", "CIFRE", "ESTIMA/ЭСТИМА", "KERRANOVA/КЕРРАНОВА",
                        "REX CERAMICHE"]
    manafacturer_search_hight = Manufacturer.objects.filter(is_active=True, name_manufacturer__in=list_manafactory)

    # Collection on the base of COUNTRIES in accordance with the list of list_manafactory
    country = []
    for sear_country in manafacturer_search_hight:
        country.append(sear_country.manufacturer_country.name_manufacturer_country)
    country = Manufacturer_Country.objects.filter(name_manufacturer_country__in=country)

    type_material = Collection_Type_Material_For_Search.objects.all()

    # Collection on the base of PRESENCE in accordance with the list of list_manafactory
    collection_ava = Collection_Image.objects.filter(is_main_collection=True, is_active_collection=True,
                                                     name_collection__manufacturer_collection__name_manufacturer__in=list_manafactory)
    list_availability_s = []
    for avas in collection_ava:
        list_availability_s.append(avas.name_collection.availability_collection)

    availability_s = Availability.objects.filter(name_availability__in=list_availability_s)

    # Collection on the base of PRICE GROUP in accordance with the list of list_manafactory
    price_ava = Collection_Image.objects.filter(is_main_collection=True, is_active_collection=True,
                                                name_collection__manufacturer_collection__name_manufacturer__in=list_manafactory)
    list_prise_ava = []
    for list_prise_ava_singl in price_ava:
        list_prise_ava.append(list_prise_ava_singl.name_collection.price_group_collection.name_price_group)

    price = Price_Group.objects.filter(name_price_group__in=list_prise_ava)

    collecti = Collection.objects.all()

    # Collection on a base APPLICATION
    application = Collection_Application_For_Search.objects.all()

    # Collection on a base TYPE of MATERIAL
    type_material = Collection_Type_Material_For_Search.objects.all()

    resilt_collections_images = Collection_Image.objects.filter(is_active_collection=True, is_main_collection=True,
                                                                name_collection__is_active_collection=True,
                                                                name_collection__manufacturer_collection__name_manufacturer__in=list_manafactory)

    request_get_country = request.GET.getlist('country')
    request_get_manafacturer = request.GET.getlist('manafacturer')
    request_get_price = request.GET.getlist('price')
    request_get_availability = request.GET.getlist('availability')
    request_get_type_material = request.GET.getlist('type_material')
    request_get_application = request.GET.getlist('application')

    request_get_cancel = request.GET.getlist('cancel')
    request_get_find = request.GET.getlist('find')

    if 'Искать' in request_get_find:
        result_search = []
        list_search = []
        result = []
        if request_get_manafacturer != []:
            for data_m in request_get_manafacturer:
                data_for_search = Collection.objects.filter(is_active_collection=True,
                                                            manufacturer_collection__id=data_m,
                                                            manufacturer_collection__name_manufacturer__in=list_manafactory)
                if data_for_search.exists():
                    list_search.append(data_for_search)
            for in_list in list_search:
                in_list_re = in_list.values()
                for zipis in in_list_re:
                    result.append(zipis["id"])
            result = set(result)
            result_search.append(result)

        result = []
        if request_get_application != []:
            for data_m in request_get_application:
                if data_m == "bathrooms":
                    res_dic = Collection_Application_For_Search.objects.filter(collection_application_is_active=True,
                                                                               collection_application_bathrooms=True)
                if data_m == "floor":
                    res_dic = Collection_Application_For_Search.objects.filter(collection_application_is_active=True,
                                                                               collection_application_floor=True)
                if data_m == "apron":
                    res_dic = Collection_Application_For_Search.objects.filter(collection_application_is_active=True,
                                                                               collection_application_apron=True)
                if data_m == "outdoor":
                    res_dic = Collection_Application_For_Search.objects.filter(collection_application_is_active=True,
                                                                               collection_application_outdoor=True)
                if data_m == "residential":
                    res_dic = Collection_Application_For_Search.objects.filter(collection_application_is_active=True,
                                                                               collection_application_residential=True)
                if data_m == "projects":
                    res_dic = Collection_Application_For_Search.objects.filter(collection_application_is_active=True,
                                                                               collection_application_projects=True)
                if res_dic.exists():
                    for res_dic_in in res_dic:
                        result.append(res_dic_in.id)
            result = set(result)
            result_search.append(result)

        result = []
        if request_get_country != []:
            for data_m in request_get_country:
                data_for_search = Collection.objects.filter(is_active_collection=True,
                                                            manufacturer_collection__manufacturer_country__id=data_m)
                if data_for_search.exists():
                    list_search.append(data_for_search)
            for in_list in list_search:
                in_list_re = in_list.values()
                for zip in in_list_re:
                    result.append(zip["id"])
            result = set(result)
            result_search.append(result)

        result = []
        if request_get_type_material != []:
            for data_m in request_get_type_material:
                if data_m == "ceramic":
                    res_dic = Collection_Type_Material_For_Search.objects.filter(
                        collection_type_material_is_active=True,
                        collection_type_material_ceramic=True)
                if data_m == "porcelain":
                    res_dic = Collection_Type_Material_For_Search.objects.filter(
                        collection_type_material_is_active=True,
                        collection_type_material_porcelain=True)

                if res_dic.exists():
                    for res_dic_in in res_dic:
                        result.append(res_dic_in.id)
            result = set(result)
            result_search.append(result)

        result = []
        if request_get_availability != []:
            for data_m in request_get_availability:
                data_for_search = Collection.objects.filter(is_active_collection=True,
                                                            availability_collection__id=data_m)
                if data_for_search.exists():
                    list_search.append(data_for_search)
            for in_list in list_search:
                in_list_re = in_list.values()
                for zip in in_list_re:
                    result.append(zip["id"])
            result = set(result)
            result_search.append(result)

        result = []
        if request_get_price != []:
            for data_m in request_get_price:
                data_for_search = Collection.objects.filter(is_active_collection=True,
                                                            price_group_collection__id=data_m)
                if data_for_search.exists():
                    list_search.append(data_for_search)
            for in_list in list_search:
                in_list_re = in_list.values()
                for zip in in_list_re:
                    result.append(zip["id"])
            result = set(result)
            result_search.append(result)

        result_all = []
        for alfa in result_search:
            for betta in alfa:
                result_all.append(betta)

        list_only = []

        len_resu = len(result_search)  # We get length result_search - list with the corteges of ID of collections

        for list_resu_only in result_all:  # We pass on result_all - incorporated ID from all positions of queries on a search
            if result_all.count(
                    list_resu_only) == len_resu and list_resu_only not in list_only:  # We check every element for an amount equal to all queries, if it is equal to all queries that it necessary ID
                list_only.append(list_resu_only)

        result_all = list_only

        resilt_collections = Collection.objects.filter(is_active_collection=True, id__in=result_all)
        resilt_collections_images = Collection_Image.objects.filter(is_active_collection=True, is_main_collection=True,
                                                                    name_collection__is_active_collection=True,
                                                                    name_collection__id__in=result_all,
                                                                    name_collection__manufacturer_collection__name_manufacturer__in=list_manafactory)

        # Stock a block in the base of result of search of collections coming from a sectional search is beginning
        # A Subblock collecting data from the result of sectional search is beginning
        collections_single_projects_materials = Collection.objects.filter(id__in=result_all,
                                                                          manufacturer_collection__name_manufacturer__in=list_manafactory)
        list_collection = []
        list_statistica = []
        for collection_single_projects_materials in collections_single_projects_materials:
            list_collection.append(collection_single_projects_materials.id)
        # A Subblock collecting data from the result of sectional search is an end

        #  A Subblock collecting data from all base of queries of sectional search on the sessions key and page is beginning
        if Collection.objects.filter(id__in=result_all,
                                     manufacturer_collection__name_manufacturer__in=list_manafactory).exists():
            all_statistica = Statistic_Find_Bloc.objects.filter(session_key=session_key, page="projects_materials")
            for statistica in all_statistica:
                list_statistica.append(statistica.collection)
        # A Subblock collecting data from all base of queries of sectional search on the sessions key and page is an end

        # Subblock of record in case of absence of result of sectional search in a base is beginning
        if str(list_collection) not in list_statistica and len(str(list_collection)) > 2:
            Statistic_Find_Bloc.objects.create(session_key=session_key, collection=list_collection,
                                               page="projects_materials")
        # Subblock of record in case of absence of result of sectional search in a base is an end
        # Stock a block in the base of result of search of collections coming from a sectional search is beginning

        # Checking for a presence as a result of retrieval of data
        if resilt_collections_images.exists() == True:
            response_view = True
            # Receipt of way at the query of search
            response = str(request.get_full_path())
            # Transformation of line to the query and receipt of necessary remain of way for adding to pagginator
            response = response.replace("/projects_materials/", "")
            create_base = Search_For_Project.objects.filter(session_key=session_key)

            if "page" not in response:
                if create_base.exists() == True:
                    Search_For_Project.objects.filter(session_key=session_key).update(response=response,
                                                                                      request_get_manafacturer=request_get_manafacturer,
                                                                                      request_get_country=request_get_country,
                                                                                      request_get_price=request_get_price,
                                                                                      request_get_availability=request_get_availability,
                                                                                      request_get_application=request_get_application,
                                                                                      request_get_type_material=request_get_type_material)
                if create_base.exists() == False:
                    Search_For_Project.objects.create(session_key=session_key, response=response,
                                                      request_get_manafacturer=request_get_manafacturer,
                                                      request_get_country=request_get_country,
                                                      request_get_price=request_get_price,
                                                      request_get_availability=request_get_availability,
                                                      request_get_application=request_get_application,
                                                      request_get_type_material=request_get_type_material)
                    Search_Diller_Otdel.objects.filter(session_key=session_key).delete()
                    Search_Manafactory.objects.filter(session_key=session_key).delete()
                    Search_Manafactory_Single.objects.filter(session_key=session_key).delete()
                    Search_Low_Addition.objects.filter(session_key=session_key).delete()
                    Search_Search.objects.filter(session_key=session_key).delete()

                    # Checking for absence as a result of retrieval of data

        if resilt_collections_images.exists() == False:
            response_view = False
            resilt_collections_images = Collection_Image.objects.filter(is_active_collection=True,
                                                                        is_main_collection=True,
                                                                        name_collection__is_active_collection=True,
                                                                        name_collection__manufacturer_collection__name_manufacturer__in=list_manafactory)

        response_for_search = Search_For_Project.objects.filter(session_key=session_key)
        for response_for_web in response_for_search:
            pass

    if 'Сбросить фильтр поиска' in request_get_cancel:
        response_view = False
        resilt_collections_images = Collection_Image.objects.filter(is_active_collection=True, is_main_collection=True,
                                                                    name_collection__is_active_collection=True,
                                                                    name_collection__manufacturer_collection__name_manufacturer__in=list_manafactory)
        delete_base = Search_For_Project.objects.filter(session_key=session_key)
        if delete_base.exists() == True:
            delete_base.delete()
        if delete_base.exists() == False:
            pass

    # Preparation to paggination
    resilt_collections_images = resilt_collections_images.order_by('id')
    # Paggination of page is beginning
    paginator = Paginator(resilt_collections_images, 4)
    page = request.GET.get('page')

    try:
        resilt_collections_images = paginator.page(page)
    except PageNotAnInteger:
        resilt_collections_images = paginator.page(1)
    except EmptyPage:
        resilt_collections_images = paginator.page(paginator.num_pages)
    # Paggination of page is an end

    if request_get_manafacturer != []:
        for info_sig in Search_For_Project.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_manafacturer = True  # Marker of display of information about a search
            str_manafacturer = str(
                info_sig.request_get_manafacturer)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_manafacturer)

            if len(str_manafacturer) > 2:
                srez = str_manafacturer[2:len_str - 2]  # We produce the cut of line deleting from []
                info_manafacturer_veb = srez.split("', '")  # Line feed in the list of values of ID
                info_manafacturer_veb = Manufacturer.objects.filter(
                    id__in=info_manafacturer_veb)  # Receipt of query from a base in accordance with a list

    if request_get_country != []:
        for info_sig in Search_For_Project.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_country = True  # Marker of display of information about a search
            str_country = str(
                info_sig.request_get_country)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_country)
            srez = str_country[2:len_str - 2]  # We produce the cut of line deleting from []
            info_country_veb = srez.split("', '")  # Line feed in the list of values of ID
            info_country_veb = Manufacturer_Country.objects.filter(
                id__in=info_country_veb)  # Receipt of query from a base in accordance with a list

    if request_get_price != []:
        for info_sig in Search_For_Project.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_price = True  # Marker of display of information about a search
            str_price = str(
                info_sig.request_get_price)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_price)
            srez = str_price[2:len_str - 2]  # We produce the cut of line deleting from []
            info_price_veb = srez.split("', '")  # Line feed in the list of values of ID
            info_price_veb = Price_Group.objects.filter(
                id__in=info_price_veb)  # Receipt of query from a base in accordance with a list

    if request_get_availability != []:
        for info_sig in Search_For_Project.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_availability = True  # Marker of display of information about a search
            str_availability = str(
                info_sig.request_get_availability)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_availability)
            srez = str_availability[2:len_str - 2]  # We produce the cut of line deleting from []
            info_availability_veb = srez.split("', '")  # Line feed in the list of values of ID
            info_availability_veb = Availability.objects.filter(
                id__in=info_availability_veb)  # Receipt of query from a base in accordance with a list

    if request_get_application != []:
        for info_sig in Search_For_Project.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_application = True  # Marker of display of information about a search

            str_application = str(
                info_sig.request_get_application)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_application)
            srez = str_application[2:len_str - 2]  # We produce the cut of line deleting from []
            info_application_veb = srez.split("', '")  # Line feed in the list of values of ID

            result_application = []
            for info_sig in info_application_veb:
                if info_sig == "bathrooms":
                    res_application = "Для ванных комнат"
                if info_sig == "floor":
                    res_application = "Для кухни/Напольная плитка"
                if info_sig == "apron":
                    res_application = "Для кухни/Фартук"
                if info_sig == "outdoor":
                    res_application = "Для уличного применения"
                if info_sig == "residential":
                    res_application = "Жилой интерьер"
                if info_sig == "projects":
                    res_application = "Общественные интерьеры/Проекты"
                result_application.append(res_application)

    if request_get_type_material != []:
        for info_sig in Search_For_Project.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_type_material = True  # Marker of display of information about a search

            str_type_material = str(
                info_sig.request_get_type_material)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_type_material)
            srez = str_type_material[2:len_str - 2]  # We produce the cut of line deleting from []
            info_type_material_veb = srez.split("', '")  # Line feed in the list of values of ID

            result_type_material = []
            for info_sig in info_type_material_veb:

                if info_sig == "ceramic":
                    res_type_material = "Керамическая плитка"
                if info_sig == "porcelain":
                    res_type_material = "Керамогранит"

                result_type_material.append(res_type_material)

    return render(request, 'main/projects_materials.html', locals())


def projects_materials_ukr(request):
    #  A record of data about the visit of web-site is beginning
    session_key = request.session.session_key
    # Checking for being of record in the base of the sessions key is beginning
    if Log_In_Site.objects.filter(session_key=session_key).count():
        #  Record in the base of mark in track is beginning
        find_max = Eye.objects.filter(session_key=session_key)
        max_id_in = 0
        for find_single in find_max:
            if max_id_in < int(find_single.id):
                max_id_in = int(find_single.id)
        page_max_many = Eye.objects.filter(session_key=session_key, page="Проектные материалы", id=max_id_in)
        if page_max_many.count() != 0:
            for page_max in page_max_many:
                pass
            if page_max.page == "Проектные материалы":
                Eye.objects.get(session_key=session_key, page="Проектные материалы", id=max_id_in).delete()

        Eye.objects.create(session_key=session_key,
                           page="Проектные материалы",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key))
        #  Record in the base of mark in track is an end
    else:
        #  Record in the base of being of FTU on a web-site and creation of mark of his location - beginning
        Log_In_Site.objects.create(session_key=session_key, leng="rus")
        Eye.objects.create(session_key=session_key,
                           page="Проектные материалы",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key, leng="rus"))
        #  Record in the base of being of FTU on a web-site and creation of mark of his location - end
        # Checking for being of record in the base of the sessions key is an end
        #  A record of data about the visit of web-site is an end

    #  The signal processing on switching of language is beginning
    data = request.POST
    if data.get("submit") == "rus":
        Log_In_Site.objects.filter(session_key=session_key).update(leng="rus")
        return redirect('projects_materials')
    # The signal processing on switching of language is beginning

    all_info_footer = Footer.objects.filter(is_active=True)
    all_info_project_material = Projects_Materials.objects.filter(is_active=True)

    all_info_project = Projects_Materials.objects.filter(is_active=True)

    for project_info in all_info_project:
        pass

    view_all_help = False  # Marker for the show of information about a search (changes a value in the end)

    response_view = False

    list_manafactory = ["ATLAS CONCORDE", "ATLAS CONCORDE RUSSIA", "CIFRE", "ESTIMA/ЭСТИМА", "KERRANOVA/КЕРРАНОВА",
                        "REX CERAMICHE"]
    manafacturer_search_hight = Manufacturer.objects.filter(is_active=True, name_manufacturer__in=list_manafactory)

    # Collection on the base of COUNTRIES in accordance with the list of list_manafactory
    country = []
    for sear_country in manafacturer_search_hight:
        country.append(sear_country.manufacturer_country.name_manufacturer_country)
    country = Manufacturer_Country.objects.filter(name_manufacturer_country__in=country)

    type_material = Collection_Type_Material_For_Search.objects.all()

    # Collection on the base of PRESENCE in accordance with the list of list_manafactory
    collection_ava = Collection_Image.objects.filter(is_main_collection=True, is_active_collection=True,
                                                     name_collection__manufacturer_collection__name_manufacturer__in=list_manafactory)
    list_availability_s = []
    for avas in collection_ava:
        list_availability_s.append(avas.name_collection.availability_collection)

    availability_s = Availability.objects.filter(name_availability__in=list_availability_s)

    # Collection on the base of PRICE GROUP in accordance with the list of list_manafactory
    price_ava = Collection_Image.objects.filter(is_main_collection=True, is_active_collection=True,
                                                name_collection__manufacturer_collection__name_manufacturer__in=list_manafactory)
    list_prise_ava = []
    for list_prise_ava_singl in price_ava:
        list_prise_ava.append(list_prise_ava_singl.name_collection.price_group_collection.name_price_group)

    price = Price_Group.objects.filter(name_price_group__in=list_prise_ava)

    collecti = Collection.objects.all()

    # Collection on a base APPLICATION
    application = Collection_Application_For_Search.objects.all()

    # Collection on a base TYPE of MATERIAL
    type_material = Collection_Type_Material_For_Search.objects.all()

    resilt_collections_images = Collection_Image.objects.filter(is_active_collection=True, is_main_collection=True,
                                                                name_collection__is_active_collection=True,
                                                                name_collection__manufacturer_collection__name_manufacturer__in=list_manafactory)

    request_get_country = request.GET.getlist('country')
    request_get_manafacturer = request.GET.getlist('manafacturer')
    request_get_price = request.GET.getlist('price')
    request_get_availability = request.GET.getlist('availability')
    request_get_type_material = request.GET.getlist('type_material')
    request_get_application = request.GET.getlist('application')

    request_get_cancel = request.GET.getlist('cancel')
    request_get_find = request.GET.getlist('find')

    if 'Шукати' in request_get_find:
        result_search = []
        list_search = []
        result = []
        if request_get_manafacturer != []:
            for data_m in request_get_manafacturer:
                data_for_search = Collection.objects.filter(is_active_collection=True,
                                                            manufacturer_collection__id=data_m,
                                                            manufacturer_collection__name_manufacturer__in=list_manafactory)
                if data_for_search.exists():
                    list_search.append(data_for_search)
            for in_list in list_search:
                in_list_re = in_list.values()
                for zipis in in_list_re:
                    result.append(zipis["id"])
            result = set(result)
            result_search.append(result)

        result = []
        if request_get_application != []:
            for data_m in request_get_application:
                if data_m == "bathrooms":
                    res_dic = Collection_Application_For_Search.objects.filter(collection_application_is_active=True,
                                                                               collection_application_bathrooms=True)
                if data_m == "floor":
                    res_dic = Collection_Application_For_Search.objects.filter(collection_application_is_active=True,
                                                                               collection_application_floor=True)
                if data_m == "apron":
                    res_dic = Collection_Application_For_Search.objects.filter(collection_application_is_active=True,
                                                                               collection_application_apron=True)
                if data_m == "outdoor":
                    res_dic = Collection_Application_For_Search.objects.filter(collection_application_is_active=True,
                                                                               collection_application_outdoor=True)
                if data_m == "residential":
                    res_dic = Collection_Application_For_Search.objects.filter(collection_application_is_active=True,
                                                                               collection_application_residential=True)
                if data_m == "projects":
                    res_dic = Collection_Application_For_Search.objects.filter(collection_application_is_active=True,
                                                                               collection_application_projects=True)
                if res_dic.exists():
                    for res_dic_in in res_dic:
                        result.append(res_dic_in.id)
            result = set(result)
            result_search.append(result)

        result = []
        if request_get_country != []:
            for data_m in request_get_country:
                data_for_search = Collection.objects.filter(is_active_collection=True,
                                                            manufacturer_collection__manufacturer_country__id=data_m)
                if data_for_search.exists():
                    list_search.append(data_for_search)
            for in_list in list_search:
                in_list_re = in_list.values()
                for zip in in_list_re:
                    result.append(zip["id"])
            result = set(result)
            result_search.append(result)

        result = []
        if request_get_type_material != []:
            for data_m in request_get_type_material:
                if data_m == "ceramic":
                    res_dic = Collection_Type_Material_For_Search.objects.filter(
                        collection_type_material_is_active=True,
                        collection_type_material_ceramic=True)
                if data_m == "porcelain":
                    res_dic = Collection_Type_Material_For_Search.objects.filter(
                        collection_type_material_is_active=True,
                        collection_type_material_porcelain=True)

                if res_dic.exists():
                    for res_dic_in in res_dic:
                        result.append(res_dic_in.id)
            result = set(result)
            result_search.append(result)

        result = []
        if request_get_availability != []:
            for data_m in request_get_availability:
                data_for_search = Collection.objects.filter(is_active_collection=True,
                                                            availability_collection__id=data_m)
                if data_for_search.exists():
                    list_search.append(data_for_search)
            for in_list in list_search:
                in_list_re = in_list.values()
                for zip in in_list_re:
                    result.append(zip["id"])
            result = set(result)
            result_search.append(result)

        result = []
        if request_get_price != []:
            for data_m in request_get_price:
                data_for_search = Collection.objects.filter(is_active_collection=True,
                                                            price_group_collection__id=data_m)
                if data_for_search.exists():
                    list_search.append(data_for_search)
            for in_list in list_search:
                in_list_re = in_list.values()
                for zip in in_list_re:
                    result.append(zip["id"])
            result = set(result)
            result_search.append(result)

        result_all = []
        for alfa in result_search:
            for betta in alfa:
                result_all.append(betta)

        list_only = []

        len_resu = len(result_search)  # We get length result_search - list with the corteges of ID of collections

        for list_resu_only in result_all:  # We pass on result_all - incorporated ID from all positions of queries on a search
            if result_all.count(
                    list_resu_only) == len_resu and list_resu_only not in list_only:  # We check every element for an amount equal to all queries, if it is equal to all queries that it necessary ID
                list_only.append(list_resu_only)

        result_all = list_only

        resilt_collections = Collection.objects.filter(is_active_collection=True, id__in=result_all)
        resilt_collections_images = Collection_Image.objects.filter(is_active_collection=True, is_main_collection=True,
                                                                    name_collection__is_active_collection=True,
                                                                    name_collection__id__in=result_all,
                                                                    name_collection__manufacturer_collection__name_manufacturer__in=list_manafactory)

        # Stock a block in the base of result of search of collections coming from a sectional search is beginning
        # A Subblock collecting data from the result of sectional search is beginning
        collections_single_projects_materials = Collection.objects.filter(id__in=result_all,
                                                                          manufacturer_collection__name_manufacturer__in=list_manafactory)
        list_collection = []
        list_statistica = []
        for collection_single_projects_materials in collections_single_projects_materials:
            list_collection.append(collection_single_projects_materials.id)
        # A Subblock collecting data from the result of sectional search is an end

        # A Subblock collecting data from all base of queries of sectional search on the session key and page is beginning
        if Collection.objects.filter(id__in=result_all,
                                     manufacturer_collection__name_manufacturer__in=list_manafactory).exists():
            all_statistica = Statistic_Find_Bloc.objects.filter(session_key=session_key, page="projects_materials")
            for statistica in all_statistica:
                list_statistica.append(statistica.collection)
        # A Subblock collecting data from all base of queries of sectional search on the session key and page is an end

        # Subblock of record in case of absence of result of sectional search in a base is beginning
        if str(list_collection) not in list_statistica and len(str(list_collection)) > 2:
            Statistic_Find_Bloc.objects.create(session_key=session_key, collection=list_collection,
                                               page="projects_materials")
        # Subblock of record in case of absence of result of sectional search in a base is an end
        # Stock a block in the base of result of search of collections coming from a sectional search is beginning

        # Checking for a presence as a result of retrieval of data
        if resilt_collections_images.exists() == True:
            response_view = True
            # Receipt of way at the query of search
            response = str(request.get_full_path())
            # Transformation of line to the query and receipt of necessary remain of way for adding to paggination
            response = response.replace("/projects_materials_ukr/", "")
            create_base = Search_For_Project.objects.filter(session_key=session_key)

            if "page" not in response:
                if create_base.exists() == True:
                    Search_For_Project.objects.filter(session_key=session_key).update(response=response,
                                                                                      request_get_manafacturer=request_get_manafacturer,
                                                                                      request_get_country=request_get_country,
                                                                                      request_get_price=request_get_price,
                                                                                      request_get_availability=request_get_availability,
                                                                                      request_get_application=request_get_application,
                                                                                      request_get_type_material=request_get_type_material)
                if create_base.exists() == False:
                    Search_For_Project.objects.create(session_key=session_key, response=response,
                                                      request_get_manafacturer=request_get_manafacturer,
                                                      request_get_country=request_get_country,
                                                      request_get_price=request_get_price,
                                                      request_get_availability=request_get_availability,
                                                      request_get_application=request_get_application,
                                                      request_get_type_material=request_get_type_material)
                    Search_Diller_Otdel.objects.filter(session_key=session_key).delete()
                    Search_Manafactory.objects.filter(session_key=session_key).delete()
                    Search_Manafactory_Single.objects.filter(session_key=session_key).delete()
                    Search_Low_Addition.objects.filter(session_key=session_key).delete()
                    Search_Search.objects.filter(session_key=session_key).delete()

                    # Checking for absence as a result of retrieval of data

        if resilt_collections_images.exists() == False:
            response_view = False
            resilt_collections_images = Collection_Image.objects.filter(is_active_collection=True,
                                                                        is_main_collection=True,
                                                                        name_collection__is_active_collection=True,
                                                                        name_collection__manufacturer_collection__name_manufacturer__in=list_manafactory)

        response_for_search = Search_For_Project.objects.filter(session_key=session_key)
        for response_for_web in response_for_search:
            pass

    if 'Скинути фільтр пошуку' in request_get_cancel:
        response_view = False
        resilt_collections_images = Collection_Image.objects.filter(is_active_collection=True, is_main_collection=True,
                                                                    name_collection__is_active_collection=True,
                                                                    name_collection__manufacturer_collection__name_manufacturer__in=list_manafactory)
        delete_base = Search_For_Project.objects.filter(session_key=session_key)
        if delete_base.exists() == True:
            delete_base.delete()
        if delete_base.exists() == False:
            pass

    # Preparation to paggination
    resilt_collections_images = resilt_collections_images.order_by('id')
    # Paggination of page is beginning
    paginator = Paginator(resilt_collections_images, 4)
    page = request.GET.get('page')

    try:
        resilt_collections_images = paginator.page(page)
    except PageNotAnInteger:
        resilt_collections_images = paginator.page(1)
    except EmptyPage:
        resilt_collections_images = paginator.page(paginator.num_pages)
        # Paggination of page is an end

    if request_get_manafacturer != []:
        for info_sig in Search_For_Project.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_manafacturer = True  # Marker of display of information about a search
            str_manafacturer = str(
                info_sig.request_get_manafacturer)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_manafacturer)
            if len(str_manafacturer) > 2:
                srez = str_manafacturer[2:len_str - 2]  # We produce the cut of line of deletion from []
                info_manafacturer_veb = srez.split("', '")  # Line feed in the list of values of ID
                info_manafacturer_veb = Manufacturer.objects.filter(
                    id__in=info_manafacturer_veb)  # Receipt of query from a base in accordance with a list

    if request_get_country != []:
        for info_sig in Search_For_Project.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_country = True  # Marker of display of information about a search
            str_country = str(
                info_sig.request_get_country)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_country)
            srez = str_country[2:len_str - 2]  # We produce the cut of line of deletion from []
            info_country_veb = srez.split("', '")  # Line feed in the list of values of ID
            info_country_veb = Manufacturer_Country.objects.filter(
                id__in=info_country_veb)  # Receipt of query from a base in accordance with a list

    if request_get_price != []:
        for info_sig in Search_For_Project.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_price = True  # Marker of display of information about a search
            str_price = str(
                info_sig.request_get_price)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_price)
            srez = str_price[2:len_str - 2]  # We produce the cut of line of deletion from []
            info_price_veb = srez.split("', '")  # Line feed in the list of values of ID
            info_price_veb = Price_Group.objects.filter(
                id__in=info_price_veb)  # Receipt of query from a base in accordance with a list

    if request_get_availability != []:
        for info_sig in Search_For_Project.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_availability = True  # Marker of display of information about a search
            str_availability = str(
                info_sig.request_get_availability)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_availability)
            srez = str_availability[2:len_str - 2]  # We produce the cut of line of deletion from []
            info_availability_veb = srez.split("', '")  # Line feed in the list of values of ID
            info_availability_veb = Availability.objects.filter(
                id__in=info_availability_veb)  # Receipt of query from a base in accordance with a list

    if request_get_application != []:
        for info_sig in Search_For_Project.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_application = True  # Marker of display of information about a search

            str_application = str(
                info_sig.request_get_application)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_application)
            srez = str_application[2:len_str - 2]  # We produce the cut of line of deletion from []
            info_application_veb = srez.split("', '")  # Line feed in the list of values of ID

            result_application = []
            for info_sig in info_application_veb:

                if info_sig == "bathrooms":
                    res_application = "Для ванных комнат"
                if info_sig == "floor":
                    res_application = "Для кухни/Напольная плитка"
                if info_sig == "apron":
                    res_application = "Для кухни/Фартук"
                if info_sig == "outdoor":
                    res_application = "Для уличного применения"
                if info_sig == "residential":
                    res_application = "Жилой интерьер"
                if info_sig == "projects":
                    res_application = "Общественные интерьеры/Проекты"

                result_application.append(res_application)

    if request_get_type_material != []:
        for info_sig in Search_For_Project.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_type_material = True  # Marker of display of information about a search

            str_type_material = str(
                info_sig.request_get_type_material)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_type_material)
            srez = str_type_material[2:len_str - 2]  # We produce the cut of line of deletion from []
            info_type_material_veb = srez.split("', '")  # Line feed in the list of values of ID

            result_type_material = []
            for info_sig in info_type_material_veb:

                if info_sig == "ceramic":
                    res_type_material = "Керамическая плитка"
                if info_sig == "porcelain":
                    res_type_material = "Керамогранит"

                result_type_material.append(res_type_material)

    return render(request, 'main/projects_materials_ukr.html', locals())


def main(request):
    manaf_main = Manufacturer.objects.get(name_manufacturer="ATLAS CONCORDE")
    manufacturer_singl_id = manaf_main.id
    session_key = request.session.session_key

    #  A record of data about the visit of web-site is beginning
    session_key = request.session.session_key
    # Checking for being of record in the base of the sessions key is beginning
    manafacturer_for_static = Manufacturer.objects.get(id=manufacturer_singl_id)
    if Log_In_Site.objects.filter(session_key=session_key).count():
        #  Record in the base of mark in track is beginning
        find_max = Eye.objects.filter(session_key=session_key)
        max_id_in = 0
        for find_single in find_max:

            if max_id_in < int(find_single.id):
                max_id_in = int(find_single.id)
        page_max_many = Eye.objects.filter(session_key=session_key,
                                           page=str(manafacturer_for_static.name_manufacturer), id=max_id_in)
        if page_max_many.count() != 0:
            for page_max in page_max_many:
                pass
            if page_max.page == str(manafacturer_for_static.name_manufacturer):
                Eye.objects.get(session_key=session_key, page=str(manafacturer_for_static.name_manufacturer),
                                id=max_id_in).delete()

        Eye.objects.create(session_key=session_key,
                           page=str(manafacturer_for_static.name_manufacturer),
                           log_in_site=Log_In_Site.objects.get(session_key=session_key),
                           locate_manafactur=True)
        #  Record in the base of mark in track is an end
    else:
        #  Record in the base of being of FTU on a web-site and creation of mark of his location - beginning
        Log_In_Site.objects.create(session_key=session_key, leng="rus")
        Eye.objects.create(session_key=session_key,
                           page=str(manafacturer_for_static.name_manufacturer),
                           log_in_site=Log_In_Site.objects.get(session_key=session_key, leng="rus"),
                           locate_manafactur=True)
        #  Record in the base of being of FTU on a web-site and creation of mark of his location - end
        # Checking for being of record in the base of the sessions key is an end
    #  A record of data about the visit of web-site is an end

    #  The signal processing on switching of language is beginning
        data = request.POST

        if data.get("submit") == "ukr":
            Log_In_Site.objects.filter(session_key=session_key).update(leng="ukr")
            return redirect('manufacturer_singl_ukr', manufacturer_singl_id_ukr=manufacturer_singl_id)
    # The signal processing on switching of language is end

    # The included in a shadow area is beginning
    data = Login_Form()
    if request.method == "POST":
        data = Login_Form(request.POST)
        if data.is_valid():
            form = data.cleaned_data
            len_user = User_Login.objects.filter(is_active_login=True, login_login=form.get("login"),
                                                 password_login=form.get("password")).count()
            if len_user > 0:
                User_Login.objects.filter(is_active_login=True, login_login=form.get("login"),
                                          password_login=form.get("password")).update(session_key_login=session_key)
                user = User_Login.objects.get(is_active_login=True, login_login=form.get("login"),
                                              password_login=form.get("password"))
                return HttpResponseRedirect(reverse("shadow"))
    # The included in a shadow area is end

    all_info_footer = Footer.objects.filter(is_active=True)
    response_view = False
    view_all_help = False
    manufacturer_singl_web = Manufacturer.objects.get(id=manufacturer_singl_id)
    result_all_collection_for_web = Collection.objects.filter(is_active_collection=True)

    # Collection on the base of PRICE GROUPS
    price_group = Price_Group.objects.filter()

    # Collection on the base of PRESENCE
    availability = Availability.objects.filter()

    request_get_application = request.GET.getlist('application')
    request_get_availability = request.GET.getlist('availability')
    request_get_price = request.GET.getlist('price')

    request_get_cancel = request.GET.getlist('cancel')
    request_get_find = request.GET.getlist('find')

    # A block of search (sectional search) is beginning
    if 'Искать' in request_get_find:
        result_search = []
        list_search = []
        result = []

        if request_get_application != []:
            for data_m in request_get_application:
                if data_m == "bathrooms":
                    res_dic = Collection_Application_For_Search.objects.filter(
                        collection_application_is_active=True,
                        collection_application_bathrooms=True,
                        name_collection__manufacturer_collection__id=manufacturer_singl_id)
                if data_m == "floor":
                    res_dic = Collection_Application_For_Search.objects.filter(
                        collection_application_is_active=True,
                        collection_application_floor=True,
                        name_collection__manufacturer_collection__id=manufacturer_singl_id)
                if data_m == "apron":
                    res_dic = Collection_Application_For_Search.objects.filter(
                        collection_application_is_active=True,
                        collection_application_apron=True,
                        name_collection__manufacturer_collection__id=manufacturer_singl_id)
                if data_m == "outdoor":
                    res_dic = Collection_Application_For_Search.objects.filter(
                        collection_application_is_active=True,
                        collection_application_outdoor=True,
                        name_collection__manufacturer_collection__id=manufacturer_singl_id)
                if data_m == "residential":
                    res_dic = Collection_Application_For_Search.objects.filter(
                        collection_application_is_active=True,
                        collection_application_residential=True,
                        name_collection__manufacturer_collection__id=manufacturer_singl_id)
                if data_m == "projects":
                    res_dic = Collection_Application_For_Search.objects.filter(
                        collection_application_is_active=True,
                        collection_application_projects=True,
                        name_collection__manufacturer_collection__id=manufacturer_singl_id)
                if res_dic.exists():
                    for res_dic_in in res_dic:
                        reformer = Collection.objects.get(id=res_dic_in.name_collection.id)
                        result.append(int(reformer.id))
            result = set(result)
            result_search.append(result)

        result = []
        if request_get_availability != []:
            for data_m in request_get_availability:
                data_for_search = Collection.objects.filter(is_active_collection=True,
                                                            availability_collection__id=data_m,
                                                            manufacturer_collection__id=manufacturer_singl_id)
                if data_for_search.exists():
                    list_search.append(data_for_search)
            for in_list in list_search:
                in_list_re = in_list.values()
                for zip in in_list_re:
                    result.append(zip["id"])
            result = set(result)
            result_search.append(result)

        result = []
        if request_get_price != []:
            for data_m in request_get_price:
                data_for_search = Collection.objects.filter(is_active_collection=True,
                                                            price_group_collection__id=data_m,
                                                            manufacturer_collection__id=manufacturer_singl_id)
                if data_for_search.exists():
                    list_search.append(data_for_search)
            for in_list in list_search:
                in_list_re = in_list.values()
                for zip in in_list_re:
                    result.append(zip["id"])
            result = set(result)
            result_search.append(result)

        result_all = []
        for alfa in result_search:
            for betta in alfa:
                result_all.append(betta)

        list_only = []
        len_resu = len(result_search)  # We get length result_search - list with the corteges of ID of collections
        for list_resu_only in result_all:  # We pass on result_all - incorporated ID from all positions of queries on a search
            if result_all.count(
                    list_resu_only) == len_resu and list_resu_only not in list_only:  # We check every element for an amount equal to all queries, if it is equal to all queries that it necessary ID
                list_only.append(list_resu_only)
        result_all = list_only
        resilt_collections_images = Collection_Image.objects.filter(is_active_collection=True,
                                                                    is_main_collection=True,
                                                                    name_collection__is_active_collection=True,
                                                                    name_collection__id__in=result_all,
                                                                    name_collection__manufacturer_collection__id=manufacturer_singl_id)

        # Stock a block in the base of result of search of collections coming from a sectional search is beginning
        #  A Subblock collecting data from the result of sectional search is beginning
        collection_for_page_manufacturer_single = Collection.objects.filter(id__in=result_all,
                                                                            manufacturer_collection__id=manufacturer_singl_id)
        list_collection = []
        list_statistica = []
        for collection_single_manafa in collection_for_page_manufacturer_single:
            list_collection.append(collection_single_manafa.id)
        # A Subblock collecting data from the result of sectional search is an end

        # A Subblock collecting data from all base of queries of sectional search on the session key and page is beginning
        if Collection.objects.filter(id__in=result_all, manufacturer_collection__id=manufacturer_singl_id).exists():
            all_statistica = Statistic_Find_Bloc.objects.filter(session_key=session_key, page="manufacturer_single")
            for statistica in all_statistica:
                list_statistica.append(statistica.collection)
        # A Subblock collecting data from all base of queries of sectional search on the session key and page is an end

        # Subblock of record in case of absence of result of sectional search in a base is beginning
        if str(list_collection) not in list_statistica and len(str(list_collection)) > 2:
            Statistic_Find_Bloc.objects.create(session_key=session_key, collection=list_collection,
                                               page="manufacturer_single")
            # Subblock of record in case of absence of result of sectional search in a base is an end
            # Stock a block in the base of result of search of collections coming from a sectional search is an end

        # Checking for a presence as a result of retrieval of data
        if resilt_collections_images.exists() == True:
            response_view = True
            # Receipt of way at the query of search
            response = str(request.get_full_path())
            # Transformation of line to the query and receipt of necessary remain of way for adding to paggination
            pach = "/manufacturer_singl/" + str(manufacturer_singl_id) + "/"
            response = response.replace(pach, "")
            create_base = Search_Manafactory_Single.objects.filter(session_key=session_key)

            if "page" not in response:
                if create_base.exists() == True:
                    Search_Manafactory_Single.objects.filter(session_key=session_key).update(response=response,
                                                                                             request_get_price=request_get_price,
                                                                                             request_get_availability=request_get_availability,
                                                                                             request_get_application=request_get_application)
                if create_base.exists() == False:
                    Search_Manafactory_Single.objects.create(session_key=session_key, response=response,
                                                             request_get_price=request_get_price,
                                                             request_get_availability=request_get_availability,
                                                             request_get_application=request_get_application)
                    Search_Diller_Otdel.objects.filter(session_key=session_key).delete()
                    Search_Manafactory.objects.filter(session_key=session_key).delete()
                    Search_For_Project.objects.filter(session_key=session_key).delete()
                    Search_Low_Addition.objects.filter(session_key=session_key).delete()
                    Search_Search.objects.filter(session_key=session_key).delete()

            # Checking for absence as a result of retrieval of data
        if resilt_collections_images.exists() == False:
            response_view = False
            resilt_collections_images = Collection_Image.objects.filter(is_active_collection=True,
                                                                        is_main_collection=True,
                                                                        name_collection__is_active_collection=True,
                                                                        name_collection__manufacturer_collection__id=manufacturer_singl_id)

        response_for_search = Search_Manafactory_Single.objects.filter(session_key=session_key)
        for response_for_web in response_for_search:
            pass

    if 'Сбросить фильтр поиска' in request_get_cancel:
        response_view = False
        resilt_collections_images = Collection_Image.objects.filter(is_active_collection=True,
                                                                    is_main_collection=True,
                                                                    name_collection__is_active_collection=True,
                                                                    name_collection__manufacturer_collection__id=manufacturer_singl_id)
        delete_base = Search_Manafactory_Single.objects.filter(session_key=session_key)

        if delete_base.exists() == True:
            delete_base.delete()
        if delete_base.exists() == False:
            pass
    # A block of search (sectional search) is an end

    if request_get_price != []:
        result_all_collection_for_web = Collection.objects.filter(id__in=result_all)
        for info_sig in Search_Manafactory_Single.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_price = True  # Marker of display of information about a search
            str_price = str(
                info_sig.request_get_price)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_price)
            srez = str_price[2:len_str - 2]  # We produce the cut of line deleting from []
            info_price_veb = srez.split("', '")  # Line feed in the list of values of ID
            info_price_veb = Price_Group.objects.filter(
                id__in=info_price_veb)  # Receipt of query from a base in accordance with a list

    if request_get_availability != []:
        result_all_collection_for_web = Collection.objects.filter(id__in=result_all)
        for info_sig in Search_Manafactory_Single.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_availability = True  # Marker of display of information about a search
            str_availability = str(
                info_sig.request_get_availability)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_availability)
            srez = str_availability[2:len_str - 2]  # We produce the cut of line deleting from []
            info_availability_veb = srez.split("', '")  # Line feed in the list of values of ID
            info_availability_veb = Availability.objects.filter(
                id__in=info_availability_veb)  # Receipt of query from a base in accordance with a list

    if request_get_application != []:
        result_all_collection_for_web = Collection.objects.filter(id__in=result_all)
        for info_sig in Search_Manafactory_Single.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_application = True  # Marker of display of information about a search
            str_application = str(
                info_sig.request_get_application)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_application)
            srez = str_application[2:len_str - 2]  # We produce the cut of line deleting from []
            info_application_veb = srez.split("', '")  # Line feed in the list of values of ID

            result_application = []
            for info_sig in info_application_veb:
                if info_sig == "bathrooms":
                    res_application = "Для ванных комнат"
                if info_sig == "floor":
                    res_application = "Для кухни/Напольная плитка"
                if info_sig == "apron":
                    res_application = "Для кухни/Фартук"
                if info_sig == "outdoor":
                    res_application = "Для уличного применения"
                if info_sig == "residential":
                    res_application = "Жилой интерьер"
                if info_sig == "projects":
                    res_application = "Общественные интерьеры/Проекты"
                result_application.append(res_application)

    # Paggination of page is beginning
    result_all_collection_for_web = result_all_collection_for_web.order_by('id')
    paginator = Paginator(result_all_collection_for_web, 24)
    page = request.GET.get('page')

    try:
        collection_web = paginator.page(page)
    except PageNotAnInteger:
        collection_web = paginator.page(1)
    except EmptyPage:
        collection_web = paginator.page(paginator.num_pages)
    # A block for additional information of amount of tiles and lower menu is beginning
    spisok_for = {}
    dict_for = []
    for asing in collection_web.object_list:
        azis = Product.objects.filter(is_active=True, collection_product__id=asing.id)
        leni = azis.count()
        # We collect all data on the type of products
        prod_type = []
        for azi in azis:
            sravnenie = Product_Type.objects.get(name_product_type=azi.product_type_product.name_product_type)
            if sravnenie not in prod_type:
                prod_type.append(sravnenie)
        spisok_for = {"id_collection": asing.id, "len_product": leni, "type_product_down": prod_type}
        dict_for.append(spisok_for)
    # A block for additional information of amount of tiles and lower menu is an end
    # Paggination of page is an end

    show_enter_shadow = True

    return render(request, 'main/main.html', locals())


def main_ukr(request):
    #  A record of data about the visit of web-site is beginning
    session_key = request.session.session_key
    # Checking for being of record in the base of the sessions key is beginning
    if Log_In_Site.objects.filter(session_key=session_key).count():
        #  Record in the base of mark in track is beginning
        find_max = Eye.objects.filter(session_key=session_key)
        max_id_in = 0
        for find_single in find_max:
            if max_id_in < int(find_single.id):
                max_id_in = int(find_single.id)
        page_max_many = Eye.objects.filter(session_key=session_key, page="Главная", id=max_id_in)
        if page_max_many.count() != 0:
            for page_max in page_max_many:
                pass
            if page_max.page == "Главная":
                Eye.objects.get(session_key=session_key, page="Главная", id=max_id_in).delete()

        Eye.objects.create(session_key=session_key,
                           page="Главная",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key))
        #  Record in the base of mark in track is an end
    else:
        #  Record in the base of being of FTU on a web-site and creation of mark of his location - beginning
        Log_In_Site.objects.create(session_key=session_key, leng="rus")
        Eye.objects.create(session_key=session_key,
                           page="Главная",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key, leng="rus"))
        #  Record in the base of being of FTU on a web-site and creation of mark of his location - end
        # Checking for being of record in the base of the sessions key is an end
        #  A record of data about the visit of web-site is an end

    #  The signal processing on switching of language is beginning
    data = request.POST
    if data.get("submit") == "rus":
        Log_In_Site.objects.filter(session_key=session_key).update(leng="rus")
        return redirect('main')
    # The signal processing on switching of language is beginning

    all_info_footer = Footer.objects.filter(is_active=True)
    img_main = For_IMG_Main.objects.filter(is_active=True)
    collection_for_main = Collection_Image.objects.filter(is_active_collection=True, is_main_collection=True,
                                                          name_collection__is_view_main=True)
    nhs = Collection_Search_NHS.objects.all()

    data = Login_Form()
    if request.method == "POST":
        data = Login_Form(request.POST)
        if data.is_valid():
            form = data.cleaned_data

            len_user = User_Login.objects.filter(is_active_login=True, login_login=form.get("login"),
                                                 password_login=form.get("password")).count()
            if len_user > 0:
                User_Login.objects.filter(is_active_login=True, login_login=form.get("login"),
                                          password_login=form.get("password")).update(session_key_login=session_key)
                user = User_Login.objects.get(is_active_login=True, login_login=form.get("login"),
                                              password_login=form.get("password"))
                return HttpResponseRedirect(reverse("shadow"))

    all_info_main = For_Main.objects.filter(is_active=True)

    for main_info in all_info_main:
        pass

    return render(request, 'main/main_ukr.html', locals())


def search(request):
    #  A record of data about the visit of web-site is beginning
    session_key = request.session.session_key
    # Checking for being of record in the base of the sessions key is beginning
    if Log_In_Site.objects.filter(session_key=session_key).count():
        #  Record in the base of mark in track is beginning
        Eye.objects.create(session_key=session_key,
                           page="Простой поиск",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key))
        #  Record in the base of mark in track is an end
    else:
        #  Record in the base of being of FTU on a web-site and creation of mark of his location - beginning
        Log_In_Site.objects.create(session_key=session_key, leng="rus")
        Eye.objects.create(session_key=session_key,
                           page="Простой поиск",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key, leng="rus"))
        #  Record in the base of being of FTU on a web-site and creation of mark of his location - end
        # Checking for being of record in the base of the sessions key is an end
    #  A record of data about the visit of web-site is an end

    #  The signal processing on switching of language is beginning
    data = request.POST
    if data.get("submit") == "ukr":
        Log_In_Site.objects.filter(session_key=session_key).update(leng="ukr")
        return redirect('search_ukr')
    # The signal processing on switching of language is beginning

    all_info_footer = Footer.objects.filter(is_active=True)

    for data in request.GET:
        pass
    keyword = str(request.GET.get("keyword"))

    list_collections = []

    manafacturer_search = Manufacturer.objects.filter(is_active=True,
                                                      name_manufacturer__icontains=keyword)  # We check and collect a producer on accordance
    if manafacturer_search.exists():  # Checking for a presence in the query of data
        for result_manafacturer in manafacturer_search:  # On one we reach the elements of producer
            result = Collection_Image.objects.filter(is_active_collection=True, is_main_collection=True,
                                                     name_collection__manufacturer_collection__name_manufacturer=result_manafacturer.name_manufacturer)
            # We process a result and conduct checking for a presence as a result or to us necessity
            if result.exists():  # Verification in the presence of result
                result_find_manafacturer = []  # We create a list in that then we bring ID of collections
                for result_single_manafacturer in result:
                    result_find_manafacturer.append(result_single_manafacturer.name_collection.id)
                # We conduct the record of result in a base
                Statistic_Find_Simple.objects.create(session_key=session_key,
                                                     find_manafacturer=result_find_manafacturer)

            for results in result:
                list_collections.append(results.id)
        send = "Найдено соответсвие по поиску "
    else:
        result = Collection_Image.objects.filter(is_active_collection=True, is_main_collection=True,
                                                 name_collection__name_collection__icontains=keyword)
        if result.exists():
            result_find_collection = []
            for result_single_collection in result:
                result_find_collection.append(result_single_collection.name_collection.id)
                list_collections.append(result_single_collection.id)
            send = "Найдено соответсвие по поиску "
            Statistic_Find_Simple.objects.create(session_key=session_key, find_collections=result_find_collection)
        else:
            send = "Не найдено соответсвие по поиску "

    # Receipt of way at the query of search
    response = str(request.get_full_path())
    # Transformation of line to the query and receipt of necessary remain of way for adding to pagination
    response = response.replace("/search/", "")
    create_base = Search_Search.objects.filter(session_key=session_key)

    if "page" not in response:
        if create_base.exists() == True:
            Search_Search.objects.filter(session_key=session_key).update(response=response)
        if create_base.exists() == False:
            Search_Search.objects.create(session_key=session_key, response=response)
            Search_Diller_Otdel.objects.filter(session_key=session_key).delete()
            Search_Manafactory.objects.filter(session_key=session_key).delete()
            Search_Manafactory_Single.objects.filter(session_key=session_key).delete()
            Search_For_Project.objects.filter(session_key=session_key).delete()
            Search_Low_Addition.objects.filter(session_key=session_key).delete()

    response_for_search = Search_Search.objects.filter(session_key=session_key)
    for response_for_web in response_for_search:
        pass

    list_collections = Collection_Image.objects.filter(id__in=list_collections)
    # Preparation to paggination
    list_collections = list_collections.order_by('id')
    # Paggination of page is beginning
    paginator = Paginator(list_collections, 24)
    page = request.GET.get('page')

    try:
        list_collections = paginator.page(page)
    except PageNotAnInteger:
        list_collections = paginator.page(1)
    except EmptyPage:
        list_collections = paginator.page(paginator.num_pages)
    # Paggination of page is an end

    return render(request, 'main/search.html', locals())


def search_ukr(request):
    #  A record of data about the visit of web-site is beginning
    session_key = request.session.session_key
    # Checking for being of record in the base of the sessions key is beginning
    if Log_In_Site.objects.filter(session_key=session_key).count():
        #  Record in the base of mark in track is beginning
        Eye.objects.create(session_key=session_key,
                           page="Простой поиск",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key))
        #  Record in the base of mark in track is an end
    else:
        #  Record in the base of being of FTU on a web-site and creation of mark of his location - beginning
        Log_In_Site.objects.create(session_key=session_key, leng="rus")
        Eye.objects.create(session_key=session_key,
                           page="Простой поиск",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key, leng="rus"))
        #  Record in the base of being of FTU on a web-site and creation of mark of his location - end
        # Checking for being of record in the base of the sessions key is an end
    #  A record of data about the visit of web-site is an end

    #  The signal processing on switching of language is beginning
    data = request.POST
    if data.get("submit") == "rus":
        Log_In_Site.objects.filter(session_key=session_key).update(leng="rus")
        return redirect('search')
    # The signal processing on switching of language is beginning

    all_info_footer = Footer.objects.filter(is_active=True)

    for data in request.GET:
        pass
    keyword = str(request.GET.get("keyword"))

    list_collections = []

    manafacturer_search = Manufacturer.objects.filter(is_active=True,
                                                      name_manufacturer__icontains=keyword)  # Проверяем и собираем производителя по соответсвию
    if manafacturer_search.exists():  # Проверка на наличие в запросе данных
        for result_manafacturer in manafacturer_search:  # Поединично достаем элементы производителя
            result = Collection_Image.objects.filter(is_active_collection=True, is_main_collection=True,
                                                     name_collection__manufacturer_collection__name_manufacturer=result_manafacturer.name_manufacturer)
            # We process a result and conduct checking for a presence as a result or to us necessity
            if result.exists():  # Verification in the presence of result
                result_find_manafacturer = []  # We create a list in that then we bring ID of collections
                for result_single_manafacturer in result:
                    result_find_manafacturer.append(result_single_manafacturer.name_collection.id)
                # We conduct the record of result in a base
                Statistic_Find_Simple.objects.create(session_key=session_key,
                                                     find_manafacturer=result_find_manafacturer)

            for results in result:
                list_collections.append(results.id)
        send = "Знайдено відповідність з пошуку "
    else:
        result = Collection_Image.objects.filter(is_active_collection=True, is_main_collection=True,
                                                 name_collection__name_collection__icontains=keyword)
        if result.exists():
            result_find_collection = []
            for result_single_collection in result:
                result_find_collection.append(result_single_collection.name_collection.id)
                list_collections.append(result_single_collection.id)
            send = "Знайдено відповідність з пошуку "
            Statistic_Find_Simple.objects.create(session_key=session_key, find_collections=result_find_collection)
        else:
            send = "Не знайдено відповідність з пошуку "

    # Receipt of way at the query of search
    response = str(request.get_full_path())
    # Transformation of line to the query and receipt of necessary remain of way for adding to pagginator
    response = response.replace("/search_ukr/", "")
    create_base = Search_Search.objects.filter(session_key=session_key)

    if "page" not in response:
        if create_base.exists() == True:
            Search_Search.objects.filter(session_key=session_key).update(response=response)
        if create_base.exists() == False:
            Search_Search.objects.create(session_key=session_key, response=response)
            Search_Diller_Otdel.objects.filter(session_key=session_key).delete()
            Search_Manafactory.objects.filter(session_key=session_key).delete()
            Search_Manafactory_Single.objects.filter(session_key=session_key).delete()
            Search_For_Project.objects.filter(session_key=session_key).delete()
            Search_Low_Addition.objects.filter(session_key=session_key).delete()

    response_for_search = Search_Search.objects.filter(session_key=session_key)
    for response_for_web in response_for_search:
        pass

    list_collections = Collection_Image.objects.filter(id__in=list_collections)
    # Preparation to paggination
    list_collections = list_collections.order_by('id')
    # Paggination of page is beginning
    paginator = Paginator(list_collections, 4)
    page = request.GET.get('page')

    try:
        list_collections = paginator.page(page)
    except PageNotAnInteger:
        list_collections = paginator.page(1)
    except EmptyPage:
        list_collections = paginator.page(paginator.num_pages)
    # Pagination of page is an end

    return render(request, 'main/search_ukr.html', locals())


def search_hight(request):
    #  A record of data about the visit of web-site is beginning
    session_key = request.session.session_key
    # Checking for being of record in the base of the sessions key is beginning
    if Log_In_Site.objects.filter(session_key=session_key).count():
        #  Record in the base of mark in track is beginning
        Eye.objects.create(session_key=session_key,
                           page="Блочный поиск",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key))
        #  Record in the base of mark in track is an end
    else:
        #  Record in the base of being of FTU on a web-site and creation of mark of his location - beginning
        Log_In_Site.objects.create(session_key=session_key, leng="rus")
        Eye.objects.create(session_key=session_key,
                           page="Блочный поиск",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key, leng="rus"))
        #  Record in the base of being of FTU on a web-site and creation of mark of his location - end
        # Checking for being of record in the base of the sessions key is an end
    #  A record of data about the visit of web-site is an end

    #  The signal processing on switching of language is beginning
    data = request.POST

    if data.get("submit") == "ukr":
        Log_In_Site.objects.filter(session_key=session_key).update(leng="ukr")
        return redirect('search_hight_ukr')
    # The signal processing on switching of language is beginning

    all_info_footer = Footer.objects.filter(is_active=True)

    view_all_help = False  # Marker for the show of information about a search (changes a value in the end)

    response_view = False

    manafacturer_search_hight = Manufacturer.objects.filter(is_active=True)

    ava = Collection_Image.objects.filter(is_main_collection=True, is_active_collection=True,
                                          name_collection__manufacturer_collection__in=manafacturer_search_hight)

    ava_product = Product_Image.objects.filter(is_main=True, is_active=True,
                                               product__collection_product__manufacturer_collection__in=manafacturer_search_hight)

    request_for_web = {}  # Creation of dictionary for the conclusion of information in description of the extended search
    list_nhs_ava = []
    list_country_ava = []
    list_price_ava = []
    list_size_ava = []
    list_availability_ava = []
    result_all = []

    marker = False  # Creation of marker
    marker_style = False
    marker_application = False
    marker_nhs = False
    marker_type_material = False
    marker_type_floor = False
    marker_texturer = False
    marker_facturer = False
    marker_colour = False
    marker_availability = False
    marker_size = False
    marker_price = False

    new_search = True

    for ava_singl in ava:
        list_nhs_ava.append(ava_singl.name_collection.name_collection_nhs)
        list_country_ava.append(ava_singl.name_collection.manufacturer_collection.manufacturer_country)
        list_price_ava.append(ava_singl.name_collection.price_group_collection)
        list_availability_ava.append(ava_singl.name_collection.availability_collection)

    for ava_singl_prod in ava_product:
        list_size_ava.append(ava_singl_prod.product.size_product)

    search_nhs = Collection_Search_NHS.objects.filter(name_collection_nhs__in=list_nhs_ava)
    country = Manufacturer_Country.objects.filter(name_manufacturer_country__in=list_country_ava)
    size = Size.objects.filter(name_size__in=list_size_ava)
    price = Price_Group.objects.filter(name_price_group__in=list_price_ava)
    availability_s = Availability.objects.filter(name_availability__in=list_availability_ava)

    application = Collection_Application_For_Search.objects.filter(name_collection__is_active_collection=True)
    style = Collection_Style_For_Search.objects.filter(name_style_collection__is_active_collection=True)
    type_material = Collection_Type_Material_For_Search.objects.filter(
        name_collection_type_material__is_active_collection=True)
    type_floor = Collection_Floor_For_Search.objects.filter(name_floor_collection__is_active_collection=True)
    texturer = Collection_Texturer_For_Search.objects.filter(name_texturer_collection__is_active_collection=True)
    facturer = Collection_Facturer_For_Search.objects.filter(name_facturer_collection__is_active_collection=True)

    resilt_collections_images = Collection_Image.objects.filter(is_active_collection=True, is_main_collection=True,
                                                                name_collection__is_active_collection=True)
    resilt_collections = Collection_Image.objects.filter(is_active_collection=True)

    request_get_nhs = request.GET.getlist('nhs')
    request_get_manafacturer = request.GET.getlist('manafacturer')
    request_get_application = request.GET.getlist('application')
    request_get_style = request.GET.getlist('style')
    request_get_country = request.GET.getlist('country')
    request_get_type_material = request.GET.getlist('type_material')
    request_get_type_floor = request.GET.getlist('type_floor')
    request_get_availability = request.GET.getlist('availability')
    request_get_texturer = request.GET.getlist('texturer')
    request_get_size = request.GET.getlist('size')
    request_get_price = request.GET.getlist('price')
    request_get_facturer = request.GET.getlist('facturer')
    request_get_colour = request.GET.getlist('colour')
    request_get_cancel = request.GET.getlist('cancel')
    request_get_find = request.GET.getlist('find')

    if 'Искать' in request_get_find:
        result_search = []
        list_search = []
        result = []
        if request_get_nhs != []:
            for data in request_get_nhs:
                data_for_search = Collection.objects.filter(is_active_collection=True, name_collection_nhs__id=data)
                if data_for_search.exists():
                    list_search.append(data_for_search)
            for in_list in list_search:
                in_list_re = in_list.values()
                for zip in in_list_re:
                    result.append(zip["id"])
            result = set(result)
            result_search.append(result)
            marker_nhs = True

        result = []
        application_prom = []
        if request_get_application != []:
            for data_m in request_get_application:
                if data_m == "bathrooms":
                    res_dic = Collection_Application_For_Search.objects.filter(collection_application_is_active=True,
                                                                               collection_application_bathrooms=True)

                    info_res = []
                    for res_in in res_dic:
                        info_res.append(Collection.objects.get(name_collection=res_in.name_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "floor":
                    res_dic = Collection_Application_For_Search.objects.filter(collection_application_is_active=True,
                                                                               collection_application_floor=True)

                    info_res = []
                    for res_in in res_dic:
                        info_res.append(Collection.objects.get(name_collection=res_in.name_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "apron":
                    res_dic = Collection_Application_For_Search.objects.filter(collection_application_is_active=True,
                                                                               collection_application_apron=True)

                    info_res = []
                    for res_in in res_dic:
                        info_res.append(Collection.objects.get(name_collection=res_in.name_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "outdoor":
                    res_dic = Collection_Application_For_Search.objects.filter(collection_application_is_active=True,
                                                                               collection_application_outdoor=True)

                    info_res = []
                    for res_in in res_dic:
                        info_res.append(Collection.objects.get(name_collection=res_in.name_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "residential":
                    res_dic = Collection_Application_For_Search.objects.filter(collection_application_is_active=True,
                                                                               collection_application_residential=True)

                    info_res = []
                    for res_in in res_dic:
                        info_res.append(Collection.objects.get(name_collection=res_in.name_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "projects":
                    res_dic = Collection_Application_For_Search.objects.filter(collection_application_is_active=True,
                                                                               collection_application_projects=True)

                    info_res = []
                    for res_in in res_dic:
                        info_res.append(Collection.objects.get(name_collection=res_in.name_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                result = []
                if res_dic.exists():
                    for res_dic_in in res_dic:
                        result.append(res_dic_in.id)
                result = set(result)
                application_prom.append(result)

                marker_application = True

        result_search.extend(application_prom)

        result = []
        style_prom = []
        if request_get_style != []:
            for data_m in request_get_style:

                if data_m == "vintage":
                    res_dic = Collection_Style_For_Search.objects.filter(collection_stile_is_active=True,
                                                                         collection_stile_vintage=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_style_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "classic":
                    res_dic = Collection_Style_For_Search.objects.filter(collection_stile_is_active=True,
                                                                         collection_stile_classic=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_style_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "modern":
                    res_dic = Collection_Style_For_Search.objects.filter(collection_stile_is_active=True,
                                                                         collection_stile_modern=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_style_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                result = []
                if res_dic.exists():
                    for res_dic_in in res_dic:
                        result.append(res_dic_in.id)
                result = set(result)
                style_prom.append(result)

                marker_style = True

        result_search.extend(style_prom)

        result = []
        type_material_prom = []
        if request_get_type_material != []:
            for data_m in request_get_type_material:
                if data_m == "grout":
                    res_dic = Collection_Type_Material_For_Search.objects.filter(
                        collection_type_material_is_active=True,
                        collection_type_material_grout=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(Collection.objects.get(
                            name_collection=res_in.name_collection_type_material.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "ceramic":
                    res_dic = Collection_Type_Material_For_Search.objects.filter(
                        collection_type_material_is_active=True,
                        collection_type_material_ceramic=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(Collection.objects.get(
                            name_collection=res_in.name_collection_type_material.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "porcelain":
                    res_dic = Collection_Type_Material_For_Search.objects.filter(
                        collection_type_material_is_active=True,
                        collection_type_material_porcelain=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(Collection.objects.get(
                            name_collection=res_in.name_collection_type_material.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "clinker":
                    res_dic = Collection_Type_Material_For_Search.objects.filter(
                        collection_type_material_is_active=True,
                        collection_type_material_clinker=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(Collection.objects.get(
                            name_collection=res_in.name_collection_type_material.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "natural":
                    res_dic = Collection_Type_Material_For_Search.objects.filter(
                        collection_type_material_is_active=True,
                        collection_type_material_natural=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(Collection.objects.get(
                            name_collection=res_in.name_collection_type_material.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "leveling":
                    res_dic = Collection_Type_Material_For_Search.objects.filter(
                        collection_type_material_is_active=True,
                        collection_type_material_leveling=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(Collection.objects.get(
                            name_collection=res_in.name_collection_type_material.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "glass":
                    res_dic = Collection_Type_Material_For_Search.objects.filter(
                        collection_type_material_is_active=True,
                        collection_type_material_glass=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(Collection.objects.get(
                            name_collection=res_in.name_collection_type_material.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "steps":
                    res_dic = Collection_Type_Material_For_Search.objects.filter(
                        collection_type_material_is_active=True,
                        collection_type_material_steps=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(Collection.objects.get(
                            name_collection=res_in.name_collection_type_material.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                result = []
                if res_dic.exists():
                    for res_dic_in in res_dic:
                        result.append(res_dic_in.id)
                result = set(result)
                type_material_prom.append(result)

                marker_type_material = True

        result_search.extend(type_material_prom)

        result = []
        type_floor_prom = []
        if request_get_type_floor != []:
            for data_m in request_get_type_floor:
                if data_m == "floor":
                    res_dic = Collection_Floor_For_Search.objects.filter(collection_floor_is_active=True,
                                                                         collection_floor_floor=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_floor_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "wall":
                    res_dic = Collection_Floor_For_Search.objects.filter(collection_floor_is_active=True,
                                                                         collection_floor_wall=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_floor_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "universal":
                    res_dic = Collection_Floor_For_Search.objects.filter(collection_floor_is_active=True,
                                                                         collection_floor_universal=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_floor_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                result = []
                if res_dic.exists():
                    for res_dic_in in res_dic:
                        result.append(res_dic_in.id)
                result = set(result)
                type_floor_prom.append(result)

                marker_type_floor = True

        result_search.extend(type_floor_prom)

        result = []
        availability_prom = []
        if request_get_availability != []:
            for data_m in request_get_availability:
                data_for_search = Collection.objects.filter(is_active_collection=True,
                                                            availability_collection__id=data_m)
                info_res = []
                for data_m in data_for_search:
                    info_res.append(data_m.id)
                availability_prom.append(info_res)
                marker_availability = True
        result_search.extend(availability_prom)

        result = []
        texturer_prom = []
        if request_get_texturer != []:
            for data_m in request_get_texturer:
                if data_m == "3d":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_3d=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_texturer_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "art":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_art=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_texturer_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "concrete":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_concrete=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_texturer_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "geometrical":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_geometrical=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_texturer_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "damaskato":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_damaskato=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_texturer_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "wood":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_wood=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_texturer_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "imitationbrick":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_imitationbrick=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_texturer_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "imitationskin":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_imitationskin=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_texturer_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "rock":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_rock=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_texturer_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "cotto":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_cotto=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_texturer_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "crackle":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_crackle=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_texturer_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "metal":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_metal=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_texturer_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "monocolor":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_monocolor=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_texturer_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "marble":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_marble=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_texturer_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "onyx":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_onyx=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_texturer_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "patchwork":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_patchwork=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_texturer_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "cloth":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_cloth=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_texturer_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "travertine":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_travertine=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_texturer_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "flowers":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_flowers=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_texturer_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "ethnic":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_ethnic=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_texturer_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                result = []
                if res_dic.exists():
                    for res_dic_in in res_dic:
                        result.append(res_dic_in.id)
                result = set(result)
                texturer_prom.append(result)
                marker_texturer = True

        result_search.extend(texturer_prom)

        result = []
        perem_seach = []
        size_prom = []
        if request_get_size != []:
            for data_m in request_get_size:
                data_for_search_product = Product_Image.objects.filter(is_active=True, is_main=True,
                                                                       product__size_product__id=data_m)
                perem_seach = []
                for data_in_prod in data_for_search_product:
                    perem = data_in_prod.product.collection_product.id
                    perem_seach.append(perem)
                result_size = []
                for perem in perem_seach:
                    if perem not in result_size:
                        result_size.append(perem)
                        marker_size = True
                result_size = set(result_size)
                size_prom.append(result_size)
            result_search.extend(size_prom)

        result = []
        price_prom = []
        if request_get_price != []:
            for data_m in request_get_price:
                data_for_search = Collection.objects.filter(is_active_collection=True,
                                                            price_group_collection__id=data_m)
                perem_seach = []
                for data_in in data_for_search:
                    perem_seach.append(data_in.id)
                    marker_price = True
                perem_seach = set(perem_seach)
                price_prom.append(perem_seach)
            result_search.extend(price_prom)

        result = []
        facturer_prom = []
        if request_get_facturer != []:
            for data_m in request_get_facturer:
                if data_m == "glossy":
                    res_dic = Collection_Facturer_For_Search.objects.filter(collection_facturer_is_active=True,
                                                                            collection_stile_glossy=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_facturer_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "matte":
                    res_dic = Collection_Facturer_For_Search.objects.filter(collection_facturer_is_active=True,
                                                                            collection_stile_matte=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_facturer_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "polished":
                    res_dic = Collection_Facturer_For_Search.objects.filter(collection_facturer_is_active=True,
                                                                            collection_stile_polished=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_facturer_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "polopolarized":
                    res_dic = Collection_Facturer_For_Search.objects.filter(collection_facturer_is_active=True,
                                                                            collection_stile_polopolarized=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_facturer_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "satin":
                    res_dic = Collection_Facturer_For_Search.objects.filter(collection_facturer_is_active=True,
                                                                            collection_stile_satin=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_facturer_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "aged":
                    res_dic = Collection_Facturer_For_Search.objects.filter(collection_facturer_is_active=True,
                                                                            collection_stile_aged=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_facturer_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "structured":
                    res_dic = Collection_Facturer_For_Search.objects.filter(collection_facturer_is_active=True,
                                                                            collection_stile_structured=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_facturer_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                result = []
                if res_dic.exists():
                    for res_dic_in in res_dic:
                        result.append(res_dic_in.id)
                result = set(result)
                facturer_prom.append(result)

                marker_facturer = True

        result_search.extend(facturer_prom)

        result = []
        colour_prom = []
        if request_get_colour != []:
            for data_m in request_get_colour:
                if data_m == "beige":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_beige=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_colour_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "white":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_white=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_colour_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "burgundy":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_burgundy=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_colour_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "blue":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_blue=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_colour_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "yellow":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_yellow=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_colour_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "green":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_green=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_colour_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "gold":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_gold=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_colour_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "brown":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_brown=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_colour_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "red":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_red=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_colour_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "multicolor":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_multicolor=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_colour_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "orange":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_orange=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_colour_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "pink":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_pink=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_colour_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "silver_platinum":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_silver_platinum=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_colour_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "silver_grey":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_silver_grey=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_colour_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "silver_darkblue":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_silver_darkblue=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_colour_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "silver_lilac":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_silver_lilac=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_colour_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                if data_m == "silver_black":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_silver_black=True)
                    info_res = []
                    for res_in in res_dic:
                        info_res.append(
                            Collection.objects.get(name_collection=res_in.name_colour_collection.name_collection))
                    res_dic = Collection.objects.filter(name_collection__in=info_res)

                result = []
                if res_dic.exists():
                    for res_dic_in in res_dic:
                        result.append(res_dic_in.id)
                result = set(result)
                colour_prom.append(result)
                marker_colour = True
        result_search.extend(colour_prom)

        result_all = []
        for alfa in result_search:
            for betta in alfa:
                result_all.append(betta)
        list_only = []
        len_resu = len(result_search)  # We get length result_search - list with the corteges of ID of collections

        for list_resu_only in result_all:  # We pass on result_all - incorporated ID from all positions of queries on a search
            if result_all.count(
                    list_resu_only) == len_resu and list_resu_only not in list_only:  # We check every element for an amount equal to all queries, if it is equal to all queries that it necessary ID
                list_only.append(list_resu_only)

        result_all = list_only

        resilt_collections = Collection.objects.filter(is_active_collection=True, id__in=result_all)

        # Stock a block in the base of result of search of collections coming from a sectional search is beginning
        # A Subblock collecting data from the result of sectional search is beginning
        collections_search_hight = Collection.objects.filter(id__in=result_all)
        list_collection = []
        list_statistica = []
        for collection_search_hight in collections_search_hight:
            list_collection.append(collection_search_hight.id)
        # A Subblock collecting data from the result of sectional search is an end

        # A Subblock collecting data from all base of queries of sectional search on the sessions key and page is beginning
        if Collection.objects.filter(id__in=result_all).exists():
            all_statistica = Statistic_Find_Bloc.objects.filter(session_key=session_key, page="search_hight")
            for statistica in all_statistica:
                list_statistica.append(statistica.collection)
        # A Subblock collecting data from all base of queries of sectional search on the sessions key and page is an end

        # Subblock of record in case of absence of result of sectional search in a base is beginning
        if str(list_collection) not in list_statistica and len(str(list_collection)) > 2:
            Statistic_Find_Bloc.objects.create(session_key=session_key, collection=list_collection,
                                               page="search_hight")
        # Subblock of record in case of absence of result of sectional search in a base is an end

        # Stock a block in the base of result of search of collections coming from a sectional search is an end

        # Checking for a presence as a result of retrieval of data
        if marker_style == True or marker_application == True or marker_nhs == True or marker_type_material == True \
                or marker_type_floor == True or marker_texturer == True or marker_facturer == True or marker_colour == True \
                or marker_availability == True or marker_size == True or marker_price == True:
            response_view = True
            # Receipt of way at the query of search
            response = str(request.get_full_path())
            # Transformation of line to the query and receipt of necessary remain of way for adding to paggination
            response = response.replace("/search_hight/", "")
            create_base = Search_Low_Addition.objects.filter(session_key=session_key)

            if "page" not in response:
                if create_base.exists() == True:
                    Search_Low_Addition.objects.filter(session_key=session_key).update(response=response,
                                                                                       request_get_nhs=request_get_nhs,
                                                                                       request_get_manafacturer=request_get_manafacturer,
                                                                                       request_get_size=request_get_size,
                                                                                       request_get_country=request_get_country,
                                                                                       request_get_price=request_get_price,
                                                                                       request_get_availability=request_get_availability,
                                                                                       request_get_colour=request_get_colour,
                                                                                       request_get_facturer=request_get_facturer,
                                                                                       request_get_texturer=request_get_texturer,
                                                                                       request_get_application=request_get_application,
                                                                                       request_get_style=request_get_style,
                                                                                       request_get_type_material=request_get_type_material,
                                                                                       request_get_type_floor=request_get_type_floor)
                if create_base.exists() == False:
                    Search_Low_Addition.objects.create(session_key=session_key, response=response,
                                                       request_get_nhs=request_get_nhs,
                                                       request_get_manafacturer=request_get_manafacturer,
                                                       request_get_size=request_get_size,
                                                       request_get_country=request_get_country,
                                                       request_get_price=request_get_price,
                                                       request_get_availability=request_get_availability,
                                                       request_get_colour=request_get_colour,
                                                       request_get_facturer=request_get_facturer,
                                                       request_get_texturer=request_get_texturer,
                                                       request_get_application=request_get_application,
                                                       request_get_style=request_get_style,
                                                       request_get_type_material=request_get_type_material,
                                                       request_get_type_floor=request_get_type_floor)
                    Search_Diller_Otdel.objects.filter(session_key=session_key).delete()
                    Search_Manafactory.objects.filter(session_key=session_key).delete()
                    Search_Manafactory_Single.objects.filter(session_key=session_key).delete()
                    Search_For_Project.objects.filter(session_key=session_key).delete()
                    Search_Search.objects.filter(session_key=session_key).delete()

        # Checking for absence as a result of retrieval of data

        if resilt_collections.exists() == False:
            response_view = False
            resilt_collections = Collection.objects.filter(is_active_collection=True)

        response_for_search = Search_Low_Addition.objects.filter(session_key=session_key)
        for response_for_web in response_for_search:
            pass

    if 'Сбросить фильтр поиска' in request_get_cancel:
        response_view = False
        resilt_collections = Collection.objects.filter(is_active_collection=True)
        delete_base = Search_Low_Addition.objects.filter(session_key=session_key)

        if delete_base.exists() == True:
            delete_base.delete()
        if delete_base.exists() == False:
            pass

    # Preparation to paggination
    if result_all == []:  # Denotation of markers in default of collections at a search
        view_all_help = True
        marker = True
    resilt_collections_images = Collection_Image.objects.filter(is_main_collection=True, is_active_collection=True,
                                                                name_collection__id__in=result_all)
    resilt_collections_images = resilt_collections_images.order_by('id')
    # Paggination of page is beginning
    paginator = Paginator(resilt_collections_images, 24)
    page = request.GET.get('page')

    try:
        resilt_collections_images = paginator.page(page)
    except PageNotAnInteger:
        resilt_collections_images = paginator.page(1)
    except EmptyPage:
        resilt_collections_images = paginator.page(paginator.num_pages)
    # Paggination of page is an end

    if request_get_nhs != []:
        new_search = False  # A marker is a new page or no
        view_all_help = True  # Marker of display of information about a search
        view_all_nhs = True  # Marker of display of information about a search
        for info_sig in Search_Low_Addition.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search

            str_info = str(
                info_sig.request_get_nhs)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_info)
            srez = str_info[2:len_str - 2]  # We produce the cut of line deleting from []
            info_nhs_veb = srez.split("', '")  # Line feed in the list of values of ID
            info_nhs_veb = Collection_Search_NHS.objects.filter(
                id__in=info_nhs_veb)  # Receipt of query from a base in accordance with a list

    if request_get_manafacturer != []:
        for info_sig in Search_Low_Addition.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_manafacturer = True  # Marker of display of information about a search
            str_manafacturer = str(
                info_sig.request_get_manafacturer)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_manafacturer)
            srez = str_manafacturer[2:len_str - 2]  # We produce the cut of line deleting from []
            info_manafacturer_veb = srez.split("', '")  # Line feed in the list of values of ID
            info_manafacturer_veb = Manufacturer.objects.filter(
                id__in=info_manafacturer_veb)  # Receipt of query from a base in accordance with a list

    if request_get_size != []:
        new_search = False  # A marker is a new page or no
        view_all_help = True  # Marker of display of information about a search
        view_all_size = True  # Marker of display of information about a search
        for info_sig in Search_Low_Addition.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_size = True  # Marker of display of information about a search
            str_size = str(
                info_sig.request_get_size)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_size)
            srez = str_size[2:len_str - 2]  # We produce the cut of line deleting from []
            info_size_veb = srez.split("', '")  # Line feed in the list of values of ID
            info_size_veb = Size.objects.filter(
                id__in=info_size_veb)  # Receipt of query from a base in accordance with a list

    if request_get_country != []:
        for info_sig in Search_Low_Addition.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_country = True  # Marker of display of information about a search
            str_country = str(
                info_sig.request_get_country)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_country)
            srez = str_country[2:len_str - 2]  # We produce the cut of line deleting from []
            info_country_veb = srez.split("', '")  # Line feed in the list of values of ID
            info_country_veb = Manufacturer_Country.objects.filter(
                id__in=info_country_veb)  # Receipt of query from a base in accordance with a list

    if request_get_price != []:
        new_search = False  # A marker is a new page or no
        view_all_help = True  # Marker of display of information about a search
        view_all_price = True  # Marker of display of information about a search
        for info_sig in Search_Low_Addition.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_price = True  # Marker of display of information about a search
            str_price = str(
                info_sig.request_get_price)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_price)
            srez = str_price[2:len_str - 2]  # We produce the cut of line deleting from []
            info_price_veb = srez.split("', '")  # Line feed in the list of values of ID
            info_price_veb = Price_Group.objects.filter(
                id__in=info_price_veb)  # Receipt of query from a base in accordance with a list

    if request_get_availability != []:
        new_search = False  # A marker is a new page or no
        view_all_help = True  # Marker of display of information about a search
        view_all_availability = True  # Marker of display of information about a search
        for info_sig in Search_Low_Addition.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_availability = True  # Marker of display of information about a search
            str_availability = str(
                info_sig.request_get_availability)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_availability)
            srez = str_availability[2:len_str - 2]  # We produce the cut of line deleting from []
            info_availability_veb = srez.split("', '")  # Line feed in the list of values of ID
            info_availability_veb = Availability.objects.filter(
                id__in=info_availability_veb)  # Receipt of query from a base in accordance with a list

    if request_get_colour != []:
        new_search = False  # A marker is a new page or no
        view_all_help = True  # Marker of display of information about a search
        view_all_colour = True  # Marker of display of information about a search
        for info_sig in Search_Low_Addition.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_colour = True  # Marker of display of information about a search

            str_colour = str(
                info_sig.request_get_colour)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_colour)
            srez = str_colour[2:len_str - 2]  # We produce the cut of line deleting from []
            info_colour_veb = srez.split("', '")  # Line feed in the list of values of ID

            result_colour = []
            for info_sig in info_colour_veb:
                if info_sig == "beige":
                    res_colour = "Бежевый"
                if info_sig == "white":
                    res_colour = "Белый"
                if info_sig == "burgundy":
                    res_colour = "Бордовый"
                if info_sig == "blue":
                    res_colour = "Голубой"
                if info_sig == "yellow":
                    res_colour = "Желтый"
                if info_sig == "green":
                    res_colour = "Зеленый"
                if info_sig == "gold":
                    res_colour = "Золотой"
                if info_sig == "brown":
                    res_colour = "Коричневый"
                if info_sig == "red":
                    res_colour = "Красный"
                if info_sig == "multicolor":
                    res_colour = "Мультиколор"
                if info_sig == "orange":
                    res_colour = "Оранжевый"
                if info_sig == "pink":
                    res_colour = "Розовый"
                if info_sig == "silver_platinum":
                    res_colour = "Серебряный/Платина"
                if info_sig == "silver_grey":
                    res_colour = "Серый"
                if info_sig == "silver_darkblue":
                    res_colour = "Синий"
                if info_sig == "silver_lilac":
                    res_colour = "Сиреневый"
                if info_sig == "silver_black":
                    res_colour = "Черный"

                result_colour.append(res_colour)

    if request_get_facturer != []:
        new_search = False  # A marker is a new page or no
        view_all_help = True  # Marker of display of information about a search
        view_all_facturer = True  # Marker of display of information about a search
        for info_sig in Search_Low_Addition.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_facturer = True  # Marker of display of information about a search

            str_facturer = str(
                info_sig.request_get_facturer)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_facturer)
            srez = str_facturer[2:len_str - 2]  # We produce the cut of line deleting from []
            info_facturer_veb = srez.split("', '")  # Line feed in the list of values of ID

            result_facturer = []
            for info_sig in info_facturer_veb:
                if info_sig == "glossy":
                    res_facturer = "Глянцевая/Настенная"
                if info_sig == "matte":
                    res_facturer = "Матовая"
                if info_sig == "polished":
                    res_facturer = "Полированная"
                if info_sig == "polopolarized":
                    res_facturer = "Полуполированная/Лапатированная"
                if info_sig == "satin":
                    res_facturer = "Сатинированная"
                if info_sig == "aged":
                    res_facturer = "Состаренная/Рустичная"
                if info_sig == "structured":
                    res_facturer = "Структурированная/Рельефная"

                result_facturer.append(res_facturer)

    if request_get_texturer != []:
        new_search = False  # A marker is a new page or no
        view_all_help = True  # Marker of display of information about a search
        view_all_texturer = True  # Marker of display of information about a search

        for info_sig in Search_Low_Addition.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_texturer = True  # Marker of display of information about a search

            str_texturer = str(
                info_sig.request_get_texturer)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_texturer)
            srez = str_texturer[2:len_str - 2]  # We produce the cut of line deleting from []
            info_texturer_veb = srez.split("', '")  # Line feed in the list of values of ID

            result_texturer = []
            for info_sig in info_texturer_veb:

                if info_sig == "3d":
                    res_texturer = "3D/Трехмерная"
                if info_sig == "art":
                    res_texturer = "Арт"
                if info_sig == "concrete":
                    res_texturer = "Бетон/Цемент/Штукатурка"
                if info_sig == "geometrical":
                    res_texturer = "Геометрический рисунок"
                if info_sig == "damaskato":
                    res_texturer = "Дамаскато/Вензеля"
                if info_sig == "wood":
                    res_texturer = "Дерево/Керамический паркет"
                if info_sig == "imitationbrick":
                    res_texturer = "Имитация кирпичной кладки"
                if info_sig == "imitationskin":
                    res_texturer = "Имитация кожи"
                if info_sig == "rock":
                    res_texturer = "Камень"
                if info_sig == "cotto":
                    res_texturer = "Котто/имитация"
                if info_sig == "crackle":
                    res_texturer = "Кракле"
                if info_sig == "metal":
                    res_texturer = "Металл"
                if info_sig == "monocolor":
                    res_texturer = "Моноколор"
                if info_sig == "marble":
                    res_texturer = "Мрамор"
                if info_sig == "onyx":
                    res_texturer = "Оникс"
                if info_sig == "patchwork":
                    res_texturer = "Патчворк"
                if info_sig == "cloth":
                    res_texturer = "Ткань"
                if info_sig == "travertine":
                    res_texturer = "Травертин"
                if info_sig == "flowers":
                    res_texturer = "Цветы/Растения"
                if info_sig == "ethnic":
                    res_texturer = "Этнический рисунок"

                result_texturer.append(res_texturer)

    if request_get_application != []:
        new_search = False  # A marker is a new page or no
        view_all_help = True  # Marker of display of information about a search
        view_all_application = True  # Marker of display of information about a search

        for info_sig in Search_Low_Addition.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search

            str_application = str(
                info_sig.request_get_application)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_application)
            srez = str_application[2:len_str - 2]  # We produce the cut of line deleting from []
            info_application_veb = srez.split("', '")  # Line feed in the list of values of ID

            result_application = []
            for info_sig in info_application_veb:

                if info_sig == "bathrooms":
                    res_application = "Для ванных комнат"
                if info_sig == "floor":
                    res_application = "Для кухни/Напольная плитка"
                if info_sig == "apron":
                    res_application = "Для кухни/Фартук"
                if info_sig == "outdoor":
                    res_application = "Для уличного применения"
                if info_sig == "residential":
                    res_application = "Жилой интерьер"
                if info_sig == "projects":
                    res_application = "Общественные интерьеры/Проекты"

                result_application.append(res_application)

    if request_get_style != []:
        new_search = False  # A marker is a new page or no
        view_all_help = True  # Marker of display of information about a search
        view_all_style = True  # Marker of display of information about a search

        for info_sig in Search_Low_Addition.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search

            str_style = str(
                info_sig.request_get_style)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_style)
            srez = str_style[2:len_str - 2]  # We produce the cut of line deleting from []
            info_style_veb = srez.split("', '")  # Line feed in the list of values of ID

            result_style = []
            for info_sig in info_style_veb:
                if info_sig == "vintage":
                    res_style = "Винтаж"
                if info_sig == "classic":
                    res_style = "Классика"
                if info_sig == "modern":
                    res_style = "Современный"
                result_style.append(res_style)

    if request_get_type_material != []:
        new_search = False  # A marker is a new page or no
        view_all_help = True  # Marker of display of information about a search
        view_all_type_material = True  # Marker of display of information about a search
        for info_sig in Search_Low_Addition.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search

            str_type_material = str(
                info_sig.request_get_type_material)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_type_material)
            srez = str_type_material[2:len_str - 2]  # We produce the cut of line deleting from []
            info_type_material_veb = srez.split("', '")  # Line feed in the list of values of ID

            result_type_material = []
            for info_sig in info_type_material_veb:

                if info_sig == "grout":
                    res_type_material = "Затирка/Клей/Строительная химия"
                if info_sig == "ceramic":
                    res_type_material = "Керамическая плитка"
                if info_sig == "porcelain":
                    res_type_material = "Керамогранит"
                if info_sig == "clinker":
                    res_type_material = "Клинкерная плитка"
                if info_sig == "natural":
                    res_type_material = "Натуральный камень"
                if info_sig == "leveling":
                    res_type_material = "Система выравнивания плитки"
                if info_sig == "glass":
                    res_type_material = "Стеклянная мозаика"
                if info_sig == "steps":
                    res_type_material = "Ступени"

                result_type_material.append(res_type_material)

    if request_get_type_floor != []:
        new_search = False  # A marker is a new page or no
        view_all_help = True  # Marker of display of information about a search
        view_all_type_floor = True  # Marker of display of information about a search
        for info_sig in Search_Low_Addition.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search

            str_type_floor = str(
                info_sig.request_get_type_floor)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_type_floor)
            srez = str_type_floor[2:len_str - 2]  # We produce the cut of line deleting from []
            info_type_floor_veb = srez.split("', '")  # Line feed in the list of values of ID

            result_type_floor = []
            for info_sig in info_type_floor_veb:

                if info_sig == "floor":
                    res_type_floor = "Для пола"
                if info_sig == "wall":
                    res_type_floor = "Для стен"
                if info_sig == "universal":
                    res_type_floor = "Универсальная"

                result_type_floor.append(res_type_floor)

    return render(request, 'main/search_hight.html', locals())


def search_hight_ukr(request):
    #  A record of data about the visit of web-site is beginning
    session_key = request.session.session_key
    # Checking for being of record in the base of the sessions key is beginning
    if Log_In_Site.objects.filter(session_key=session_key).count():
        # Record in the base of mark in track is beginning
        Eye.objects.create(session_key=session_key,
                           page="Блочный поиск",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key))
        # Record in the base of mark in track is an end
    else:
        # Record in the base of being of FTU on a web-site and creation of mark of his location - beginning
        Log_In_Site.objects.create(session_key=session_key, leng="rus")
        Eye.objects.create(session_key=session_key,
                           page="Блочный поиск",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key, leng="rus"))
        # Record in the base of being of FTU on a web-site and creation of mark of his location - end
        # Checking for being of record in the base of the sessions key is an end
    #  A record of data about the visit of web-site is an end

    #  The signal processing on switching of language is beginning
    data = request.POST
    if data.get("submit") == "rus":
        Log_In_Site.objects.filter(session_key=session_key).update(leng="rus")
        return redirect('search_hight')
    # The signal processing on switching of language is beginning

    all_info_footer = Footer.objects.filter(is_active=True)

    view_all_help = False  # Marker for the show of information about a search (changes a value in the end)

    response_view = False

    manafacturer_search_hight = Manufacturer.objects.filter(is_active=True)

    ava = Collection_Image.objects.filter(is_main_collection=True, is_active_collection=True,
                                          name_collection__manufacturer_collection__in=manafacturer_search_hight)

    ava_product = Product_Image.objects.filter(is_main=True, is_active=True,
                                               product__collection_product__manufacturer_collection__in=manafacturer_search_hight)

    request_for_web = {}  # Creation of dictionary for the conclusion of information in description of the extended search
    list_nhs_ava = []
    list_country_ava = []
    list_price_ava = []
    list_size_ava = []
    list_availability_ava = []
    for ava_singl in ava:
        list_nhs_ava.append(ava_singl.name_collection.name_collection_nhs)
        list_country_ava.append(ava_singl.name_collection.manufacturer_collection.manufacturer_country)
        list_price_ava.append(ava_singl.name_collection.price_group_collection)
        list_availability_ava.append(ava_singl.name_collection.availability_collection)

    for ava_singl_prod in ava_product:
        list_size_ava.append(ava_singl_prod.product.size_product)

    search_nhs = Collection_Search_NHS.objects.filter(name_collection_nhs__in=list_nhs_ava)
    country = Manufacturer_Country.objects.filter(name_manufacturer_country__in=list_country_ava)
    size = Size.objects.filter(name_size__in=list_size_ava)
    price = Price_Group.objects.filter(name_price_group__in=list_price_ava)
    availability_s = Availability.objects.filter(name_availability__in=list_availability_ava)

    application = Collection_Application_For_Search.objects.filter(name_collection__is_active_collection=True)
    style = Collection_Style_For_Search.objects.filter(name_style_collection__is_active_collection=True)
    type_material = Collection_Type_Material_For_Search.objects.filter(
        name_collection_type_material__is_active_collection=True)
    type_floor = Collection_Floor_For_Search.objects.filter(name_floor_collection__is_active_collection=True)
    texturer = Collection_Texturer_For_Search.objects.filter(name_texturer_collection__is_active_collection=True)
    facturer = Collection_Facturer_For_Search.objects.filter(name_facturer_collection__is_active_collection=True)

    resilt_collections_images = Collection_Image.objects.filter(is_active_collection=True, is_main_collection=True,
                                                                name_collection__is_active_collection=True)

    request_get_nhs = request.GET.getlist('nhs')
    request_get_manafacturer = request.GET.getlist('manafacturer')
    request_get_application = request.GET.getlist('application')
    request_get_style = request.GET.getlist('style')
    request_get_country = request.GET.getlist('country')
    request_get_type_material = request.GET.getlist('type_material')
    request_get_type_floor = request.GET.getlist('type_floor')
    request_get_availability = request.GET.getlist('availability')
    request_get_texturer = request.GET.getlist('texturer')
    request_get_size = request.GET.getlist('size')
    request_get_price = request.GET.getlist('price')
    request_get_facturer = request.GET.getlist('facturer')
    request_get_colour = request.GET.getlist('colour')
    request_get_cancel = request.GET.getlist('cancel')
    request_get_find = request.GET.getlist('find')

    if 'Шукати' in request_get_find:
        result_search = []
        list_search = []
        result = []
        if request_get_nhs != []:
            for data in request_get_nhs:
                data_for_search = Collection.objects.filter(is_active_collection=True, name_collection_nhs__id=data)
                if data_for_search.exists():
                    list_search.append(data_for_search)
            for in_list in list_search:
                in_list_re = in_list.values()
                for zip in in_list_re:
                    result.append(zip["id"])
            result = set(result)
            result_search.append(result)

        list_search = []
        result = []
        if request_get_manafacturer != []:
            for data_m in request_get_manafacturer:
                data_for_search = Collection.objects.filter(is_active_collection=True,
                                                            manufacturer_collection__id=data_m)
                if data_for_search.exists():
                    list_search.append(data_for_search)
            for in_list in list_search:
                in_list_re = in_list.values()
                for zip in in_list_re:
                    result.append(zip["id"])
            result = set(result)
            result_search.append(result)

        result = []
        if request_get_application != []:
            for data_m in request_get_application:
                if data_m == "bathrooms":
                    res_dic = Collection_Application_For_Search.objects.filter(collection_application_is_active=True,
                                                                               collection_application_bathrooms=True)
                if data_m == "floor":
                    res_dic = Collection_Application_For_Search.objects.filter(collection_application_is_active=True,
                                                                               collection_application_floor=True)
                if data_m == "apron":
                    res_dic = Collection_Application_For_Search.objects.filter(collection_application_is_active=True,
                                                                               collection_application_apron=True)
                if data_m == "outdoor":
                    res_dic = Collection_Application_For_Search.objects.filter(collection_application_is_active=True,
                                                                               collection_application_outdoor=True)
                if data_m == "residential":
                    res_dic = Collection_Application_For_Search.objects.filter(collection_application_is_active=True,
                                                                               collection_application_residential=True)
                if data_m == "projects":
                    res_dic = Collection_Application_For_Search.objects.filter(collection_application_is_active=True,
                                                                               collection_application_projects=True)
                if res_dic.exists():
                    for res_dic_in in res_dic:
                        result.append(res_dic_in.id)
            result = set(result)
            result_search.append(result)

        result = []
        if request_get_style != []:
            for data_m in request_get_style:
                if data_m == "vintage":
                    res_dic = Collection_Style_For_Search.objects.filter(collection_stile_is_active=True,
                                                                         collection_stile_vintage=True)
                if data_m == "classic":
                    res_dic = Collection_Style_For_Search.objects.filter(collection_stile_is_active=True,
                                                                         collection_stile_classic=True)
                if data_m == "modern":
                    res_dic = Collection_Style_For_Search.objects.filter(collection_stile_is_active=True,
                                                                         collection_stile_modern=True)
                if res_dic.exists():
                    for res_dic_in in res_dic:
                        result.append(res_dic_in.id)
            result = set(result)
            result_search.append(result)

        result = []
        if request_get_country != []:
            for data_m in request_get_country:
                data_for_search = Collection.objects.filter(is_active_collection=True,
                                                            manufacturer_collection__manufacturer_country__id=data_m)
                if data_for_search.exists():
                    list_search.append(data_for_search)
            for in_list in list_search:
                in_list_re = in_list.values()
                for zip in in_list_re:
                    result.append(zip["id"])
            result = set(result)
            result_search.append(result)

        result = []
        if request_get_type_material != []:
            for data_m in request_get_type_material:
                if data_m == "grout":
                    res_dic = Collection_Type_Material_For_Search.objects.filter(
                        collection_type_material_is_active=True,
                        collection_type_material_grout=True)
                if data_m == "ceramic":
                    res_dic = Collection_Type_Material_For_Search.objects.filter(
                        collection_type_material_is_active=True,
                        collection_type_material_ceramic=True)
                if data_m == "porcelain":
                    res_dic = Collection_Type_Material_For_Search.objects.filter(
                        collection_type_material_is_active=True,
                        collection_type_material_porcelain=True)
                if data_m == "clinker":
                    res_dic = Collection_Type_Material_For_Search.objects.filter(
                        collection_type_material_is_active=True,
                        collection_type_material_clinker=True)
                if data_m == "natural":
                    res_dic = Collection_Type_Material_For_Search.objects.filter(
                        collection_type_material_is_active=True,
                        collection_type_material_natural=True)
                if data_m == "leveling":
                    res_dic = Collection_Type_Material_For_Search.objects.filter(
                        collection_type_material_is_active=True,
                        collection_type_material_leveling=True)
                if data_m == "glass":
                    res_dic = Collection_Type_Material_For_Search.objects.filter(
                        collection_type_material_is_active=True,
                        collection_type_material_glass=True)
                if data_m == "steps":
                    res_dic = Collection_Type_Material_For_Search.objects.filter(
                        collection_type_material_is_active=True,
                        collection_type_material_steps=True)

                if res_dic.exists():
                    for res_dic_in in res_dic:
                        result.append(res_dic_in.id)
            result = set(result)
            result_search.append(result)

        result = []
        for data_m in request_get_type_floor:
            if data_m == "floor":
                res_dic = Collection_Floor_For_Search.objects.filter(collection_floor_is_active=True,
                                                                     collection_floor_floor=True)
            if data_m == "wall":
                res_dic = Collection_Floor_For_Search.objects.filter(collection_floor_is_active=True,
                                                                     collection_floor_wall=True)
            if data_m == "universal":
                res_dic = Collection_Floor_For_Search.objects.filter(collection_floor_is_active=True,
                                                                     collection_floor_universal=True)
            if res_dic.exists():
                for res_dic_in in res_dic:
                    result.append(res_dic_in.id)
        if request_get_type_floor != []:
            result = set(result)
            result_search.append(result)

        result = []
        if request_get_availability != []:
            for data_m in request_get_availability:
                data_for_search = Collection.objects.filter(is_active_collection=True,
                                                            availability_collection__id=data_m)
                if data_for_search.exists():
                    list_search.append(data_for_search)
            for in_list in list_search:
                in_list_re = in_list.values()
                for zip in in_list_re:
                    result.append(zip["id"])
            result = set(result)
            result_search.append(result)

        result = []
        if request_get_texturer != []:
            for data_m in request_get_texturer:
                if data_m == "3d":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_3d=True)
                if data_m == "art":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_art=True)
                if data_m == "concrete":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_concrete=True)
                if data_m == "geometrical":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_geometrical=True)
                if data_m == "damaskato":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_damaskato=True)
                if data_m == "wood":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_wood=True)
                if data_m == "imitationbrick":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_imitationbrick=True)
                if data_m == "imitationskin":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_imitationskin=True)
                if data_m == "rock":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_rock=True)
                if data_m == "cotto":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_cotto=True)
                if data_m == "crackle":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_crackle=True)
                if data_m == "metal":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_metal=True)
                if data_m == "monocolor":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_monocolor=True)
                if data_m == "marble":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_marble=True)
                if data_m == "onyx":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_onyx=True)
                if data_m == "patchwork":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_patchwork=True)
                if data_m == "cloth":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_cloth=True)
                if data_m == "travertine":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_travertine=True)
                if data_m == "flowers":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_flowers=True)
                if data_m == "ethnic":
                    res_dic = Collection_Texturer_For_Search.objects.filter(collection_texturer_is_active=True,
                                                                            collection_texturer_ethnic=True)
                if res_dic.exists():
                    for res_dic_in in res_dic:
                        result.append(res_dic_in.id)
            result = set(result)
            result_search.append(result)

        result = []
        perem_seach = []
        if request_get_size != []:
            for data_m in request_get_size:
                data_for_search_product = Product_Image.objects.filter(is_active=True, is_main=True,
                                                                       product__size_product__id=data_m)
                for data_in_prod in data_for_search_product:
                    if data_in_prod.product.collection_product.id != None:
                        perem = data_in_prod.product.collection_product.id
                        perem_seach.append(perem)
            perem_seach = set(perem_seach)
            result_search.append(perem_seach)

        result = []
        if request_get_price != []:
            for data_m in request_get_price:
                data_for_search = Collection.objects.filter(is_active_collection=True,
                                                            price_group_collection__id=data_m)
                if data_for_search.exists():
                    list_search.append(data_for_search)
            for in_list in list_search:
                in_list_re = in_list.values()
                for zip in in_list_re:
                    result.append(zip["id"])
            result = set(result)
            result_search.append(result)

        result = []
        if request_get_facturer != []:
            for data_m in request_get_facturer:
                if data_m == "glossy":
                    res_dic = Collection_Facturer_For_Search.objects.filter(collection_facturer_is_active=True,
                                                                            collection_stile_glossy=True)
                if data_m == "matte":
                    res_dic = Collection_Facturer_For_Search.objects.filter(collection_facturer_is_active=True,
                                                                            collection_stile_matte=True)
                if data_m == "polished":
                    res_dic = Collection_Facturer_For_Search.objects.filter(collection_facturer_is_active=True,
                                                                            collection_stile_polished=True)
                if data_m == "polopolarized":
                    res_dic = Collection_Facturer_For_Search.objects.filter(collection_facturer_is_active=True,
                                                                            collection_stile_polopolarized=True)
                if data_m == "satin":
                    res_dic = Collection_Facturer_For_Search.objects.filter(collection_facturer_is_active=True,
                                                                            collection_stile_satin=True)
                if data_m == "aged":
                    res_dic = Collection_Facturer_For_Search.objects.filter(collection_facturer_is_active=True,
                                                                            collection_stile_aged=True)
                if data_m == "structured":
                    res_dic = Collection_Facturer_For_Search.objects.filter(collection_facturer_is_active=True,
                                                                            collection_stile_structured=True)
                if res_dic.exists():
                    for res_dic_in in res_dic:
                        result.append(res_dic_in.id)
            result = set(result)
            result_search.append(result)

        result = []
        if request_get_colour != []:
            for data_m in request_get_colour:
                if data_m == "beige":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_beige=True)
                if data_m == "white":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_white=True)
                if data_m == "burgundy":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_burgundy=True)
                if data_m == "blue":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_blue=True)
                if data_m == "yellow":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_yellow=True)
                if data_m == "green":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_green=True)
                if data_m == "gold":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_gold=True)
                if data_m == "brown":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_brown=True)
                if data_m == "red":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_red=True)
                if data_m == "multicolor":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_multicolor=True)
                if data_m == "orange":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_orange=True)
                if data_m == "pink":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_pink=True)
                if data_m == "silver_platinum":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_silver_platinum=True)
                if data_m == "silver_grey":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_silver_grey=True)
                if data_m == "silver_darkblue":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_silver_darkblue=True)
                if data_m == "silver_lilac":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_silver_lilac=True)
                if data_m == "silver_black":
                    res_dic = Collection_Colour_For_Search.objects.filter(collection_colour_is_active=True,
                                                                          collection_colour_silver_black=True)
                if res_dic.exists():
                    for res_dic_in in res_dic:
                        result.append(res_dic_in.id)
            result = set(result)
            result_search.append(result)

        result_all = []
        for alfa in result_search:
            for betta in alfa:
                result_all.append(betta)

        list_only = []

        len_resu = len(result_search)  # We get length result_search - list with the corteges of ID of collections

        for list_resu_only in result_all:  # We pass on result_all - incorporated ID from all positions of queries on a search
            if result_all.count(
                    list_resu_only) == len_resu and list_resu_only not in list_only:  # We check every element for an amount equal to all queries, if it is equal to all queries that it necessary ID
                list_only.append(list_resu_only)

        result_all = list_only

        resilt_collections = Collection.objects.filter(is_active_collection=True, id__in=result_all)
        resilt_collections_images = Collection_Image.objects.filter(is_active_collection=True, is_main_collection=True,
                                                                    name_collection__is_active_collection=True,
                                                                    name_collection__id__in=result_all)

        # Stock a block in the base of result of search of collections coming from a sectional search is beginning
        # A Subblock collecting data from the result of sectional search is beginning
        collections_search_hight = Collection.objects.filter(id__in=result_all)
        list_collection = []
        list_statistica = []
        for collection_search_hight in collections_search_hight:
            list_collection.append(collection_search_hight.id)
        # A Subblock collecting data from the result of sectional search is an end

        # A Subblock collecting data from all base of queries of sectional search on the session key and page is beginning
        if Collection.objects.filter(id__in=result_all).exists():
            all_statistica = Statistic_Find_Bloc.objects.filter(session_key=session_key, page="search_hight")
            for statistica in all_statistica:
                list_statistica.append(statistica.collection)
        # A Subblock collecting data from all base of queries of sectional search on the session key and page is an end

        # Subblock of record in case of absence of result of sectional search in a base is beginning
        if str(list_collection) not in list_statistica and len(str(list_collection)) > 2:
            Statistic_Find_Bloc.objects.create(session_key=session_key, collection=list_collection,
                                               page="search_hight")
        # Subblock of record in case of absence of result of sectional search in a base is an end
        # Stock a block in the base of result of search of collections coming from a sectional search is an end

        # Checking for a presence as a result of retrieval of data
        if resilt_collections_images.exists() == True:
            response_view = True
            # Receipt of way at the query of search
            response = str(request.get_full_path())
            # Transformation of line to the query and receipt of necessary remain of way for adding to pagginator
            response = response.replace("/search_hight/", "")
            create_base = Search_Low_Addition.objects.filter(session_key=session_key)

            if "page" not in response:
                if create_base.exists() == True:
                    Search_Low_Addition.objects.filter(session_key=session_key).update(response=response,
                                                                                       request_get_nhs=request_get_nhs,
                                                                                       request_get_manafacturer=request_get_manafacturer,
                                                                                       request_get_size=request_get_size,
                                                                                       request_get_country=request_get_country,
                                                                                       request_get_price=request_get_price,
                                                                                       request_get_availability=request_get_availability,
                                                                                       request_get_colour=request_get_colour,
                                                                                       request_get_facturer=request_get_facturer,
                                                                                       request_get_texturer=request_get_texturer,
                                                                                       request_get_application=request_get_application,
                                                                                       request_get_style=request_get_style,
                                                                                       request_get_type_material=request_get_type_material,
                                                                                       request_get_type_floor=request_get_type_floor)
                if create_base.exists() == False:
                    Search_Low_Addition.objects.create(session_key=session_key, response=response,
                                                       request_get_nhs=request_get_nhs,
                                                       request_get_manafacturer=request_get_manafacturer,
                                                       request_get_size=request_get_size,
                                                       request_get_country=request_get_country,
                                                       request_get_price=request_get_price,
                                                       request_get_availability=request_get_availability,
                                                       request_get_colour=request_get_colour,
                                                       request_get_facturer=request_get_facturer,
                                                       request_get_texturer=request_get_texturer,
                                                       request_get_application=request_get_application,
                                                       request_get_style=request_get_style,
                                                       request_get_type_material=request_get_type_material,
                                                       request_get_type_floor=request_get_type_floor)
                    Search_Diller_Otdel.objects.filter(session_key=session_key).delete()
                    Search_Manafactory.objects.filter(session_key=session_key).delete()
                    Search_Manafactory_Single.objects.filter(session_key=session_key).delete()
                    Search_For_Project.objects.filter(session_key=session_key).delete()
                    Search_Search.objects.filter(session_key=session_key).delete()

        # Checking for absence as a result of retrieval of data

        if resilt_collections_images.exists() == False:
            response_view = False
            resilt_collections_images = Collection_Image.objects.filter(is_active_collection=True,
                                                                        is_main_collection=True,
                                                                        name_collection__is_active_collection=True)

        response_for_search = Search_Low_Addition.objects.filter(session_key=session_key)
        for response_for_web in response_for_search:
            pass

    if 'Скинути фільтр пошуку' in request_get_cancel:
        response_view = False
        resilt_collections_images = Collection_Image.objects.filter(is_active_collection=True, is_main_collection=True,
                                                                    name_collection__is_active_collection=True)
        delete_base = Search_Low_Addition.objects.filter(session_key=session_key)

        if delete_base.exists() == True:
            delete_base.delete()
        if delete_base.exists() == False:
            pass

    # Preparation to paggination
    resilt_collections_images = resilt_collections_images.order_by('id')
    # Paggination of page is beginning
    paginator = Paginator(resilt_collections_images, 4)
    page = request.GET.get('page')

    try:
        resilt_collections_images = paginator.page(page)
    except PageNotAnInteger:
        resilt_collections_images = paginator.page(1)
    except EmptyPage:
        resilt_collections_images = paginator.page(paginator.num_pages)
    # Paggination of page is an end

    if request_get_nhs != []:
        for info_sig in Search_Low_Addition.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_nhs = True  # Marker of display of information about a search
            str_info = str(
                info_sig.request_get_nhs)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_info)
            srez = str_info[2:len_str - 2]  # We produce the cut of line deleting from []
            info_nhs_veb = srez.split("', '")  # Line feed in the list of values of ID
            info_nhs_veb = Collection_Search_NHS.objects.filter(
                id__in=info_nhs_veb)  # Receipt of query from a base in accordance with a list

    if request_get_manafacturer != []:
        for info_sig in Search_Low_Addition.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_manafacturer = True  # Marker of display of information about a search
            str_manafacturer = str(
                info_sig.request_get_manafacturer)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_manafacturer)
            srez = str_manafacturer[2:len_str - 2]  # We produce the cut of line deleting from []
            info_manafacturer_veb = srez.split("', '")  # Line feed in the list of values of ID
            info_manafacturer_veb = Manufacturer.objects.filter(
                id__in=info_manafacturer_veb)  # Receipt of query from a base in accordance with a list

    if request_get_size != []:
        for info_sig in Search_Low_Addition.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_size = True  # Marker of display of information about a search
            str_size = str(
                info_sig.request_get_size)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_size)
            srez = str_size[2:len_str - 2]  # We produce the cut of line deleting from []
            info_size_veb = srez.split("', '")  # Line feed in the list of values of ID
            info_size_veb = Size.objects.filter(
                id__in=info_size_veb)  # Receipt of query from a base in accordance with a list

    if request_get_country != []:
        for info_sig in Search_Low_Addition.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_country = True  # Marker of display of information about a search
            str_country = str(
                info_sig.request_get_country)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_country)
            srez = str_country[2:len_str - 2]  # We produce the cut of line deleting from []
            info_country_veb = srez.split("', '")  # Line feed in the list of values of ID
            info_country_veb = Manufacturer_Country.objects.filter(
                id__in=info_country_veb)  # Receipt of query from a base in accordance with a list

    if request_get_price != []:
        for info_sig in Search_Low_Addition.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_price = True  # Marker of display of information about a search
            str_price = str(
                info_sig.request_get_price)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_price)
            srez = str_price[2:len_str - 2]  # We produce the cut of line deleting from []
            info_price_veb = srez.split("', '")  # Line feed in the list of values of ID
            info_price_veb = Price_Group.objects.filter(
                id__in=info_price_veb)  # Receipt of query from a base in accordance with a list

    if request_get_availability != []:
        for info_sig in Search_Low_Addition.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_availability = True  # Marker of display of information about a search
            str_availability = str(
                info_sig.request_get_availability)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_availability)
            srez = str_availability[2:len_str - 2]  # We produce the cut of line deleting from []
            info_availability_veb = srez.split("', '")  # Line feed in the list of values of ID
            info_availability_veb = Availability.objects.filter(
                id__in=info_availability_veb)  # Receipt of query from a base in accordance with a list

    if request_get_colour != []:
        for info_sig in Search_Low_Addition.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_colour = True  # Marker of display of information about a search

            str_colour = str(
                info_sig.request_get_colour)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_colour)
            srez = str_colour[2:len_str - 2]  # We produce the cut of line deleting from []
            info_colour_veb = srez.split("', '")  # Line feed in the list of values of ID

            result_colour = []
            for info_sig in info_colour_veb:
                if info_sig == "beige":
                    res_colour = "Бежевий"
                if info_sig == "white":
                    res_colour = "Білий"
                if info_sig == "burgundy":
                    res_colour = "Бордовий"
                if info_sig == "blue":
                    res_colour = "Блакитний"
                if info_sig == "yellow":
                    res_colour = "Жовтий"
                if info_sig == "green":
                    res_colour = "Зелений"
                if info_sig == "gold":
                    res_colour = "Золотий"
                if info_sig == "brown":
                    res_colour = "Коричневий"
                if info_sig == "red":
                    res_colour = "Червоний"
                if info_sig == "multicolor":
                    res_colour = "Мультиколір"
                if info_sig == "orange":
                    res_colour = "Помаранчевий"
                if info_sig == "pink":
                    res_colour = "Рожевий"
                if info_sig == "silver_platinum":
                    res_colour = "Срібний/Платина"
                if info_sig == "silver_grey":
                    res_colour = "Сірий"
                if info_sig == "silver_darkblue":
                    res_colour = "Синій"
                if info_sig == "silver_lilac":
                    res_colour = "Бузковий"
                if info_sig == "silver_black":
                    res_colour = "Чорний"

                result_colour.append(res_colour)

    if request_get_facturer != []:
        for info_sig in Search_Low_Addition.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_facturer = True  # Marker of display of information about a search

            str_facturer = str(
                info_sig.request_get_facturer)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_facturer)
            srez = str_facturer[2:len_str - 2]  # We produce the cut of line deleting from []
            info_facturer_veb = srez.split("', '")  # Line feed in the list of values of ID

            result_facturer = []
            for info_sig in info_facturer_veb:
                if info_sig == "glossy":
                    res_facturer = "Глянцевий/Настінна"
                if info_sig == "matte":
                    res_facturer = "Матова"
                if info_sig == "polished":
                    res_facturer = "Полірована"
                if info_sig == "polopolarized":
                    res_facturer = "Напівполірована/Лапатірованная"
                if info_sig == "satin":
                    res_facturer = "Сатинована"
                if info_sig == "aged":
                    res_facturer = "Состаренная/Рустічная"
                if info_sig == "structured":
                    res_facturer = "Структурована/Рельєфна"

                result_facturer.append(res_facturer)

    if request_get_texturer != []:
        for info_sig in Search_Low_Addition.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_texturer = True  # Marker of display of information about a search

            str_texturer = str(
                info_sig.request_get_texturer)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_texturer)
            srez = str_texturer[2:len_str - 2]  # We produce the cut of line deleting from []
            info_texturer_veb = srez.split("', '")  # Line feed in the list of values of ID

            result_texturer = []
            for info_sig in info_texturer_veb:

                if info_sig == "3d":
                    res_texturer = "3D/Тривимірна"
                if info_sig == "art":
                    res_texturer = "Арт"
                if info_sig == "concrete":
                    res_texturer = "Бетон/Цемент/Штукатурка"
                if info_sig == "geometrical":
                    res_texturer = "Геометричний малюнок"
                if info_sig == "damaskato":
                    res_texturer = "Дамаскато/Вензелі"
                if info_sig == "wood":
                    res_texturer = "Дерево/Керамічний паркет"
                if info_sig == "imitationbrick":
                    res_texturer = "Імітація цегляної кладки"
                if info_sig == "imitationskin":
                    res_texturer = "Імітація шкіри"
                if info_sig == "rock":
                    res_texturer = "Камінь"
                if info_sig == "cotto":
                    res_texturer = "Котто/Імітація"
                if info_sig == "crackle":
                    res_texturer = "Кракле"
                if info_sig == "metal":
                    res_texturer = "Метал"
                if info_sig == "monocolor":
                    res_texturer = "Моноколір"
                if info_sig == "marble":
                    res_texturer = "Мармур"
                if info_sig == "onyx":
                    res_texturer = "Онікс"
                if info_sig == "patchwork":
                    res_texturer = "Печворк"
                if info_sig == "cloth":
                    res_texturer = "Тканина"
                if info_sig == "travertine":
                    res_texturer = "Травертин"
                if info_sig == "flowers":
                    res_texturer = "Квіти/Рослини"
                if info_sig == "ethnic":
                    res_texturer = "Етнічний малюнок"

                result_texturer.append(res_texturer)

    if request_get_application != []:
        for info_sig in Search_Low_Addition.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_application = True  # Marker of display of information about a search

            str_application = str(
                info_sig.request_get_application)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_application)
            srez = str_application[2:len_str - 2]  # We produce the cut of line deleting from []
            info_application_veb = srez.split("', '")  # Line feed in the list of values of ID

            result_application = []
            for info_sig in info_application_veb:

                if info_sig == "bathrooms":
                    res_application = "Для ванних кімнат"
                if info_sig == "floor":
                    res_application = "Для кухні/Плитка для підлоги"
                if info_sig == "apron":
                    res_application = "Для кухні/Фартух"
                if info_sig == "outdoor":
                    res_application = "Для вуличного застосування"
                if info_sig == "residential":
                    res_application = "Житловий інтер'єр"
                if info_sig == "projects":
                    res_application = "Громадські інтер'єри/Проекти"

                result_application.append(res_application)

    if request_get_style != []:
        for info_sig in Search_Low_Addition.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_style = True  # Marker of display of information about a search

            str_style = str(
                info_sig.request_get_style)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_style)
            srez = str_style[2:len_str - 2]  # We produce the cut of line deleting from []
            info_style_veb = srez.split("', '")  # Line feed in the list of values of ID

            result_style = []
            for info_sig in info_style_veb:

                if info_sig == "vintage":
                    res_style = "Вінтаж"
                if info_sig == "classic":
                    res_style = "Класика"
                if info_sig == "modern":
                    res_style = "Сучасний"

                result_style.append(res_style)

    if request_get_type_material != []:
        for info_sig in Search_Low_Addition.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_type_material = True  # Marker of display of information about a search

            str_type_material = str(
                info_sig.request_get_type_material)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_type_material)
            srez = str_type_material[2:len_str - 2]  # We produce the cut of line deleting from []
            info_type_material_veb = srez.split("', '")  # Line feed in the list of values of ID

            result_type_material = []
            for info_sig in info_type_material_veb:

                if info_sig == "grout":
                    res_type_material = "Затирка/Клей/Будівельна хімія"
                if info_sig == "ceramic":
                    res_type_material = "Керамічна плитка"
                if info_sig == "porcelain":
                    res_type_material = "Керамограніт"
                if info_sig == "clinker":
                    res_type_material = "Клінкерна плитка"
                if info_sig == "natural":
                    res_type_material = "Натуральний камінь"
                if info_sig == "leveling":
                    res_type_material = "Система вирівнювання плитки"
                if info_sig == "glass":
                    res_type_material = "Cкляна мозаїка"
                if info_sig == "steps":
                    res_type_material = "Сходинки"

                result_type_material.append(res_type_material)

    if request_get_type_floor != []:
        for info_sig in Search_Low_Addition.objects.filter(
                session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_type_floor = True  # Marker of display of information about a search

            str_type_floor = str(
                info_sig.request_get_type_floor)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_type_floor)
            srez = str_type_floor[2:len_str - 2]  # We produce the cut of line deleting from []
            info_type_floor_veb = srez.split("', '")  # Line feed in the list of values of ID

            result_type_floor = []
            for info_sig in info_type_floor_veb:

                if info_sig == "floor":
                    res_type_floor = "Для підлоги"
                if info_sig == "wall":
                    res_type_floor = "Для стін"
                if info_sig == "universal":
                    res_type_floor = "Універсальна"

                result_type_floor.append(res_type_floor)

    return render(request, 'main/search_hight_ukr.html', locals())
