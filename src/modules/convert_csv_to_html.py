import csv
from lxml import etree


class ConvertCsvToHtml:
    def __init__(self, filepath):
        self.filepath = filepath
        self.index_spell_description = 0
        self.root = etree.Element("tbody")
        self.table_row = ""
        self.spell_name = ""
        self.spell_description_list = []

    def invoke(self):
        self.read_in_file()
        self.generate_output()

    def read_in_file(self):
        with open(self.filepath, "r", newline='') as file:
            csv_reader = csv.reader(file)
            for index, row in enumerate(csv_reader):
                if index == 0:
                    self.index_spell_description = len(row) - 2
                else:
                    self.table_row = etree.SubElement(self.root, "tr")
                    self.handle_row(row)
                    self.root.append(self.table_row)

    def handle_row(self, row: list):
        for index, col in enumerate(row):
            if index == 0:
                self.spell_name = col.strip()
                self.get_spell_desc_list(row)
                self.add_spell_name_and_desc()
            elif 0 < index < self.index_spell_description:
                self.add_table_data(col)

    def get_spell_desc_list(self, row_split: list):
        self.spell_description_list = []
        for elem in row_split[self.index_spell_description:]:
            self.spell_description_list.append(elem.strip())

    def add_spell_name_and_desc(self):
        table_data = self.add_spell_name()
        div_spell_desc = etree.SubElement(table_data, "div")
        div_spell_desc.set("class", "spell-description")
        self.add_spell_description(div_spell_desc)

    def add_spell_name(self):
        table_data = etree.SubElement(self.table_row, "td")
        table_data.set("class", "table__td-spell-name")
        spell_span = etree.SubElement(table_data, "span")
        spell_span.text = self.spell_name.strip()
        return table_data

    def add_spell_description(self, parent_elem):
        self.add_spell_description_name(parent_elem)
        self.add_spell_description_description(parent_elem)

    def add_spell_description_name(self, parent_elem):
        div_spell_desc_name = etree.SubElement(parent_elem, "div")
        div_spell_desc_name.set("class", "spell-description__name")
        div_spell_desc_name.text = self.spell_name.strip()

    def add_spell_description_description(self, parent_elem):
        div_spell_desc = etree.SubElement(parent_elem, "div")
        div_spell_desc.set("class", "spell-description__description")
        for sd in self.spell_description_list:
            if sd.strip():
                p1 = etree.SubElement(div_spell_desc, "p")
                p1.text = sd.strip()

    def add_table_data(self, str_input: str):
        table_data = etree.SubElement(self.table_row, "td")
        table_data.text = str_input.strip()

    def generate_output(self):
        str1 = etree.tostring(self.root, pretty_print=True)
        output_file = "".join(self.filepath.split(".csv")[:-1]) + "_HTML.html"
        with open(output_file, "wb") as f:
            f.write(str1)
        print("Finished writing to {0}".format(output_file))
