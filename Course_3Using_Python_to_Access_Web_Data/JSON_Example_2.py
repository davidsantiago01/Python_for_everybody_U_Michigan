import json
#Square Brackets menas a list, so ID 001 and ID 009 is are dictionaries = a list of two dictionaries
input = '''[  
{"id" : "001",
"x" : "2",
"name" : "Chuck"
},
{"id" : "009",
"x" : "7",
"name" : "Chuck"
}
]'''

info = json.loads (input)
print ("User count:" , len(info))
for item in info:
  print ("Name", item["name"])
  print ("Id", item["id"])
  print ("Attribute", item["x"])

User count: 2
Name Chuck
Id 001
Attribute 2
Name Chuck
Id 009
Attribute 7
