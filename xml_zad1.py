from xml.dom import minidom

DOMTree = minidom.parse('dane.xml')
print(DOMTree.toxml())
# <?xml version="1.0" ?><znajomi>
#     <osoba>
#         <imie foo="zzz">Zygmunt</imie>
#         <email>1@1.pl</email>
#     </osoba>
#     <osoba>
#         <imie foo="aaaa">Janina</imie>
#         <email>2@2.pl</email>
#     </osoba>
# </znajomi>
print(type(DOMTree.toxml()))  # <class 'str'>

cNodes = DOMTree.childNodes
print(cNodes)  # [<DOM Element: znajomi at 0x2201ca079b0>]
print(cNodes[0])  # <DOM Element: znajomi at 0x17fe17779b0>
print(cNodes[0].getElementsByTagName('osoba'))
# [<DOM Element: osoba at 0x2314a447920>, <DOM Element: osoba at 0x2314a447ad0>]
print(cNodes[0].getElementsByTagName('osoba')[0])  # <DOM Element: osoba at 0x2c60df57920>
print(cNodes[0].getElementsByTagName('osoba')[0].toxml())
# <osoba>
#         <imie foo="zzz">Zygmunt</imie>
#         <email>1@1.pl</email>
#     </osoba>
print(cNodes[0].getElementsByTagName('osoba')[0].getElementsByTagName('imie'))
# [<DOM Element: imie at 0x16ba73275c0>]
print(cNodes[0].getElementsByTagName('osoba')[0].getElementsByTagName('imie')[0].toxml())
# <imie foo="zzz">Zygmunt</imie>
print(cNodes[0].getElementsByTagName('osoba')[0].getElementsByTagName('imie')[0].firstChild.data)
# Zygmunt
