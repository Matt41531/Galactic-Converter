#!/usr/bin/python

import cgi, cgitb

def main():
    form = cgi.FieldStorage()

    Incurrency = form.getvalue('Incurrency')
    Outcurrency = form.getvalue('Outcurrency')
    Amount = form.getvalue('Amount')
    Commodity = form.getvalue('Commodity')
    print "Content-type: text/html\n\n"
    print "<html>"
    print "<h1>"
    if validateAmount(Amount):
        Result = convert(Incurrency, Outcurrency, Amount)
        printTable(Incurrency, Outcurrency, Amount, Result)
    else: 
        errorCode = "Invalid amount"
        printTable(Incurrency, Outcurrency, Amount, errorCode)
    print "</h1>"
    print "</html>"

def validateAmount(Amount): 
    if Amount is None:    
        #print "Error: Please specify an amount"
    elif Amount.isdigit():
        #print "DEBUG: Your amount is ", Amount
        return True
    else:
        #print "DEBUG:Error: Invalid amount input"
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

main()
