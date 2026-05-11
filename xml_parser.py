import xml.etree.ElementTree as ET
data = '''<person>
  <name>krrish</name>
  <phone type = "intl">
    +1 734 303 4456
    </phone>
    <email hide = "yes"/>
</person>'''

tree = ET.fromstring(data)
print('name: ',tree.find('name').text)
print('Attr: ',tree.find('email').get('hide'))
print('phone: ',tree.find('phone').text)
    