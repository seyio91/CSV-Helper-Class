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

    def writeCsvDict(self, filename, header, content):
        try:
            with open(filename, 'w+', newline='', encoding="utf-8") as csvFile:
                writer = csv.DictWriter(csvFile, fieldnames=header)
                writer.writeheader()
                for row in content:
                    writer.writerow(row)
            print('wrote %s line to %s' %(len(content), filename))
        except FileNotFoundError:
            printError(filename)

    def writeCsvList(self, filename, header, content):
        try:
            with open(filename, 'w+', newline='') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(header)
                for row in content:
                    writer.writerow(row)
            print('wrote %s line to %s' % (len(content), filename))
        except FileNotFoundError:
            printError(filename)