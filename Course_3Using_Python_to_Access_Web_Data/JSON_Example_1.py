import json
data = '''{
"name" : "Chuck",
"phone" : {
"type" : "intl",
"number" : "+1 734 303 4456"},
"email" : {
"hide" : "yes"}
}'''
#JSON represents data as nested "lists" and "dictionaries"
info = json.loads(data)
print ("Name:" info ["name"])
print ("Hide:" info ["email"], ["hide"])

Name: Chuck
Hide: {'hide': 'yes'} ['hide']
