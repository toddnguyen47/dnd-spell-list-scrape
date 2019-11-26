import unittest
from modules.convert_csv_to_html import ConvertCsvToHtml


class TestConvertCsvToHtml(unittest.TestCase):
    def setUp(self) -> None:
        self.filepath = "clericSpellListDesc.csv"
        self.obj = ConvertCsvToHtml(self.filepath)

    # @unittest.skip("")
    def test_handle_spell_name_and_description(self):
        line = [
            'Guidance',
            '0',
            '1 action',
            'Touch',
            'V S',
            'Up to 1 minute',
            'You touch one willing creature. Once before the spell ends, the target can roll a '
            'd4 and add the number rolled to one ability check of its choice. ' \
            'It can roll the die before or after making the ability check. The spell then ends.',
            'At higher levels, this does nothing']
        self.obj.get_spell_desc_list(line)

        expected = [
            'You touch one willing creature. Once before the spell ends, the target can roll a '
            'd4 and add the number rolled to one ability check of its choice. '
            'It can roll the die before or after making the ability check. The spell then ends.',
            "At higher levels, this does nothing"
        ]
        self.assertListEqual(expected, self.obj.spell_description_list)

