from bs4 import BeautifulSoup
from datetime import datetime
import requests
import json

def get_info():

    # Horário
    last_upd = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Definindo o site
    # Nesse caso utilizei o link para os dados de Porto Alegre, mas poderia utilizar
    # outro método, por exemplo passando a longitude e a latitude do local desejado:
    # https://weather.com/weather/today/l/-30.02,-51.22 - Bairro Marcílio Dias, Porto Alegre, RS

    html_page = requests.get("https://weather.com/weather/today/l/02497c1d67234f59ca3948f6a3361bfe5ebd55a13098b72e30391e48ce83be28").text
    soup = BeautifulSoup(html_page,"lxml")

    # Localização
    current_location = soup.find("div", class_ = "CurrentConditions--header--27uOE")
    location = current_location.find("h1", class_ = "CurrentConditions--location--kyTeL").text

    # Temperatura
    current_temperature = soup.find("div", class_ = "CurrentConditions--primary--2SVPh")
    temperature_c = round((int(current_temperature.find("span", class_ = "CurrentConditions--tempValue--3a50n").text[:-1]) - 32) * (5 / 9),2)

    # Sensação Térmica
    current_feelslike = soup.find("div", class_ = "TodayDetailsCard--feelsLikeTemp--3fwAJ")
    feelslike = round((int(current_feelslike.find("span", class_ = "TodayDetailsCard--feelsLikeTempValue--Cf9Sl").text[:-1]) - 32) * (5 / 9),2)

    # Detalhes
    current_details = soup.find("div", class_ = "TodayDetailsCard--detailsContainer--16Hg0")

    # Umidade
    humidity = current_details.find("span",{"data-testid":"PercentageValue"}).text

    #print("Data: "+last_upd, "Localizacao: "+location, "Temperatura: "+temperature_c, "Sensacao Termica: "+ feelslike, "Humidade: "+ humidity)
    #r = json.loads(json.dumps(infos))
    #print(r)
    return last_upd, location, temperature_c, feelslike, humidity
