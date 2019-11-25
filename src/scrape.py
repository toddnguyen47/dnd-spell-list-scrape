from modules.scrape_module import ScrapeModules
from modules.extract_csv_and_scrape import ExtractCsvAndScrape
from selenium import webdriver

if __name__ == "__main__":
    driver = webdriver.Firefox()
    ecs = ExtractCsvAndScrape(driver=driver, csv_dir="./resources/")
    ecs.invoke()

    driver.close()
    print("Finished!")
