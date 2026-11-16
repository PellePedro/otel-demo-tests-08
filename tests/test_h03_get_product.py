import json  # noqa: F401


def test_h03_66vchsjnup_aud_0001(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h03_1ymwwn1n4o_bgn_0002(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h03_l9ecav7kim_brl_0003(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h03_2zyfj3gm2n_cad_0004(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h03_0puk6v6ev0_chf_0005(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h03_ls4psxunum_cny_0006(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h03_9siqt8tojo_czk_0007(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h03_6e92zmyyfz_dkk_0008(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h03_hqtgwgpnh4_eur_0009(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h03_oljcespc7z_gbp_0010(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h03_66vchsjnup_hkd_0011(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h03_1ymwwn1n4o_hrk_0012(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h03_l9ecav7kim_huf_0013(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h03_2zyfj3gm2n_idr_0014(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h03_0puk6v6ev0_ils_0015(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h03_ls4psxunum_inr_0016(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "INR"


def test_h03_9siqt8tojo_isk_0017(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h03_6e92zmyyfz_jpy_0018(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h03_hqtgwgpnh4_krw_0019(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h03_oljcespc7z_mxn_0020(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h03_66vchsjnup_myr_0021(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h03_1ymwwn1n4o_nok_0022(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h03_l9ecav7kim_nzd_0023(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h03_2zyfj3gm2n_php_0024(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h03_0puk6v6ev0_pln_0025(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h03_ls4psxunum_ron_0026(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "RON"


def test_h03_9siqt8tojo_rub_0027(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h03_6e92zmyyfz_sek_0028(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h03_hqtgwgpnh4_sgd_0029(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h03_oljcespc7z_thb_0030(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "THB"


def test_h03_66vchsjnup_try_0031(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h03_1ymwwn1n4o_usd_0032(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "USD"
    assert product["priceUsd"]["units"] == 129
    assert product["priceUsd"]["nanos"] == 950000000


def test_h03_l9ecav7kim_zar_0033(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h03_2zyfj3gm2n_aud_0034(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h03_0puk6v6ev0_bgn_0035(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h03_ls4psxunum_brl_0036(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h03_9siqt8tojo_cad_0037(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h03_6e92zmyyfz_chf_0038(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h03_hqtgwgpnh4_cny_0039(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h03_oljcespc7z_czk_0040(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h03_66vchsjnup_dkk_0041(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h03_1ymwwn1n4o_eur_0042(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h03_l9ecav7kim_gbp_0043(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h03_2zyfj3gm2n_hkd_0044(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h03_0puk6v6ev0_hrk_0045(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h03_ls4psxunum_huf_0046(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h03_9siqt8tojo_idr_0047(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h03_6e92zmyyfz_ils_0048(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h03_hqtgwgpnh4_inr_0049(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "INR"


def test_h03_oljcespc7z_isk_0050(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h03_66vchsjnup_jpy_0051(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h03_1ymwwn1n4o_krw_0052(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h03_l9ecav7kim_mxn_0053(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h03_2zyfj3gm2n_myr_0054(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h03_0puk6v6ev0_nok_0055(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h03_ls4psxunum_nzd_0056(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h03_9siqt8tojo_php_0057(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h03_6e92zmyyfz_pln_0058(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h03_hqtgwgpnh4_ron_0059(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "RON"


def test_h03_oljcespc7z_rub_0060(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h03_66vchsjnup_sek_0061(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h03_1ymwwn1n4o_sgd_0062(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h03_l9ecav7kim_thb_0063(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "THB"


def test_h03_2zyfj3gm2n_try_0064(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h03_0puk6v6ev0_usd_0065(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "USD"
    assert product["priceUsd"]["units"] == 175
    assert product["priceUsd"]["nanos"] == 0


def test_h03_ls4psxunum_zar_0066(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h03_9siqt8tojo_aud_0067(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h03_6e92zmyyfz_bgn_0068(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h03_hqtgwgpnh4_brl_0069(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h03_oljcespc7z_cad_0070(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h03_66vchsjnup_chf_0071(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h03_1ymwwn1n4o_cny_0072(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h03_l9ecav7kim_czk_0073(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h03_2zyfj3gm2n_dkk_0074(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h03_0puk6v6ev0_eur_0075(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h03_ls4psxunum_gbp_0076(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h03_9siqt8tojo_hkd_0077(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h03_6e92zmyyfz_hrk_0078(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h03_hqtgwgpnh4_huf_0079(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h03_oljcespc7z_idr_0080(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h03_66vchsjnup_ils_0081(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h03_1ymwwn1n4o_inr_0082(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "INR"


def test_h03_l9ecav7kim_isk_0083(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h03_2zyfj3gm2n_jpy_0084(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h03_0puk6v6ev0_krw_0085(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h03_ls4psxunum_mxn_0086(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h03_9siqt8tojo_myr_0087(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h03_6e92zmyyfz_nok_0088(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h03_hqtgwgpnh4_nzd_0089(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h03_oljcespc7z_php_0090(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h03_66vchsjnup_pln_0091(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h03_1ymwwn1n4o_ron_0092(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "RON"


def test_h03_l9ecav7kim_rub_0093(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h03_2zyfj3gm2n_sek_0094(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h03_0puk6v6ev0_sgd_0095(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h03_ls4psxunum_thb_0096(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "THB"


def test_h03_9siqt8tojo_try_0097(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h03_6e92zmyyfz_usd_0098(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "USD"
    assert product["priceUsd"]["units"] == 69
    assert product["priceUsd"]["nanos"] == 950000000


def test_h03_hqtgwgpnh4_zar_0099(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h03_oljcespc7z_aud_0100(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h03_66vchsjnup_bgn_0101(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h03_1ymwwn1n4o_brl_0102(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h03_l9ecav7kim_cad_0103(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h03_2zyfj3gm2n_chf_0104(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h03_0puk6v6ev0_cny_0105(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h03_ls4psxunum_czk_0106(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h03_9siqt8tojo_dkk_0107(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h03_6e92zmyyfz_eur_0108(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h03_hqtgwgpnh4_gbp_0109(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h03_oljcespc7z_hkd_0110(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h03_66vchsjnup_hrk_0111(api):
    resp = api.get("/api/products/66VCHSJNUP", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "66VCHSJNUP"
    assert product["name"] == 'Starsense Explorer Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h03_1ymwwn1n4o_huf_0112(api):
    resp = api.get("/api/products/1YMWWN1N4O", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "1YMWWN1N4O"
    assert product["name"] == 'Eclipsmart Travel Refractor Telescope'
    assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h03_l9ecav7kim_idr_0113(api):
    resp = api.get("/api/products/L9ECAV7KIM", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "L9ECAV7KIM"
    assert product["name"] == 'Lens Cleaning Kit'
    assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h03_2zyfj3gm2n_ils_0114(api):
    resp = api.get("/api/products/2ZYFJ3GM2N", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "2ZYFJ3GM2N"
    assert product["name"] == 'Roof Binoculars'
    assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h03_0puk6v6ev0_inr_0115(api):
    resp = api.get("/api/products/0PUK6V6EV0", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "0PUK6V6EV0"
    assert product["name"] == 'Solar System Color Imager'
    assert product["priceUsd"]["currencyCode"] == "INR"


def test_h03_ls4psxunum_isk_0116(api):
    resp = api.get("/api/products/LS4PSXUNUM", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "LS4PSXUNUM"
    assert product["name"] == 'Red Flashlight'
    assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h03_9siqt8tojo_jpy_0117(api):
    resp = api.get("/api/products/9SIQT8TOJO", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "9SIQT8TOJO"
    assert product["name"] == 'Optical Tube Assembly'
    assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h03_6e92zmyyfz_krw_0118(api):
    resp = api.get("/api/products/6E92ZMYYFZ", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "6E92ZMYYFZ"
    assert product["name"] == 'Solar Filter'
    assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h03_hqtgwgpnh4_mxn_0119(api):
    resp = api.get("/api/products/HQTGWGPNH4", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "HQTGWGPNH4"
    assert product["name"] == 'The Comet Book'
    assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h03_oljcespc7z_myr_0120(api):
    resp = api.get("/api/products/OLJCESPC7Z", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    product = resp.json()
    assert product["id"] == "OLJCESPC7Z"
    assert product["name"] == 'National Park Foundation Explorascope'
    assert product["priceUsd"]["currencyCode"] == "MYR"
