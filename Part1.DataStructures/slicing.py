# Slice Objects
# Slices made up of 3 parts list[start:end:step]
# casual use
# we have a string:
txt = "helloWorld"
# we want only hello
hello = txt[:5]
# print(hello)

#or maybe we only want Decussated characters 
dec = txt[::2] # 2 step
# print(dec)

# the step part can also be in reverse
rev = txt[::-1]
# print(rev)

# or -2
rev2 = txt[::-2]
# print(rev2)

# we have a slice() method that is charge for slicing sequences
# to evaluate the expression seq[start:end:step] python calls seq.__getitem__(slice(start, end, step))

# with slice() we can name slices just like spreadsheets let assign name for cell ranges
# in this example we will slice a invoice using slice() method
invoice = """
0.....6.................................40........52...55........
1909  Pimoroni PiBrella                     $17.50    3    $52.50
1489  6mm Tactile Switch x20                $4.95     2    $9.90
1510  Panavise Jr. - PV-201                 $28.00    1    $28.00
1601  PiTFT Mini Kit 320x240                $34.95    1    $34.95
"""
SKU = slice(0, 6) # we cannot use sequences for this purpose it well throgh an error "string indices must be integers"
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
items = invoice.split("\n")[2:]

# OK, we have out lineItems and position of its units
# now we will execute a for loop to extract units of each items

for item in items:
    # print(item[UNIT_PRICE], item[DESCRIPTION])
    pass

# Amazing.



