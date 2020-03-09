from csv import DictReader, reader, DictWriter, writer


Class CsvHelperModule:
    def readCsvAsDict(self, filename):
        with open(filename, 'r', encoding="utf8") as csvFile:
            reader = csv.DictReader(csvFile)
            print('Opening File %s' %filename)
            return list(reader), reader.fieldnames      