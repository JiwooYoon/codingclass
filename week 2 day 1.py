import requests # requests 라이브러리 설치 필요

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()
gu_infos = rjson['RealtimeCityAir']['row']


def get_MVL(gu_name):
    for gu_info in gu_infos:
        if gu_info['MSRSTE_NM'] == gu_name:
            return gu_info['IDEX_MVL']
    return 'N/A'



print (get_MVL('서초구'))
print (get_MVL('관악구'))