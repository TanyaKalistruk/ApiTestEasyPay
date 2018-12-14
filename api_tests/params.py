class Urls:
    url = 'http://localhost:8080/authorization'
    url_update_price = 'http://localhost:8080/manager/utility/price/add'
    url_delete_inspector = 'http://localhost:8080/manager/schedule/deleteInspector'
    url_add_inspector = 'http://localhost:8080/manager/schedule/addInspector'


class Par:
    new_price = '8'
    inspector_id = 110
    id_add = ["110"]


class Json:
    params_login_manager = {"email": "manager1@gmail.com", "password": "Admin123"}
    update_price = {"currentPriceId": 7, "price": Par.new_price, "date": "2018-12-14", "utilityPriceDTO":
        {"utilityId": 2, "utilityName": "ДнепрОблЭнерго", "active": True}, "priceAddressDTO":
                        {"addressId": 2, "cityName": "Кривий Ріг", "streetName": "вулиця Ватутіна",
                         "houseNumber": "18"}, "active": True}
    negative_update_price = {"currentPriceId": 7, "price": '-1', "date": "2018-12-14", "utilityPriceDTO":
        {"utilityId": 2, "utilityName": "ДнепрОблЭнерго", "active": True}, "priceAddressDTO":
                                 {"addressId": 2, "cityName": "Кривий Ріг", "streetName": "вулиця Ватутіна",
                                  "houseNumber": "18"}, "active": True}


class Header:
    header = {'Content-Type': 'application/json'}
