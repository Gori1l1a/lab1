def unique_elements(lst):
    result=[]
    
    def unpack(list_1):
        for item in list_1:
            if type(item)==list:
                unpack(item)
            else:
                if item not in result:
                    result.append(item)
                    
    unpack(lst) 
    return result


list_a=[1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2, 3]]]]
print("Уникальные элементы:", unique_elements(list_a))