def ezpy.read(FILENAME):
  file = open(FILENAME, "r")
  content = file.read()
  file.close()
