import yaml
'''Read yaml file'''
file = open('yamlToPrint.yaml', encoding="UTF-8")
res = yaml.load(file, Loader=yaml.FullLoader)
print(type(res))

'''Output yaml file content in two methods'''
for lis in res:
    print(lis['Sex'])
    print(lis['Age'])

for lis in res:
    print(lis.get('Age'))
    print(lis.get('Sex'))
