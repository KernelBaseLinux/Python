try:
   fh = open("sample.txt", "r")
   b = fh.read()
   print(b)
except IOError:
   print("Error: can\'t find file or read data")

