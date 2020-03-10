import unittest
from csvhelp import printError, CsvHelperModule


class TestCSVHelperMethods(unittest.TestCase):

    def test_csvDictReader_Helper(self):
        readerDict, headers = CsvHelperModule.readCsvAsDict('csv_test_file/testfile.csv')
        self.assertEqual(headers, ['FirstName','LastName','Country','City'])
        self.assertEqual(readerDict[0], {'LastName': 'Seyi', 'City': 'Lagos', 'Country': 'Nigeria', 'FirstName': 'Obaweya'})

    def test_csvReader_Helper(self):
        pass

    def test_csvDictWriter_Helper(self):
        pass

    def test_csvWriter_Helper(self):
        pass

if __name__ == '__main__':
    unittest.main()