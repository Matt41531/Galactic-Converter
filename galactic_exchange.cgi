#!/usr/bin/python

import cgi, cgitb
from random import uniform
class DataEntry:
    def __init__(self,name,value):
        self.isValidDict = {
                "-1": "None",
                "0": "Valid",
                "1": "NotValid"
        }
        self.exchangeFromDollars = {
                "usdollar": 1,
                "euro": .88,
                "xarn": 26.2,
                "icekrona": 119.88,
                "polandzloty": 3.76,
                "galacticrock": .0123456
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
    DataValues = [Incurrency, Outcurrency, Amount]
    isConvert = True
    if Commodity.value is not None:
        isConvert = False
    print "Content-type: text/html\n\n"
    print "<html>"
    print "<h1>"
    if isConvert: #User wants to convert one currency to another
        allValid = validateData(DataValues) 
        if allValid:
            answer = convert(DataValues)
            printConvertTable(DataValues,Result = answer)
        else:
            printConvertTable(DataValues)
    else: #User wantsto look up a commodity price
        answer = lookup(Commodity)
        if answer is not None: #Commodity was valid so answer is valid
            printLookupTable(Commodity,Result = answer)
        else: #Commodity was not valid
            printLookupTable(Commodity)

    print "</h1>"
    print "</html>"

def validateData(dataArray):
    allValid = True
    #Validate Incurrency
    if dataArray[0].value is None: # if None
        dataArray[0].isValid = dataArray[0].isValidDict["-1"]
        allValid = False
    elif dataArray[0].value in dataArray[0].exchangeFromDollars: #if Valid
        dataArray[0].isValid = dataArray[0].isValidDict["0"]
    else: #if not valid & not none
        dataArray[0].isValid = dataArray[0].isValidDict["1"]
        allValid = False
    #Validate outcurrency
    if dataArray[1].value is None: # if None
        dataArray[1].isValid = dataArray[1].isValidDict["-1"]
        allValid = False
    elif dataArray[1].value in dataArray[1].exchangeFromDollars: #if Valid
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
    
def printConvertTable(dataArray, **keywordParameters):
    blue = "#4c4cff"
    red = "#dc143c"
    green = "7fff00"
    print "<table>"
    print "<tr>"
    print "<th>Incurrency:</th>"
    print "<th>Outcurrency:</th>"
    print "<th>Quanitity:</th>"
    print "<th></th>"
    print "<th>Result:</th>"
    print "<tr>"
    missingCount = 0
    #Loop through values and print correctly (colored)
    for dataValue in dataArray:
        #DEBUG: print "VALUES:", dataValue.isValid
        if dataValue.isValid is "NotValid":
            #make currency blue
            print "<td>"
            if dataValue.name is "Amount":
                invalidColor = green
            else:
                invalidColor = blue
            print "<span style=\"background-color: ", invalidColor,"\">"
            print dataValue.value
            print "</span>"
            print "</td>"
        elif dataValue.isValid is "None":
            print "<td>"
            print "<span style=\"background-color: ", red,"\">"
            print "Missing"
            print "</span>"
            print "</td>"
            missingCount += 1
        else:
            print "<td>", dataValue.value, "</td>"
    #Print the error message if there was an error
    print "<td></td>"
    if ('Result' in keywordParameters): #Result generated, everything is valid
        print "<td>", keywordParameters['Result'], "</td>"
    elif missingCount is len(dataArray): #All are none
        print "<td> Nothing submitted, nothing returned </td>"
    elif dataArray[2].isValid is not "Valid": #Invalid amount
        print "<td> Invalid amount </td>"
    else: #One of the currencies are invalid
        print "<td> Invalid currency </td>"
    print "</tr>"
    print "</tr>"
    print "</table>"

def convert(dataArray):
    Incurrency = dataArray[0].value
    Outcurrency = dataArray[1].value
    Amount = dataArray[2].value
    IncurrencyInDollars = (int(Amount) / dataArray[0].exchangeFromDollars[Incurrency]) 
    convertedCurrency = IncurrencyInDollars * dataArray[1].exchangeFromDollars[Outcurrency]
    return convertedCurrency

def lookup(commodity): 
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
    if commodity.value in commodityDict:
        isValid = True
        commodityRange = commodityDict[commodity.value]
        result = simulate(float(commodityRange[0]),float(commodityRange[1]))
    else: #Not valid
        commodity.isValid = commodity.isValidDict["1"]
        result = None
    return result
    

def simulate(lowerBound, upperBound):
    value = uniform(lowerBound,upperBound)
    return value

        
def printLookupTable(commodity,**keywordParameters):
    blue = "#4c4cff"
    print "<table>"
    print "<tr>"
    print "<th>Commodity:</th>"
    print "<th></th>"
    print "<th>Result:</th>"
    print "<tr>"
    isCorrect = True
    if commodity.isValid is "NotValid":
        #make currency blue
        print "<td>"
        print "<span style=\"background-color: ", blue,"\">"
        print commodity.value
        print "</span>"
        print "</td>"
        isCorrect = False
    else:
        print "<td>", commodity.value, "</td>"
    #Print the error message if there was an error
    print "<td></td>"
    if ('Result' in keywordParameters):
        print "<td>", keywordParameters['Result'], "</td>"
    else:
        print "<td> Invalid currency </td>"
    print "</tr>"
    print "</tr>"
    print "</table>"



main()
