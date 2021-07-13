from fuzzywuzzy import process, fuzz
def name_match(name1,name2):
    # ratio = fuzz.ratio(name1,name2)
    # print(ratio)
    ratio = process.extract(name1,name2)
    # for k, v in ratio:
    #     if v >= 90:
    #         print(k)
    print(ratio)





name_match('TBM Hotel', ['MTB Hotel','BTM Hotel', 'Hotel BTM'])
    