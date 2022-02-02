import requests , pandas as pd
from  bs4 import BeautifulSoup as bs4
from time import sleep
s = requests.session()
for i in range(1,20):
    data=f"reload=1&ajax=%7B%22tab_id%22%3A%22t0%22%2C%22cur_page%22%3A{i}%2C%22cur_trie%22%3A%22distance%22%2C%22query%22%3A%22exception%22%2C%22critere%22%3A%7B%7D%2C%22sliders%22%3A%7B%22range_motorisation%22%3A%7B%22id%22%3A%22%23range_range_motorisation%22%2C%22face%22%3A%22range_motorisation%22%2C%22max_counter%22%3A1149%2C%22min%22%3A%221%22%2C%22max%22%3A%222000%22%7D%2C%22prix%22%3A%7B%22id%22%3A%22%23range_prix%22%2C%22face%22%3A%22prix%22%2C%22max_counter%22%3A231%2C%22min%22%3A%221%22%2C%22max%22%3A%22400000%22%7D%2C%22km%22%3A%7B%22id%22%3A%22%23range_km%22%2C%22face%22%3A%22km%22%2C%22max_counter%22%3A412%2C%22min%22%3A%221%22%2C%22max%22%3A%22500000%22%7D%2C%22millesime%22%3A%7B%22id%22%3A%22%23range_millesime%22%2C%22face%22%3A%22millesime%22%2C%22max_counter%22%3A236%2C%22min%22%3A%221910%22%2C%22max%22%3A%222022%22%7D%7D%2C%22req_num%22%3A4%2C%22nb_results%22%3A%221862%22%2C%22current_location_distance%22%3A-1%2C%22logged_in%22%3Afalse%7D&tab=%5B%22t0%22%5D"

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,fr;q=0.8',
    'cache-control':'max-age=0',
    'content-length': '976',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.leparking-moto.fr',
    'referer': 'https://www.leparking-moto.fr/moto-occasion/exception.html',
    'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site':'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }
    sleep(1)
    res = s.post("https://www.leparking-moto.fr/moto-occasion/exception.html",headers=headers,data=data)


    soup = bs4(res.text,"lxml")
    #li-result
    results= soup.find_all("li",{"class":"li-result"})
    
    for result in results:
        marke = (result.select_one("span.brand").text)

        model =(result.select_one("span.sub-title.title-block").text).strip()

        prix=(result.select_one("p.prix").text).strip()
        Cylindr= (result.select("ul.info li")[0].text).strip() #Cylindrée
        Kilom= (result.select("ul.info li")[1].text).strip() #Kilomètre
        Année= (result.select("ul.info li")[2].text).strip() #Année
        LOCALISATION =(result.select_one("div.location").text).strip() #LOCALISATION
        code_postale= (result.select("ul.info li")[4].text).strip() #Année"""
        desc = (result.select_one("div.desc"))
        if desc!= None:
            desc = (result.select_one("div.desc").text).strip()
        
        print(marke)
        df=pd.DataFrame.from_dict([{"marke":marke,"model":model,"prix":prix,"Cylindrée":Cylindr,"Kilomètre":Kilom,"Année":Année,"LOCALISATION":LOCALISATION+f"({code_postale})"}])

        df.to_csv(f"moto-occasion.csv",mode='a',index = False,header=False)
