from django.shortcuts import render
from main.models import For_Сatalog, For_IMG_Main, Footer, Search_Manafactory, Search_Manafactory_Single, Search_Diller_Otdel, \
    Search_For_Project, Search_Low_Addition, Search_Search
from products.models import Manufacturer, Collection, Collection_Image, Product, Product_Image, Product_Type, Manufacturer_Country, \
    Availability, Price_Group, Collection_Application_For_Search
from orders.forms import Find_Project_Form
from orders.models import Find_Project
from shadow.models import Statistic_User_Sing_In_ColProd, Statistic_Find_Bloc, Log_In_Site, Eye

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import redirect
from django.shortcuts import render
from main.models import For_Сatalog, For_IMG_Main, Footer, Search_Manafactory, Search_Manafactory_Single, Search_Diller_Otdel, \
    Search_For_Project, Search_Low_Addition, Search_Search
from products.models import Manufacturer, Collection, Collection_Image, Product, Product_Image, Product_Type, Manufacturer_Country, \
    Availability, Price_Group, Collection_Application_For_Search
from orders.forms import Find_Project_Form
from orders.models import Find_Project
from shadow.models import Statistic_User_Sing_In_ColProd, Statistic_Find_Bloc, Log_In_Site, Eye

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import redirect

import smtplib
from smtplib import SMTPAuthenticationError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create your views here.

def products(request):
    all_info_footer = Footer.objects.filter(is_active=True)
    products = Product_Image.objects.filter(is_active=True, is_main=True)

    return render(request, 'products/products.html', locals())


def collection(request):
    all_info_footer = Footer.objects.filter(is_active=True)
    collections = Collection_Image.objects.filter(is_main_collection=True, name_collection__is_active_collection=True)

    return render(request, 'products/collection.html', locals())


def manufacturer(request):
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
        page_max_many = Eye.objects.filter(session_key=session_key, page="Каталог", id=max_id_in)
        if page_max_many.count() != 0:
            for page_max in page_max_many:
                pass
            if page_max.page == "Каталог":
                Eye.objects.get(session_key=session_key, page="Каталог", id=max_id_in).delete()

        Eye.objects.create(session_key=session_key,
                           page="Каталог",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key))
        # Record in the base of mark in track is an end
    else:
        # Record in the base of being of FTU on a web-site and creation of mark of his location - beginning
        Log_In_Site.objects.create(session_key=session_key, leng="rus")
        Eye.objects.create(session_key=session_key,
                           page="Каталог",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key, leng="rus"))
        # Record in the base of being of FTU on a web-site and creation of mark of his location - end
    # Checking for being of record in the base of the sessions key is an end
    # A record of data about the visit of web-site is an end
    #  The signal processing on switching of language is beginning
    data = request.POST
    if data.get("submit") == "ukr":
        Log_In_Site.objects.filter(session_key=session_key).update(leng="ukr")
        return redirect('manufacturer_ukr')
    # The signal processing on switching of language is end
    all_info_footer = Footer.objects.filter(is_active=True)
    response_view = False
    view_all_help = False
    text_and_img_manufacturers = For_Сatalog.objects.filter(is_active=True)
    for manufacturers_info in text_and_img_manufacturers:
        pass
    manufacturers = Manufacturer.objects.filter(is_active=True)
# Collection on the base of COUNTRIES in accordance with the list of manafactory
    country = []
    for sear_country in manufacturers:
        country.append(sear_country.manufacturer_country.name_manufacturer_country)
    country = Manufacturer_Country.objects.filter(name_manufacturer_country__in=country)
    request_get_country = request.GET.getlist('country')
    request_get_cancel = request.GET.getlist('cancel')
    request_get_find = request.GET.getlist('find')
    if 'Искать' in request_get_find:
        if request_get_country is not None:
            manufacturers_low = []
            for country_for_search in request_get_country:
                manufacturers_incom = list(Manufacturer.objects.filter(manufacturer_country__id=country_for_search))
                for manufacturers_incom_in in manufacturers_incom:
                    manufacturers_low.append(manufacturers_incom_in)
        manufacturers = Manufacturer.objects.filter(name_manufacturer__in=manufacturers_low)
# Stock a block in the base of result of search of collections coming from a sectional search is beginning
        # A Subblock collecting data from the result of sectional search is beginning
        collection_for_page_manufacturer = Collection.objects.filter(manufacturer_collection__name_manufacturer__in=manufacturers_low)
        list_collecti_manafa = []
        list_statistica = []
        for collection_single_manafa in collection_for_page_manufacturer:
            list_collecti_manafa.append(collection_single_manafa.id)
        # A Subblock collecting data from the result of sectional search is an end
        # A Subblock collecting data from all base of queries of sectional search on the session key and page is beginning
        if Collection.objects.filter(manufacturer_collection__name_manufacturer__in=manufacturers_low).exists():
            all_statistica = Statistic_Find_Bloc.objects.filter(session_key=session_key, page="manufacturer")
            for statistica in all_statistica:
                list_statistica.append(statistica.collection)
        # A Subblock collecting data from all base of queries of sectional search on the session key and page is an end
        # Subblock of record in case of absence of result of sectional search in a base is beginning
        if str(list_collecti_manafa) not in list_statistica and len(str(list_collecti_manafa)) > 2:
            Statistic_Find_Bloc.objects.create(session_key=session_key, collection=list_collecti_manafa, page="manufacturer")
        # Subblock of record in case of absence of result of sectional search in a base is an end
# Stock a block in the base of result of search of collections coming from a sectional search is an end
        # Checking for a presence as a result of retrieval of data
        if manufacturers.exists() == True:
            response_view = True
            # Receipt of way at the query of search
            response = str(request.get_full_path())
            # Transformation of line to the query and receipt of necessary remain of way for adding to pagginator
            response = response.replace("/manufacturer/", "")
            create_base = Search_Manafactory.objects.filter(session_key=session_key)
            if "page" not in response:
                if create_base.exists() == True:
                    Search_Manafactory.objects.filter(session_key=session_key).update(response=response, request_get_country=request_get_country)
                if create_base.exists() == False:
                    Search_Manafactory.objects.create(session_key=session_key, response=response, request_get_country=request_get_country)
                    Search_Diller_Otdel.objects.filter(session_key=session_key).delete()
                    Search_Manafactory_Single.objects.filter(session_key=session_key).delete()
                    Search_For_Project.objects.filter(session_key=session_key).delete()
                    Search_Low_Addition.objects.filter(session_key=session_key).delete()
                    Search_Search.objects.filter(session_key=session_key).delete()
                    # Checking for absence as a result of retrieval of data
        if manufacturers.exists() == False:
            response_view = False
            manufacturers = Manufacturer.objects.filter(is_active=True)
        response_for_search = Search_Manafactory.objects.filter(session_key=session_key)
        for response_for_web in response_for_search:
            pass
    if 'Сбросить фильтр поиска' in request_get_cancel:
        response_view = False
        manufacturers = Manufacturer.objects.filter(is_active=True)
        delete_base = Search_Manafactory.objects.filter(session_key=session_key)
        if delete_base.exists() == True:
            delete_base.delete()
        if delete_base.exists() == False:
            pass
    dictin = dict()
    dictin_out = []
    if manufacturers != None:
        for manufacturer in manufacturers:
            z = dict()
            collecti = Collection_Image.objects.filter(is_active_collection=True, name_collection__manufacturer_collection__id=manufacturer.id, is_main_collection=True)
            len_collecti = len(collecti)
            manufacturer_id = manufacturer.id
            dictin[manufacturer_id] = len_collecti
            z["manufacturer_id"] = manufacturer.id
            z["len_collecti"] = len_collecti
            z["collection"] = collecti
            dictin_out.append(z)
    kol_collections = Collection_Image.objects.filter(is_active_collection=True)
# Preparation to paggination
    manufacturers = manufacturers.order_by('id')
# Paggination of page is beginning
    paginator = Paginator(manufacturers, 4)
    page = request.GET.get('page')
    try:
        manufacturers = paginator.page(page)
    except PageNotAnInteger:
        manufacturers = paginator.page(1)
    except EmptyPage:
        manufacturers = paginator.page(paginator.num_pages)
# Paggination of page is an end
    if request_get_country != []:
        for info_sig in Search_Manafactory.objects.filter(session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_country = True  # Marker of display of information about a search
            str_country = str(info_sig.request_get_country)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_country)
            srez = str_country[2:len_str - 2]  # We produce the cut of line deleting from []
            info_country_veb = srez.split("', '")  # Line feed in the list of values of ID
            info_country_veb = Manufacturer_Country.objects.filter(id__in=info_country_veb)  # Receipt of query from a base in accordance with a list

    return render(request, 'products/manufacturer.html', locals())


def manufacturer_ukr(request):
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
        page_max_many = Eye.objects.filter(session_key=session_key, page="Каталог", id=max_id_in)
        if page_max_many.count() != 0:
            for page_max in page_max_many:
                pass
            if page_max.page == "Каталог":
                Eye.objects.get(session_key=session_key, page="Каталог", id=max_id_in).delete()

        Eye.objects.create(session_key=session_key,
                           page="Каталог",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key))
        # Record in the base of mark in track is an end
    else:
        # Record in the base of being of FTU on a web-site and creation of mark of his location - beginning
        Log_In_Site.objects.create(session_key=session_key, leng="rus")
        Eye.objects.create(session_key=session_key,
                           page="Каталог",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key, leng="rus"))
        # Record in the base of being of FTU on a web-site and creation of mark of his location - end
    # Checking for being of record in the base of the sessions key is an end
    # A record of data about the visit of web-site is an end

    # The signal processing on switching of language is beginning
    data = request.POST
    if data.get("submit") == "rus":
        Log_In_Site.objects.filter(session_key=session_key).update(leng="rus")
        return redirect('manufacturer')
    # The signal processing on switching of language is end
    all_info_footer = Footer.objects.filter(is_active=True)
    response_view = False
    view_all_help = False
    text_and_img_manufacturers = For_Сatalog.objects.filter(is_active=True)
    for manufacturers_info in text_and_img_manufacturers:
        pass
    manufacturers = Manufacturer.objects.filter(is_active=True)

# Collection on the base of COUNTRIES in accordance with the list of manafactory
    country = []
    for sear_country in manufacturers:
        country.append(sear_country.manufacturer_country.name_manufacturer_country)
    country = Manufacturer_Country.objects.filter(name_manufacturer_country__in=country)

    request_get_country = request.GET.getlist('country')
    request_get_cancel = request.GET.getlist('cancel')
    request_get_find = request.GET.getlist('find')

    if 'Шукати' in request_get_find:
        if request_get_country is not None:
            manufacturers_low = []
            for country_for_search in request_get_country:
                manufacturers_incom = list(Manufacturer.objects.filter(manufacturer_country__id=country_for_search))
                for manufacturers_incom_in in manufacturers_incom:
                    manufacturers_low.append(manufacturers_incom_in)

        manufacturers = Manufacturer.objects.filter(name_manufacturer__in=manufacturers_low)

# Stock a block in the base of result of search of collections coming from a sectional search is beginning
        # A Subblock collecting data from the result of sectional search is beginning
        collection_for_page_manufacturer = Collection.objects.filter(manufacturer_collection__name_manufacturer__in=manufacturers_low)
        list_collecti_manafa = []
        list_statistica = []
        for collection_single_manafa in collection_for_page_manufacturer:
            list_collecti_manafa.append(collection_single_manafa.id)
        # A Subblock collecting data from the result of sectional search is an end

        # A Subblock collecting data from all base of queries of sectional search on the session key and page is beginning
        if Collection.objects.filter(manufacturer_collection__name_manufacturer__in=manufacturers_low).exists():
            all_statistica = Statistic_Find_Bloc.objects.filter(session_key=session_key, page="manufacturer")
            for statistica in all_statistica:
                list_statistica.append(statistica.collection)
        # A Subblock collecting data from all base of queries of sectional search on the session key and page is an end

        # Subblock of record in case of absence of result of sectional search in a base is beginning
        if str(list_collecti_manafa) not in list_statistica and len(str(list_collecti_manafa)) > 2:
            Statistic_Find_Bloc.objects.create(session_key=session_key, collection=list_collecti_manafa, page="manufacturer")
            # Subblock of record in case of absence of result of sectional search in a base is an end
# Stock a block in the base of result of search of collections coming from a sectional search is an end

        # Checking for a presence as a result of retrieval of data
        if manufacturers.exists() == True:
            response_view = True
            # Receipt of way at the query of search
            response = str(request.get_full_path())
            # Transformation of line to the query and receipt of necessary remain of way for adding to pagginator
            response = response.replace("/manufacturer_ukr/", "")
            create_base = Search_Manafactory.objects.filter(session_key=session_key)

            if "page" not in response:
                if create_base.exists() == True:
                    Search_Manafactory.objects.filter(session_key=session_key).update(response=response, request_get_country=request_get_country)
                if create_base.exists() == False:
                    Search_Manafactory.objects.create(session_key=session_key, response=response, request_get_country=request_get_country)
                    Search_Diller_Otdel.objects.filter(session_key=session_key).delete()
                    Search_Manafactory_Single.objects.filter(session_key=session_key).delete()
                    Search_For_Project.objects.filter(session_key=session_key).delete()
                    Search_Low_Addition.objects.filter(session_key=session_key).delete()
                    Search_Search.objects.filter(session_key=session_key).delete()

                    # Checking for absence as a result of retrieval of data

        if manufacturers.exists() == False:
            response_view = False
            manufacturers = Manufacturer.objects.filter(is_active=True)

        response_for_search = Search_Manafactory.objects.filter(session_key=session_key)
        for response_for_web in response_for_search:
            pass

    if 'Скинути фільтр пошуку' in request_get_cancel:
        response_view = False
        manufacturers = Manufacturer.objects.filter(is_active=True)
        delete_base = Search_Manafactory.objects.filter(session_key=session_key)
        if delete_base.exists() == True:
            delete_base.delete()
        if delete_base.exists() == False:
            pass

    dictin = dict()
    dictin_out = []

    if manufacturers != None:
        for manufacturer in manufacturers:
            z = dict()
            collecti = Collection_Image.objects.filter(is_active_collection=True, name_collection__manufacturer_collection__id=manufacturer.id, is_main_collection=True)
            len_collecti = len(collecti)
            manufacturer_id = manufacturer.id
            dictin[manufacturer_id] = len_collecti
            z["manufacturer_id"] = manufacturer.id
            z["len_collecti"] = len_collecti
            z["collection"] = collecti
            dictin_out.append(z)

    kol_collections = Collection_Image.objects.filter(is_active_collection=True)

# Preparation to paggination
    manufacturers = manufacturers.order_by('id')
# Paggination of page is beginning
    paginator = Paginator(manufacturers, 4)
    page = request.GET.get('page')

    try:
        manufacturers = paginator.page(page)
    except PageNotAnInteger:
        manufacturers = paginator.page(1)
    except EmptyPage:
        manufacturers = paginator.page(paginator.num_pages)
# Paggination of page is an end

    if request_get_country != []:
        for info_sig in Search_Manafactory.objects.filter(session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_country = True  # Marker of display of information about a search
            str_country = str(info_sig.request_get_country)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_country)
            srez = str_country[2:len_str - 2]  # We produce the cut of line deleting from []
            info_country_veb = srez.split("', '")  # Line feed in the list of values of ID
            info_country_veb = Manufacturer_Country.objects.filter(id__in=info_country_veb)  # Receipt of query from a base in accordance with a list

    return render(request, 'products/manufacturer_ukr.html', locals())


def manufacturer_singl(request, manufacturer_singl_id):
    # A record of data about the visit of web-site is beginning
    session_key = request.session.session_key
    # Checking for being of record in the base of the sessions key is beginning
    manafacturer_for_static = Manufacturer.objects.get(id=manufacturer_singl_id)
    if Log_In_Site.objects.filter(session_key=session_key).count():
    # Record in the base of mark in track is beginning
        find_max = Eye.objects.filter(session_key=session_key)
        max_id_in = 0
        for find_single in find_max:
            if max_id_in < int(find_single.id):
                max_id_in = int(find_single.id)
        page_max_many = Eye.objects.filter(session_key=session_key, page=str(manafacturer_for_static.name_manufacturer), id=max_id_in)
        if page_max_many.count() != 0:
            for page_max in page_max_many:
                pass
            if page_max.page == str(manafacturer_for_static.name_manufacturer):
                Eye.objects.get(session_key=session_key, page=str(manafacturer_for_static.name_manufacturer), id=max_id_in).delete()

        Eye.objects.create(session_key=session_key,
                           page=str(manafacturer_for_static.name_manufacturer),
                           log_in_site=Log_In_Site.objects.get(session_key=session_key),
                           locate_manafactur=True)
        # Record in the base of mark in track is an end
    else:
        # Record in the base of being of FTU on a web-site and creation of mark of his location - beginning
        Log_In_Site.objects.create(session_key=session_key, leng="rus")
        Eye.objects.create(session_key=session_key,
                           page=str(manafacturer_for_static.name_manufacturer),
                           log_in_site=Log_In_Site.objects.get(session_key=session_key, leng="rus"),
                           locate_manafactur=True)
            # Record in the base of being of FTU on a web-site and creation of mark of his location - end
        # Checking for being of record in the base of the sessions key is an end
        # A record of data about the visit of web-site is an end

    # The signal processing on switching of language is beginning
    data = request.POST

    if data.get("submit") == "ukr":
        Log_In_Site.objects.filter(session_key=session_key).update(leng="ukr")
        return redirect('manufacturer_singl_ukr', manufacturer_singl_id_ukr=manufacturer_singl_id)
    # The signal processing on switching of language is end

    all_info_footer = Footer.objects.filter(is_active=True)

    response_view = False

    view_all_help = False

    manufacturer_singl_web = Manufacturer.objects.get(id=manufacturer_singl_id)

    resilt_collections_images = Collection_Image.objects.filter(is_active_collection=True,
                                                                is_main_collection=True,
                                                                name_collection__is_active_collection=True,
                                                                name_collection__manufacturer_collection__id=manufacturer_singl_id)

    # Collection on the base of PRICE GROUPS
    price_group = []
    for price_ava in resilt_collections_images:
        price_group.append(price_ava.name_collection.price_group_collection.name_price_group)
    price_group = Price_Group.objects.filter(name_price_group__in=price_group)

    # Collection on the base of PRESENCE
    availability = []
    for availability_ava in resilt_collections_images:
        availability.append(availability_ava.name_collection.availability_collection.name_availability)
    availability = Availability.objects.filter(name_availability__in=availability)

    request_get_application = request.GET.getlist('application')
    request_get_availability = request.GET.getlist('availability')
    request_get_price = request.GET.getlist('price')

    request_get_cancel = request.GET.getlist('cancel')
    request_get_find = request.GET.getlist('find')

    if 'Искать' in request_get_find:
        result_search = []
        list_search = []
        result = []

        if request_get_application != []:
            for data_m in request_get_application:
                if data_m == "bathrooms":
                    res_dic = Collection_Application_For_Search.objects.filter(
                        collection_application_is_active=True,
                        collection_application_bathrooms=True, name_collection__manufacturer_collection__id=manufacturer_singl_id)
                if data_m == "floor":
                    res_dic = Collection_Application_For_Search.objects.filter(
                        collection_application_is_active=True,
                        collection_application_floor=True, name_collection__manufacturer_collection__id=manufacturer_singl_id)
                if data_m == "apron":
                    res_dic = Collection_Application_For_Search.objects.filter(
                        collection_application_is_active=True,
                        collection_application_apron=True, name_collection__manufacturer_collection__id=manufacturer_singl_id)
                if data_m == "outdoor":
                    res_dic = Collection_Application_For_Search.objects.filter(
                        collection_application_is_active=True,
                        collection_application_outdoor=True, name_collection__manufacturer_collection__id=manufacturer_singl_id)
                if data_m == "residential":
                    res_dic = Collection_Application_For_Search.objects.filter(
                        collection_application_is_active=True,
                        collection_application_residential=True, name_collection__manufacturer_collection__id=manufacturer_singl_id)
                if data_m == "projects":
                    res_dic = Collection_Application_For_Search.objects.filter(
                        collection_application_is_active=True,
                        collection_application_projects=True, name_collection__manufacturer_collection__id=manufacturer_singl_id)
                if res_dic.exists():
                    for res_dic_in in res_dic:
                        result.append(res_dic_in.id)
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
            if result_all.count(list_resu_only) == len_resu and list_resu_only not in list_only:  # We check every element for an amount equal to all queries, if it is equal to all queries that it necessary ID
                list_only.append(list_resu_only)
        result_all = list_only
        resilt_collections_images = Collection_Image.objects.filter(is_active_collection=True, is_main_collection=True,
                                                                    name_collection__is_active_collection=True, name_collection__id__in=result_all,
                                                                    name_collection__manufacturer_collection__id=manufacturer_singl_id)

    # Stock a block in the base of result of search of collections coming from a sectional search is beginning
        # A Subblock collecting data from the result of sectional search is beginning
        collection_for_page_manufacturer_single = Collection.objects.filter(id__in=result_all, manufacturer_collection__id=manufacturer_singl_id)
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
        # A Subblock collecting data from all base of queries of sectional search on the session key and page is beginning

        # Subblock of record in case of absence of result of sectional search in a base is beginning
        if str(list_collection) not in list_statistica and len(str(list_collection)) > 2:
            Statistic_Find_Bloc.objects.create(session_key=session_key, collection=list_collection, page="manufacturer_single")
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

    # Block for the conclusion of types of tile
    collecti = Collection.objects.filter(is_active_collection=True, manufacturer_collection__id=manufacturer_singl_id)

    spisok_for = {}
    dict_for = []
    for asing in collecti:
        azis = Product_Image.objects.filter(is_active=True, is_main=True, product__collection_product__id=asing.id)
        leni = azis.count()
        # We collect all data on the type of products
        prod_type = []
        for azi in azis:
            prod_type.append(azi.product.product_type_product.name_product_type)

        type_product = Product_Type.objects.filter(name_product_type__in=prod_type)
        spisok_for = {"id_collection": asing.id, "len_product": leni, "type_product_down": type_product}
        dict_for.append(spisok_for)

    # Preparation to paggination
    resilt_collections_images = resilt_collections_images.order_by('id')
    # Paggination of page is beginning
    paginator = Paginator(resilt_collections_images, 24)
    page = request.GET.get('page')
    try:
        collection_for_manufacturer_singl_image_web = paginator.page(page)
    except PageNotAnInteger:
        collection_for_manufacturer_singl_image_web = paginator.page(1)
    except EmptyPage:
        collection_for_manufacturer_singl_image_web = paginator.page(paginator.num_pages)
    # Paggination of page is an end

    # Beginning of conclusion of information at a search (Criteria of search)
    if request_get_price != []:
        for info_sig in Search_Manafactory_Single.objects.filter(session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_price = True  # Marker of display of information about a search
            str_price = str(info_sig.request_get_price)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_price)
            srez = str_price[2:len_str - 2]  # We produce the cut of line deleting from []
            info_price_veb = srez.split("', '")  # Line feed in the list of values of ID
            info_price_veb = Price_Group.objects.filter(id__in=info_price_veb)  # Receipt of query from a base in accordance with a list

    if request_get_availability != []:
        for info_sig in Search_Manafactory_Single.objects.filter(session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_availability = True  # Marker of display of information about a search
            str_availability = str(info_sig.request_get_availability)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_availability)
            srez = str_availability[2:len_str - 2]  # We produce the cut of line deleting from []
            info_availability_veb = srez.split("', '")  # Line feed in the list of values of ID
            info_availability_veb = Availability.objects.filter(id__in=info_availability_veb)  # Receipt of query from a base in accordance with a list

    if request_get_application != []:
        for info_sig in Search_Manafactory_Single.objects.filter(session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_application = True  # Marker of display of information about a search

            str_application = str(info_sig.request_get_application)  # We get from a base a line from ID and begin to transform in a list for the further use
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

    return render(request, 'products/manufacturer_singl.html', locals())


def manufacturer_singl_ukr(request, manufacturer_singl_id_ukr):
    # A record of data about the visit of web-site is beginning
    session_key = request.session.session_key
    # Checking for being of record in the base of the sessions key is beginning
    manafacturer_for_static = Manufacturer.objects.get(id=manufacturer_singl_id_ukr)
    if Log_In_Site.objects.filter(session_key=session_key).count():
        # Record in the base of mark in track is beginning
        find_max = Eye.objects.filter(session_key=session_key)
        max_id_in = 0
        for find_single in find_max:
            if max_id_in < int(find_single.id):
                max_id_in = int(find_single.id)
        page_max_many = Eye.objects.filter(session_key=session_key, page=str(manafacturer_for_static.name_manufacturer), id=max_id_in)
        if page_max_many.count() != 0:
            for page_max in page_max_many:
                pass
            if page_max.page == str(manafacturer_for_static.name_manufacturer):
                Eye.objects.get(session_key=session_key, page=str(manafacturer_for_static.name_manufacturer), id=max_id_in).delete()

        Eye.objects.create(session_key=session_key,
                           page=str(manafacturer_for_static.name_manufacturer),
                           log_in_site=Log_In_Site.objects.get(session_key=session_key),
                           locate_manafactur=True)
        # Record in the base of mark in track is an end
    else:
        # Record in the base of being of FTU on a web-site and creation of mark of his location - beginning
        Log_In_Site.objects.create(session_key=session_key, leng="rus")
        Eye.objects.create(session_key=session_key,
                           page=str(manafacturer_for_static.name_manufacturer),
                           log_in_site=Log_In_Site.objects.get(session_key=session_key, leng="rus"),
                           locate_manafactur=True)
        # Record in the base of being of FTU on a web-site and creation of mark of his location - end
        # Checking for being of record in the base of the sessions key is an end
    # A record of data about the visit of web-site is an end

    # The signal processing on switching of language is beginning
    data = request.POST
    if data.get("submit") == "rus":
        Log_In_Site.objects.filter(session_key=session_key).update(leng="rus")
        return redirect('manufacturer_singl', manufacturer_singl_id=manufacturer_singl_id_ukr)
    # The signal processing on switching of language is end
    all_info_footer = Footer.objects.filter(is_active=True)
    response_view = False
    view_all_help = False
    manufacturer_singl_web = Manufacturer.objects.get(id=manufacturer_singl_id_ukr)
    resilt_collections_images = Collection_Image.objects.filter(is_active_collection=True,
                                                                is_main_collection=True,
                                                                name_collection__is_active_collection=True,
                                                                name_collection__manufacturer_collection__id=manufacturer_singl_id_ukr)

    # Collection on the base of PRICE GROUPS
    price_group = []
    for price_ava in resilt_collections_images:
        price_group.append(price_ava.name_collection.price_group_collection.name_price_group)
    price_group = Price_Group.objects.filter(name_price_group__in=price_group)

    # Collection on the base of PRESENCE
    availability = []
    for availability_ava in resilt_collections_images:
        availability.append(availability_ava.name_collection.availability_collection.name_availability)
    availability = Availability.objects.filter(name_availability__in=availability)
    request_get_application = request.GET.getlist('application')
    request_get_availability = request.GET.getlist('availability')
    request_get_price = request.GET.getlist('price')
    request_get_cancel = request.GET.getlist('cancel')
    request_get_find = request.GET.getlist('find')

    if 'Шукати' in request_get_find:
        result_search = []
        list_search = []
        result = []

        if request_get_application != []:
            for data_m in request_get_application:
                if data_m == "bathrooms":
                    res_dic = Collection_Application_For_Search.objects.filter(
                        collection_application_is_active=True,
                        collection_application_bathrooms=True, name_collection__manufacturer_collection__id=manufacturer_singl_id_ukr)
                if data_m == "floor":
                    res_dic = Collection_Application_For_Search.objects.filter(
                        collection_application_is_active=True,
                        collection_application_floor=True, name_collection__manufacturer_collection__id=manufacturer_singl_id_ukr)
                if data_m == "apron":
                    res_dic = Collection_Application_For_Search.objects.filter(
                        collection_application_is_active=True,
                        collection_application_apron=True, name_collection__manufacturer_collection__id=manufacturer_singl_id_ukr)
                if data_m == "outdoor":
                    res_dic = Collection_Application_For_Search.objects.filter(
                        collection_application_is_active=True,
                        collection_application_outdoor=True, name_collection__manufacturer_collection__id=manufacturer_singl_id_ukr)
                if data_m == "residential":
                    res_dic = Collection_Application_For_Search.objects.filter(
                        collection_application_is_active=True,
                        collection_application_residential=True, name_collection__manufacturer_collection__id=manufacturer_singl_id_ukr)
                if data_m == "projects":
                    res_dic = Collection_Application_For_Search.objects.filter(
                        collection_application_is_active=True,
                        collection_application_projects=True, name_collection__manufacturer_collection__id=manufacturer_singl_id_ukr)
                if res_dic.exists():
                    for res_dic_in in res_dic:
                        result.append(res_dic_in.id)
            result = set(result)
            result_search.append(result)

        result = []
        if request_get_availability != []:
            for data_m in request_get_availability:
                data_for_search = Collection.objects.filter(is_active_collection=True,
                                                            availability_collection__id=data_m,
                                                            manufacturer_collection__id=manufacturer_singl_id_ukr)
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
                                                            manufacturer_collection__id=manufacturer_singl_id_ukr)
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
            if result_all.count(list_resu_only) == len_resu and list_resu_only not in list_only:  # We check every element for an amount equal to all queries, if it is equal to all queries that it necessary ID
                list_only.append(list_resu_only)
        result_all = list_only
        resilt_collections_images = Collection_Image.objects.filter(is_active_collection=True, is_main_collection=True,
                                                                    name_collection__is_active_collection=True, name_collection__id__in=result_all,
                                                                    name_collection__manufacturer_collection__id=manufacturer_singl_id_ukr)

    # Stock a block in the base of result of search of collections coming from a sectional search is beginning
        # A Subblock collecting data from the result of sectional search is beginning
        collection_for_page_manufacturer_single = Collection.objects.filter(id__in=result_all, manufacturer_collection__id=manufacturer_singl_id_ukr)
        list_collection = []
        list_statistica = []
        for collection_single_manafa in collection_for_page_manufacturer_single:
            list_collection.append(collection_single_manafa.id)
        # A Subblock collecting data from the result of sectional search is an end

        # A Subblock collecting data from all base of queries of sectional search on the session key and page is beginning
        if Collection.objects.filter(id__in=result_all, manufacturer_collection__id=manufacturer_singl_id_ukr).exists():
            all_statistica = Statistic_Find_Bloc.objects.filter(session_key=session_key, page="manufacturer_single")
            for statistica in all_statistica:
                list_statistica.append(statistica.collection)
        # A Subblock collecting data from all base of queries of sectional search on the session key and page is an end

        # Subblock of record in case of absence of result of sectional search in a base is beginning
        if str(list_collection) not in list_statistica and len(str(list_collection)) > 2:
            Statistic_Find_Bloc.objects.create(session_key=session_key, collection=list_collection, page="manufacturer_single")
        # Subblock of record in case of absence of result of sectional search in a base is an end
    # Stock a block in the base of result of search of collections coming from a sectional search is an end

        # Checking for a presence as a result of retrieval of data
        if resilt_collections_images.exists() == True:
            response_view = True
            # Receipt of way at the query of search
            response = str(request.get_full_path())
            # Transformation of line to the query and receipt of necessary remain of way for adding to paggination
            pach = "/manufacturer_singl/" + str(manufacturer_singl_id_ukr) + "/"
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

                    # Проверка на отсутствие в результате поиска данных
        if resilt_collections_images.exists() == False:
            response_view = False
            resilt_collections_images = Collection_Image.objects.filter(is_active_collection=True,
                                                                        is_main_collection=True,
                                                                        name_collection__is_active_collection=True,
                                                                        name_collection__manufacturer_collection__id=manufacturer_singl_id_ukr)

        response_for_search = Search_Manafactory_Single.objects.filter(session_key=session_key)

        for response_for_web in response_for_search:
            pass

    if 'Сбросить фильтр поиска' in request_get_cancel:
        response_view = False
        resilt_collections_images = Collection_Image.objects.filter(is_active_collection=True,
                                                                    is_main_collection=True,
                                                                    name_collection__is_active_collection=True,
                                                                    name_collection__manufacturer_collection__id=manufacturer_singl_id_ukr)
        delete_base = Search_Manafactory_Single.objects.filter(session_key=session_key)

        if delete_base.exists() == True:
            delete_base.delete()
        if delete_base.exists() == False:
            pass

    # Block for the conclusion of types of tile
    collecti = Collection.objects.filter(is_active_collection=True, manufacturer_collection__id=manufacturer_singl_id_ukr)

    spisok_for = {}
    dict_for = []
    for asing in collecti:
        azis = Product_Image.objects.filter(is_active=True, is_main=True, product__collection_product__id=asing.id)
        leni = azis.count()
        # We collect all data on the type of products
        prod_type = []
        for azi in azis:
            prod_type.append(azi.product.product_type_product.name_product_type)

        type_product = Product_Type.objects.filter(name_product_type__in=prod_type)
        spisok_for = {"id_collection": asing.id, "len_product": leni, "type_product_down": type_product}
        dict_for.append(spisok_for)

    # Preparation to paggination
    resilt_collections_images = resilt_collections_images.order_by('id')
    # Paggination of page is beginning
    paginator = Paginator(resilt_collections_images, 4)
    page = request.GET.get('page')

    try:
        collection_for_manufacturer_singl_image_web = paginator.page(page)
    except PageNotAnInteger:
        collection_for_manufacturer_singl_image_web = paginator.page(1)
    except EmptyPage:
        collection_for_manufacturer_singl_image_web = paginator.page(paginator.num_pages)
# Paggination of page is an end

# Beginning of conclusion of information at a search (Criteria of search)
    if request_get_price != []:
        for info_sig in Search_Manafactory_Single.objects.filter(session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_price = True  # Marker of display of information about a search
            str_price = str(info_sig.request_get_price)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_price)
            srez = str_price[2:len_str - 2]  # We produce the cut of line deleting from []
            info_price_veb = srez.split("', '")  # Line feed in the list of values of ID
            info_price_veb = Price_Group.objects.filter(id__in=info_price_veb)  # Receipt of query from a base in accordance with a list

    if request_get_availability != []:
        for info_sig in Search_Manafactory_Single.objects.filter(session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_availability = True  # Marker of display of information about a search
            str_availability = str(info_sig.request_get_availability)  # We get from a base a line from ID and begin to transform in a list for the further use
            len_str = len(str_availability)
            srez = str_availability[2:len_str - 2]  # We produce the cut of line deleting from []
            info_availability_veb = srez.split("', '")  # Line feed in the list of values of ID
            info_availability_veb = Availability.objects.filter(id__in=info_availability_veb)  # Receipt of query from a base in accordance with a list

    if request_get_application != []:
        for info_sig in Search_Manafactory_Single.objects.filter(session_key=session_key):  # Block of processing of data for the conclusion of information about a search
            view_all_help = True  # Marker of display of information about a search
            view_all_application = True  # Marker of display of information about a search

            str_application = str(info_sig.request_get_application)  # We get from a base a line from ID and begin to transform in a list for the further use
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

    return render(request, 'products/manufacturer_singl_ukr.html', locals())


def collection_singl(request, id_patch):
    session_key = request.session.session_key
    name_collection_re = Collection.objects.get(id_patch=id_patch)
    collection_singl_id = name_collection_re.id

    view_send = False

    # A record of data about the visit of web-site is beginning
    session_key = request.session.session_key
    # Checking for being of record in the base of the sessions key is beginning
    collection_for_static = Collection.objects.get(id=collection_singl_id)
    if Log_In_Site.objects.filter(session_key=session_key).count():
        # Record in the base of mark in track is beginning
        find_max = Eye.objects.filter(session_key=session_key)
        max_id_in = 0
        for find_single in find_max:
            if max_id_in < int(find_single.id):
                max_id_in = int(find_single.id)
        page_max_many = Eye.objects.filter(session_key=session_key, page=str(collection_for_static.name_collection), id=max_id_in)
        if page_max_many.count() != 0:
            for page_max in page_max_many:
                pass
            if page_max.page == str(collection_for_static.name_collection):
                Eye.objects.get(session_key=session_key, page=str(collection_for_static.name_collection), id=max_id_in).delete()

        Eye.objects.create(session_key=session_key,
                           page=str(collection_for_static.name_collection),
                           log_in_site=Log_In_Site.objects.get(session_key=session_key),
                           locate_collection=True)
         # Record in the base of mark in track is an end
    else:
        # Record in the base of being of FTU on a web-site and creation of mark of his location - beginning
        Log_In_Site.objects.create(session_key=session_key, leng="rus")
        Eye.objects.create(session_key=session_key,
                           page=str(collection_for_static.name_collection),
                           log_in_site=Log_In_Site.objects.get(session_key=session_key, leng="rus"),
                           locate_collection=True)
        # Record in the base of being of FTU on a web-site and creation of mark of his location - end
    # Checking for being of record in the base of the sessions key is an end
    # A record of data about the visit of web-site is an end

    # A record in the base of visit of collection (for statistics) is beginning
    searchs_static_collection = Statistic_User_Sing_In_ColProd.objects.filter(session_key=session_key)
    list_searchs_static_collection = []
    for search_static_collection in searchs_static_collection:
        list_searchs_static_collection.append(search_static_collection.collection)
    if str(collection_singl_id) not in list_searchs_static_collection:
        Statistic_User_Sing_In_ColProd.objects.create(session_key=session_key, collection=str(collection_singl_id))
    # A record in the base of visit of collection (for statistics) is an end

    all_info_footer = Footer.objects.filter(is_active=True)

    collection_singl_web = Collection.objects.get(id=collection_singl_id)
    images_for_collection = Collection_Image.objects.filter(is_active_collection=True, name_collection__id=collection_singl_id)
    products_for_collection_singl_web = Product.objects.filter(collection_product=collection_singl_web)

    products_images = Product_Image.objects.filter(is_active=True, is_main=True, product__is_active=True, product__collection_product=collection_singl_id)
    dict_img_products = dict()
    list_img_products = list()
    for products_image in products_images:
        marker = str(products_image.product.id)
        marker_re = "#" + marker

        data_target = str(products_image.product.vendor_code_product)
        data_target_re = "#" + data_target
        id = products_image.product.id
        name = products_image.product.name_product
        dict_img_products = {'id': id, 'name': name,
                             'data_target_re': data_target_re, 'data_target': data_target,
                             'marker_re': marker_re, 'marker': marker}
        list_img_products.append(dict_img_products)

    products_types = Product_Type.objects.all()

    list_type = []
    for product_image in products_images:
        if product_image.product.product_type_product not in list_type:
            list_type.append(product_image.product.product_type_product)

    # Treatment of form on the receipt of order-project on a miscalculation
    data = request.POST

    # The signal processing on switching of language is beginning
    if data.get("submit") == "ukr":
        Log_In_Site.objects.filter(session_key=session_key).update(leng="ukr")
        return redirect('collection_singl_ukr', collection_singl_id_ukr=collection_singl_id)
    # The signal processing on switching of language is an end

    if data.get("submit") == 'find_project':
        form = Find_Project_Form(request.POST, request.FILES)
        if request.POST and form.is_valid:
            data = request.POST
            data_files = request.FILES
            name = data.get("name")
            email = data.get("email")
            phone = data.get("phone")
            adress = data.get("adress")
            comment = data.get("comment")
            project = data_files.get("project")
            send_project_in_base = Find_Project.objects.create(customer_name=name, customer_email=email,
                                                               customer_phone=phone, customer_address=adress,
                                                               comments=comment, project=project, status_id=1,
                                                               session_key=session_key)
            collection_for_static = Collection.objects.get(id=collection_singl_id)

            email_us = "shop.project.cerama.casa@gmail.com"
            password = '12345678qwe'
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email_us, password)
            msg = MIMEMultipart()
            msg['From'] = email_us
            msg['To'] = "bestmen911@gmail.com"
            msg['Subject'] = "Отправлен проект на рассмотрение."
            text = "Отправлен проект на рассмотрение. " + "Коллекция - " + str(collection_for_static.name_collection) + ". " + "ФИО - " + str(name) + ". " + "Email - " + str(email) + ". " + "Телефон - " + str(phone) + ". " + "Адрес - " + str(adress) + ". " + "Комменрарий - " + str(comment) + ". "
            msg.attach(MIMEText(text))
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            server.quit()

            # Block of record of information about departure of project time for consideration is beginning
            Eye.objects.create(session_key=session_key, page="Отправка проекта на рассмотрение",
                               log_in_site=Log_In_Site.objects.get(session_key=session_key), locate_collection=True,
                               send_project=True,
                               send_project_id=send_project_in_base.id)
            # Block of record of information about departure of project time for consideration is an end

            return redirect('collection_singl_project', collection_singl_id=collection_singl_id)

    return render(request, 'products/collection_singl.html', locals())


def collection_singl_ukr(request, collection_singl_id_ukr):
    # A record of data about the visit of web-site is beginning
    session_key = request.session.session_key
    # Checking for being of record in the base of the sessions key is beginning
    collection_for_static = Collection.objects.get(id=collection_singl_id_ukr)
    if Log_In_Site.objects.filter(session_key=session_key).count():
        # Record in the base of mark in track is beginning
        find_max = Eye.objects.filter(session_key=session_key)
        max_id_in = 0
        for find_single in find_max:
            if max_id_in < int(find_single.id):
                max_id_in = int(find_single.id)
        page_max_many = Eye.objects.filter(session_key=session_key, page=str(collection_for_static.name_collection), id=max_id_in)
        if page_max_many.count() != 0:
            for page_max in page_max_many:
                pass
            if page_max.page == str(collection_for_static.name_collection):
                Eye.objects.get(session_key=session_key, page=str(collection_for_static.name_collection), id=max_id_in).delete()

        Eye.objects.create(session_key=session_key,
                           page=str(collection_for_static.name_collection),
                           log_in_site=Log_In_Site.objects.get(session_key=session_key),
                           locate_collection=True)
         # Record in the base of mark in track is an end
    else:
        # Record in the base of being of FTU on a web-site and creation of mark of his location - beginning
        Log_In_Site.objects.create(session_key=session_key, leng="ukr")
        Eye.objects.create(session_key=session_key,
                           page=str(collection_for_static.name_collection),
                           log_in_site=Log_In_Site.objects.get(session_key=session_key, leng="ukr"),
                           locate_collection=True)
        # Record in the base of being of FTU on a web-site and creation of mark of his location - end
    # Checking for being of record in the base of the sessions key is an end
    # A record of data about the visit of web-site is an end

    # A record in the base of visit of collection (for statistics) is beginning
    searchs_static_collection = Statistic_User_Sing_In_ColProd.objects.filter(session_key=session_key)

    list_searchs_static_collection = []

    for search_static_collection in searchs_static_collection:
        list_searchs_static_collection.append(search_static_collection.collection)
    if str(collection_singl_id_ukr) not in list_searchs_static_collection:
        Statistic_User_Sing_In_ColProd.objects.create(session_key=session_key, collection=str(collection_singl_id_ukr))
    # A record in the base of visit of collection (for statistics) is an end

    all_info_footer = Footer.objects.filter(is_active=True)

    collection_singl_web = Collection.objects.get(id=collection_singl_id_ukr)
    images_for_collection = Collection_Image.objects.filter(is_active_collection=True, name_collection__id=collection_singl_id_ukr)
    products_for_collection_singl_web = Product.objects.filter(collection_product=collection_singl_web)

    products_images = Product_Image.objects.filter(is_active=True, is_main=True, product__is_active=True, product__collection_product=collection_singl_id_ukr)
    products_types = Product_Type.objects.all()

    list_type = []
    for product_image in products_images:
        if product_image.product.product_type_product not in list_type:
            list_type.append(product_image.product.product_type_product)

    # Treatment of form on the receipt of order-project on a miscalculation
    data = request.POST

    # The signal processing on switching of language is beginning
    if data.get("submit") == "rus":
        Log_In_Site.objects.filter(session_key=session_key).update(leng="rus")
        return redirect('collection_singl', collection_singl_id=collection_singl_id_ukr)
    # The signal processing on switching of language is an end

    if data.get("submit") == 'find_project':
        form = Find_Project_Form(request.POST, request.FILES)
        if request.POST and form.is_valid:
            data = request.POST
            data_files = request.FILES
            name = data.get("name")
            email = data.get("email")
            phone = data.get("phone")
            adress = data.get("adress")
            comment = data.get("comment")
            project = data_files.get("project")

            send_project_in_base = Find_Project.objects.create(customer_name=name, customer_email=email,
                                                               customer_phone=phone, customer_address=adress,
                                                               comments=comment, project=project, status_id=1,
                                                               session_key=session_key)

            collection_for_static = Collection.objects.get(id=collection_singl_id_ukr)
            # Block of record of information about departure of project time for consideration is beginning
            Eye.objects.create(session_key=session_key, page="Отправка проекта на рассмотрение",
                               log_in_site=Log_In_Site.objects.get(session_key=session_key), locate_collection=True,
                               send_project=True,
                               send_project_id=send_project_in_base.id)
            # Block of record of information about departure of project time for consideration is an end
            return redirect('collection_singl_project_ukr', collection_singl_id_ukr=collection_singl_id_ukr)

            form = Find_Project_Form(request.POST, request.FILES)

    return render(request, 'products/collection_singl_ukr.html', locals())


def products_singl(request, products_singl_id):
    # A record of data about the visit of web-site is beginning
    session_key = request.session.session_key
    # Сhecking for being of record in the base of the session key is beginning
    product_for_static = Product.objects.get(id=products_singl_id)
    if Log_In_Site.objects.filter(session_key=session_key).count():
        # Record in the base of mark in track is beginning
        find_max = Eye.objects.filter(session_key=session_key)
        max_id_in = 0
        for find_single in find_max:
            if max_id_in < int(find_single.id):
                max_id_in = int(find_single.id)
        page_max_many = Eye.objects.filter(session_key=session_key, page=str(product_for_static.name_product), id=max_id_in)
        if page_max_many.count() != 0:
            for page_max in page_max_many:
                pass
            if page_max.page == str(product_for_static.name_product):
                Eye.objects.get(session_key=session_key, page=str(product_for_static.name_product), id=max_id_in).delete()

        Eye.objects.create(session_key=session_key,
                           page=str(product_for_static.name_product),
                           log_in_site=Log_In_Site.objects.get(session_key=session_key),
                           locate_product=True)
        # Record in the base of mark in track is an end
    else:
        # Record in the base of being of FTU on a web-site and creation of mark of his location - beginning
        Log_In_Site.objects.create(session_key=session_key, leng="rus")
        Eye.objects.create(session_key=session_key,
                           page=str(product_for_static.name_product),
                           log_in_site=Log_In_Site.objects.get(session_key=session_key, leng="rus"),
                           locate_product=True)
        # Record in the base of being of FTU on a web-site and creation of mark of his location - end
    # Checking for being of record in the base of the sessions key is an end
    # A record of data about the visit of web-site is an end

    # A record in the base of visit of product (for statistics) is beginning
    searchs_static_product = Statistic_User_Sing_In_ColProd.objects.filter(session_key=session_key)

    list_searchs_static_product = []
    searchs_static_product_single = Product.objects.get(id=products_singl_id)
    Statistic_User_Sing_In_ColProd.objects.create(session_key=session_key, collection_product=str(searchs_static_product_single.collection_product.id))
    # A record in the base of visit of collection (for statistics) is an end

    # A receipt of signal about changing of language is beginning
    data = request.POST
    if data.get("submit") == "ukr":
        Log_In_Site.objects.filter(session_key=session_key).update(leng="ukr")
        return redirect('products_singl_ukr', products_singl_id_ukr=products_singl_id)
    # A receipt of signal about changing of language is an end

    all_info_footer = Footer.objects.filter(is_active=True)

    product_singl_web = Product.objects.get(id=products_singl_id)
    image_for_product_singl_web = Product_Image.objects.filter(product=product_singl_web)

    if not session_key:
        request.session.cycle_key()

    return render(request, 'products/product_singl.html', locals())


def products_singl_ukr(request, products_singl_id_ukr):
    # A record of data about the visit of web-site is beginning
    session_key = request.session.session_key
    # Checking for being of record in the base of the sessions key is beginning
    product_for_static = Product.objects.get(id=products_singl_id_ukr)
    if Log_In_Site.objects.filter(session_key=session_key).count():
        # Record in the base of mark in track is beginning
        find_max = Eye.objects.filter(session_key=session_key)
        max_id_in = 0
        for find_single in find_max:
            if max_id_in < int(find_single.id):
                max_id_in = int(find_single.id)
        page_max_many = Eye.objects.filter(session_key=session_key, page=str(product_for_static.name_product), id=max_id_in)
        if page_max_many.count() != 0:
            for page_max in page_max_many:
                pass
            if page_max.page == str(product_for_static.name_product):
                Eye.objects.get(session_key=session_key, page=str(product_for_static.name_product), id=max_id_in).delete()

        Eye.objects.create(session_key=session_key,
                           page=str(product_for_static.name_product),
                           log_in_site=Log_In_Site.objects.get(session_key=session_key),
                           locate_product=True)
        # Record in the base of mark in track is an end
    else:
        # Record in the base of being of FTU on a web-site and creation of mark of his location - beginning
        Log_In_Site.objects.create(session_key=session_key, leng="ukr")
        Eye.objects.create(session_key=session_key,
                           page=str(product_for_static.name_product),
                           log_in_site=Log_In_Site.objects.get(session_key=session_key, leng="ukr"),
                           locate_product=True)
        # Record in the base of being of FTU on a web-site and creation of mark of his location - end
    # Checking for being of record in the base of the sessions key is an end
    # A record of data about the visit of web-site is an end

    # A record in the base of visit of product (for statistics) is beginning
    searchs_static_product = Statistic_User_Sing_In_ColProd.objects.filter(session_key=session_key)

    list_searchs_static_product = []
    searchs_static_product_single = Product.objects.get(id=products_singl_id_ukr)
    Statistic_User_Sing_In_ColProd.objects.create(session_key=session_key, collection_product=str(searchs_static_product_single.collection_product.id))
    # A record in the base of visit of collection (for statistics) is an end

    #  A receipt of signal on changing of language is beginning
    data = request.POST
    if data.get("submit") == "rus":
        Log_In_Site.objects.filter(session_key=session_key).update(leng="rus")
        return redirect('products_singl', products_singl_id=products_singl_id_ukr)
    # A receipt of signal on changing of language is an end

    all_info_footer = Footer.objects.filter(is_active=True)

    product_singl_web = Product.objects.get(id=products_singl_id_ukr)
    image_for_product_singl_web = Product_Image.objects.filter(product=product_singl_web)

    if not session_key:
        request.session.cycle_key()

    return render(request, 'products/product_singl_ukr.html', locals())


def collection_singl_project(request, collection_singl_id):
    # A record of data about the visit of web-site is beginning
    session_key = request.session.session_key
    # Checking for being of record in the base of the sessions key is beginning
    collection_for_static = Collection.objects.get(id=collection_singl_id)
    if Log_In_Site.objects.filter(session_key=session_key).count():
        # Record in the base of mark in track is beginning
        find_max = Eye.objects.filter(session_key=session_key)
        max_id_in = 0
        for find_single in find_max:
            if max_id_in < int(find_single.id):
                max_id_in = int(find_single.id)
        page_max_many = Eye.objects.filter(session_key=session_key, page="Отправка проекта на рассмотрение",
                                           id=max_id_in)
        if page_max_many.count() != 0:
            for page_max in page_max_many:
                pass
            if page_max.page == "Отправка проекта на рассмотрение":
                Eye.objects.get(session_key=session_key, page="Отправка проекта на рассмотрение",
                                id=max_id_in).delete()

        Eye.objects.create(session_key=session_key,
                           page="Отправка проекта на рассмотрение",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key),
                           locate_collection=True)
        # Record in the base of mark in track is an end
    else:
        # Record in the base of being of FTU on a web-site and creation of mark of his location - beginning
        Log_In_Site.objects.create(session_key=session_key, leng="rus")
        Eye.objects.create(session_key=session_key,
                           page="Отправка проекта на рассмотрение",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key, leng="rus"),
                           locate_collection=True)
        # Record in the base of being of FTU on a web-site and creation of mark of his location - end
    # Checking for being of record in the base of the sessions key is an end
    # A record of data about the visit of web-site is an end

    all_info_footer = Footer.objects.filter(is_active=True)

    collection_singl_web = Collection.objects.get(id=collection_singl_id)

    # The signal processing on switching of language is beginning
    data = request.POST
    if data.get("submit") == "ukr":
        Log_In_Site.objects.filter(session_key=session_key).update(leng="ukr")
        return redirect('collection_singl_project_ukr', collection_singl_id_ukr=collection_singl_id)
    # The signal processing on switching of language is an end

    return render(request, 'products/collection_singl_project.html', locals())


def collection_singl_project_ukr(request, collection_singl_id_ukr):
    # A record of data about the visit of web-site is beginning
    session_key = request.session.session_key
    # Checking for being of record in the base of the sessions key is beginning
    collection_for_static = Collection.objects.get(id=collection_singl_id_ukr)
    if Log_In_Site.objects.filter(session_key=session_key).count():
        # Record in the base of mark in track is beginning
        find_max = Eye.objects.filter(session_key=session_key)
        max_id_in = 0
        for find_single in find_max:
            if max_id_in < int(find_single.id):
                max_id_in = int(find_single.id)
        page_max_many = Eye.objects.filter(session_key=session_key, page="Отправка проекта на рассмотрение",
                                           id=max_id_in)
        if page_max_many.count() != 0:
            for page_max in page_max_many:
                pass
            if page_max.page == "Отправка проекта на рассмотрение":
                Eye.objects.get(session_key=session_key, page="Отправка проекта на рассмотрение",
                                id=max_id_in).delete()

        Eye.objects.create(session_key=session_key,
                           page="Отправка проекта на рассмотрение",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key),
                           locate_collection=True)
        # Record in the base of mark in track is an end
    else:
        # Record in the base of being of FTU on a web-site and creation of mark of his location - beginning
        Log_In_Site.objects.create(session_key=session_key, leng="rus")
        Eye.objects.create(session_key=session_key,
                           page="Отправка проекта на рассмотрение",
                           log_in_site=Log_In_Site.objects.get(session_key=session_key, leng="rus"),
                           locate_collection=True)
        # Record in the base of being of FTU on a web-site and creation of mark of his location - end
    # Checking for being of record in the base of the sessions key is an end
    # A record of data about the visit of web-site is an end

    all_info_footer = Footer.objects.filter(is_active=True)

    collection_singl_web = Collection.objects.get(id=collection_singl_id_ukr)

    # The signal processing on switching of language is beginning
    data = request.POST
    if data.get("submit") == "rus":
        Log_In_Site.objects.filter(session_key=session_key).update(leng="rus")
        return redirect('collection_singl_project', collection_singl_id=collection_singl_id_ukr)
    # The signal processing on switching of language is end

    return render(request, 'products/collection_singl_project_ukr.html', locals())