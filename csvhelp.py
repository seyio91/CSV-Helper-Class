import csv


Class CsvHelperModule:
    def printError(filename):
        print('%s not found' %filename)

    def readCsvAsDict(self, filename):
        try:
            with open(filename, 'r', encoding="utf8") as csvFile:
                reader = csv.DictReader(csvFile)
                print('Opening File %s' %filename)
                return list(reader), reader.fieldnames
        except FileNotFoundError:
            printError(filename)  

    def readCsvAsList(self, filename):
        try:
            with open(filename, 'r', encoding="utf8") as csvFile:
                reader = csv.reader(csvFile)
                content = list(reader)
                header = content.pop(0)
                return content, header
        except FileNotFoundError:
            printError(filename)