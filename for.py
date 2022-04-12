
def Mergee(dict1,dict2):
    return(dict1.update(dict2))
    


dict1 = {'1':2343,'23':134,'3':233}
dict2 = {'9':2343,'28':134,'7':233}
print(Mergee(dict1,dict2))

print(dict1)