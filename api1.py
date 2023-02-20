def get_web(self):
        #connect url
        httpool = urllib3.PoolManager()
        # get html
        resultat = httpool.request('GET',self.url)
        # retorn html
        return resultat.data.decode("utf-8")
        pass 
    
        def parse_html(self, html):
        #convertir bs4
        soup= bs4.BeautifulSoup(html,features="html-parser")
        soup.find_all('div',attrs=('id',"main"))(0)
        #buscar bs4 -> codi
        element_div= soup.find_all('div', attrs=('id',"main"))[0]
        codi = element_div.find_all('pre')[0]
        #retornar codi 
        return codi.text
        pass

def get_data(self):
        #descarregar-se web
        self .get_web()
        #llegit html
        dades= self.parse_html(dades)
        # retornar dades
        return dades
        pass

if __name__== " __main__":
        client = Client()
        dades = client.get_data()
        print(dades)