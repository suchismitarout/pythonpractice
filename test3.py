d = {"results":[{"address_components" : [
            {
               "long_name" : "22/1",
               "short_name" : "22/1",
               "types" : [ "street_number" ]
            },
            {
               "long_name" : "2nd Main Road",
               "short_name" : "2nd Main Rd",
               "types" : [ "route" ]
            },
            {
               "long_name" : "APMC Yard",
               "short_name" : "APMC Yard",
               "types" : [ "political", "sublocality", "sublocality_level_3" ]
            },
            {
               "long_name" : "Yesvantpur Industrial Suburb",
               "short_name" : "Yesvantpur Industrial Suburb",
               "types" : [ "political", "sublocality", "sublocality_level_2" ]
            },
            {
               "long_name" : "Yeswanthpur",
               "short_name" : "Yeswanthpur",
               "types" : [ "political", "sublocality", "sublocality_level_1" ]
            },
            {
               "long_name" : "Bengaluru",
               "short_name" : "Bengaluru",
               "types" : [ "locality", "political" ]
            }]}]}

print(d["results"][0]["address_components"][5]['long_name'])

