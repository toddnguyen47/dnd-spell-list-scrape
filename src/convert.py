from modules.convert_csv_to_html import ConvertCsvToHtml
import os

if __name__ == "__main__":
    convertObj = ConvertCsvToHtml(os.path.join(
        os.getcwd(), "outputs", "clericSpellListDomainDesc.csv"))
    convertObj.invoke()
