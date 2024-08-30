dict1={1:"one", 2:"two"}
dict2={3:"three", 4:"four"}
dict3={5:"five", 6:"six"}

def concatenate(d1,d2,d3):
    new_dict = {}
    for d in [d1,d2,d3]:
        new_dict.update(d)
    return new_dict

print(concatenate(dict1,dict2,dict3))
