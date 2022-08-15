import openpyxl, pprint
print('Opening workbook...')
wb = openpyxl.load_workbook('SalesFigures.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}

for row in range(2, sheet.max_row + 1):

    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value


# Step 2: Populate the Data Structure