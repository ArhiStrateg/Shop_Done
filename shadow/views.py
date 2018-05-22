from django.shortcuts import render

from orders.models import Find_Project, Order, Status,ProductInOrder
from shadow.forms import Project_Form_For_Shadow, Order_Form_For_Shadow
from shadow.models import Send_Project, Send_Orders, Statistic_Find_Simple, Statistic_Find_Bloc, Eye, Log_In_Site
from main.models import User_Login
from products.models import Product, Product_Image, Collection, Manufacturer, Manufacturer_Country, Price_Group, Availability, \
    Collection_Search_NHS, Size, Product_Type, Collection_Image, Collection_Colour_For_Search, Collection_Floor_For_Search, \
    Collection_Style_For_Search, Collection_Facturer_For_Search, Collection_Texturer_For_Search, Collection_Type_Material_For_Search, \
    Collection_Application_For_Search

from django.core.files.base import File


from datetime import datetime
import csv
from PIL import Image, ImageDraw
import os


def shadow(request):
    # Verification in the presence of record of registration (connecting of the session key)
    show = False
    session_key = request.session.session_key
    user = User_Login.objects.filter(is_active_login=True, session_key_login=session_key)
    if user:
        show = True
    # Completion of verification in the presence of record of registration (connecting of the session key)

    # Informative block projects and warrants are beginning
    orders_all = Order.objects.filter()
    status_all = Status.objects.filter()

    list_status = []
    sum_result = []

    for status_single in status_all:
        result_order = {}
        list_status.append(status_single.id)

        for status in list_status:
            list_order_status = []
            order_status = Order.objects.filter(status__id=int(status_single.id))
            for order in order_status:
                list_order_status.append(order)
            leni = len(list_order_status)
        result_order.update({"status_id": status_single.id, "leni": leni})
        sum_result.append(result_order)

    progects_all = Find_Project.objects.filter()

    list_status = []
    sum_resul = []

    for status_single in status_all:
        result_project = {}
        list_status.append(status_single.id)

        for status in list_status:
            list_project_status = []
            project_status = Find_Project.objects.filter(status__id=int(status_single.id))
            for project in project_status:
                list_project_status.append(project.id)
            leni = len(list_project_status)
        result_project.update({"project_id": status_single.id, "leni": leni})
        sum_resul.append(result_project)
    # Informative block projects and warrants are an end

    # Informative block statistical data are beginning
    # Collection of information for a simple search is beginning
    statistic_simple = Statistic_Find_Simple.objects.filter()
    # Collection of information for a simple search is an end

    # Collection of information for a sectional search is beginning
    statistic_bloc = Statistic_Find_Bloc.objects.filter()
    # Collection of information for a sectional search is an end

    # Collection of information for statistics of visits of time and users is beginning
    all_users = Log_In_Site.objects.filter()
    # Collection of information for statistics of visits of time and users is an end

    # Collection of information for statistics of visits is beginning
    query_set_manafactur = Eye.objects.filter(locate_manafactur=True)
    # Collection of information for statistics of visits is an end
    # Informative block statistical data are an end

    return render(request, 'shadow/shadow.html', locals())


def shadow_projects(request):
    # Verification in the presence of record of registration (connecting of the session key)
    show = False
    session_key = request.session.session_key
    user = User_Login.objects.filter(is_active_login=True, session_key_login=session_key)
    if user:
        show = True
    # Completion of verification in the presence of record of registration (connecting of the session key)

    status_all = Status.objects.filter()
    status_all_rigth = Status.objects.filter()
    progects_all = Find_Project.objects.filter()

    request_get = request.GET

    request_find = request.GET.getlist('find')
    request_status_id = request.GET.getlist('status_id')
    request_cancel = request.GET.getlist('cancel')

    list_status = []
    sum_resul_right = []

    # Capture of data for the left part of conclusion of information
    for status_single in status_all:
        result_project = {}
        list_status.append(status_single.id)

        for status in list_status:
            list_project_status = []
            project_status = Find_Project.objects.filter(status__id=int(status_single.id))
            for project in project_status:
                list_project_status.append(project)
            leni = len(list_project_status)
        result_project.update({"status_name": status_single.name_status,"id": status_single.id, "leni": leni, "project": list_project_status})
        sum_resul_right.append(result_project)
    # Completion of capture of data for the left part of conclusion of information

    if 'Искать' in request_find:
        if request_status_id != []:
            status_all = Status.objects.filter(id__in=request_status_id)
            for status_id in request_status_id:
                pass
        else:
            pass

    if 'Сбросить фильтр поиска' in request_cancel:
        pass

    list_status = []
    sum_resul = []

    for status_single in status_all:
        result_project = {}
        list_status.append(status_single.id)

        for status in list_status:
            list_project_status = []
            project_status = Find_Project.objects.filter(status__id=int(status_single.id))
            for project in project_status:
                list_project_status.append(project)
            leni = len(list_project_status)
        result_project.update({"status_name": status_single.name_status,"id": status_single.id, "leni": leni, "project": list_project_status})
        sum_resul.append(result_project)

    info_order = {}  # We collect a dictionary for information (last date, amount of comments, ID for attachment)
    list_id = []
    list_id_result = []

    data_info_vtor = Send_Project.objects.filter()

    for data_info in data_info_vtor:
        if data_info.project.id not in list_id:
            list_id.append(int(data_info.project.id))

    for ftor in list_id:
        info_order = {}
        dlinna = Send_Project.objects.filter(project=ftor).count()
        summa_quer = Send_Project.objects.filter(project=ftor)

        max_id_info = 0

        for summa in summa_quer:
            if summa.id > max_id_info:
                max_id_info = summa.id

        info_order.update({"id_project": ftor, "leni": dlinna, "max_id": Send_Project.objects.get(id=max_id_info)})
        list_id_result.append(info_order)

    return render(request, 'shadow/shadow_projects.html', locals())


def shadow_orders(request):
    # Verification in the presence of record of registration (connecting of the session key)
    show = False
    session_key = request.session.session_key
    user = User_Login.objects.filter(is_active_login=True, session_key_login=session_key)
    if user:
        show = True
    # Completion of verification in the presence of record of registration (connecting of the session key)

    orders_all = Order.objects.filter()
    status_all = Status.objects.filter()
    products_in_orders = ProductInOrder.objects.filter()

    request_get = request.GET

    request_find = request.GET.getlist('find')
    request_status_id = request.GET.getlist('status_id')
    request_cancel = request.GET.getlist('cancel')

    # Capture of data for the left part of conclusion of information
    list_status = []
    sum_result_right = []

    for status_single in status_all:
        result_order = {}
        list_status.append(status_single.id)

        for status in list_status:
            list_order_status = []
            order_status = Order.objects.filter(status__id=int(status_single.id))
            for order in order_status:
                list_order_status.append(order)
            leni = int(len(list_order_status))
        result_order.update({"status_name": status_single.name_status, "id": status_single.id,  "leni": leni, "orders": list_order_status})
        sum_result_right.append(result_order)
    # Completion of capture of data for the left part of conclusion of information

    if 'Искать' in request_find:
        if request_status_id != []:
            status_all = Status.objects.filter(id__in=request_status_id)
            for status_id in request_status_id:
                pass
        else:
            pass

    if 'Сбросить фильтр поиска' in request_cancel:
        pass


    list_status = []
    sum_result = []

    for status_single in status_all:
        result_order = {}
        list_status.append(status_single.id)

        for status in list_status:
            list_order_status = []
            order_status = Order.objects.filter(status__id=int(status_single.id))
            for order in order_status:
                list_order_status.append(order)
            leni = int(len(list_order_status))
        result_order.update({"status_name": status_single.name_status, "id": status_single.id,  "leni": leni, "orders": list_order_status})
        sum_result.append(result_order)

    info_order = {}  # We collect a dictionary for second-rate information (date, comments, ID for attachment)
    list_id = []
    list_id_result = []

    data_info_vtor = Send_Orders.objects.filter()

    for data_info in data_info_vtor:
        if data_info.order.id not in list_id:
            list_id.append(int(data_info.order.id))

    for ftor in list_id:
        info_order = {}
        dlinna = Send_Orders.objects.filter(order=ftor).count()
        summa_quer = Send_Orders.objects.filter(order=ftor)

        max_id_info = 0

        for summa in summa_quer:
            if summa.id > max_id_info:
                max_id_info = summa.id

        info_order.update({"id_order": ftor, "leni": dlinna, "max_id": Send_Orders.objects.get(id=max_id_info)})
        list_id_result.append(info_order)

    return render(request, 'shadow/shadow_orders.html', locals())


def project_singl(request, project_singl_id):
    # Verification in the presence of record of registration (connecting of the session key)
    show = False
    session_key = request.session.session_key
    user = User_Login.objects.filter(is_active_login=True, session_key_login=session_key)
    if user:
        show = True
    # Completion of verification in the presence of record of registration (connecting of the session key)

    project_singl_one = Find_Project.objects.get(id=project_singl_id)
    text_send = Send_Project.objects.filter(project=Find_Project.objects.get(id=project_singl_id))

    all_status = Status.objects.all()

    request_get_status = request.GET.getlist('status')
    request_get_save = request.GET.getlist('save')

    form = Project_Form_For_Shadow(request.POST, request.FILES)
    if request.POST and form.is_valid:
        data = request.POST

        files_data = request.FILES
        files_data = files_data.get('project')

        save_status = data.get('status')
        save_true = data.get('save')

        save_project = data.get('project')
        save_comment = data.get('comment')

        if save_true == 'Сохранить изменение' and save_status != []:
            save_status = ''.join(save_status)  # We translate from a list in to the flow of value in status
            Find_Project.objects.filter(id=project_singl_id).update(status=int(save_status))  # We produce a record in a base - RECOVERY of data

        if save_true == 'Save comment' and (save_project != [] or save_comment != []):
            save_comment = ''.join(save_comment)  # We translate from a list in to the flow of value in status

            Send_Project.objects.create(text_send=save_comment, project_img=files_data,
                                        project=Find_Project.objects.get(id=project_singl_id),
                                        autor=User_Login.objects.get(is_active_login=True, session_key_login=session_key))

    project_singl_one = Find_Project.objects.get(id=project_singl_id)
    text_send = Send_Project.objects.filter(project=Find_Project.objects.get(id=project_singl_id))

    lovim = 0
    data_max = 0

    for max_id in text_send:  # Search of the last date coming from maximal ID
        lovim = max_id.id
        if lovim > data_max:
            data_max = lovim

    if data_max != 0:
        data_max = Send_Project.objects.get(project=Find_Project.objects.get(id=project_singl_id), id=data_max)


    return render(request, 'shadow/shadow_project_singl.html', locals())


def order_singl(request, order_singl_id):
    # Verification in the presence of record of registration (connecting of the session key)
    show = False
    session_key = request.session.session_key
    user = User_Login.objects.filter(is_active_login=True, session_key_login=session_key)
    if user:
        show = True
    # Completion of verification in the presence of record of registration (connecting of the session key)

    session_key = request.session.session_key

    order_singl_one = Order.objects.get(id=order_singl_id)
    text_send = Send_Orders.objects.filter(order=Order.objects.get(id=order_singl_id))
    product_in_order = ProductInOrder.objects.filter(order=Order.objects.get(id=order_singl_id))

    all_status = Status.objects.all()

    request_get_status = request.GET.getlist('status')
    request_get_save = request.GET.getlist('save')

    form = Order_Form_For_Shadow(request.POST, request.FILES)
    if request.POST and form.is_valid:
        data = request.POST

        files_data = request.FILES
        files_data = files_data.get('order')

        save_status = data.get('status')
        save_true = data.get('save')

        save_order = data.get('order')
        save_comment = data.get('comment')

        if save_true == 'Сохранить изменение' and save_status != "":
            save_status = ''.join(save_status)  # We translate from a list in to the flow of value in status
            Order.objects.filter(id=order_singl_id).update(status=int(save_status))  # We produce a record in a base - RECOVERY of data

        if save_true == 'Save comment' and (save_order != [] or save_comment != []):
            save_comment = ''.join(save_comment)  # We translate from a list in to the flow of value in status

            Send_Orders.objects.create(text_send=save_comment, order_img=files_data, order=Order.objects.get(id=order_singl_id),
                                       autor=User_Login.objects.get(is_active_login=True, session_key_login=session_key))

        if save_true == 'Сохранить изменения в заказе':

            for name, value in data.items():  # Logic of making alteration in WARRANTS
                if name.startswith("product_in_order_"):
                    product_in_order_up_id = name.split("product_in_order_")[1]
                    product_in_order_up = ProductInOrder.objects.get(id=product_in_order_up_id, is_active=True)
                    product_in_order_up.nmb = int(value)
                    product_in_order_up.save(force_update=True)

            for name_d, value_d in data.items():  # Logic of moving away from WARRANT
                if name_d.startswith("product_is_delet_"):
                    products_in_bascet_no_active = name_d.split("product_is_delet_")[1]
                    product_in_order_del = ProductInOrder.objects.get(id=products_in_bascet_no_active, is_active=True)
                    product_in_order_del.delete()

    order_singl_one = Order.objects.get(id=order_singl_id)
    text_send = Send_Orders.objects.filter(order=Order.objects.get(id=order_singl_id))

    lovim = 0
    data_max = 0

    for max_id in text_send:  # Search of the last date coming from maximal ID
        lovim = max_id.id
        if lovim > data_max:
            data_max = lovim

    if data_max != 0:
        data_max = Send_Orders.objects.get(order=Order.objects.get(id=order_singl_id), id=data_max)

    return render(request, 'shadow/shadow_order_singl.html', locals())


def statistic(request):
    # Verification in the presence of record of registration (connecting of the session key)
    show = False
    session_key = request.session.session_key
    user = User_Login.objects.filter(is_active_login=True, session_key_login=session_key)
    if user:
        show = True
    # Completion of verification in the presence of record of registration (connecting of the session key)

    session_key = request.session.session_key
    now = datetime.now()
    now = datetime.date(now)

    # Collection of information for a simple search is beginning
    statistic_simple = Statistic_Find_Simple.objects.filter()

    list_statistic_now = []
    list_statistic_for_manafactor = []
    list_statistic_for_manafactor_now = []
    list_statistic_for_collection = []
    list_statistic_for_collection_now = []

    for statistic in statistic_simple:
        if now == datetime.date(statistic.created):
            list_statistic_now.append(statistic.created)

        if statistic.find_collections:
            list_statistic_for_collection.append(statistic)
            if now == datetime.date(statistic.created):
                list_statistic_for_collection_now.append(statistic)

        if statistic.find_manafacturer:
            list_statistic_for_manafactor.append(statistic)
            if now == datetime.date(statistic.created):
                list_statistic_for_manafactor_now.append(statistic)

    len_list_statistic_now = len(list_statistic_now)
    len_list_statistic_for_collection = len(list_statistic_for_collection)
    len_list_statistic_for_collection_now = len(list_statistic_for_collection_now)
    len_list_statistic_for_manafactor = len(list_statistic_for_manafactor)
    len_list_statistic_for_manafactor_now = len(list_statistic_for_manafactor_now)

    # Collection of information for a simple search is an end

    # Collection of information for a sectional search is beginning
    statistic_bloc = Statistic_Find_Bloc.objects.filter()

    list_statistic_bloc_now = []
    list_statistic_for_bloc_search = []
    list_statistic_for_bloc_search_now = []
    list_statistic_for_minus_bloc_search = []
    list_statistic_for_minus_bloc_search_now = []

    for statistic in statistic_bloc:
        if now == datetime.date(statistic.created):
            list_statistic_bloc_now.append(statistic.created)

        if statistic.page == "search_hight":
            list_statistic_for_bloc_search.append(statistic)
            if now == datetime.date(statistic.created):
                list_statistic_for_bloc_search_now.append(statistic)

        if statistic.page != "search_hight":
            list_statistic_for_minus_bloc_search.append(statistic)
            if now == datetime.date(statistic.created):
                list_statistic_for_minus_bloc_search_now.append(statistic)

    len_list_statistic_bloc_now = len(list_statistic_bloc_now)
    len_list_statistic_for_bloc_search = len(list_statistic_for_bloc_search)
    len_list_statistic_for_bloc_search_now = len(list_statistic_for_bloc_search_now)
    len_list_statistic_for_minus_bloc_search = len(list_statistic_for_minus_bloc_search)
    len_list_statistic_for_minus_bloc_search_now = len(list_statistic_for_minus_bloc_search_now)
    # Collection of information for a sectional search is an end

    # Collection of information for statistics of visits of time and users is beginning
    all_users = Log_In_Site.objects.filter()
    all_users_project = Eye.objects.filter(page="Отправка проекта на рассмотрение")
    all_users_buy = Eye.objects.filter(page="Окончание оформления ордера")

    # Conclusion of information about time of user after today is beginning
    all_users_time_now = []
    for user in all_users:
        data_in = user.created
        if now == datetime.date(data_in):
            all_users_time_now.append(user.session_key)

    list_all_users_now = []
    dict_all_users_now = {}
    nmb_all_users_now = 0
    time_delta = now - now
    for user in all_users_time_now:
        created_time = Log_In_Site.objects.get(session_key=user)
        created_time = created_time.created
        max_id = 0
        for eye_max in Eye.objects.filter(session_key=user):
            eye_max_in = eye_max.id
            if max_id < eye_max_in:
                max_id = eye_max_in
        max_id = Eye.objects.get(id=max_id)
        max_id = max_id.created

        time_delta = max_id - created_time

        list_all_users_now.append(time_delta)
        nmb_all_users_now += 1

    summa_time_now = time_delta - time_delta
    for user in list_all_users_now:
        summa_time_now += user

    if nmb_all_users_now == 0:
        mid_time_now = 0
    if nmb_all_users_now != 0:
        mid_time_now = summa_time_now / nmb_all_users_now
    # Conclusion of information about time of user after today is an end

    # Conclusion of information about time of users for complete period - beginning
    nmb_users = Log_In_Site.objects.filter().count()
    list_all_users = []
    dict_all_users = {}
    nmb_all_users = 0
    for user in all_users:
        created_time = Log_In_Site.objects.get(session_key=user.session_key)
        created_time = created_time.created
        max_id = 0
        for eye_max in Eye.objects.filter(session_key=user.session_key):
            eye_max_in = eye_max.id
            if max_id < eye_max_in:
                max_id = eye_max_in
        max_id = Eye.objects.get(id=max_id)
        max_id = max_id.created

        time_delta = max_id - created_time

        list_all_users.append(time_delta)
        nmb_all_users += 1

    summa_time = time_delta - time_delta
    for user in list_all_users:
        summa_time += user

    mid_time = summa_time/nmb_all_users
    # Conclusion of information about time of user for complete period - beginning
    # Collection of information for statistics of visits of time and users is an end

    # Collection of information for statistics of visits is beginning
    query_set_manafactur = Eye.objects.filter(locate_manafactur=True)
    query_set_collection = Eye.objects.filter(locate_collection=True)
    query_set_product = Eye.objects.filter(locate_product=True)

    # Cleaning of query about collections from a -=Send project on view=- is beginning
    list_query_set_collection_swap = []
    for query_set in query_set_collection:
        if query_set.page != "Отправка проекта на рассмотрение":
            list_query_set_collection_swap.append(query_set.id)
    query_set_collection = Eye.objects.filter(id__in=list_query_set_collection_swap)
    # Cleaning of query about collections from a -=Send project on view=- is end

    list_manafactur = []
    for query in query_set_manafactur:
        data_in = query.created
        if now == datetime.date(data_in):
            list_manafactur.append(query.id)

    query_set_manafacturer_now = Eye.objects.filter(locate_manafactur=True, id__in=list_manafactur)

    list_collection = []
    for query in query_set_collection:
        data_in = query.created
        if now == datetime.date(data_in):
            list_collection.append(query.id)

    query_set_collection_now = Eye.objects.filter(locate_collection=True, id__in=list_collection)

    list_product = []
    for query in query_set_product:
        data_in = query.created
        if now == datetime.date(data_in):
            list_product.append(query.id)

    query_set_product_now = Eye.objects.filter(locate_product=True, id__in=list_product)
    # Collection of information for statistics of visits is an end

    return render(request, 'shadow/statistic.html', locals())


def statistic_simple_find(request):
    # Verification in the presence of record of registration (connecting of the session key)
    show = False
    session_key = request.session.session_key
    user = User_Login.objects.filter(is_active_login=True, session_key_login=session_key)
    if user:
        show = True
    # Completion of verification in the presence of record of registration (connecting of the session key)

    statistic_simple = Statistic_Find_Simple.objects.filter()
    now = datetime.now()
    now = datetime.date(now)

    list_statistic_for_manafactor = []
    list_statistic_for_manafactor_now = []
    list_statistic_for_collection = []
    list_statistic_for_collection_now = []
    list_statistic_now = []

    for statistic_single_simple in statistic_simple:
        if now == datetime.date(statistic_single_simple.created):
            list_statistic_now.append(statistic_single_simple)

        if statistic_single_simple.find_collections:
            list_statistic_for_collection.append(statistic_single_simple)
            if now == datetime.date(statistic_single_simple.created):
                list_statistic_for_collection_now.append(statistic_single_simple)

        if statistic_single_simple.find_manafacturer:
            list_statistic_for_manafactor.append(statistic_single_simple)
            if now == datetime.date(statistic_single_simple.created):
                list_statistic_for_manafactor_now.append(statistic_single_simple)

        len_list_statistic_for_collection = len(list_statistic_for_collection)
        len_list_statistic_for_collection_now = len(list_statistic_for_collection_now)
        len_list_statistic_for_manafactor = len(list_statistic_for_manafactor)
        len_list_statistic_for_manafactor_now = len(list_statistic_for_manafactor_now)
        len_list_statistic_now = len(list_statistic_now)

    # Complete data on statistics of collections (complete period) are beginning
    result_find_collection = {}

    for statist_single_collection in list_statistic_for_collection:  # We sort out a list with objects from a base

        len_statist_single_collection = len(statist_single_collection.find_collections)
        one_statist_single_collection = statist_single_collection.find_collections
        srez_statist_single_collection = one_statist_single_collection[1:len_statist_single_collection - 1]  # We are released from []
        if len(srez_statist_single_collection) == 1:
            proverka = True
            if srez_statist_single_collection not in result_find_collection and proverka == True:
                result_find_collection[srez_statist_single_collection] = 1
                proverka = False

            if srez_statist_single_collection in result_find_collection and proverka == True:
                result_find_collection[srez_statist_single_collection] += 1

        if len(srez_statist_single_collection) != 1:
            list_in_srez_statist_single_collection = srez_statist_single_collection.split(", ")
            for psevdo_result in list_in_srez_statist_single_collection:
                proverka_other = True

                if psevdo_result not in result_find_collection and proverka_other == True:
                    result_find_collection[psevdo_result] = 1
                    proverka_other = False

                if psevdo_result in result_find_collection and proverka_other == True:
                    result_find_collection[psevdo_result] += 1

    summa = 0
    for find_collection in result_find_collection:
        summa += result_find_collection[find_collection]

    spisok_find_collection = []

    for find_collection in result_find_collection:
        collection = Collection.objects.get(id=int(find_collection))
        slovar_find_collection = {"name_collection": collection.name_collection,
                                  "kol_povtor": result_find_collection[find_collection],
                                  "prosent": int((100/summa)*result_find_collection[find_collection])}
        if (100/summa)*result_find_collection[find_collection] > 9:
            spisok_find_collection.append(slovar_find_collection)

    # Complete data on statistics of collections (complete period) are an end

    # Complete data on statistics of collections (after today) are beginning
    result_find_collection_now = {}

    for statist_single_collection in list_statistic_for_collection_now:  # We sort out a list with objects from a base

        len_statist_single_collection = len(statist_single_collection.find_collections)
        one_statist_single_collection = statist_single_collection.find_collections
        srez_statist_single_collection = one_statist_single_collection[
                                         1:len_statist_single_collection - 1]  # We are released from []
        if len(srez_statist_single_collection) == 1:
            proverka = True
            if srez_statist_single_collection not in result_find_collection_now and proverka == True:
                result_find_collection_now[srez_statist_single_collection] = 1
                proverka = False

            if srez_statist_single_collection in result_find_collection_now and proverka == True:
                result_find_collection_now[srez_statist_single_collection] += 1

        if len(srez_statist_single_collection) != 1:
            list_in_srez_statist_single_collection = srez_statist_single_collection.split(", ")
            for psevdo_result in list_in_srez_statist_single_collection:
                proverka_other = True

                if psevdo_result not in result_find_collection_now and proverka_other == True:
                    result_find_collection_now[psevdo_result] = 1
                    proverka_other = False

                if psevdo_result in result_find_collection_now and proverka_other == True:
                    result_find_collection_now[psevdo_result] += 1

    summa = 0
    for find_collection in result_find_collection_now:
        summa += result_find_collection_now[find_collection]

    spisok_find_collection_now = []

    for find_collection in result_find_collection_now:
        collection = Collection.objects.get(id=int(find_collection))
        slovar_find_collection = {"name_collection": collection.name_collection,
                                  "kol_povtor": result_find_collection_now[find_collection],
                                  "prosent": int((100 / summa) * result_find_collection_now[find_collection])}
        if (100 / summa) * result_find_collection_now[find_collection] > 9:
            spisok_find_collection_now.append(slovar_find_collection)

    # Complete data on statistics of collections (after today) are an end

    # Complete data on statistics of producers (complete period) are beginning
    result_find_manafacturer = {}

    for statist_single_manafacturer in list_statistic_for_manafactor:  # We sort out a list with objects from a base

        len_statist_single_manafacturer = len(statist_single_manafacturer.find_manafacturer)
        one_statist_single_manafacturer = statist_single_manafacturer.find_manafacturer
        srez_statist_single_manafacturer = one_statist_single_manafacturer[
                                         1:len_statist_single_manafacturer - 1]  # We are released from []
        if len(srez_statist_single_manafacturer) == 1:
            proverka = True
            if srez_statist_single_manafacturer not in result_find_manafacturer and proverka == True:
                result_find_manafacturer[srez_statist_single_manafacturer] = 1
                proverka = False

            if srez_statist_single_manafacturer in result_find_manafacturer and proverka == True:
                result_find_manafacturer[srez_statist_single_manafacturer] += 1

        if len(srez_statist_single_manafacturer) != 1:
            list_in_srez_statist_single_manafacturer = srez_statist_single_manafacturer.split(", ")
            for psevdo_result in list_in_srez_statist_single_manafacturer:
                proverka_other = True

                if psevdo_result not in result_find_manafacturer and proverka_other == True:
                    result_find_manafacturer[psevdo_result] = 1
                    proverka_other = False

                if psevdo_result in result_find_manafacturer and proverka_other == True:
                    result_find_manafacturer[psevdo_result] += 1

    summa = 0
    for find_manafacturer in result_find_manafacturer:
        summa += result_find_manafacturer[find_manafacturer]

    spisok_find_manafacturer = []

    for find_manafacturer in result_find_manafacturer:
        manafacturer = Collection.objects.get(id=int(find_manafacturer))
        slovar_find_manafacturer = {"name_manafacturer_collection": manafacturer.name_collection,
                                  "kol_povtor": result_find_manafacturer[find_manafacturer],
                                  "prosent": int((100 / summa) * result_find_manafacturer[find_manafacturer])}
        if (100 / summa) * result_find_manafacturer[find_collection] > 9:
            spisok_find_manafacturer.append(slovar_find_manafacturer)

    # Complete data on statistics of producers (complete period) are an end

    # Complete data on statistics of producers (after today) are beginning
    result_find_manafacturer_now = {}

    for statist_single_manafactor_now in list_statistic_for_manafactor_now:  # We sort out a list with objects from a base

        len_statist_single_manafacturer_now = len(statist_single_manafactor_now.find_manafacturer)
        one_statist_single_manafacturer_now = statist_single_manafactor_now.find_manafacturer
        srez_statist_single_manafacturer_now = one_statist_single_manafacturer_now[
                                         1:len_statist_single_manafacturer_now - 1]  # Избавляемся от []
        if len(srez_statist_single_manafacturer_now) == 1:
            proverka = True
            if srez_statist_single_manafacturer_now not in result_find_manafacturer_now and proverka == True:
                result_find_manafacturer_now[srez_statist_single_manafacturer_now] = 1
                proverka = False

            if srez_statist_single_manafacturer_now in result_find_manafacturer_now and proverka == True:
                result_find_manafacturer_now[srez_statist_single_manafacturer_now] += 1

        if len(srez_statist_single_manafacturer_now) != 1:
            list_in_srez_statist_single_manafacturer_now = srez_statist_single_manafacturer_now.split(", ")
            for psevdo_result in list_in_srez_statist_single_manafacturer_now:
                proverka_other = True

                if psevdo_result not in result_find_manafacturer_now and proverka_other == True:
                    result_find_manafacturer_now[psevdo_result] = 1
                    proverka_other = False

                if psevdo_result in result_find_manafacturer_now and proverka_other == True:
                    result_find_manafacturer_now[psevdo_result] += 1

    summa = 0
    for find_manafacturer_now in result_find_manafacturer_now:
        summa += result_find_manafacturer_now[find_manafacturer_now]

    spisok_find_manafacturer_now = []

    for find_manafacturer in result_find_manafacturer_now:
        collection = Collection.objects.get(id=int(find_manafacturer))
        slovar_find_manafacturer_now = {"name_manafacturer_now": collection.name_collection,
                                  "kol_povtor": result_find_manafacturer_now[find_manafacturer],
                                  "prosent": int((100 / summa) * result_find_manafacturer_now[find_manafacturer])}
        if (100 / summa) * result_find_manafacturer_now[find_manafacturer] > 9:
            spisok_find_manafacturer_now.append(slovar_find_manafacturer_now)

    # Complete data on statistics of producers (after today) are an end

    # Complete data on statistics of producers (complete period) are beginning
    result_find = {}

    for statist in statistic_simple:

        if statist.find_manafacturer == None:
            len_statist_collections = len(statist.find_collections)
            one_statist_collections = statist.find_collections
            srez_statist_collections = one_statist_collections[
                                               1:len_statist_collections - 1]  # Избавляемся от []
            if len(srez_statist_collections) == 1:
                proverka = True
                if srez_statist_collections not in result_find and proverka == True:
                    result_find[srez_statist_collections] = 1
                    proverka = False
                if srez_statist_collections in result_find and proverka == True:
                    result_find[srez_statist_collections] += 1
            if len(srez_statist_collections) != 1:
                list_in_srez_statist_collections = srez_statist_collections.split(", ")
                for psevdo_result in list_in_srez_statist_collections:
                    proverka_other = True
                    if psevdo_result not in result_find and proverka_other == True:
                        result_find[psevdo_result] = 1
                        proverka_other = False
                    if psevdo_result in result_find and proverka_other == True:
                        result_find[psevdo_result] += 1


        if statist.find_collections == None:
            len_statist_manafacturer = len(statist.find_manafacturer)
            one_statist_manafacturer = statist.find_manafacturer
            srez_statist_manafacturer = one_statist_manafacturer[
                                               1:len_statist_manafacturer - 1]  # Избавляемся от []
            if len(srez_statist_manafacturer) == 1:
                proverka = True
                if srez_statist_manafacturer not in result_find and proverka == True:
                    result_find[srez_statist_manafacturer] = 1
                    proverka = False

                if srez_statist_manafacturer in result_find and proverka == True:
                    result_find[srez_statist_manafacturer] += 1

            if len(srez_statist_manafacturer) != 1:
                list_in_srez_statist_manafacturer = srez_statist_manafacturer.split(", ")
                for psevdo_result in list_in_srez_statist_manafacturer:
                    proverka_other = True

                    if psevdo_result not in result_find and proverka_other == True:
                        result_find[psevdo_result] = 1
                        proverka_other = False

                    if psevdo_result in result_find and proverka_other == True:
                        result_find[psevdo_result] += 1

    summa = 0
    for find in result_find:
        summa += result_find[find]

    spisok_find = []

    for find in result_find:
        manafacturer = Collection.objects.get(id=int(find))
        slovar_find = {"name_manafacturer_collection": manafacturer.name_collection,
                                    "kol_povtor": result_find[find],
                                    "prosent": int((100 / summa) * result_find[find])}
        if (100 / summa) * result_find[find] > 9:
            spisok_find.append(slovar_find)

    # Complete data on statistics of producers (complete period) are an end

    # Complete data on statistics (for a day) are beginning
    result_find_now = {}

    for statist_now in list_statistic_now:

        if statist_now.find_manafacturer == None:
            len_statist_now_collections = len(statist_now.find_collections)
            one_statist_now_collections = statist_now.find_collections
            srez_statist_now_collections = one_statist_now_collections[
                                       1:len_statist_now_collections - 1]  # Избавляемся от []

            if len(srez_statist_now_collections) == 1:
                proverka = True
                if srez_statist_now_collections not in result_find_now and proverka == True:
                    result_find_now[srez_statist_now_collections] = 1
                    proverka = False
                if srez_statist_now_collections in result_find_now and proverka == True:
                    result_find_now[srez_statist_now_collections] += 1

            if len(srez_statist_now_collections) != 1:
                list_in_srez_statist_now_collections = srez_statist_now_collections.split(", ")
                for psevdo_result in list_in_srez_statist_now_collections:
                    proverka_other = True
                    if psevdo_result not in result_find_now and proverka_other == True:
                        result_find_now[psevdo_result] = 1
                        proverka_other = False
                    if psevdo_result in result_find_now and proverka_other == True:
                        result_find_now[psevdo_result] += 1

        if statist_now.find_collections == None:

            len_statist_now_manafacturer = len(statist_now.find_manafacturer)
            one_statist_now_manafacturer = statist_now.find_manafacturer
            srez_statist_now_manafacturer = one_statist_now_manafacturer[
                                        1:len_statist_now_manafacturer - 1]  # Избавляемся от []
            if len(srez_statist_now_manafacturer) == 1:
                proverka = True
                if srez_statist_now_manafacturer not in result_find_now and proverka == True:
                    result_find_now[srez_statist_now_manafacturer] = 1
                    proverka = False

                if srez_statist_now_manafacturer in result_find_now and proverka == True:
                    result_find_now[srez_statist_now_manafacturer] += 1

            if len(srez_statist_now_manafacturer) != 1:
                list_in_srez_statist_now_manafacturer = srez_statist_now_manafacturer.split(", ")
                for psevdo_result in list_in_srez_statist_now_manafacturer:
                    proverka_other = True

                    if psevdo_result not in result_find_now and proverka_other == True:
                        result_find_now[psevdo_result] = 1
                        proverka_other = False

                    if psevdo_result in result_find_now and proverka_other == True:
                        result_find_now[psevdo_result] += 1

    summa = 0
    for find_now in result_find_now:
        summa += result_find_now[find_now]

    spisok_find_now = []

    for find_now in result_find_now:
        manafacturer = Collection.objects.get(id=int(find_now))
        slovar_find_now = {"name_manafacturer_collection_now": manafacturer.name_collection,
                       "kol_povtor": result_find_now[find_now],
                       "prosent": int((100 / summa) * result_find_now[find_now])}
        if (100 / summa) * result_find_now[find_now] > 9:
            spisok_find_now.append(slovar_find_now)

    # Complete data on statistics of producers (for a day) are an end

    return render(request, 'shadow/statistic_simple_find.html', locals())


def statistic_bloc_find(request):
    # Verification in the presence of record of registration (connecting of the session key)
    show = False
    session_key = request.session.session_key
    user = User_Login.objects.filter(is_active_login=True, session_key_login=session_key)
    if user:
        show = True
    # Completion of verification in the presence of record of registration (connecting of the session key)

    # Collection of information for a sectional search is beginning
    statistics_bloc = Statistic_Find_Bloc.objects.filter()
    statistics_bloc_search_hight = Statistic_Find_Bloc.objects.filter(page="search_hight")
    statistics_bloc_not_in = Statistic_Find_Bloc.objects.exclude(page="search_hight")
    now = datetime.now()
    now = datetime.date(now)

    list_statistic_bloc_now = []
    list_statistic_for_bloc_search = []
    list_statistic_for_bloc_search_now = []
    list_statistic_for_minus_bloc_search = []
    list_statistic_for_minus_bloc_search_now = []

    for statistic in statistics_bloc:
        if now == datetime.date(statistic.created):
            list_statistic_bloc_now.append(statistic)

        if statistic.page == "search_hight":
            list_statistic_for_bloc_search.append(statistic)
            if now == datetime.date(statistic.created):
                list_statistic_for_bloc_search_now.append(statistic)

        if statistic.page != "search_hight":
            list_statistic_for_minus_bloc_search.append(statistic)
            if now == datetime.date(statistic.created):
                list_statistic_for_minus_bloc_search_now.append(statistic)

    len_list_statistic_bloc_now = len(list_statistic_bloc_now)
    len_list_statistic_for_bloc_search = len(list_statistic_for_bloc_search)
    len_list_statistic_for_bloc_search_now = len(list_statistic_for_bloc_search_now)
    len_list_statistic_for_minus_bloc_search = len(list_statistic_for_minus_bloc_search)
    len_list_statistic_for_minus_bloc_search_now = len(list_statistic_for_minus_bloc_search_now)
    # Collection of information for a sectional search is an end

    # Complete data on general statistics of sectional queries (complete period) are beginning
    vol_id_collection = []
    result_bloc_find = {}
    vtorostepen_result_bloc_find = []

    # We sort out all data from a base on sectional queries is a result a list from ID of all collections is beginning
    for statistic_bloc in statistics_bloc:
        len_statistic_bloc = len(str(statistic_bloc.collection))
        srez_bloc = str(statistic_bloc.collection)[1:len_statistic_bloc - 1]  # We produce the cut of line deleting from []
        if len(srez_bloc) == 1:
            vol_id_collection.append(int(srez_bloc))

        if len(srez_bloc) > 1:
            infos_srez_bloc = srez_bloc.split(", ")
            for info_srez_bloc in infos_srez_bloc:
                vol_id_collection.append(int(info_srez_bloc))
    # We sort out all data from a base on sectional queries is a result a list from IDES of all collections is an end

    # We create a list from single IDES of collections is beginning
    for vo_id_collection in vol_id_collection:
        if vo_id_collection not in vtorostepen_result_bloc_find:
            vtorostepen_result_bloc_find.append(vo_id_collection)
    # We create a list from single ID of collections is beginning

    # We create a dictionary with key is the name of collection and by an amount and percent is beginning
    list_result_bloc_find = []
    povtor_summa_bloc = 0
    for vtorostep_result_bloc_find in vtorostepen_result_bloc_find:
        result_bloc_find = {'id_collection': vtorostep_result_bloc_find, 'povtor': vol_id_collection.count(vtorostep_result_bloc_find)}
        list_result_bloc_find.append(result_bloc_find)
        povtor_summa_bloc += vol_id_collection.count(vtorostep_result_bloc_find)

    result_for_web_blok_dict = {}
    result_for_web_blok = []
    for result_bloc_find_single in list_result_bloc_find:
        bloc_collection_single = Collection.objects.get(id=int(result_bloc_find_single['id_collection']))
        result_for_web_blok_dict = {'name_collection': bloc_collection_single.name_collection, 'povtor': int(result_bloc_find_single['povtor']),
                                    'prosent': int((100/povtor_summa_bloc)*result_bloc_find_single['povtor'])}
        if int((100/povtor_summa_bloc)*result_bloc_find_single['povtor']) > 9:
            result_for_web_blok.append(result_for_web_blok_dict)

    # We create a dictionary with key is the name of collection and by an amount and percent is an end
    # Complete data on general statistics of sectional queries (complete period) are an end

    # Complete data on general statistics of sectional queries (for this day) are beginning
    vol_id_collection_now = []
    result_bloc_find_now = {}
    vtorostepen_result_bloc_find_now = []

    # We sort out all data from a base on sectional queries is a result a list from ID of all collections is beginning
    for statistic_bloc in list_statistic_bloc_now:
        len_statistic_bloc = len(str(statistic_bloc.collection))
        srez_bloc = str(statistic_bloc.collection)[1:len_statistic_bloc - 1]  # Производим срез строки избавляясь от []
        if len(srez_bloc) == 1:
            vol_id_collection_now.append(int(srez_bloc))

        if len(srez_bloc) > 1:
            infos_srez_bloc = srez_bloc.split(", ")
            for info_srez_bloc in infos_srez_bloc:
                vol_id_collection_now.append(int(info_srez_bloc))
    # We sort out all data from a base on sectional queries is a result a list from ID of all collections is an end

    # We create a list from single ID of collections is beginning
    for vo_id_collection in vol_id_collection_now:
        if vo_id_collection not in vtorostepen_result_bloc_find_now:
            vtorostepen_result_bloc_find_now.append(vo_id_collection)
    # We create a list from single ID of collections is beginning

    # We create a dictionary with key is the name of collection and by an amount and percent is beginning
    list_result_bloc_find_now = []
    povtor_summa_bloc_now = 0
    for vtorostep_result_bloc_find in vtorostepen_result_bloc_find_now:
        result_bloc_find_now = {'id_collection': vtorostep_result_bloc_find,
                            'povtor': vol_id_collection_now.count(vtorostep_result_bloc_find)}
        list_result_bloc_find_now.append(result_bloc_find_now)
        povtor_summa_bloc_now += vol_id_collection_now.count(vtorostep_result_bloc_find)

    result_for_web_blok_dict_now = {}
    result_for_web_blok_now = []
    for result_bloc_find_single in list_result_bloc_find_now:
        bloc_collection_single = Collection.objects.get(id=int(result_bloc_find_single['id_collection']))
        result_for_web_blok_dict_now = {'name_collection': bloc_collection_single.name_collection,
                                    'povtor': int(result_bloc_find_single['povtor']),
                                    'prosent': int((100 / povtor_summa_bloc_now) * result_bloc_find_single['povtor'])}
        if int((100 / povtor_summa_bloc_now) * result_bloc_find_single['povtor']) > 9:
            result_for_web_blok_now.append(result_for_web_blok_dict_now)
    # We create a dictionary with key is the name of collection and by an amount and percent is an end
    # Complete data on general statistics of sectional queries (for this day) are beginning

    # Complete data on statistics of sectional queries are the extended search (complete period) - beginning
    vol_id_collection_sh = []
    result_bloc_find_sh = {}
    vtorostepen_result_bloc_find_sh = []

    # We sort out all data from a base on sectional queries is a result a list from ID of all collections is beginning
    for statistic_bloc in statistics_bloc_search_hight:
        len_statistic_bloc = len(str(statistic_bloc.collection))
        srez_bloc = str(statistic_bloc.collection)[
                    1:len_statistic_bloc - 1]  # We produce the cut of line deleting from []
        if len(srez_bloc) == 1:
            vol_id_collection_sh.append(int(srez_bloc))

        if len(srez_bloc) > 1:
            infos_srez_bloc = srez_bloc.split(", ")
            for info_srez_bloc in infos_srez_bloc:
                vol_id_collection_sh.append(int(info_srez_bloc))
    # We sort out all data from a base on sectional queries is a result a list from IDES of all collections is an end

    # We create a list from single ID of collections is beginning
    for vo_id_collection in vol_id_collection_sh:
        if vo_id_collection not in vtorostepen_result_bloc_find_sh:
            vtorostepen_result_bloc_find_sh.append(vo_id_collection)
    # We create a list from single ID of collections is beginning

    # We create a dictionary with key is the name of collection and by an amount and percent is beginning
    list_result_bloc_find_sh = []
    povtor_summa_bloc_sh = 0
    for vtorostep_result_bloc_find in vtorostepen_result_bloc_find_sh:
        result_bloc_find_sh = {'id_collection': vtorostep_result_bloc_find,
                            'povtor': vol_id_collection_sh.count(vtorostep_result_bloc_find)}
        list_result_bloc_find_sh.append(result_bloc_find_sh)
        povtor_summa_bloc_sh += vol_id_collection_sh.count(vtorostep_result_bloc_find)

    result_for_web_blok_dict_sh = {}
    result_for_web_blok_sh = []
    for result_bloc_find_single in list_result_bloc_find_sh:
        bloc_collection_single = Collection.objects.get(id=int(result_bloc_find_single['id_collection']))
        result_for_web_blok_dict_sh = {'name_collection': bloc_collection_single.name_collection,
                                    'povtor': int(result_bloc_find_single['povtor']),
                                    'prosent': int((100 / povtor_summa_bloc_sh) * result_bloc_find_single['povtor'])}
        if int((100 / povtor_summa_bloc_sh) * result_bloc_find_single['povtor']) > 9:
            result_for_web_blok_sh.append(result_for_web_blok_dict_sh)

    # We create a dictionary with key is the name of collection and by an amount and percent is an end
    # Complete data on statistics of sectional queries are the extended search (complete period) - end

    # Data on general statistics of sectional queries (for this day) are the extended search - beginning
    vol_id_collection_sh_now = []
    result_bloc_find_sh_now = {}
    vtorostepen_result_bloc_find_sh_now = []

    # We sort out all data from a base on sectional queries is a result a list from ID of all collections is beginning
    for statistic_bloc in list_statistic_for_bloc_search_now:
        len_statistic_bloc = len(str(statistic_bloc.collection))
        srez_bloc = str(statistic_bloc.collection)[
                    1:len_statistic_bloc - 1]  # We produce the cut of line deleting from []
        if len(srez_bloc) == 1:
            vol_id_collection_sh_now.append(int(srez_bloc))

        if len(srez_bloc) > 1:
            infos_srez_bloc = srez_bloc.split(", ")
            for info_srez_bloc in infos_srez_bloc:
                vol_id_collection_sh_now.append(int(info_srez_bloc))
    # We sort out all data from a base on sectional queries is a result a list from ID of all collections is an end

    # We create a list from single ID of collections is beginning
    for vo_id_collection in vol_id_collection_sh_now:
        if vo_id_collection not in vtorostepen_result_bloc_find_sh_now:
            vtorostepen_result_bloc_find_sh_now.append(vo_id_collection)
    # We create a list from single ID of collections is beginning

    # We create a dictionary with key is the name of collection and by an amount and percent is beginning
    list_result_bloc_find_sh_now = []
    povtor_summa_bloc_sh_now = 0
    for vtorostep_result_bloc_find in vtorostepen_result_bloc_find_sh_now:
        result_bloc_find_sh_now = {'id_collection': vtorostep_result_bloc_find,
                                'povtor': vol_id_collection_sh_now.count(vtorostep_result_bloc_find)}
        list_result_bloc_find_sh_now.append(result_bloc_find_sh_now)
        povtor_summa_bloc_sh_now += vol_id_collection_sh_now.count(vtorostep_result_bloc_find)

    result_for_web_blok_dict_sh_now = {}
    result_for_web_blok_sh_now = []
    for result_bloc_find_single in list_result_bloc_find_sh_now:
        bloc_collection_single = Collection.objects.get(id=int(result_bloc_find_single['id_collection']))
        result_for_web_blok_dict_sh_now = {'name_collection': bloc_collection_single.name_collection,
                                        'povtor': int(result_bloc_find_single['povtor']),
                                        'prosent': int(
                                            (100 / povtor_summa_bloc_sh_now) * result_bloc_find_single['povtor'])}
        if int((100 / povtor_summa_bloc_sh_now) * result_bloc_find_single['povtor']) > 9:
            result_for_web_blok_sh_now.append(result_for_web_blok_dict_sh_now)
    # We create a dictionary with key is the name of collection and by an amount and percent is an end
    # Data on general statistics of sectional queries (for this day) are the extended search - end

    # Complete data on statistics of sectional queries - except the extended search (complete period) - beginning
    vol_id_collection_is_sh = []
    result_bloc_find_is_sh = {}
    vtorostepen_result_bloc_find_is_sh = []

    # We sort out all data from a base on sectional queries is a result a list from IDES of all collections is beginning
    for statistic_bloc in statistics_bloc_not_in:
        len_statistic_bloc = len(str(statistic_bloc.collection))
        srez_bloc = str(statistic_bloc.collection)[
                    1:len_statistic_bloc - 1]  # We produce the cut of line deleting from []
        if len(srez_bloc) == 1:
            vol_id_collection_is_sh.append(int(srez_bloc))

        if len(srez_bloc) > 1:
            infos_srez_bloc = srez_bloc.split(", ")
            for info_srez_bloc in infos_srez_bloc:
                vol_id_collection_is_sh.append(int(info_srez_bloc))
    # We sort out all data from a base on sectional queries is a result a list from ID of all collections is an end

    # We create a list from single ID of collections is beginning
    for vo_id_collection in vol_id_collection_is_sh:
        if vo_id_collection not in vtorostepen_result_bloc_find_is_sh:
            vtorostepen_result_bloc_find_is_sh.append(vo_id_collection)
    # We create a list from single ID of collections is end

    # We create a dictionary with key is the name of collection and by an amount and percent is beginning
    list_result_bloc_find_is_sh = []
    povtor_summa_bloc_is_sh = 0
    for vtorostep_result_bloc_find in vtorostepen_result_bloc_find_is_sh:
        result_bloc_find_is_sh = {'id_collection': vtorostep_result_bloc_find,
                               'povtor': vol_id_collection_is_sh.count(vtorostep_result_bloc_find)}
        list_result_bloc_find_is_sh.append(result_bloc_find_is_sh)
        povtor_summa_bloc_is_sh += vol_id_collection_is_sh.count(vtorostep_result_bloc_find)

    result_for_web_blok_dict_sh = {}
    result_for_web_blok_is_sh = []
    for result_bloc_find_single in list_result_bloc_find_is_sh:
        bloc_collection_single = Collection.objects.get(id=int(result_bloc_find_single['id_collection']))
        result_for_web_blok_dict_is_sh = {'name_collection': bloc_collection_single.name_collection,
                                       'povtor': int(result_bloc_find_single['povtor']),
                                       'prosent': int(
                                           (100 / povtor_summa_bloc_is_sh) * result_bloc_find_single['povtor'])}
        if int((100 / povtor_summa_bloc_is_sh) * result_bloc_find_single['povtor']) > 9:
            result_for_web_blok_is_sh.append(result_for_web_blok_dict_is_sh)
    # We create a dictionary with key is the name of collection and by an amount and percent is an end
    # Complete data on statistics of sectional queries - except the extended search (complete period) - end

    # Complete data on statistics of sectional queries - except the extended search (for this day) - beginning
    vol_id_collection_is_sh_now = []
    result_bloc_find_sh_now = {}
    vtorostepen_result_bloc_find_sh_now = []

    # We sort out all data from a base on sectional queries is a result a list from ID of all collections is beginning
    for statistic_bloc in list_statistic_for_minus_bloc_search_now:
        len_statistic_bloc = len(str(statistic_bloc.collection))
        srez_bloc = str(statistic_bloc.collection)[
                    1:len_statistic_bloc - 1]  # We produce the cut of line deleting from []
        if len(srez_bloc) == 1:
            vol_id_collection_is_sh_now.append(int(srez_bloc))

        if len(srez_bloc) > 1:
            infos_srez_bloc = srez_bloc.split(", ")
            for info_srez_bloc in infos_srez_bloc:
                vol_id_collection_is_sh_now.append(int(info_srez_bloc))
    # We sort out all data from a base on sectional queries is a result a list from IDES of all collections is an end

    #  We create a list from single ID of collections is beginning
    for vo_id_collection in vol_id_collection_is_sh_now:
        if vo_id_collection not in vtorostepen_result_bloc_find_sh_now:
            vtorostepen_result_bloc_find_sh_now.append(vo_id_collection)
    # We create a list from single ID of collections is beginning

    #  We create a dictionary with key is the name of collection and by an amount and percent is beginning
    list_result_bloc_find_sh_now = []
    povtor_summa_bloc_is_sh_now = 0
    for vtorostep_result_bloc_find in vtorostepen_result_bloc_find_sh_now:
        result_bloc_find_sh_now = {'id_collection': vtorostep_result_bloc_find,
                                   'povtor': vol_id_collection_is_sh_now.count(vtorostep_result_bloc_find)}
        list_result_bloc_find_sh_now.append(result_bloc_find_sh_now)
        povtor_summa_bloc_is_sh_now += vol_id_collection_is_sh_now.count(vtorostep_result_bloc_find)

    result_for_web_blok_dict_is_sh_now = {}
    result_for_web_blok_is_sh_now = []
    for result_bloc_find_single in list_result_bloc_find_sh_now:
        bloc_collection_single = Collection.objects.get(id=int(result_bloc_find_single['id_collection']))
        result_for_web_blok_dict_is_sh_now = {'name_collection': bloc_collection_single.name_collection,
                                           'povtor': int(result_bloc_find_single['povtor']),
                                           'prosent': int(
                                               (100 / povtor_summa_bloc_is_sh_now) * result_bloc_find_single[
                                                   'povtor'])}
        if int((100 / povtor_summa_bloc_is_sh_now) * result_bloc_find_single['povtor']) > 9:
            result_for_web_blok_is_sh_now.append(result_for_web_blok_dict_is_sh_now)

        # We create a dictionary with key is the name of collection and by an amount and percent is an end
    # Complete data on statistics of sectional queries - except the extended search (for this day) - end


    return render(request, 'shadow/statistic_bloc_find.html', locals())


def statistic_in(request):
    # Verification in the presence of record of registration (connecting of the session key)
    show = False
    session_key = request.session.session_key
    user = User_Login.objects.filter(is_active_login=True, session_key_login=session_key)
    if user:
        show = True
    # Completion of verification in the presence of record of registration (connecting of the session key)

    # Determination of today's date is beginning
    now = datetime.now()
    now = datetime.date(now)
    # Determination of today's date is an end

    # Collection of these general on visits pages is beginning
    query_set_manafactur = Eye.objects.filter(locate_manafactur=True)
    query_set_collection = Eye.objects.filter(locate_collection=True)
    query_set_product = Eye.objects.filter(locate_product=True)


    # Cleaning of query about collections from a -=Send project on view=- is beginning
    list_query_set_collection_swap = []
    for query_set in query_set_collection:
        if query_set.page != "Отправка проекта на рассмотрение":
            list_query_set_collection_swap.append(query_set.id)
    query_set_collection = Eye.objects.filter(id__in=list_query_set_collection_swap)
    # Cleaning of query about collections from a -=Send project on view=- is end

    list_manafactur = []
    for query in query_set_manafactur:
        data_in = query.created
        if now == datetime.date(data_in):
            list_manafactur.append(query.id)

    query_set_manafacturer_now = Eye.objects.filter(locate_manafactur=True, id__in=list_manafactur)

    list_collection = []
    for query in query_set_collection:
        data_in = query.created
        if now == datetime.date(data_in):
            list_collection.append(query.id)

    query_set_collection_now = Eye.objects.filter(locate_collection=True, id__in=list_collection)

    list_product = []
    for query in query_set_product:
        data_in = query.created
        if now == datetime.date(data_in):
            list_product.append(query.id)

    query_set_product_now = Eye.objects.filter(locate_product=True, id__in=list_product)
    # Collection of these general on visits pages is an end

    # We collect general statistics on collections (complete) is beginning
    list_collections_eye = []
    list_collections_eye_all = []
    for query in query_set_collection:
        list_collections_eye_all.append(query.page)
        if query.page not in list_collections_eye and query.page != "Отправка проекта на рассмотрение":
            list_collections_eye.append(query.page)

    list_re_list_collections_eye = []
    summa = 0
    for list_in in list_collections_eye:
        dict_collections_eye = dict(name=str(list_in), povtor=list_collections_eye_all.count(list_in))
        summa += list_collections_eye_all.count(list_in)
        list_re_list_collections_eye.append(dict_collections_eye)

    result_in_collections = []
    for list_in in list_collections_eye:
        collections_in_single = Collection.objects.get(name_collection=str(list_in))
        dict_collections_eye = dict(name=str(list_in), manafacturer=collections_in_single.manufacturer_collection.name_manufacturer,
                                    povtor=list_collections_eye_all.count(list_in),
                                    prosent=int((100/summa)*list_collections_eye_all.count(list_in)))
        if dict_collections_eye["prosent"] > 9:
            result_in_collections.append(dict_collections_eye)
    # We collect general statistics on collections (complete) is an end

    # We collect general statistics on collections (for this day) is beginning
    list_collections_eye_now = []
    list_collections_eye_all_now = []
    for query in query_set_collection_now:
        list_collections_eye_all_now.append(query.page)
        if query.page not in list_collections_eye_now and query.page != "Отправка проекта на рассмотрение":
            list_collections_eye_now.append(query.page)

    list_re_list_collections_eye_now = []
    summa = 0
    for list_in in list_collections_eye_now:
        dict_collections_eye = dict(name=str(list_in), povtor=list_collections_eye_all_now.count(list_in))
        summa += list_collections_eye_all_now.count(list_in)
        list_re_list_collections_eye_now.append(dict_collections_eye)

    result_in_collections_now = []
    for list_in in list_collections_eye_now:
        collections_in_single = Collection.objects.get(name_collection=str(list_in))
        dict_collections_eye = dict(name=str(list_in), manafacturer=collections_in_single.manufacturer_collection.name_manufacturer,
                                    povtor=list_collections_eye_all_now.count(list_in),
                                    prosent=int((100 / summa) * list_collections_eye_all_now.count(list_in)))

        if dict_collections_eye["prosent"] > 9:
            result_in_collections_now.append(dict_collections_eye)
    # We collect general statistics on collections (for this day) is an end

    # We collect general statistics on producers (complete) is beginning
    list_manafactur_eye = []
    list_manafactur_eye_all = []
    for query in query_set_manafactur:
        list_manafactur_eye_all.append(query.page)
        if query.page not in list_manafactur_eye:
            list_manafactur_eye.append(query.page)

    list_re_list_manafactur_eye = []
    summa = 0
    for list_in in list_manafactur_eye:
        dict_collections_eye = dict(name=str(list_in), povtor=list_manafactur_eye_all.count(list_in))
        summa += list_manafactur_eye_all.count(list_in)
        list_re_list_manafactur_eye.append(dict_collections_eye)

    result_in_manafactur = []
    for list_in in list_manafactur_eye:
        dict_collections_eye = dict(name=str(list_in),
                                    povtor=list_manafactur_eye_all.count(list_in),
                                    prosent=int((100 / summa) * list_manafactur_eye_all.count(list_in)))
        if dict_collections_eye["prosent"] > 9:
            result_in_manafactur.append(dict_collections_eye)
    # We collect general statistics on producers (complete) is an end

    # We collect general statistics on producers (for this day) is beginning
    list_manafactur_eye_now = []
    list_manafactur_eye_all_now = []
    for query in query_set_manafacturer_now:
        list_manafactur_eye_all_now.append(query.page)
        if query.page not in list_manafactur_eye_now:
            list_manafactur_eye_now.append(query.page)

    list_re_list_manafactur_eye_now = []
    summa = 0
    for list_in in list_manafactur_eye_now:
        dict_manafactur_eye = dict(name=str(list_in), povtor=list_manafactur_eye_all_now.count(list_in))
        summa += list_manafactur_eye_all_now.count(list_in)
        list_re_list_manafactur_eye_now.append(dict_manafactur_eye)

    result_in_manafactur_now = []
    for list_in in list_manafactur_eye_now:
        dict_manafactur_eye = dict(name=str(list_in),
                                    povtor=list_manafactur_eye_all_now.count(list_in),
                                    prosent=int((100 / summa) * list_manafactur_eye_all_now.count(list_in)))
        if dict_manafactur_eye["prosent"] > 9:
            result_in_manafactur_now.append(dict_manafactur_eye)
    # We collect general statistics on producers (for this day) is an end

    # We collect general statistics on foods (complete) is beginning
    list_product_eye = []
    list_product_eye_all = []
    for query in query_set_product:
        list_product_eye_all.append(query.page)
        if query.page not in list_product_eye:
            list_product_eye.append(query.page)

    list_re_list_product_eye = []
    summa = 0
    for list_in in list_product_eye:
        dict_product_eye = dict(name=str(list_in), povtor=list_product_eye_all.count(list_in))
        summa += list_product_eye_all.count(list_in)
        list_re_list_product_eye.append(dict_collections_eye)

    result_in_product = []
    for list_in in list_product_eye:
        product_in_single = Product.objects.get(name_product=str(list_in))
        dict_product_eye = dict(name=str(list_in), collection=product_in_single.collection_product.name_collection,
                                manafacturer=product_in_single.collection_product.manufacturer_collection.name_manufacturer,
                                povtor=list_product_eye_all.count(list_in),
                                prosent=int((100 / summa) * list_product_eye_all.count(list_in)))
        if dict_product_eye["prosent"] > 9:
            result_in_product.append(dict_product_eye)
    # We collect general statistics on foods (complete) is an end

    # We collect general statistics on foods (for this day) is beginning
    list_product_eye_now = []
    list_product_eye_all_now = []
    for query in query_set_product_now:
        list_product_eye_all_now.append(query.page)
        if query.page not in list_product_eye_now:
            list_product_eye_now.append(query.page)

    list_re_list_product_eye_now = []
    summa = 0
    for list_in in list_product_eye_now:
        dict_product_eye = dict(name=str(list_in), povtor=list_product_eye_all_now.count(list_in))
        summa += list_product_eye_all_now.count(list_in)
        list_re_list_product_eye_now.append(dict_product_eye)

    result_in_product_now = []
    for list_in in list_product_eye_now:
        product_in_single = Product.objects.get(name_product=str(list_in))
        dict_product_eye = dict(name=str(list_in), collection=product_in_single.collection_product.name_collection,
                                manafacturer=product_in_single.collection_product.manufacturer_collection.name_manufacturer,
                                povtor=list_product_eye_all_now.count(list_in),
                                prosent=int((100 / summa) * list_product_eye_all_now.count(list_in)))
        if dict_product_eye["prosent"] > 9:
            result_in_product_now.append(dict_product_eye)
    # We collect general statistics on foods (for this day) is an end

    return render(request, 'shadow/statistic_in.html', locals())


def session_key_eye(request, session_key_eye_id):
    # Verification in the presence of record of registration (connecting of the session key)
    show = False
    session_key = request.session.session_key
    user = User_Login.objects.filter(is_active_login=True, session_key_login=session_key)
    if user:
        show = True
    # Completion of verification in the presence of record of registration (connecting of the session key)

    statistic_all = Eye.objects.filter(session_key=session_key_eye_id)
    statistic_all_collection = Eye.objects.filter(session_key=session_key_eye_id, locate_collection=True)
    statistic_all_manafactur = Eye.objects.filter(session_key=session_key_eye_id, locate_manafactur=True)
    statistic_all_product = Eye.objects.filter(session_key=session_key_eye_id, locate_product=True)

    # Preparation of timing for chronology is beginning

    list_time = []
    for qwerty in statistic_all:
        True_exit = 0
        for query in statistic_all:
            if qwerty.id < query.id and True_exit == 0:
                True_exit = 1
                if qwerty.locate_product == True:
                    type = "product"
                if qwerty.locate_collection == True:
                    type = "collections"
                if qwerty.locate_manafactur == True:
                    type = "manafacturer"
                if qwerty.locate_manafactur != True and qwerty.locate_collection != True and qwerty.locate_product != True:
                    type = "site"
                time_re = str(query.created - qwerty.created)
                dict_eye = dict(delta=time_re[0:-7], page=qwerty.page, type_page=type)

                list_time.append(dict_eye)
    # Preparation of timing for chronology is an end

    # We collect general statistics on collections is beginning
    list_collection_eye = []
    list_collection_eye_all = []
    for query in statistic_all_collection:
        list_collection_eye_all.append(query.page)
        if query.page not in list_collection_eye and query.page != "Отправка проекта на рассмотрение":
            list_collection_eye.append(query.page)

    # An analysis of time for collections is beginning
    second_list_collection = []
    for query in list_collection_eye:
        element_collection = Eye.objects.filter(session_key=session_key_eye_id, locate_collection=True, page=query)
        dict_collection_eye = dict(name=str(query), query_set_result=element_collection)
        second_list_collection.append(dict_collection_eye)

    list_time_collection = []
    for query in second_list_collection:
        for query_single in query['query_set_result']:
            True_exit = 0
            for re_query_single in Eye.objects.filter(session_key=session_key_eye_id):
                if int(query_single.id) < re_query_single.id and True_exit == 0:
                    dict_collection_eye = dict(delta=re_query_single.created-query_single.created, page=query_single.page)
                    True_exit = 1
                    list_time_collection.append(dict_collection_eye)

    now = datetime.now()
    now = datetime.date(now)
    time_delta_all = now - now

    list_result_re_collection = []
    for query in list_collection_eye:
        for qwerty in list_time_collection:
            if query == str(qwerty["page"]):
                time_delta_all += qwerty["delta"]
        time_delta_all_re = str(time_delta_all)
        time_delta_all = now - now
        dict_collection_eye = dict(summa_time=time_delta_all_re[0:-7], page=query)
        list_result_re_collection.append(dict_collection_eye)
    # An analysis of time for collections is an end

    list_re_list_collection_eye = []
    summa = 0
    for list_in in list_collection_eye:
        summa += list_collection_eye_all.count(list_in)

    result_in_collection = []
    for list_in in list_collection_eye:
        collection_in_single = Collection.objects.get(name_collection=str(list_in))
        for list_result_re_single in list_result_re_collection:
            if str(list_result_re_single["page"]) == str(list_in):
                dict_collection_eye = dict(name=str(list_in),
                                           manafacturer=collection_in_single.manufacturer_collection.name_manufacturer,
                                           povtor=list_collection_eye_all.count(list_in),
                                           prosent=int((100 / summa) * list_collection_eye_all.count(list_in)),
                                           time_summa=str(list_result_re_single["summa_time"]))

        result_in_collection.append(dict_collection_eye)
    # We collect general statistics on collections is an end

    # We collect general statistics on producers is beginning
    list_manafactur_eye = []
    list_manafactur_eye_all = []
    for query in statistic_all_manafactur:
        list_manafactur_eye_all.append(query.page)
        if query.page not in list_manafactur_eye:
            list_manafactur_eye.append(query.page)

    # An analysis of time for collections is beginning
    second_list_manafactur = []
    for query in list_manafactur_eye:
        element_manafactur = Eye.objects.filter(session_key=session_key_eye_id, locate_manafactur=True, page=query)
        dict_manafactur_eye = dict(name=str(query), query_set_result=element_manafactur)
        second_list_manafactur.append(dict_manafactur_eye)

    list_time_manafactur = []
    for query in second_list_manafactur:
        for query_single in query['query_set_result']:
            True_exit = 0
            for re_query_single in Eye.objects.filter(session_key=session_key_eye_id):
                if int(query_single.id) < re_query_single.id and True_exit == 0:
                    dict_manafactur_eye = dict(delta=re_query_single.created-query_single.created, page=query_single.page)
                    True_exit = 1
                    list_time_manafactur.append(dict_manafactur_eye)

    now = datetime.now()
    now = datetime.date(now)
    time_delta_all = now - now

    list_result_re_manafactur = []
    for query in list_manafactur_eye:
        for qwerty in list_time_manafactur:
            if query == str(qwerty["page"]):
                time_delta_all += qwerty["delta"]
        time_delta_all_re = str(time_delta_all)
        time_delta_all = now - now
        dict_manafactur_eye = dict(summa_time=time_delta_all_re[0:-7], page=query)
        list_result_re_manafactur.append(dict_manafactur_eye)
    # An analysis of time for collections is an end


    list_re_list_manafactur_eye = []
    summa = 0
    for list_in in list_manafactur_eye:
        summa += list_manafactur_eye_all.count(list_in)

    result_in_manafactur = []
    for list_in in list_manafactur_eye:
        for list_result_re_single in list_result_re_manafactur:
            if str(list_result_re_single["page"]) == str(list_in):
                dict_manafactur_eye = dict(name=str(list_in),
                                           povtor=list_manafactur_eye_all.count(list_in),
                                           prosent=int((100 / summa) * list_manafactur_eye_all.count(list_in)),
                                           time_summa = str(list_result_re_single["summa_time"]))
        result_in_manafactur.append(dict_manafactur_eye)
    # We collect general statistics on producers is an end

    # We collect general statistics on a product is beginning
    list_product_eye = []
    list_product_eye_all = []
    for query in statistic_all_product:
        list_product_eye_all.append(query.page)
        if query.page not in list_product_eye:
            list_product_eye.append(query.page)


    # An analysis of time for collections is beginning
    second_list_product = []
    for query in list_product_eye:
        element_product = Eye.objects.filter(session_key=session_key_eye_id, locate_product=True, page=query)
        dict_product_eye = dict(name=str(query), query_set_result=element_product)
        second_list_product.append(dict_product_eye)

    list_time_product = []
    for query in second_list_product:
        for query_single in query['query_set_result']:
            True_exit = 0
            for re_query_single in Eye.objects.filter(session_key=session_key_eye_id):
                if int(query_single.id) < re_query_single.id and True_exit == 0:
                    dict_product_eye = dict(delta=re_query_single.created-query_single.created, page=query_single.page)
                    True_exit = 1
                    list_time_product.append(dict_product_eye)

    now = datetime.now()
    now = datetime.date(now)
    time_delta_all = now - now

    list_result_re_product = []
    for query in list_product_eye:
        for qwerty in list_time_product:
            if query == str(qwerty["page"]):
                time_delta_all += qwerty["delta"]
        time_delta_all_re = str(time_delta_all)
        time_delta_all = now - now
        dict_product_eye = dict(summa_time=time_delta_all_re[0:-7], page=query)
        list_result_re_product.append(dict_product_eye)

    # An analysis of time for collections is an end

    list_re_list_product_eye = []
    summa = 0
    for list_in in list_product_eye:
        summa += list_product_eye_all.count(list_in)

    result_in_product = []
    for list_in in list_product_eye:
        product_in_single = Product.objects.get(name_product=str(list_in))
        for list_result_re_single in list_result_re_product:
            if str(list_result_re_single["page"]) == str(list_in):
                dict_product_eye = dict(name=str(list_in), collection=product_in_single.collection_product.name_collection,
                                        manafacturer=product_in_single.collection_product.manufacturer_collection.name_manufacturer,
                                        povtor=list_product_eye_all.count(list_in),
                                        prosent=int((100 / summa) * list_product_eye_all.count(list_in)),
                                        time_summa=str(list_result_re_single["summa_time"]))
        result_in_product.append(dict_product_eye)
    # We collect general statistics on a product is an end

    return render(request, 'shadow/session_key_eye.html', locals())


def time_delta(request):
    # Verification in the presence of record of registration (connecting of the session key)
    show = False
    session_key = request.session.session_key
    user = User_Login.objects.filter(is_active_login=True, session_key_login=session_key)
    if user:
        show = True
    # Completion of verification in the presence of record of registration (connecting of the session key)

    now = datetime.now()
    now = datetime.date(now)

    all_users = Log_In_Site.objects.filter()
    all_users_project = Eye.objects.filter(page="Отправка проекта на рассмотрение")
    all_users_buy = Eye.objects.filter(page="Окончание оформления ордера")

    all_users_now = []
    for user in all_users:
        data_in = user.created
        if now == datetime.date(data_in):
            all_users_now.append(user.id)
    all_users_now = Log_In_Site.objects.filter(id__in=all_users_now)

    all_users_project_now = []
    for user in all_users_project:
        data_in = user.created
        if now == datetime.date(data_in):
            all_users_project_now.append(user.id)
    all_users_project_now = Eye.objects.filter(id__in=all_users_project_now)

    all_users_buy_now = []
    for user in all_users_buy:
        data_in = user.created
        if now == datetime.date(data_in):
            all_users_buy_now.append(user.id)
    all_users_buy_now = Eye.objects.filter(id__in=all_users_buy_now)

    # Conclusion of information about time of user after today is beginning
    nmb_users_now = Log_In_Site.objects.filter(session_key=session_key).count()

    all_users_time_now = []
    for user in all_users:
        data_in = user.created
        if now == datetime.date(data_in):
            all_users_time_now.append(user.session_key)

    list_all_users_now = []
    dict_all_users_now = {}
    nmb_all_users_now = 0
    time_delta = now - now
    for user in all_users_time_now:
        created_time = Log_In_Site.objects.get(session_key=user)
        created_time = created_time.created
        max_id = 0
        for eye_max in Eye.objects.filter(session_key=user):
            eye_max_in = eye_max.id
            if max_id < eye_max_in:
                max_id = eye_max_in
        max_id = Eye.objects.get(id=max_id)
        max_id = max_id.created

        time_delta = max_id - created_time

        dict_all_users_now = {'session_key_now': session_key, 'time_now': time_delta}
        list_all_users_now.append(dict_all_users_now)
        nmb_all_users_now += 1

    summa_time_now = time_delta - time_delta
    for user in list_all_users_now:
        summa_time_now += user['time_now']

    if nmb_all_users_now == 0:
        mid_time_now = 0
    if nmb_all_users_now != 0:
        mid_time_now = summa_time_now / nmb_all_users_now
    # Conclusion of information about time of user after today is an end

    # Conclusion of information about time of user for complete period - beginning
    nmb_users = Log_In_Site.objects.filter().count()
    list_all_users = []
    dict_all_users = {}
    nmb_all_users = 0
    for user in all_users:
        created_time = Log_In_Site.objects.get(session_key=user.session_key)
        created_time = created_time.created
        max_id = 0
        for eye_max in Eye.objects.filter(session_key=user.session_key):
            eye_max_in = eye_max.id
            if max_id < eye_max_in:
                max_id = eye_max_in
        max_id = Eye.objects.get(id=max_id)
        max_id = max_id.created

        time_delta = max_id - created_time

        dict_all_users = {'session_key': session_key, 'time': time_delta}
        list_all_users.append(dict_all_users)
        nmb_all_users += 1

    summa_time = time_delta - time_delta
    for user in list_all_users:
        summa_time += user['time']

    mid_time = summa_time/nmb_all_users
    # Conclusion of information about time of user for complete period - beginning

    return render(request, 'shadow/time_delta.html', locals())


def projects_and_orders(request):
    # Verification in the presence of record of registration (connecting of the session key)
    show = False
    session_key = request.session.session_key
    user = User_Login.objects.filter(is_active_login=True, session_key_login=session_key)
    if user:
        show = True
    # Completion of verification in the presence of record of registration (connecting of the session key)

    orders_all = Order.objects.filter()
    status_all = Status.objects.filter()

    list_status = []
    sum_result = []

    for status_single in status_all:
        result_order = {}
        list_status.append(status_single.id)

        for status in list_status:
            list_order_status = []
            order_status = Order.objects.filter(status__id=int(status_single.id))
            for order in order_status:
                list_order_status.append(order)
            leni = len(list_order_status)
        result_order.update({"status_id": status_single.id, "leni": leni, "orders": list_order_status})
        sum_result.append(result_order)

    progects_all = Find_Project.objects.filter()

    list_status = []
    sum_resul = []

    for status_single in status_all:
        result_project = {}
        list_status.append(status_single.id)

        for status in list_status:
            list_project_status = []
            project_status = Find_Project.objects.filter(status__id=int(status_single.id))
            for project in project_status:
                list_project_status.append(project.id)
            leni = len(list_project_status)
        result_project.update({"project_id": status_single.id, "leni": leni, "project": list_project_status})
        sum_resul.append(result_project)


    return render(request, 'shadow/projects_and_orders.html', locals())


def pars(request):
    # Verification in the presence of record of registration (connecting of the session key)
    show = False
    session_key = request.session.session_key
    user = User_Login.objects.filter(is_active_login=True, session_key_login=session_key)
    if user:
        show = True
    # Completion of verification in the presence of record of registration (connecting of the session key)

    # A block of record of the names of ways for collections is beginning
    data = request.POST
    if data.get('Image_resize') == 'Подготовка изображений для показа мини':
        all_collections_img = Collection_Image.objects.filter(is_active_collection=True, is_main_collection=True)

        for collection_img in all_collections_img:
            id = collection_img.name_collection.id
            image = Image.open(collection_img.image_collection)
            width = 250
            height = 168

            size = (width, height)
            img_result = image.resize(size, Image.NEAREST)

            name = str(id)+".jpg"

            full_name = "media/temp/" + name
            img_result.save(full_name, "JPEG")

            Collection.objects.filter(id=id).update(image_collection_mini=full_name)
        return render(request, 'shadow/pars.html', locals())

    for data_colour in data:
        if data_colour == "Id_patch":
            all_collection = Collection.objects.filter(is_active_collection=True)
            for collection in all_collection:
                name_collection = collection.name_collection
                id = collection.id
                name_collection = name_collection.lower()
                name_collection = name_collection.replace(" ", "_")
                name_collection = name_collection.replace("&", "_")
                Collection.objects.filter(is_active_collection=True, id=id).update(id_patch=name_collection)
    # A block of record of the names of ways for collections is an end

    # Creation of markers for creation and перезаписи of producers, collections is beginning
    save_manaf = False
    save_colle = False
    save_contr = False
    save_prise_group = False
    save_availability = False
    save_nhs = False
    recheng_img = False
    # Creation of markers for creation and перезаписи of producers, collections is end

    data = request.POST
    # Bringing in the base of parameters of search is beginning
    for data_colour in data:
        if data_colour == "Colour":
            filename = "./temp_files/filter/" + "colour.csv"
            with open(filename, "r", newline="") as file:
                reader_file = csv.reader(file)
                for row in reader_file:
                    if row[1] == "Бежевый":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Colour_For_Search.objects.filter(name_colour_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(name_collection=single_collection)
                                Collection_Colour_For_Search.objects.filter(name_colour_collection=name_collection).update(collection_colour_beige=True)
                            else:
                                name_collection = Collection.objects.get(name_collection=single_collection)
                                Collection_Colour_For_Search.objects.create(name_colour_collection=name_collection,
                                                                            collection_colour_is_active=True,
                                                                            collection_colour_beige=True)
                    if row[1] == "Белый":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Colour_For_Search.objects.filter(
                                name_colour_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(name_collection=single_collection)
                                Collection_Colour_For_Search.objects.filter(
                                    name_colour_collection=name_collection).update(collection_colour_white=True)
                            else:
                                name_collection = Collection.objects.get(name_collection=single_collection)
                                Collection_Colour_For_Search.objects.create(
                                    name_colour_collection=name_collection,
                                    collection_colour_is_active=True,
                                    collection_colour_white=True)

                    if row[1] == "Голубой":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Colour_For_Search.objects.filter(
                                name_colour_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(name_collection=single_collection)
                                Collection_Colour_For_Search.objects.filter(
                                    name_colour_collection=name_collection).update(collection_colour_blue=True)
                            else:
                                name_collection = Collection.objects.get(name_collection=single_collection)
                                Collection_Colour_For_Search.objects.create(
                                    name_colour_collection=name_collection,
                                    collection_colour_is_active=True,
                                    collection_colour_blue=True)

                    if row[1] == "Желтый":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Colour_For_Search.objects.filter(
                                name_colour_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(name_collection=single_collection)
                                Collection_Colour_For_Search.objects.filter(
                                    name_colour_collection=name_collection).update(collection_colour_yellow=True)
                            else:
                                name_collection = Collection.objects.get(name_collection=single_collection)
                                Collection_Colour_For_Search.objects.create(
                                    name_colour_collection=name_collection,
                                    collection_colour_is_active=True,
                                    collection_colour_yellow=True)

                    if row[1] == "Зеленый":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Colour_For_Search.objects.filter(
                                name_colour_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(name_collection=single_collection)
                                Collection_Colour_For_Search.objects.filter(
                                    name_colour_collection=name_collection).update(
                                    collection_colour_green=True)
                            else:
                                name_collection = Collection.objects.get(name_collection=single_collection)
                                Collection_Colour_For_Search.objects.create(
                                    name_colour_collection=name_collection,
                                    collection_colour_is_active=True,
                                    collection_colour_green=True)

                    if row[1] == "Золотой":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Colour_For_Search.objects.filter(
                                name_colour_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(name_collection=single_collection)
                                Collection_Colour_For_Search.objects.filter(
                                    name_colour_collection=name_collection).update(
                                    collection_colour_gold=True)
                            else:
                                name_collection = Collection.objects.get(name_collection=single_collection)
                                Collection_Colour_For_Search.objects.create(
                                    name_colour_collection=name_collection,
                                    collection_colour_is_active=True,
                                    collection_colour_gold=True)

                    if row[1] == "Коричневый":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Colour_For_Search.objects.filter(
                                name_colour_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(name_collection=single_collection)
                                Collection_Colour_For_Search.objects.filter(
                                    name_colour_collection=name_collection).update(
                                    collection_colour_brown=True)
                            else:
                                name_collection = Collection.objects.get(name_collection=single_collection)
                                Collection_Colour_For_Search.objects.create(
                                    name_colour_collection=name_collection,
                                    collection_colour_is_active=True,
                                    collection_colour_brown=True)

                    if row[1] == "Красный":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Colour_For_Search.objects.filter(
                                name_colour_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(name_collection=single_collection)
                                Collection_Colour_For_Search.objects.filter(
                                    name_colour_collection=name_collection).update(
                                    collection_colour_red=True)
                            else:
                                name_collection = Collection.objects.get(name_collection=single_collection)
                                Collection_Colour_For_Search.objects.create(
                                    name_colour_collection=name_collection,
                                    collection_colour_is_active=True,
                                    collection_colour_red=True)

                    if row[1] == "Мультиколор":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Colour_For_Search.objects.filter(
                                name_colour_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(name_collection=single_collection)
                                Collection_Colour_For_Search.objects.filter(
                                    name_colour_collection=name_collection).update(
                                    collection_colour_multicolor=True)
                            else:
                                name_collection = Collection.objects.get(name_collection=single_collection)
                                Collection_Colour_For_Search.objects.create(
                                    name_colour_collection=name_collection,
                                    collection_colour_is_active=True,
                                    collection_colour_multicolor=True)

                    if row[1] == "Оранжевый":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Colour_For_Search.objects.filter(
                                name_colour_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(name_collection=single_collection)
                                Collection_Colour_For_Search.objects.filter(
                                    name_colour_collection=name_collection).update(
                                    collection_colour_orange=True)
                            else:
                                name_collection = Collection.objects.get(name_collection=single_collection)
                                Collection_Colour_For_Search.objects.create(
                                    name_colour_collection=name_collection,
                                    collection_colour_is_active=True,
                                    collection_colour_orange=True)

                    if row[1] == "Розовый":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Colour_For_Search.objects.filter(
                                name_colour_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(name_collection=single_collection)
                                Collection_Colour_For_Search.objects.filter(
                                    name_colour_collection=name_collection).update(
                                    collection_colour_pink=True)
                            else:
                                name_collection = Collection.objects.get(name_collection=single_collection)
                                Collection_Colour_For_Search.objects.create(
                                    name_colour_collection=name_collection,
                                    collection_colour_is_active=True,
                                    collection_colour_pink=True)

                    if row[1] == "Серебряный/Платиновый":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Colour_For_Search.objects.filter(
                                name_colour_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(name_collection=single_collection)
                                Collection_Colour_For_Search.objects.filter(
                                    name_colour_collection=name_collection).update(
                                    collection_colour_silver_platinum=True)
                            else:
                                name_collection = Collection.objects.get(name_collection=single_collection)
                                Collection_Colour_For_Search.objects.create(
                                    name_colour_collection=name_collection,
                                    collection_colour_is_active=True,
                                    collection_colour_silver_platinum=True)

                    if row[1] == "Серый":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Colour_For_Search.objects.filter(
                                name_colour_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(name_collection=single_collection)
                                Collection_Colour_For_Search.objects.filter(
                                    name_colour_collection=name_collection).update(
                                    collection_colour_silver_grey=True)
                            else:
                                name_collection = Collection.objects.get(name_collection=single_collection)
                                Collection_Colour_For_Search.objects.create(
                                    name_colour_collection=name_collection,
                                    collection_colour_is_active=True,
                                    collection_colour_silver_grey=True)

                    if row[1] == "Синий":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Colour_For_Search.objects.filter(
                                name_colour_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(name_collection=single_collection)
                                Collection_Colour_For_Search.objects.filter(
                                    name_colour_collection=name_collection).update(
                                    collection_colour_silver_darkblue=True)
                            else:
                                name_collection = Collection.objects.get(name_collection=single_collection)
                                Collection_Colour_For_Search.objects.create(
                                    name_colour_collection=name_collection,
                                    collection_colour_is_active=True,
                                    collection_colour_silver_darkblue=True)

                    if row[1] == "Сиреневый":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Colour_For_Search.objects.filter(
                                name_colour_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(name_collection=single_collection)
                                Collection_Colour_For_Search.objects.filter(
                                    name_colour_collection=name_collection).update(
                                    collection_colour_silver_lilac=True)
                            else:
                                name_collection = Collection.objects.get(name_collection=single_collection)
                                Collection_Colour_For_Search.objects.create(
                                    name_colour_collection=name_collection,
                                    collection_colour_is_active=True,
                                    collection_colour_silver_lilac=True)

                    if row[1] == "Черный":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Colour_For_Search.objects.filter(
                                name_colour_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(name_collection=single_collection)
                                Collection_Colour_For_Search.objects.filter(
                                    name_colour_collection=name_collection).update(
                                    collection_colour_silver_black=True)
                            else:
                                name_collection = Collection.objects.get(name_collection=single_collection)
                                Collection_Colour_For_Search.objects.create(
                                    name_colour_collection=name_collection,
                                    collection_colour_is_active=True,
                                    collection_colour_silver_black=True)

    for data_colour in data:
        if data_colour == "Floor":
            filename = "./temp_files/filter/" + "floor.csv"
            with open(filename, "r", newline="") as file:
                reader_file = csv.reader(file)
                for row in reader_file:

                    if row[1] == "Для пола":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Floor_For_Search.objects.filter(
                                name_floor_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Floor_For_Search.objects.filter(
                                    name_floor_collection=name_collection).update(
                                    collection_floor_is_active=True,
                                    collection_floor_floor=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Floor_For_Search.objects.create(
                                    name_floor_collection=name_collection,
                                    collection_floor_is_active=True,
                                    collection_floor_floor=True)

                    if row[1] == "Для стен":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Floor_For_Search.objects.filter(
                                name_floor_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Floor_For_Search.objects.filter(
                                    name_floor_collection=name_collection).update(
                                    collection_floor_is_active=True,
                                    collection_floor_wall=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Floor_For_Search.objects.create(
                                    name_floor_collection=name_collection,
                                    collection_floor_is_active=True,
                                    collection_floor_wall=True)

                    if row[1] == "Универсальная":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Floor_For_Search.objects.filter(
                                name_floor_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Floor_For_Search.objects.filter(
                                    name_floor_collection=name_collection).update(
                                    collection_floor_is_active=True,
                                    collection_floor_universal=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Floor_For_Search.objects.create(
                                    name_floor_collection=name_collection,
                                    collection_floor_is_active=True,
                                    collection_floor_universal=True)

    for data_colour in data:
        if data_colour == "Style":
            filename = "./temp_files/filter/" + "style.csv"
            with open(filename, "r", newline="") as file:
                reader_file = csv.reader(file)
                for row in reader_file:

                    if row[1] == "Винтаж":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Style_For_Search.objects.filter(
                                name_style_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Style_For_Search.objects.filter(
                                    name_style_collection=name_collection).update(
                                    collection_stile_is_active=True,
                                    collection_stile_vintage=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Style_For_Search.objects.create(
                                    name_style_collection=name_collection,
                                    collection_stile_is_active=True,
                                    collection_stile_vintage=True)

                    if row[1] == "Классика":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Style_For_Search.objects.filter(
                                name_style_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Style_For_Search.objects.filter(
                                    name_style_collection=name_collection).update(
                                    collection_stile_is_active=True,
                                    collection_stile_classic=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Style_For_Search.objects.create(
                                    name_style_collection=name_collection,
                                    collection_stile_is_active=True,
                                    collection_stile_classic=True)

                    if row[1] == "Современный":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Style_For_Search.objects.filter(
                                name_style_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Style_For_Search.objects.filter(
                                    name_style_collection=name_collection).update(
                                    collection_stile_is_active=True,
                                    collection_stile_modern=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Style_For_Search.objects.create(
                                    name_style_collection=name_collection,
                                    collection_stile_is_active=True,
                                    collection_stile_modern=True)

    for data_colour in data:
        if data_colour == "Facturer":
            filename = "./temp_files/filter/" + "facturer.csv"
            with open(filename, "r", newline="") as file:
                reader_file = csv.reader(file)
                for row in reader_file:

                    if row[1] == "Глянцевая /настенная/":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Facturer_For_Search.objects.filter(
                                name_facturer_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Facturer_For_Search.objects.filter(
                                    name_facturer_collection=name_collection).update(
                                    collection_facturer_is_active=True,
                                    collection_stile_glossy=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Facturer_For_Search.objects.create(
                                    name_facturer_collection=name_collection,
                                    collection_facturer_is_active=True,
                                    collection_stile_glossy=True)

                    if row[1] == "Матовая":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Facturer_For_Search.objects.filter(
                                name_facturer_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Facturer_For_Search.objects.filter(
                                    name_facturer_collection=name_collection).update(
                                    collection_facturer_is_active=True,
                                    collection_stile_matte=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Facturer_For_Search.objects.create(
                                    name_facturer_collection=name_collection,
                                    collection_facturer_is_active=True,
                                    collection_stile_matte=True)

                    if row[1] == "Полированная":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Facturer_For_Search.objects.filter(
                                name_facturer_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Facturer_For_Search.objects.filter(
                                    name_facturer_collection=name_collection).update(
                                    collection_facturer_is_active=True,
                                    collection_stile_polished=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Facturer_For_Search.objects.create(
                                    name_facturer_collection=name_collection,
                                    collection_facturer_is_active=True,
                                    collection_stile_polished=True)

                    if row[1] == "Полуполированная / Лапатированная":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Facturer_For_Search.objects.filter(
                                name_facturer_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Facturer_For_Search.objects.filter(
                                    name_facturer_collection=name_collection).update(
                                    collection_facturer_is_active=True,
                                    collection_stile_polopolarized=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Facturer_For_Search.objects.create(
                                    name_facturer_collection=name_collection,
                                    collection_facturer_is_active=True,
                                    collection_stile_polopolarized=True)

                    if row[1] == "Сатинированная":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Facturer_For_Search.objects.filter(
                                name_facturer_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Facturer_For_Search.objects.filter(
                                    name_facturer_collection=name_collection).update(
                                    collection_facturer_is_active=True,
                                    collection_stile_satin=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Facturer_For_Search.objects.create(
                                    name_facturer_collection=name_collection,
                                    collection_facturer_is_active=True,
                                    collection_stile_satin=True)

                    if row[1] == "Состаренная / Рустичная":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Facturer_For_Search.objects.filter(
                                name_facturer_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Facturer_For_Search.objects.filter(
                                    name_facturer_collection=name_collection).update(
                                    collection_facturer_is_active=True,
                                    collection_stile_aged=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Facturer_For_Search.objects.create(
                                    name_facturer_collection=name_collection,
                                    collection_facturer_is_active=True,
                                    collection_stile_aged=True)

                    if row[1] == "Структурированная / Рельефная":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Facturer_For_Search.objects.filter(
                                name_facturer_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Facturer_For_Search.objects.filter(
                                    name_facturer_collection=name_collection).update(
                                    collection_facturer_is_active=True,
                                    collection_stile_structured=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Facturer_For_Search.objects.create(
                                    name_facturer_collection=name_collection,
                                    collection_facturer_is_active=True,
                                    collection_stile_structured=True)

    for data_colour in data:
        if data_colour == "Texturer":
            filename = "./temp_files/filter/" + "texturer.csv"
            with open(filename, "r", newline="") as file:
                reader_file = csv.reader(file)
                for row in reader_file:

                    if row[1] == "3D / Трехмерная":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Texturer_For_Search.objects.filter(
                                name_texturer_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Texturer_For_Search.objects.filter(
                                    name_texturer_collection=name_collection).update(
                                    collection_texturer_is_active=True,
                                    collection_texturer_3d=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Texturer_For_Search.objects.create(
                                    name_texturer_collection=name_collection,
                                    collection_texturer_is_active=True,
                                    collection_texturer_3d=True)

                    if row[1] == "Арт":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Texturer_For_Search.objects.filter(
                                name_texturer_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Texturer_For_Search.objects.filter(
                                    name_texturer_collection=name_collection).update(
                                    collection_texturer_is_active=True,
                                    collection_texturer_art=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Texturer_For_Search.objects.create(
                                    name_texturer_collection=name_collection,
                                    collection_texturer_is_active=True,
                                    collection_texturer_art=True)

                    if row[1] == "Бетон / Цемент / Штукатурка":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Texturer_For_Search.objects.filter(
                                name_texturer_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Texturer_For_Search.objects.filter(
                                    name_texturer_collection=name_collection).update(
                                    collection_texturer_is_active=True,
                                    collection_texturer_concrete=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Texturer_For_Search.objects.create(
                                    name_texturer_collection=name_collection,
                                    collection_texturer_is_active=True,
                                    collection_texturer_concrete=True)

                    if row[1] == "Геометрический рисунок":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Texturer_For_Search.objects.filter(
                                name_texturer_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Texturer_For_Search.objects.filter(
                                    name_texturer_collection=name_collection).update(
                                    collection_texturer_is_active=True,
                                    collection_texturer_geometrical=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Texturer_For_Search.objects.create(
                                    name_texturer_collection=name_collection,
                                    collection_texturer_is_active=True,
                                    collection_texturer_geometrical=True)

                    if row[1] == "Дамаскато / Вензеля":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Texturer_For_Search.objects.filter(
                                name_texturer_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Texturer_For_Search.objects.filter(
                                    name_texturer_collection=name_collection).update(
                                    collection_texturer_is_active=True,
                                    collection_texturer_damaskato=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Texturer_For_Search.objects.create(
                                    name_texturer_collection=name_collection,
                                    collection_texturer_is_active=True,
                                    collection_texturer_damaskato=True)

                    if row[1] == "Дерево / Керамический паркет":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Texturer_For_Search.objects.filter(
                                name_texturer_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Texturer_For_Search.objects.filter(
                                    name_texturer_collection=name_collection).update(
                                    collection_texturer_is_active=True,
                                    collection_texturer_wood=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Texturer_For_Search.objects.create(
                                    name_texturer_collection=name_collection,
                                    collection_texturer_is_active=True,
                                    collection_texturer_wood=True)

                    if row[1] == "Камень":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Texturer_For_Search.objects.filter(
                                name_texturer_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Texturer_For_Search.objects.filter(
                                    name_texturer_collection=name_collection).update(
                                    collection_texturer_is_active=True,
                                    collection_texturer_rock=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Texturer_For_Search.objects.create(
                                    name_texturer_collection=name_collection,
                                    collection_texturer_is_active=True,
                                    collection_texturer_rock=True)

                    if row[1] == "Котто /имитация/":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Texturer_For_Search.objects.filter(
                                name_texturer_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Texturer_For_Search.objects.filter(
                                    name_texturer_collection=name_collection).update(
                                    collection_texturer_is_active=True,
                                    collection_texturer_cotto=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Texturer_For_Search.objects.create(
                                    name_texturer_collection=name_collection,
                                    collection_texturer_is_active=True,
                                    collection_texturer_cotto=True)

                    if row[1] == "Моноколор":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Texturer_For_Search.objects.filter(
                                name_texturer_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Texturer_For_Search.objects.filter(
                                    name_texturer_collection=name_collection).update(
                                    collection_texturer_is_active=True,
                                    collection_texturer_monocolor=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Texturer_For_Search.objects.create(
                                    name_texturer_collection=name_collection,
                                    collection_texturer_is_active=True,
                                    collection_texturer_monocolor=True)

                    if row[1] == "Мрамор":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Texturer_For_Search.objects.filter(
                                name_texturer_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Texturer_For_Search.objects.filter(
                                    name_texturer_collection=name_collection).update(
                                    collection_texturer_is_active=True,
                                    collection_texturer_marble=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Texturer_For_Search.objects.create(
                                    name_texturer_collection=name_collection,
                                    collection_texturer_is_active=True,
                                    collection_texturer_marble=True)

                    if row[1] == "Ткань":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Texturer_For_Search.objects.filter(
                                name_texturer_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Texturer_For_Search.objects.filter(
                                    name_texturer_collection=name_collection).update(
                                    collection_texturer_is_active=True,
                                    collection_texturer_cloth=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Texturer_For_Search.objects.create(
                                    name_texturer_collection=name_collection,
                                    collection_texturer_is_active=True,
                                    collection_texturer_cloth=True)

                    if row[1] == "Травертин":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Texturer_For_Search.objects.filter(
                                name_texturer_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Texturer_For_Search.objects.filter(
                                    name_texturer_collection=name_collection).update(
                                    collection_texturer_is_active=True,
                                    collection_texturer_travertine=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Texturer_For_Search.objects.create(
                                    name_texturer_collection=name_collection,
                                    collection_texturer_is_active=True,
                                    collection_texturer_travertine=True)

                    if row[1] == "Цветы / Растения":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Texturer_For_Search.objects.filter(
                                name_texturer_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Texturer_For_Search.objects.filter(
                                    name_texturer_collection=name_collection).update(
                                    collection_texturer_is_active=True,
                                    collection_texturer_flowers=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Texturer_For_Search.objects.create(
                                    name_texturer_collection=name_collection,
                                    collection_texturer_is_active=True,
                                    collection_texturer_flowers=True)

    for data_colour in data:
        if data_colour == "Material":
            filename = "./temp_files/filter/" + "type_material.csv"
            with open(filename, "r", newline="") as file:
                reader_file = csv.reader(file)
                for row in reader_file:

                    if row[1] == "Керамическая плитка":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Type_Material_For_Search.objects.filter(
                                name_collection_type_material__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Type_Material_For_Search.objects.filter(
                                    name_collection_type_material=name_collection).update(
                                    collection_type_material_is_active=True,
                                    collection_type_material_ceramic=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Type_Material_For_Search.objects.create(
                                    name_collection_type_material=name_collection,
                                    collection_type_material_is_active=True,
                                    collection_type_material_ceramic=True)

                    if row[1] == "Керамогранит":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Type_Material_For_Search.objects.filter(
                                name_collection_type_material__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Type_Material_For_Search.objects.filter(
                                    name_collection_type_material=name_collection).update(
                                    collection_type_material_is_active=True,
                                    collection_type_material_porcelain=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Type_Material_For_Search.objects.create(
                                    name_collection_type_material=name_collection,
                                    collection_type_material_is_active=True,
                                    collection_type_material_porcelain=True)

    for data_colour in data:
        if data_colour == "Used":
            filename = "./temp_files/filter/" + "used.csv"
            with open(filename, "r", newline="") as file:
                reader_file = csv.reader(file)
                for row in reader_file:

                    if row[1] == "Для ванных комнат":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Application_For_Search.objects.filter(
                                name_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Application_For_Search.objects.filter(
                                    name_collection=name_collection).update(
                                    collection_application_is_active=True,
                                    collection_application_bathrooms=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Application_For_Search.objects.create(
                                    name_collection=name_collection,
                                    collection_application_is_active=True,
                                    collection_application_bathrooms=True)

                    if row[1] == "Для кухни / Напольная плитка":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Application_For_Search.objects.filter(
                                name_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Application_For_Search.objects.filter(
                                    name_collection=name_collection).update(
                                    collection_application_is_active=True,
                                    collection_application_floor=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Application_For_Search.objects.create(
                                    name_collection=name_collection,
                                    collection_application_is_active=True,
                                    collection_application_floor=True)

                    if row[1] == "Для кухни / Фартук":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Application_For_Search.objects.filter(
                                name_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Application_For_Search.objects.filter(
                                    name_collection=name_collection).update(
                                    collection_application_is_active=True,
                                    collection_application_apron=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Application_For_Search.objects.create(
                                    name_collection=name_collection,
                                    collection_application_is_active=True,
                                    collection_application_apron=True)

                    if row[1] == "Для уличного применения":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Application_For_Search.objects.filter(
                                name_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Application_For_Search.objects.filter(
                                    name_collection=name_collection).update(
                                    collection_application_is_active=True,
                                    collection_application_outdoor=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Application_For_Search.objects.create(
                                    name_collection=name_collection,
                                    collection_application_is_active=True,
                                    collection_application_outdoor=True)

                    if row[1] == "Жилой интерьер":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Application_For_Search.objects.filter(
                                name_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Application_For_Search.objects.filter(
                                    name_collection=name_collection).update(
                                    collection_application_is_active=True,
                                    collection_application_residential=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Application_For_Search.objects.create(
                                    name_collection=name_collection,
                                    collection_application_is_active=True,
                                    collection_application_residential=True)

                    if row[1] == "Общественные интерьеры / Проекты":
                        all_collections = row[2]
                        all_collections = all_collections.replace("', '", "_")
                        all_collections = all_collections.replace("['", "")
                        all_collections = all_collections.replace("']", "")
                        all_collections = all_collections.split("_")
                        for single_collection in all_collections:
                            result_find = Collection_Application_For_Search.objects.filter(
                                name_collection__name_collection=single_collection)
                            if result_find.exists():
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Application_For_Search.objects.filter(
                                    name_collection=name_collection).update(
                                    collection_application_is_active=True,
                                    collection_application_projects=True)
                            else:
                                name_collection = Collection.objects.get(
                                    name_collection=single_collection)
                                Collection_Application_For_Search.objects.create(
                                    name_collection=name_collection,
                                    collection_application_is_active=True,
                                    collection_application_projects=True)
    # Bringing in the base of parameters of search is an end

    num = 0
    push_button = ""
    for dat in data:
        if num == 1 and dat != "transform" and dat != "Colour" and dat != "Floor" and dat != "Style" and dat != "Facturer" \
                and dat != "Texturer" and dat != "Material" and dat != "Used" and dat != "Id_patch":
            name_file = "./temp_files/csv/" + "ATLAS CONCORDE" + "_" + dat + ".csv"
            with open(name_file, "r", newline="") as file:
                reader_file = csv.reader(file)
                for row in reader_file:
                    image = Image.new("RGBA", (600, 600))
                    draw = ImageDraw.Draw(image)
                    draw.rectangle(((0, 0), (600, 600)), fill=(255, 255, 255))
                    del draw

                    image_mini = Image.new("RGBA", (300, 300))
                    draw = ImageDraw.Draw(image_mini)
                    draw.rectangle(((0, 0), (600, 600)), fill=(255, 255, 255))
                    del draw

                    try:
                        img_product = Image.open(row[18]).convert("RGBA")
                        (width, height) = img_product.size

                        (width1, height1) = image.size

                        if height < width:
                            koef_mini = width / 2.9
                            width_izm = int(width * 100 / koef_mini)
                            height_izm = int(height * 100 / koef_mini)
                            position_w = int(150 - (width_izm / 2))
                            position_h = int(150 - (height_izm / 2))
                            size = (width_izm, height_izm)
                            img_product = img_product.resize(size, Image.NEAREST)
                            img_product.thumbnail(size)
                            image_mini.paste(img_product, (position_w, position_h), img_product)
                            image_mini = image_mini.convert('RGB')

                            name = row[18].replace("./temp_files/img/", "")
                            full_name = "./temp_files/mini_ing_product/" + name
                            image_mini.save(full_name, "JPEG")

                            koef = width / 5.9
                            width_izm = int(width * 100 / koef)
                            height_izm = int(height * 100 / koef)
                            position_w = int(300 - (width_izm / 2))
                            position_h = int(300 - (height_izm / 2))
                            size = (width_izm, height_izm)
                            img_product = img_product.resize(size, Image.NEAREST)
                            img_product.thumbnail(size)
                            image.paste(img_product, (position_w, position_h), img_product)
                            image.convert("RGBA")
                            logo = Image.open(row[1]).convert("RGBA")
                            logo.thumbnail((150, 150))
                            image.paste(logo, (445, 445), logo)
                            image = image.convert('RGB')

                            name = row[18].replace("./temp_files/img/", "")
                            full_name = "./temp_files/new_img_product/" + name
                            image.save(full_name, "JPEG")

                        if height == width:
                            koef_mini = width / 2.9
                            width_izm = int(width * 100 / koef_mini)
                            height_izm = int(height * 100 / koef_mini)
                            position_w = int(150 - (width_izm / 2))
                            position_h = int(150 - (height_izm / 2))
                            size = (width_izm, height_izm)
                            img_product = img_product.resize(size, Image.NEAREST)
                            img_product.thumbnail(size)
                            image_mini.paste(img_product, (position_w, position_h), img_product)
                            image_mini = image_mini.convert('RGB')

                            name = row[18].replace("./temp_files/img/", "")
                            full_name = "./temp_files/mini_ing_product/" + name
                            image_mini.save(full_name, "JPEG")
                            koef = width / 5.9
                            width_izm = int(width * 100 / koef)
                            height_izm = int(height * 100 / koef)
                            position_w = int(300 - (width_izm / 2))
                            position_h = int(300 - (height_izm / 2))
                            size = (width_izm, height_izm)
                            img_product = img_product.resize(size, Image.NEAREST)
                            img_product.thumbnail(size)
                            image.paste(img_product, (position_w, position_h), img_product)
                            image.convert("RGBA")
                            logo = Image.open(row[1]).convert("RGBA")
                            logo.thumbnail((150, 150))
                            image.paste(logo, (445, 445), logo)
                            image = image.convert('RGB')
                            name = row[18].replace("./temp_files/img/", "")
                            full_name = "./temp_files/new_img_product/" + name
                            image.save(full_name, "JPEG")

                        if height > width:
                            koef_mini = height / 2.9
                            width_izm = int(width * 100 / koef_mini)
                            height_izm = int(height * 100 / koef_mini)
                            position_w = int(150 - (width_izm / 2))
                            position_h = int(150 - (height_izm / 2))
                            size = (width_izm, height_izm)
                            img_product = img_product.resize(size, Image.NEAREST)
                            img_product.thumbnail(size)
                            image_mini.paste(img_product, (position_w, position_h), img_product)
                            # image_mini.convert("RGBA")
                            image_mini = image_mini.convert('RGB')
                            name = row[18].replace("./temp_files/img/", "")
                            full_name = "./temp_files/mini_ing_product/" + name
                            image_mini.save(full_name, "JPEG")
                            koef = height / 5.9
                            width_izm = int(width * 100 / koef)
                            height_izm = int(height * 100 / koef)
                            position_w = int(300 - (width_izm / 2))
                            position_h = int(300 - (height_izm / 2))
                            size = (width_izm, height_izm)
                            img_product = img_product.resize(size, Image.NEAREST)
                            img_product.thumbnail(size)
                            image.paste(img_product, (position_w, position_h), img_product)
                            image.convert("RGBA")
                            logo = Image.open(row[1]).convert("RGBA")
                            logo.thumbnail((150, 150))
                            image.paste(logo, (445, 445), logo)
                            image = image.convert('RGB')
                            name = row[18].replace("./temp_files/img/", "")
                            full_name = "./temp_files/new_img_product/" + name
                            image.save(full_name, "JPEG")

                    except FileNotFoundError:
                        file_used = False

    # Verification of presence of country in a base and in case of absence - creation is beginning
                    if save_contr == False:
                        all_countrys = Manufacturer_Country.objects.filter()
                        list_all_countrys = []
                        for country in all_countrys:
                            list_all_countrys.append(country.name_manufacturer_country)
                        if row[5] in list_all_countrys:
                            resave_countr = Manufacturer_Country.objects.get(name_manufacturer_country=row[5])
                        else:
                            resave_countr = Manufacturer_Country.objects.create(name_manufacturer_country=row[5])
                        save_contr = True

                    resave_countr = Manufacturer_Country.objects.get(name_manufacturer_country=row[5])
    # Verification of presence of country in a base and in case of absence - creation is end

    # Verification of presence of producer in a base and in case of absence - creation (or correction) is beginning
                    if save_manaf == False:
                        all_manaf = Manufacturer.objects.filter()
                        list_manaf = []
                        for manaf in all_manaf:
                            list_manaf.append(manaf.name_manufacturer)
                        if row[0] in list_manaf:
                            resave_manaf = Manufacturer.objects.get(name_manufacturer=row[0])
                            logo = open(row[1], 'rb')
                            django_file = File(logo)
                            name_man = row[1].replace("./temp_files/logo/", "")
                            resave_manaf.image_logo_manufacturer.save(name_man, django_file)
                            resave_manaf.save()
                        else:
                            resave_manaf = Manufacturer.objects.create(name_manufacturer=row[0], manufacturer_country=resave_countr,
                                                                       is_active=True, title=row[4], keyword=row[2], description=row[3])
                            resave_manaf.save()
    # A record of logotype is beginning
                            logo = open(row[1], 'rb')
                            django_file = File(logo)
                            name_man = row[1].replace("./temp_files/logo/", "")
                            resave_manaf.image_logo_manufacturer.save(name_man, django_file)
                            resave_manaf.save()
    # A record of logotype is an end
                        save_manaf = True
                    resave_manaf = Manufacturer.objects.get(name_manufacturer=row[0])
    # Verification of presence of producer in a base and in case of absence - creation (or correction) is an end

    # Verification of presence of price group in a base and in case of absence - creation is beginning
                    if save_prise_group == False:
                        all_prise_group = Price_Group.objects.filter()
                        list_prise_group = []
                        for prise_group in all_prise_group:
                            list_prise_group.append(prise_group.name_price_group)
                        if row[11] in list_prise_group:
                            resave_price_group = Price_Group.objects.get(name_price_group=row[11])
                        else:
                            resave_price_group = Price_Group.objects.create(name_price_group=row[11])
                        save_prise_group = True

                    resave_price_group = Price_Group.objects.get(name_price_group=row[11])
    # Verification of presence of price group in a base and in case of absence - creation is an end

    # Verification of presence of presence in a base and in case of absence - creation is beginning
                    if save_availability == False:
                        all_availability = Availability.objects.filter()
                        list_availability = []
                        for availability in all_availability:
                            list_availability.append(availability.name_availability)
                        if row[10] in list_availability:
                            resave_availability = Availability.objects.get(name_availability=row[10])
                        else:
                            resave_availability = Availability.objects.create(name_availability=row[10])
                        save_availability = True

                    resave_availability = Availability.objects.get(name_availability=row[10])
    # Verification of presence of presence in a base and in case of absence - creation is an end

    # Verification of presence of NHS in a base and in case of absence - creation is beginning
                    if save_nhs == False:
                        all_nhs = Collection_Search_NHS.objects.filter()
                        list_nhs = []
                        for nhs in all_nhs:
                            list_nhs.append(nhs.name_collection_nhs)
                        if row[13] in list_nhs and row[13] != "Статус NHS - ОТСУТСВУЕТ":
                            resave_nhs = Collection_Search_NHS.objects.get(name_collection_nhs=row[13])
                        else:
                            if row[13] != "Статус NHS - ОТСУТСВУЕТ":
                                resave_nhs = Collection_Search_NHS.objects.create(name_collection_nhs=row[13])
                        save_nhs = True

                    if row[13] != "Статус NHS - ОТСУТСВУЕТ":
                        resave_nhs = Collection_Search_NHS.objects.get(name_collection_nhs=row[13])
                    else:
                        resave_nhs = ""
    # Verification of presence of NHS in a base and in case of absence - creation is an end

    # Verification of presence of collection in a base and in case of absence - creation (or correction) is beginning
                    if save_colle == False:

    # Moving away of all pictures for collection and pdf- catalogue is beginning
                        all_imgs_collection = Collection_Image.objects.filter(name_collection__name_collection=row[6])
                        for all_img_collection in all_imgs_collection:
                            all_img_collection.delete()
    # Moving away of all pictures for collection is an end

                        all_collection = Collection.objects.filter()
                        list_all_collection = []
                        for collection_in in all_collection:
                            list_all_collection.append(collection_in.name_collection)
                        if row[6] in list_all_collection:

                            directory = "./temp_files/AtlasConcord/" + row[6] + "/"
                            files = os.listdir(directory)
                            pdf_catalog = filter(lambda x: x.endswith('.pdf'), files)
                            for pdf_files in pdf_catalog:
                                pass
                            file_pdf = open(directory + pdf_files, 'rb')
                            django_file = File(file_pdf)

                            resave_collection = Collection.objects.filter(name_collection=row[6]).update(is_active_collection=True,
                                                                                                         is_view_main=True,
                                                                                                         manufacturer_collection=resave_manaf,
                                                                                                         availability_collection=resave_availability,
                                                                                                         price_group_collection=resave_price_group,
                                                                                                         title=row[9], keyword=row[7],
                                                                                                         description=row[8])
                            if resave_nhs != "Статус NHS - ОТСУТСВУЕТ":
                                Collection.objects.filter(name_collection=row[6]).update(name_collection_nhs=resave_nhs)

                            resave_collection = Collection.objects.get(name_collection=row[6])
                            resave_collection.price_download.save(pdf_files, django_file)
                        else:
                            directory = "./temp_files/AtlasConcord/" + row[6] + "/"
                            files = os.listdir(directory)
                            pdf_catalog = filter(lambda x: x.endswith('.pdf'), files)
                            for pdf_files in pdf_catalog:
                                pass


                            file_pdf = open(directory + pdf_files, 'rb')
                            django_file = File(file_pdf)

                            resave_collection = Collection.objects.create(name_collection=row[6], is_active_collection=True,
                                                                          is_view_main=False, manufacturer_collection=resave_manaf,
                                                                          availability_collection=resave_availability,
                                                                          price_group_collection=resave_price_group,
                                                                          title=row[9], keyword=row[7], description=row[8])
                            if resave_nhs != "Статус NHS - ОТСУТСВУЕТ":
                                Collection.objects.filter(name_collection=row[6]).update(name_collection_nhs=resave_nhs)


                            resave_collection = Collection.objects.get(name_collection=row[6])
                            resave_collection.price_download.save(pdf_files, django_file)
                        save_colle = True
                    resave_collection = Collection.objects.get(name_collection=row[6])

    # Preparation and record of images and pdf- catalogue are beginning
                    if recheng_img == False:
                        recheng_img = True
                        directory = "./temp_files/AtlasConcord/" + row[6] + "/"
                        files = os.listdir(directory)
                        images = filter(lambda x: x.endswith('.jpg'), files)

                        main_img = True
                        for image in images:
                            if main_img == True:
                                new_img = Collection_Image.objects.create(name_collection=resave_collection, is_active_collection=True,
                                                                          is_main_collection=True)
                            else:
                                new_img = Collection_Image.objects.create(name_collection=resave_collection, is_active_collection=True)
                            full_collection_file = directory + image
                            img = open(full_collection_file, 'rb')
                            django_file = File(img)
                            new_img.image_collection.save(image, django_file)
                            main_img = False
    # Preparation and record of images and pdf- catalogue are an end

    # Verification of presence of collection in a base and in case of absence - creation (or correction) is an end

    # Verification of presence of size in a base and in case of absence - creation is beginning
                    all_size = Size.objects.filter()
                    list_size = []
                    for size_in in all_size:
                        list_size.append(size_in.name_size)
                    if row[16] in list_size:
                        resave_size = Size.objects.get(name_size=row[16])
                    else:
                        resave_size = Size.objects.create(name_size=row[16])

                    resave_size = Size.objects.get(name_size=row[16])
    # Verification of presence of size in a base and in case of absence - creation is an end

    # Verification of presence of type of product in a base and in case of absence - creation is beginning
                    all_type_product = Product_Type.objects.filter()
                    list_type_product = []
                    for type_product in all_type_product:
                        list_type_product.append(type_product.name_product_type)
                    if row[14] in list_type_product:
                        resave_type_product = Product_Type.objects.get(name_product_type=row[14])
                    else:
                        resave_type_product = Product_Type.objects.create(name_product_type=row[14])

                    resave_type_product = Product_Type.objects.get(name_product_type=row[14])
    # Verification of presence of type of product in a base and in case of absence - creation is an end

    # Verification of presence of product in a base and in case of absence - creation (or correction) is beginning
                    all_products = Product.objects.filter()
                    list_all_products = []
                    for products in all_products:
                        list_all_products.append(products.name_product)

                    if "Наименование фото с русскими буквами" not in row[18]:
                        if row[15] in list_all_products:
                            Product.objects.filter(name_product=row[15]).update(collection_product=resave_collection,
                                                                                size_product=resave_size, vendor_code_product=row[17],
                                                                                product_type_product=resave_type_product, is_active=True)

                            resave_product = Product.objects.get(name_product=row[15])
                            id_product = resave_product.id
    # Treatment and maintenance of image mini and normal is beginning
                            img_basa_product = Product_Image.objects.get(product__id=id_product)
                            name_img_product = row[18].replace("./temp_files/img/", "")
                            full_img_product = "./temp_files/new_img_product/" + name_img_product
                            mini_img_product = "./temp_files/mini_ing_product/" + name_img_product
                            img = open(full_img_product, 'rb')
                            django_file = File(img)
                            img_basa_product.image.save(name_img_product, django_file)

                            img_mini = open(mini_img_product, 'rb')
                            django_file_mini = File(img_mini)
                            img_basa_product.image_mini.save(name_img_product, django_file_mini)

                            img_basa_product.save()
    # Treatment and maintenance of image mini and normal is an end
                        else:
                            resave_product = Product.objects.create(name_product=row[15], collection_product=resave_collection, size_product=resave_size,
                                                                    vendor_code_product=row[17], product_type_product=resave_type_product, is_active=True)
                            id_product = resave_product.id
    # Treatment and maintenance of image mini and normal is beginning
                            img_basa_product = Product_Image.objects.create(product=resave_product, is_main=True, is_active=True)

                            name_img_product = row[18].replace("./temp_files/img/", "")
                            full_img_product = "./temp_files/new_img_product/" + name_img_product
                            mini_img_product = "./temp_files/mini_ing_product/" + name_img_product

                            img = open(full_img_product, 'rb')
                            django_file = File(img)
                            img_basa_product.image.save(name_img_product, django_file)

                            img_mini = open(mini_img_product, 'rb')
                            django_file_mini = File(img_mini)
                            img_basa_product.image_mini.save(name_img_product, django_file_mini)

                            img_basa_product.save()
    # Treatment and maintenance of image mini and normal is an end
    # Verification of presence of product in a base and in case of absence - creation (or correction) is an end
        num += 1

    return render(request, 'shadow/pars.html', locals())
