import requests
from bs4 import BeautifulSoup as bs
import json


#Petrol ofisi

def petrolOfisi(il: str = ...) -> list:
    __requests = requests.get(url=f"https://www.petrolofisi.com.tr/akaryakit-fiyatlari/{il}-akaryakit-fiyatlari")
    data = []
    if __requests.status_code == 200:
        __parse = bs(__requests.content, "lxml").find("table", attrs={"id":"fuelPricesTableDesktop"})
        
        tbodyElement = __parse.find("tbody").find_all("tr")
        for i in tbodyElement:
            data.append(json.loads(
                json.dumps({
                    "ilce":str(i.find_all("td")[0].getText()).strip(),
                    "v/maxKursunsuz95":str(i.find_all("td")[1].getText()).strip(),
                    "v/maxDiesel":str(i.find_all("td")[2].getText()).strip(),
                    "v/proDiesel":str(i.find_all("td")[3].getText()).strip(),
                    "pogazLpg":str(i.find_all("td")[4].getText()).strip()
                    
                })))

    return (data)


def plakaKodu(il: str = ...) -> str:
    __jsonFile = json.loads(open("iller.json", mode="r", encoding="utf-8").read())
    for key, value in __jsonFile.items():
        if value == il:
            return (key)



#TPPD
def türkiyePetrolleri(plakaKod) -> list:
    __requests = requests.get(url=f"https://www.tppd.com.tr/tr/akaryakit-fiyatlari?id={plakaKod}")
    data = []
    if __requests.status_code == 200:
        __parse = bs(__requests.content, "lxml").find("table", class_="col-md-12 table table-bordered cf").find("tbody").find_all("tr")
        for i in __parse:
            data.append(json.loads(json.dumps({
                "ilce":str(i.find_all("td")[0].getText()).strip(),
                "kursunsuzBenzin":str(i.find_all("td")[1].getText()).strip(),
                "gazYagı":str(i.find_all("td")[2].getText()).strip(),
                "tpMotorin":str(i.find_all("td")[3].getText()).strip(),
                "motorin":str(i.find_all("td")[4].getText()).strip(),
                "kaloriferYakiti":str(i.find_all("td")[5].getText()).strip(),
                "fuelOil":str(i.find_all("td")[6].getText()).strip(),
                "ykFuelOil":str(i.find_all("td")[7].getText()).strip(),
                "tpgaz":str(i.find_all("td")[8].getText()).strip(),

            })))
    return data
