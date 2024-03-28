import requests
import pandas as pd
import time
from bs4 import BeautifulSoup
import numpy as np
from selenium import webdriver

class Naukri:
    def get_data(loc,page_no = 0):
        url = f"https://www.naukri.com/data-analyst-jobs-in-{loc}-{page_no}"
        driver_loc = """C:\\Users\\Shreya Johari\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"""
        cService = webdriver.ChromeService(executable_path=driver_loc)
        driver = webdriver.Chrome(service = cService)
        driver.get(url)
    
        time.sleep(5)
    
        data = driver.page_source
        driver.close()
    
        soup = BeautifulSoup(data,"html.parser")
    
        profile = []
        for i,j in enumerate(soup.find_all("div",{"class":"cust-job-tuple layout-wrapper lay-2 sjw__tuple"})):
            for k in j.find_all("a",{"class":"title"}):
                profile.append(k.text)
    
        comp_name = []
        for i,j in enumerate(soup.find_all("a",{"class":"comp-name"})):
            comp_name.append(j.text)
        
        url = []
        for i,j in enumerate(soup.find_all("a",{"class":"title"},href=True)):
            url.append(j["href"])
        
        exp = []
        for i,j in enumerate(soup.find_all("span",{"class":"expwdth"})):
            exp.append(j.text)
    
        salary = []
        for i,j in enumerate(soup.find_all("span",{"class":"ni-job-tuple-icon ni-job-tuple-icon-srp-rupee sal"})):
            salary.append(j.text)
    
        location = []
        for i,j in enumerate(soup.find_all("span",{"class":"locWdth"})):
            location.append(j.text)
        
        skills = []
        for i,j in enumerate(soup.find_all("ul",{"class":"tags-gt"})):
            skills.append(j.text)
    
        post_date = []
        for i,j in enumerate(soup.find_all("span",{"class":"job-post-day"})):
            post_date.append(j.text.split(" ")[0].replace("+",""))
        
        final_data = {"Company":comp_name,
                 "Designation":profile,
                 "Experience":exp,
                 "Salary":salary,
                 "Skills":skills,
                 "Location":location,
                 "URL":url}
    
        naukri_df = pd.DataFrame(final_data)
        #naukri_df.to_csv(f"{loc}_job.csv",index = False)
        return naukri_df
    
if __name__ == "__main__":
    Naukri()