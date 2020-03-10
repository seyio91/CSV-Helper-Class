### CSV HELPER FUNCTION

### Usage
Having a sample CSV File

    sample CVSFile = """
        FirstName,LastName,Country,City
        Obaweya,Seyi,Nigeria,Lagos
        Ndakisa,Sibu,South Africa,Eastern Cape
        Phiri,Joy,South Africa,Limpopo
    """


Importing the CSV Helper Class

    from csvhelp import csvHelperModule

**readCsvAsDict Method**  

The readCsvAsDict Method uses the csv.DictReader method returns a tuple of the Content and Headers. The Content is a List of Dictionaries with the data header as key and row content as the value.

    >>> contentDict, headers = CsvHelperModule.readCsvAsDict(sampleCSVFile)

    >>> print(headers)
    ['FirstName', 'LastName', 'Country', 'City']

    >>> print(contentDict)
    [{'LastName': 'Seyi', 'City': 'Lagos', 'Country': 'Nigeria', 'FirstName': 'Obaweya'},{'LastName': 'Sibu', 'City': 'Eastern Cape', 'Country': 'South Africa', 'FirstName': 'Ndakisa'},{'LastName': 'Joy', 'City': 'Limpopo', 'Country': 'South Africa', 'FirstName': 'Phiri'}]

**readCsvAsList Method**  

The readCsvAsList Method uses the csv.reader method returns a tuple of the Content and Headers. The content is a list of rows returned as a list.

    >>> readerList, headerList = CsvHelperModule.readCsvAsList(sampleCSVFile) 

    >>> print(headerList)
    ['FirstName', 'LastName', 'Country', 'City']

    >>> print(readerList)
    [['Obaweya', 'Seyi', 'Nigeria', 'Lagos'], ['Ndakisa', 'Sibu', 'South Africa', 'Eastern Cape'], ['Phiri', 'Joy', 'South Africa', 'Limpopo']]

**writeCsvDict Method**  

The writeCsvDict Method uses the csv.DictWriter method. Takes in a File, Header and Dictionary to write to a CSV File.

    >>> csvFileToWrite = 'output.csv'

    >>> headers = ['FirstName', 'LastName', 'Country', 'City']

    >>> contentDictionary = [{'LastName': 'Seyi', 'City': 'Lagos', 'Country': 'Nigeria', 'FirstName': 'Obaweya'},{'LastName': 'Sibu', 'City': 'Eastern Cape', 'Country': 'South Africa', 'FirstName': 'Ndakisa'},{'LastName': 'Joy', 'City': 'Limpopo', 'Country': 'South Africa', 'FirstName': 'Phiri'}]

    >>> CsvHelperModule.writeCsvDict(csvFileToWrite, headers, ContentDictionary) 


**writeCsvList Method**  

The writeCsvList Method uses the csv.Writer method. Takes in a File, Header and List to write to a CSV File.

    >>> csvFileToWrite = 'output.csv'

    >>> headers = ['FirstName', 'LastName', 'Country', 'City']

    >>> contentList = [['Obaweya', 'Seyi', 'Nigeria', 'Lagos'], ['Ndakisa', 'Sibu', 'South Africa', 'Eastern Cape'], ['Phiri', 'Joy', 'South Africa', 'Limpopo']]

    >>> CsvHelperModule.writeCsvDict(csvFileToWrite, headers, ContentList) 