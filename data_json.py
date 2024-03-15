import json
datajson={
    "finland": "usimaa",
    "helsnki":[
      {
        "vuosari": "ita_helsnki",
        "eira": "etelä_helsnki"} 
    ]

}
with open ('datajson.json','w')as file:
    json.dump(datajson, file, indent=8)
   