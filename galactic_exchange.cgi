#!/usr/bin/python

import cgi, cgitb
class DataEntry:
    def __init__(self,name,value):
        self.isValidDict = {
                "-1": "None",
                "0": "Valid",
                "1": "Not valid"
        }
        self.name = name
        self.value = value
        self.isValid = None
        self.isValid = self.isValidDict["-1"]

def main():
    form = cgi.FieldStorage()
    Incurrency = DataEntry("Incurrency",form.getvalue('Incurrency'))
    Outcurrency = DataEntry("Outcurerncy",form.getvalue('Outcurrency'))
    Amount = DataEntry("Amount",form.getvalue('Amount'))
    Commodity = DataEntry("Commodity",form.getvalue('Commodity'))
    DataValues = [Incurrency, Outcurrency, Amount, Commodity]
    print "Content-type: text/html\n\n"
    print "<html>"
    print "<h1>"
    allValid = validateData(DataValues)
    print "DEBUG: Amount:", DataValues[2].isValid
    if allValid:
        Result = convert(DataValues)
        printTable(DataValues,Result)
    else:
        printTable(DataValues)
    print "</h1>"
    print "</html>"

def validateData(dataArray):
    exchangeFromDollars = {
        "dollar": 1,
        "euro": .88,
        "xarn": 26.2,
        "icekrona": 119.88,
        "polandzloty": 3.76,
        "galacticrock": .0123456
    }
    allValid = True
    #Validate Incurrency
    if dataArray[0].value is None: # if None
        dataArray[0].isValid = dataArray[0].isValidDict["-1"]
        allValid = False
    elif dataArray[0].value in exchangeFromDollars: #if Valid
        dataArray[0].isValid = dataArray[0].isValidDict["0"]
        validArray[0] = True
    else: #if not valid & not none
        dataArray[0].isValid = dataArray[0].isValidDict["1"]
        allValid = False
    #Validate outcurrency
    if dataArray[1].value is None: # if None
        dataArray[1].isValid = dataArray[1].isValidDict["-1"]
        allValid = False
    elif dataArray[1].value in exchangeFromDollars: #if Valid
        dataArray[1].isValid = dataArray[1].isValidDict["0"]
    else: #if not valid & not none
        dataArray[1].isValid = dataArray[1].isValidDict["1"]
        allValid = False
    #Validate amount
    if dataArray[2].value is None:
        dataArray[2].isValid = dataArray[2].isValidDict["-1"]
        allValid = False
    elif dataArray[2].value.isdigit():
        dataArray[2].isValid = dataArray[2].isValidDict["0"]
    else:
        dataArray[2].isValid = dataArray[2].isValidDict["1"]
        allValid = False

    return allValid
    
def printTable(dataArray, **keywordParameters):
    if ('Result' in keywordParameters):
        print "Found result"
    isError = False
    blue = "#4c4cff"
    print "<table>"
    print "<tr>"
    print "<th>Incurrency:</th>"
    print "<th>Outcurrency:</th>"
    print "<th>Quanitity:</th>"
    print "<th>Result:</th>"
    print "<tr>"
    if isinstance(result, list):
        #This is an error
        isError = True
        errorMessage = "Invalid currency"
    #DO a for loop here
    for dataValue in dataArray:
        if value.isValid is "Not valid":
            #make currency blue
            print "<td>"
            print "<span style=\"background-color: ", blue,"\">"
            print dataValue.value
            print "</span>"
            print "</td>"
        elif valie.isValid is "None":
            print "<td>"
            print "<span style=\"background-color: ", blue,"\">"
            print dataValue.value
            print "</span>"
            print "</td>"
    #Check if there was an error for the 2nd currency
    if (isError and (result[1] is 1)):
        #make 2nd currency blue
        print "<td>"
        print "<span style=\"background-color: ", blue,"\">"
        print prefCurrency
        print "</span>"
        print "</td>"
    else:
        print "<td>", prefCurrency, "</td>"
    print "<td>", quantity, "</td>"
    #Print the error message if there was an error
    if ('Result' in keywordParameters):
        print "<td>", keywordParameters['Result'], "</td>"
    elif dataArray[2].isValid is not "Valid":
        print "<td> Invalid amount </td>"
    else:
        print "<td> Invalid currency </td>"
    print "</tr>"
    print "</tr>"
    print "</table>"

def convert(dataArray):
    Incurrency = dataArray[0].value
    Outcurrency = dataArray[1].value
    Amount = dataArray[2].value
    IncurrencyInDollars =(int(Amount) / exchangeFromDollars[Incurrency]) 
    convertedCurrency = IncurrencyInDollars * exchangeFromDollars[Outcurrency]
    return convertedCurrency

def lookup(commodity):
    print "Looking..."
    commodityDict = {
            "terrangold": [1100.0,1800.0],
            "terransilver": [13.0,18.0],
            "terrancopper":[2.0,4.0],
            "xarngold":[1900.0,2800.0],
            "xarnsilver":[113.0,158.0],
            "xarncopper":[0.1,0.2],
            "corn":[338.25,440.00],
            "wheat":[438.50,600.40],
            "coffee":[101.01,1000000.0],
            "xarnsugar":[191.01,2000.0]
    }

    if commodity in commodityDict:
        print "Good job"


main()
