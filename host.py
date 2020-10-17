import yaml
import ac88web as wb

filename = input("Website file: ")
print("Reading...")
file = open(filename)
data = yaml.load(file, Loader=yaml.FullLoader)
file.close()
html = wb.compilecode(data["title"], data["body"], data["font"])
print("Press h on your keyboard to abort the host")
wb.host(wb.defport, html)
print("Aborted host.")
while True:
    pass
