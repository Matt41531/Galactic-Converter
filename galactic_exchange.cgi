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
    validateData(DataValues)
    print "Amount:", DataValues[2].isValid
    if validateAmount(Amount):
        Result = convert(Incurrency, Outcurrency, Amount)
        printTable(Incurrency, Outcurrency, Amount, Result)
    else: 
        isNone = isNoneAmount(Amount)
        if isNone:
            errorCode = "Missing amount"
        else:
            errorCode = "Invalid amount"
        printTable(Incurrency, Outcurrency, Amount, errorCode)
    print "</h1>"
    print "</html>"
def validateData(dataArray):
    #Validate inccurency

    #Validate outcurrency

    #Validate amount
    if dataArray[2].value is None:
        dataArray[2].isValid = dataArray[2].isValidDict["-1"]
    elif dataArray[2].value.isdigit():
        dataArray[2].isValid = dataArray[2].isValidDict["0"]
    else:
        dataArray[2].isValid = dataArray[2].isValidDict["1"]


def validateAmount(Amount):
    if Amount.isdigit():
        #print "DEBUG: Your amount is ", Amount
        return True
    else:
        #print "DEBUG:Error: Invalid amount input"
        return False

def isNoneAmount(Amount):
    if Amount is None:
        return True
    else:
        return False


def printTable(origCurrency, prefCurrency, quantity, result):
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
    #Check if there was an error for the 1st currency
    if (isError and (result[0] is 1)):
        #make 1st currency blue
        print "<td>"
        print "<span style=\"background-color: ", blue,"\">"
        print origCurrency
        print "</span>"
        print "</td>"
    else:
        print "<td>", origCurrency, "</td>"
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
    if isError:
        print "<td>", errorMessage, "</td>"
    else:
        print "<td>", result, "</td>"
    print "</tr>"
    print "</tr>"
    print "</table>"

def convert(origCurrency, prefCurrency, quantity):
    print "Converting ", quantity, " ", origCurrency, " to ", prefCurrency
    exchangeFromDollars = {
        "dollar": 1,
        "euro": .88,
        "xarn": 26.2,
        "icekrona": 119.88,
        "polandzloty": 3.76,
        "galacticrock": .0123456
    }
    errorCode = []
    if origCurrency in exchangeFromDollars and prefCurrency in exchangeFromDollars:
        #print "DEBUG: 1st currency valid, ", exchangeFromDollars[origCurrency]
        origCurrencyInDollars =(int(quantity) / exchangeFromDollars[origCurrency]) 
        #print "DEBUG: Orig: ", origCurrencyInDollars
        errorCode.append(0)
        #print "DEBUG:2nd currency valid"
        convertedCurrency = origCurrencyInDollars * exchangeFromDollars[prefCurrency]
        #print "DEBUG:Converted currency: ", convertedCurrency
        errorCode.append(0)
        return convertedCurrency
    elif ((origCurrency in exchangeFromDollars) and (prefCurrency not in exchangeFromDollars)):
        #Report that the 1st currency is valid but the 2nd is not
        errorCode.extend([0,1])
    elif (origCurrency not in exchangeFromDollars) and prefCurrency in exchangeFromDollars:
        #Report that the 1st currency is invalid but the 2nd currency is valid
        errorCode.extend([1,0])
    else:
        #Report that both currencies are invalid
        errorCode.extend([1,1])
    return errorCode     

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
