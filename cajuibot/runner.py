import time, csv, os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

class CajuiBot:
    def __init__(self,username, password, csv_lesson, headless):
        self.username = username
        self.password = password
        self.csv_lesson = os.path.abspath(csv_lesson)
        
        options = Options()
        options.headless = True if headless else False

        self.driver = webdriver.Firefox(options=options)
    
    def login(self):
        driver = self.driver
        driver.get("https://cajui.ifnmg.edu.br/cajui/login")
        time.sleep(3)

        input_user = driver.find_element_by_xpath('//input[@name="LoginForm[username]"]')
        input_user.click()
        input_user.clear()
        input_user.send_keys(self.username)

        input_password = driver.find_element_by_xpath('//input[@name="LoginForm[password]"]')
        input_password.click()
        input_password.clear()
        input_password.send_keys(self.password)

        button_login =  driver.find_element_by_xpath('//button[@name="login-button"]')
        button_login.click()

    def lancarUmaAula(self, id, data, inicio, qtd, conteudo):
        driver = self.driver
        driver.get(f"https://cajui.ifnmg.edu.br/portal/tecDiario/registro/cadastro?ofertaId={id}")
        time.sleep(3)
        button_adicionar = driver.find_element_by_xpath('//a[text()=" Adicionar"]')
        button_adicionar.click()
        
        input_data = driver.find_element_by_xpath('//input[@name="data-registro-data-disp"]')
        input_data.click()
        time.sleep(1)
        input_data.clear()
        input_data.send_keys(data)
        
        input_inicio = driver.find_element_by_xpath('//input[@name="Registro[hora_inicio]"]')
        input_inicio.click()
        time.sleep(1)
        input_inicio.clear()
        input_inicio.send_keys(inicio)

        input_qtd = driver.find_element_by_xpath('//input[@name="Registro[qtd_horarios]"]')
        input_qtd.click()
        time.sleep(1)
        input_qtd.clear()
        input_qtd.send_keys(qtd)

        textarea_conteudo = driver.find_element_by_xpath('//textarea[@name="Registro[descricao]"]')
        textarea_conteudo.click()
        time.sleep(1)
        textarea_conteudo.clear()
        textarea_conteudo.send_keys(conteudo)

        button_cadastrar_lancar =  driver.find_element_by_xpath('//button[@name="salvar-lancar"]')
        button_cadastrar_lancar.click()
        time.sleep(3)

        page = driver.find_element_by_tag_name('html')
        page.send_keys(Keys.END)
        time.sleep(1)

        button_salvar = driver.find_element_by_xpath('//button[text()=" Salvar"]')
        button_salvar.click()

    def lancarTodasAulas(self):
        with open(self.csv_lesson) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
               self.lancarUmaAula(row[0],row[1],row[2],row[3],row[4])
               time.sleep(3)

    def close(self):
        self.driver.quit()