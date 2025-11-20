from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_data():
    driver = webdriver.Chrome()
    
    try:
        driver.get("https://tempo.inmet.gov.br/TabelaEstacoes/A807")
        
        wait = WebDriverWait(driver, 200) # tempo grande pois o site demora as vezes pra carregar
        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "content-loading")))
        
        table = wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))
        
        data = []
        for rows in table.find_elements(By.TAG_NAME, "tr"):
            columns = rows.find_elements(By.TAG_NAME, "td")
            if columns:
                data.append([col.text for col in columns])
        
        return data
        
    finally:
        driver.quit()

data = get_data()

for info in data:
    print(info)