import requests
import json
headers = {
    "Authorization":"Bearer ya29.a0AX9GBdUCkpXGhn0tRH_c_Ipb42XcurCai26s_Tv2WOq2Gh5ZJkiXIOU4phbZjN1Bs1T_ru_iFCfAQPiVf_C3YdPuOl0aOR0iioaga-NQtC1EIlE4EYchCESYU4Z25Hd0wXXRRP6Ns0Kw44YnGWyqe040uzPfaCgYKAYQSARESFQHUCsbCqiDYb77AFaNAeg3hoPJZQQ0163"
}
 
para = {
    "name":"image7.png",
}
 
files = {
    'data':('metadata',json.dumps(para),'application/json;charset=UTF-8'),
    'file':open("C:/Users/100050/OneDrive - AIF Rwanda/Irene Nsengumukiza/Downloads/ML/ml1/formed image/image7.png",'rb')
}
 
r = requests.post("https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
