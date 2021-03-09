import gspread, os.path, datetime, locale

def getWorksheet(client, originalName):
  originalSpreadsheet = client.open(originalName)
  return(originalSpreadsheet.sheet1)

def getNewCsv(name):
  newCsvName = ("../assets/" + name + '.csv')
  return(open(newCsvName, 'w'))

def getLogFile():
  filename = "../assets/log.txt"

  if os.path.isfile(filename):
    option = "a+"
  else:
    option = "w"
    
  return(open(filename, option))

def writeLogFile(row, column):
  logFile = getLogFile()
  logFile.write("Célula <" + str(row + 1) + ":" + str(column + 1) + "> não tem conteúdo\n")
  logFile.close()
  
def formatDate(date):
  ds = list(map(int, date.split('-')))
  return(datetime.datetime(ds[0], ds[1], ds[2]).strftime("%d/%m/%Y"))

def formatCurrency(value):
  valueFloat = float(value.replace('$', '').replace(',', '').strip())
  return(locale.currency(valueFloat, grouping = True))

def formatPercent(percentage):
  if percentage.find('%') == -1:
    return(str(float(percentage) * 100) + '0%')
  else:
    return(percentage)

def main():
  client = gspread.service_account(filename = '../config/service_account.json')
  originalSpreadsheetName = "Prova Engenharia de Dados - Planilha de compras"
  worksheet = getWorksheet(client, originalSpreadsheetName)
  newCsv = getNewCsv(originalSpreadsheetName)
  locale.setlocale(locale.LC_ALL, '')

  for indexRow, row in enumerate(worksheet.get_all_values()):
    if indexRow == 0:
      for col in row:
        newCsv.write(col + ';')
    else:
      for indexCol, col in enumerate(row):
        if col:
          if indexCol == 0:
            newCsv.write(formatDate(col) + ';')
          elif indexCol == 2:
            newCsv.write(formatCurrency(col) + ';')
          elif indexCol == 3:
            newCsv.write(formatPercent(col) + ';')
          else:
            newCsv.write(col + ';')
        else:
          newCsv.write(';')
          writeLogFile(indexRow, indexCol)

    newCsv.write('\n')
  
  newCsv.close()

if __name__ == "__main__":
  main()