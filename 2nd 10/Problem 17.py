#complete
one = len("one")
two = len("two")
three = len('three')
four = len('four')
five = len('five')
six = len('six')
seven = len('seven')
eight = len('eight')
nine = len('nine')
digits = one + two + three + four + five + six + seven + eight + nine
twenty = len('twenty')
thirty = len('thirty')
forty = len('forty')
fifty = len('fifty')
sixty = len('sixty')
seventy = len('seventy')
eighty = len('eighty')
ninety = len('ninety')
tens = twenty + thirty + forty + fifty + sixty + seventy + eighty + ninety
hundred = len('hundred')
onetonineteen = len('onetwothreefourfivesixseveneightnineteneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen')
#1-20
sum = 10*onetonineteen
#20-990 10s
sum = sum + 100*tens
# all end ones
sum = sum + 80*digits
# all hundred counters
sum = sum + 100*digits
sum = sum + 900*len("hundred")
sum = sum + 891*len("and")
print(sum + len('onethousand'))
