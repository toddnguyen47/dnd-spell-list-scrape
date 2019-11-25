import utils

class ScrapeModules:
    def __init__(self, driver):
        self.secondary_index_description = 3
        self.driver = driver
        self.base_primary_url = "https://roll20.net/compendium/dnd5e/"
        self.base_secondary_url = "https://www.dnd-spells.com/spell/"
        self.spell_description_list = []
        self.class_index = 4
        self.spell = ""
        self.elems = None

    def get_spell_info(self, spell: str) -> list:
        self.spell_description_list = []
        self.spell = spell

        self.go_to_primary_site()
        if self.is_info_on_primary_site():
            self.extract_primary_site()
        else:
            self.extract_secondary_site()

        self.replace_all_non_ascii_chars_in_list()
        return self.spell_description_list

    def go_to_primary_site(self):
        url = self.base_primary_url + self.spell
        self.driver.get(url)

    def is_info_on_primary_site(self):
        self.elems = self.driver.find_elements_by_xpath("//div[contains(@class, 'single-list')]")
        return len(self.elems) > 0

    def extract_primary_site(self):
        ul_elem = self.elems[0].find_element_by_tag_name("ul")
        for index, e1 in enumerate(ul_elem.find_elements_by_tag_name("li")):
            text = e1.text
            if index < self.class_index:
                self.handle_before_classes_key(text)
            elif index > self.class_index:
                self.handle_after_classes_key(text)

    def handle_after_classes_key(self, text):
        self.spell_description_list.append(
            "\""
            + text.strip().replace("<br>", " ").replace("\n", " ")
            + "\""
        )

    def handle_before_classes_key(self, line):
        info_list = line.split(":")[1:]
        info = "".join(info_list).strip()
        self.spell_description_list.append("\"" + info + "\"")


    def extract_secondary_site(self):
        self.go_to_secondary_site()
        self.extract_secondary_info()

    def go_to_secondary_site(self):
        spell_name = self.spell.replace(" ", "-").replace("'", "").lower()
        self.driver.get(self.base_secondary_url + spell_name)

    def extract_secondary_info(self):
        elems = self.driver.find_elements_by_xpath(
            '//h1[contains(@class, "classic-title")]/following-sibling::p')
        if len(elems) <= 0:
            utils.ask_for_user_exit(self.spell)
        else:
            self.extract_secondary_info_elem_found(elems)

    def extract_secondary_info_elem_found(self, elems):
        for index, e in enumerate(elems):
            if 0 < index < 4:
                self.handle_secondary_info_text_format(e.text.strip(), index)
        self.check_for_higher_level()

    def handle_secondary_info_text_format(self, text: str, index: int) -> str:
        if text != "":
            if index == self.secondary_index_description:
                text = "\"" + text.replace("\n", " ").replace("<br>", " ") + "\""
                self.spell_description_list.append(text)
            else:
                self.separate_secondary_info(text)

    def separate_secondary_info(self, text):
        text_list = text.split("\n")
        for index, elem in enumerate(text_list):
            t = self.check_and_replace_colons(elem)
            if t.strip() != "":
                self.spell_description_list.append("\"" + t + "\"")

    def check_and_replace_colons(self, text):
        if ":" not in text:
            return text.strip()

        text = "".join(text.split(":")[1:]).strip()
        return text

    def check_for_higher_level(self) -> None:
        xpath = '//*//span[text()="At higher level"]'
        elems = self.driver.find_elements_by_xpath(xpath)
        if len(elems) > 0:
            text = self.handle_secondary_higher_level_info(xpath)
            self.spell_description_list.append(text)

    def handle_secondary_higher_level_info(self, cur_xpath) -> str:
        cur_xpath = cur_xpath + '//../following-sibling::p'
        text = self.driver.find_elements_by_xpath(cur_xpath)[0].text.strip()
        return text

    def replace_all_non_ascii_chars_in_list(self):
        for index, s in enumerate(self.spell_description_list):
            self.spell_description_list[index] = s.replace("’", "'")
