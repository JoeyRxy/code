import base64

url = input("enter file's location:\n")
try:
    f = open(url, 'rb')
    ls_f = base64.b64encode(f.read())
    f.close()
    print(ls_f)
except OSError as er:
    print("File Doesn't Exist!\n")
    print(er)
