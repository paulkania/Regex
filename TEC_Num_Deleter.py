stringz = 
"""Emphora (80)
Accnu reviews (10)
Accnue pricing (10)
Accnu ERP Pricing (H2)
Accnu ERP Reviews (H2)
Who Uses Accnu ERP? (H2)"""
 
#r'[0-9{2,}]'
stringz_no_comma = stringz.replace(',','')
stringz_no_comma = stringz_no_comma.replace('(H2)','')
stringz_no_comma = stringz_no_comma.replace('(H3)','')
stringz_no_comma = stringz_no_comma.replace('(','')
stringz_no_comma = stringz_no_comma.replace(')','')
#print(stringz_no_comma)
 
regcomped= re.compile(r'[0-9]{2,}')
regged = regcomped.sub("",stringz_no_comma)
print(regged)
