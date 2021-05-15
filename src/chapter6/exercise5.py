word = 'X-DSPAM-Confidence: 0.8475'
 # Finds the colon character
atpos = word.find(':')
 # Extracts portion after colon
var_float = word [atpos + 1:]
# Converts to floating point number
var_float = float(var_float)
print(f'This is a floating point number   {var_float}')