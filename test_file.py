import unittest, os
from csvhelp import printError, CsvHelperModule


class TestCSVHelperMethods(unittest.TestCase):
    readerCSV = 'csv_test_file/testfile.csv'
    writeCSV = 'csv_test_file/output.csv'

    csvReadDict = {'LastName': 'Seyi', 'City': 'Lagos', 'Country': 'Nigeria', 'FirstName': 'Obaweya'}
    csvReadList = ['Obaweya','Seyi','Nigeria','Lagos']
    csvreadHeader = ['FirstName','LastName','Country','City']

    def test_csvDictReader_Helper(self):
        readerDict, headers = CsvHelperModule.readCsvAsDict(self.readerCSV)
        self.assertEqual(headers, self.csvreadHeader)
        self.assertEqual(readerDict[0], self.csvReadDict)

    def test_csvReader_Helper(self):
        readerList, headerList = CsvHelperModule.readCsvAsList(self.readerCSV)
        self.assertEqual(headerList,self.csvreadHeader)
        self.assertEqual(readerList[0], self.csvReadList)

    def test_csvDictWriter_Helper(self):
        CsvHelperModule.writeCsvDict(self.writeCSV, self.csvreadHeader,[self.csvReadDict,self.csvReadDict])

    def test_csvWriter_Helper(self):
        CsvHelperModule.writeCsvList(self.writeCSV, self.csvreadHeader, [self.csvReadList, self.csvReadList])

    def tearDown(self):
        try:
            os.remove(self.writeCSV)
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    unittest.main()