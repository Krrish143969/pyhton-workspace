import urllib.request
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter location: ")
print("Retrieving", url)

data = urllib.request.urlopen(url, context=ctx).read()
print("Retrieved", len(data), "characters")

tree = ET.fromstring(data)

counts = tree.findall('.//count')

total = 0
count = 0

for item in counts:
    num = int(item.text)
    total += num
    count += 1

print("Count:", count)
print("Sum:", total)
