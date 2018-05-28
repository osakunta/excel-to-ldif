import unittest
from sample.mail_list_generator import MailListGenerator
from sample.ldif_parser import LdifParser
from data.data import ldif_file, residents
import filecmp
import glob
import os


class TestLdifGeneration(unittest.TestCase):

    def test_excel_with_invalid_values(self):
        MailListGenerator().parse_all()
        LdifParser(ldif_file, residents).write_ldif()

        list_of_files = glob.glob('data/ldif/*.ldif')
        latest_file = max(list_of_files, key=os.path.getctime)

        self.assertTrue(filecmp.cmp('tests/test_data/expected.ldif', latest_file))


if __name__ == '__main__':
    unittest.main()
