import csv, time
import functools

def funcTimer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        endtime = time.time()
        print('Time taken to run %s' %(endtime - start))
    return wrapper

class CsvHelperModule:
    # error function
    def printError(filename):
        print('%s not found' %filename)

    # CSV DictReader Helper
    def readCsvAsDict(self, filename):
        try:
            with open(filename, 'r', encoding="utf8") as csvFile:
                reader = csv.DictReader(csvFile)
                print('Opening File %s' %filename)
                return list(reader), reader.fieldnames
        except FileNotFoundError:
            printError(filename)  

    # CSV Reader Helper
    def readCsvAsList(self, filename):
        try:
            with open(filename, 'r', encoding="utf8") as csvFile:
                reader = csv.reader(csvFile)
                content = list(reader)
                header = content.pop(0)
                return content, header
        except FileNotFoundError:
            printError(filename)

    # CSV DictWrite Helper
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

class LineWriter:
    def __init__(self, filename, header):
        self.filename = filename
        self.header = header

    def writerInit(self):
        self.writeFile = open(self.filename, 'w+', newline='', encoding="utf-8")
        self.writer = csv.DictWriter(self.writeFile, fieldnames=self.header)
        self.writer.writeheader()

    def writerLine(self, row):
        self.writer.writerow(row)

    def close(self):
        self.writeFile.close()