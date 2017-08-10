# with open('town_list.txt','r') as raw:
#     lst = raw.readlines()
#
# i = 0
# j = 1
# while True:
#     if i == len(lst)-1:
#         break
#     if lst[i] == lst[i+1]:
#         lst.pop(i)
#         j+=1
#         i-=1
#     else:
#         lst[i] = '{}    {}'.format(lst[i],j)
#         j=1
#     i+=1
#
# with open('town_list.txt','w') as raw:
#     for el in lst:
#         print(el)
#         raw.write(el)
#         raw.write('\n')

def Town(town_name):
    with open('town_list.txt','r') as raw:
        lst = raw.read().split('\n')
    for i,el in enumerate(lst):
        if town_name in el:
            print(town_name,lst[i+1])
            return lst[i+1]

with open('kml.txt','r') as raw:
    lst = raw.readlines()

town_name = ''
new_doc = ''
desc = False
for el in lst[45:]:
    #print(el[:13])
    if desc == True:
        el = '      <description>Number of files: {}</description>\n'.format(Town(town_name))
        desc = False
    if el[:12] == '      <name>':
        town_name = el[12:el.index('</name>')]
        desc = True
    new_doc = new_doc + el

with open('kml_out.txt','w') as raw:
    raw.write(new_doc)
