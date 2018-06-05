text = "X-DSPAM-Confidence:    0.8475";
iPos = text.find('0')
floatFinal = float(text[iPos:])
print(floatFinal)
