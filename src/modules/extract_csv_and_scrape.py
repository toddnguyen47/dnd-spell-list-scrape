import os
from scrape_modules import ScrapeModules
import time
import io


class ExtractCsvAndScrape:
    def __init__(self, driver, csv_dir):
        self.csv_dir = csv_dir
        self.flag_first_line = True
        self.output_fp = None
        self.header_line = [
            "Casting Time", "Range", "Components", "Duration",
            "Description", "Extra Info"
        ]
        self.scrape_modules = ScrapeModules(driver)

    def invoke(self):
        self.iterate_dir()

    def iterate_dir(self):
        for file in os.listdir(self.csv_dir):
            if file.endswith(".csv"):
                self.flag_first_line = True
                self.handle_cur_file(file)

    def handle_cur_file(self, input_file):
        output_dir = os.path.join("outputs", input_file)
        self.output_fp = open(output_dir, "wb")
        self.read_file(os.path.join(self.csv_dir, input_file))
        self.output_fp.close()
        print("Finished exporting to ", output_dir)

    def read_file(self, file_input: str) -> None:
        with open(file_input, "r") as file:
            for line in file:
                self.parse_line(line)
                time.sleep(0.5)

    def parse_line(self, line):
        line = line.rstrip("\n")
        if self.flag_first_line:
            self.handle_first_line(line)
        else:
            self.handle_line(line)

    def handle_first_line(self, line):
        self.flag_first_line = False
        line_list = line.split(",")
        for header in self.header_line:
            line_list.append(header)
        self.output_to_file(line_list)

    def handle_line(self, line):
        cur_line_list = line.split(",")
        spell = cur_line_list[0].strip()
        print("Getting info for spell: " + spell)
        info_list = self.scrape_modules.get_spell_info(spell)
        self.output_only_if_info_was_extracted(cur_line_list, info_list)

    def output_only_if_info_was_extracted(self, cur_line_list, info_list):
        if len(info_list) > 0:
            cur_line_list = cur_line_list + info_list
            self.output_to_file(cur_line_list)

    def output_to_file(self, line_list):
        self.output_fp.seek(0, io.SEEK_END)
        self.output_fp.write(",".join(line_list).encode("utf-8"))
        self.output_fp.write("\n".encode("utf-8"))
        self.output_fp.flush()
