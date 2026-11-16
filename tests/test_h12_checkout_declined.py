import json  # noqa: F401


def test_h12_invalid_number_0001(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'PHP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PHP"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0002(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'PLN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PLN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0003(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'RON', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RON"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0004(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'RUB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RUB"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0005(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'SEK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SEK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0006(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'SGD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SGD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0007(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'THB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "THB"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0008(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'TRY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "TRY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0009(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'USD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "USD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0010(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'ZAR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ZAR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0011(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'AUD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "AUD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0012(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'BGN', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BGN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0013(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'BRL', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BRL"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0014(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CAD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CAD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0015(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CHF', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CHF"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0016(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CNY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CNY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0017(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'CZK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CZK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0018(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'DKK', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "DKK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0019(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'EUR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "EUR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0020(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'GBP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "GBP"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0021(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'HKD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HKD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0022(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'HRK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HRK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0023(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'HUF', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HUF"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0024(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'IDR', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "IDR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0025(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'ILS', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ILS"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0026(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'INR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "INR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0027(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'ISK', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ISK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0028(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'JPY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "JPY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0029(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'KRW', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "KRW"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0030(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'MXN', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MXN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0031(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'MYR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MYR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0032(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'NOK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NOK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0033(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'NZD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NZD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0034(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'PHP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PHP"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0035(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'PLN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PLN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0036(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'RON', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RON"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0037(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'RUB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RUB"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0038(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'SEK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SEK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0039(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'SGD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SGD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0040(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'THB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "THB"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0041(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'TRY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "TRY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0042(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'USD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "USD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0043(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'ZAR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ZAR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0044(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'AUD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "AUD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0045(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'BGN', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BGN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0046(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'BRL', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BRL"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0047(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'CAD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CAD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0048(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CHF', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CHF"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0049(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CNY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CNY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0050(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CZK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CZK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0051(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'DKK', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "DKK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0052(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'EUR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "EUR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0053(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'GBP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "GBP"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0054(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'HKD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HKD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0055(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'HRK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HRK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0056(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'HUF', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HUF"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0057(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'IDR', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "IDR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0058(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'ILS', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ILS"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0059(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'INR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "INR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0060(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'ISK', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ISK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0061(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'JPY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "JPY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0062(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'KRW', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "KRW"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0063(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'MXN', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MXN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0064(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'MYR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MYR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0065(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'NOK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NOK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0066(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'NZD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NZD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0067(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'PHP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PHP"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0068(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'PLN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PLN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0069(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'RON', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RON"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0070(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'RUB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RUB"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0071(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'SEK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SEK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0072(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'SGD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SGD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0073(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'THB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "THB"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0074(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'TRY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "TRY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0075(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'USD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "USD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0076(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'ZAR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ZAR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0077(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'AUD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "AUD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0078(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'BGN', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BGN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0079(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'BRL', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BRL"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0080(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CAD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CAD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0081(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CHF', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CHF"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0082(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'CNY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CNY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0083(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CZK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CZK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0084(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'DKK', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "DKK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0085(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'EUR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "EUR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0086(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'GBP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "GBP"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0087(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'HKD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HKD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0088(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'HRK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HRK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0089(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'HUF', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HUF"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0090(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'IDR', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "IDR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0091(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'ILS', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ILS"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0092(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'INR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "INR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0093(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'ISK', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ISK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0094(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'JPY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "JPY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0095(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'KRW', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "KRW"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0096(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'MXN', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MXN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0097(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'MYR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MYR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0098(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'NOK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NOK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0099(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'NZD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NZD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0100(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'PHP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PHP"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0101(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'PLN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PLN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0102(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'RON', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RON"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0103(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'RUB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RUB"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0104(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'SEK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SEK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0105(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'SGD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SGD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0106(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'THB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "THB"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0107(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'TRY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "TRY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0108(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'USD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "USD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0109(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'ZAR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ZAR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0110(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'AUD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "AUD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0111(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'BGN', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BGN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0112(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'BRL', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BRL"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0113(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CAD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CAD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0114(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CHF', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CHF"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0115(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CNY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CNY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0116(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CZK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CZK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0117(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'DKK', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "DKK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0118(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'EUR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "EUR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0119(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'GBP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "GBP"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0120(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'HKD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HKD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0121(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'HRK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HRK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0122(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'HUF', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HUF"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0123(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'IDR', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "IDR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0124(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'ILS', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ILS"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0125(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'INR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "INR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0126(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'ISK', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ISK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0127(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'JPY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "JPY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0128(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'KRW', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "KRW"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0129(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'MXN', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MXN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0130(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'MYR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MYR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0131(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'NOK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NOK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0132(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'NZD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NZD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0133(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'PHP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PHP"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0134(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'PLN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PLN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0135(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'RON', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RON"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0136(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'RUB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RUB"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0137(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'SEK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SEK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0138(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'SGD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SGD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0139(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'THB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "THB"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0140(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'TRY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "TRY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0141(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'USD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "USD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0142(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'ZAR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ZAR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0143(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'AUD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "AUD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0144(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'BGN', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BGN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0145(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'BRL', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BRL"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0146(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CAD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CAD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0147(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'CHF', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CHF"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0148(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CNY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CNY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0149(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CZK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CZK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0150(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'DKK', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "DKK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0151(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'EUR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "EUR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0152(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'GBP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "GBP"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0153(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'HKD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HKD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0154(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'HRK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HRK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0155(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'HUF', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HUF"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0156(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'IDR', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "IDR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0157(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'ILS', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ILS"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0158(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'INR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "INR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0159(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'ISK', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ISK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0160(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'JPY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "JPY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0161(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'KRW', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "KRW"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0162(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'MXN', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MXN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0163(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'MYR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MYR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0164(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'NOK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NOK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0165(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'NZD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NZD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0166(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'PHP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PHP"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0167(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'PLN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PLN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0168(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'RON', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RON"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0169(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'RUB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RUB"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0170(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'SEK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SEK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0171(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'SGD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SGD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0172(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'THB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "THB"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0173(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'TRY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "TRY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0174(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'USD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "USD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0175(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'ZAR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ZAR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0176(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'AUD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "AUD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0177(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'BGN', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BGN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0178(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'BRL', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BRL"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0179(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CAD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CAD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0180(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CHF', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CHF"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0181(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CNY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CNY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0182(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'CZK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CZK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0183(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'DKK', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "DKK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0184(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'EUR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "EUR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0185(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'GBP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "GBP"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0186(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'HKD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HKD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0187(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'HRK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HRK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0188(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'HUF', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HUF"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0189(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'IDR', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "IDR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0190(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'ILS', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ILS"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0191(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'INR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "INR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0192(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'ISK', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ISK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0193(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'JPY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "JPY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0194(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'KRW', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "KRW"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0195(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'MXN', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MXN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0196(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'MYR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MYR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0197(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'NOK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NOK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0198(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'NZD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NZD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0199(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'PHP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PHP"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0200(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'PLN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PLN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0201(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'RON', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RON"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0202(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'RUB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RUB"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0203(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'SEK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SEK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0204(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'SGD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SGD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0205(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'THB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "THB"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0206(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'TRY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "TRY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0207(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'USD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "USD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0208(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'ZAR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ZAR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0209(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'AUD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "AUD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0210(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'BGN', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BGN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0211(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'BRL', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BRL"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0212(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'CAD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CAD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0213(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CHF', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CHF"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0214(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CNY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CNY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0215(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CZK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CZK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0216(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'DKK', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "DKK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0217(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'EUR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "EUR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0218(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'GBP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "GBP"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0219(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'HKD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HKD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0220(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'HRK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HRK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0221(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'HUF', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HUF"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0222(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'IDR', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "IDR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0223(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'ILS', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ILS"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0224(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'INR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "INR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0225(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'ISK', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ISK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0226(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'JPY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "JPY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0227(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'KRW', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "KRW"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0228(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'MXN', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MXN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0229(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'MYR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MYR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0230(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'NOK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NOK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0231(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'NZD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NZD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0232(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'PHP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PHP"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0233(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'PLN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PLN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0234(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'RON', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RON"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0235(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'RUB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RUB"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0236(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'SEK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SEK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0237(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'SGD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SGD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0238(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'THB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "THB"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0239(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'TRY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "TRY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0240(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'USD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "USD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0241(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'ZAR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ZAR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0242(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'AUD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "AUD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0243(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'BGN', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BGN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0244(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'BRL', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BRL"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0245(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CAD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CAD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0246(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CHF', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CHF"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0247(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'CNY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CNY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0248(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CZK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CZK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0249(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'DKK', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "DKK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0250(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'EUR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "EUR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0251(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'GBP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "GBP"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0252(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'HKD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HKD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0253(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'HRK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HRK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0254(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'HUF', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HUF"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0255(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'IDR', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "IDR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0256(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'ILS', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ILS"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0257(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'INR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "INR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0258(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'ISK', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ISK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0259(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'JPY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "JPY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0260(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'KRW', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "KRW"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0261(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'MXN', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MXN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0262(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'MYR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MYR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0263(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'NOK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NOK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0264(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'NZD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NZD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0265(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'PHP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PHP"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0266(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'PLN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PLN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0267(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'RON', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RON"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0268(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'RUB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RUB"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0269(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'SEK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SEK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0270(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'SGD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SGD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0271(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'THB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "THB"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0272(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'TRY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "TRY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0273(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'USD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "USD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0274(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'ZAR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ZAR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0275(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'AUD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "AUD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0276(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'BGN', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BGN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0277(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'BRL', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BRL"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0278(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CAD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CAD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0279(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CHF', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CHF"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0280(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CNY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CNY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0281(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CZK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CZK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0282(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'DKK', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "DKK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0283(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'EUR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "EUR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0284(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'GBP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "GBP"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0285(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'HKD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HKD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0286(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'HRK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HRK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0287(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'HUF', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HUF"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0288(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'IDR', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "IDR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0289(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'ILS', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ILS"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0290(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'INR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "INR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0291(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'ISK', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ISK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0292(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'JPY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "JPY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0293(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'KRW', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "KRW"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0294(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'MXN', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MXN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0295(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'MYR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MYR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0296(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'NOK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NOK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0297(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'NZD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NZD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0298(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'PHP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PHP"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0299(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'PLN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PLN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0300(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'RON', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RON"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0301(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'RUB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RUB"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0302(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'SEK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SEK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0303(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'SGD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SGD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0304(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'THB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "THB"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0305(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'TRY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "TRY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0306(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'USD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "USD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0307(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'ZAR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ZAR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0308(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'AUD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "AUD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0309(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'BGN', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BGN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0310(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'BRL', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BRL"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0311(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CAD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CAD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0312(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'CHF', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CHF"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0313(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CNY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CNY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0314(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CZK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CZK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0315(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'DKK', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "DKK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0316(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'EUR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "EUR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0317(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'GBP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "GBP"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0318(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'HKD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HKD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0319(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'HRK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HRK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0320(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'HUF', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HUF"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0321(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'IDR', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "IDR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0322(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'ILS', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ILS"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0323(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'INR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "INR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0324(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'ISK', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ISK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0325(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'JPY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "JPY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0326(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'KRW', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "KRW"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0327(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'MXN', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MXN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0328(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'MYR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MYR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0329(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'NOK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NOK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0330(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'NZD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NZD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0331(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'PHP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PHP"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0332(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'PLN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PLN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0333(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'RON', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RON"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0334(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'RUB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RUB"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0335(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'SEK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SEK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0336(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'SGD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SGD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0337(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'THB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "THB"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0338(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'TRY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "TRY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0339(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'USD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "USD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0340(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'ZAR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ZAR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0341(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'AUD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "AUD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0342(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'BGN', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BGN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0343(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'BRL', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BRL"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0344(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CAD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CAD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0345(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CHF', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CHF"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0346(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CNY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CNY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0347(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'CZK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CZK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0348(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'DKK', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "DKK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0349(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'EUR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "EUR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0350(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'GBP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "GBP"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0351(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'HKD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HKD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0352(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'HRK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HRK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0353(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'HUF', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HUF"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0354(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'IDR', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "IDR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0355(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'ILS', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ILS"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0356(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'INR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "INR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0357(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'ISK', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ISK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0358(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'JPY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "JPY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0359(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'KRW', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "KRW"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0360(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'MXN', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MXN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0361(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'MYR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MYR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0362(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'NOK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NOK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0363(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'NZD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NZD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0364(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'PHP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PHP"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0365(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'PLN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PLN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0366(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'RON', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RON"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0367(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'RUB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RUB"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0368(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'SEK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SEK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0369(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'SGD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "SGD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0370(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'THB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "THB"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0371(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'TRY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "TRY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0372(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'USD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "USD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0373(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'ZAR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ZAR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0374(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'AUD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "AUD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0375(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'BGN', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BGN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0376(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'BRL', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "BRL"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0377(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'CAD', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CAD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0378(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CHF', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CHF"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0379(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'CNY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CNY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0380(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'CZK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "CZK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0381(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'DKK', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "DKK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0382(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'EUR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "EUR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0383(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'GBP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "GBP"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0384(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'HKD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HKD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0385(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'HRK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HRK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0386(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'HUF', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "HUF"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0387(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'IDR', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "IDR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0388(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'ILS', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ILS"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0389(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'INR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "INR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0390(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'ISK', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "ISK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0391(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "6E92ZMYYFZ", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'JPY', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "JPY"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0392(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "HQTGWGPNH4", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'KRW', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "KRW"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0393(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "OLJCESPC7Z", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'MXN', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MXN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0394(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "66VCHSJNUP", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'MYR', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "MYR"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0395(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "1YMWWN1N4O", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'NOK', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NOK"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0396(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "L9ECAV7KIM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '410 Terry Ave N', 'zipCode': '98109', 'city': 'Seattle', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'NZD', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "NZD"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0397(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "2ZYFJ3GM2N", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '100 Queen St W', 'zipCode': 'M5H 2N2', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada'}, 'userCurrency': 'PHP', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PHP"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_expired_0398(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "0PUK6V6EV0", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1600 Amphitheatre Parkway', 'zipCode': '94043', 'city': 'Mountain View', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'PLN', 'creditCard': {'creditCardNumber': '4432-8015-6152-0454', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2020, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "PLN"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_amex_0399(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "LS4PSXUNUM", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': 'One Microsoft Way', 'zipCode': '98052', 'city': 'Redmond', 'state': 'WA', 'country': 'United States'}, 'userCurrency': 'RON', 'creditCard': {'creditCardNumber': '3782-822463-10005', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 1234}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RON"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"


def test_h12_invalid_number_0400(api, user_id):
    resp = api.post("/api/cart", json={"userId": user_id, "item": {"productId": "9SIQT8TOJO", "quantity": 1}})
    assert resp.status_code == 200
    order = {'email': 'testbot@example.com', 'address': {'streetAddress': '1 Infinite Loop', 'zipCode': '95014', 'city': 'Cupertino', 'state': 'CA', 'country': 'United States'}, 'userCurrency': 'RUB', 'creditCard': {'creditCardNumber': '4432-8015-6152-0455', 'creditCardExpirationMonth': 1, 'creditCardExpirationYear': 2039, 'creditCardCvv': 672}}
    order["userId"] = user_id
    resp = api.post("/api/checkout", params={"currencyCode": "RUB"}, json=order)
    assert resp.status_code == 422
    assert resp.json()["code"] == "PAYMENT_FAILED"
