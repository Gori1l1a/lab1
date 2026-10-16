def flatten_list(lst):
    i=0
    while i<len(lst):
        if type(lst[i])==list:
            flatten_list(lst[i])
            while len(lst[i])>0:
                lst.insert(i+1,lst[i].pop())
            lst.pop(i)
        else:
            i+=1
            
list_1=[1,2,[1],3,4,[[3],[4],[5]]]
flatten_list(list_1)
print(list_1)