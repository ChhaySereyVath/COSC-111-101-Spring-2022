
def remove_all_after(array,index):
    new_array=[]
    n=0
    for i in array:
        if i < index:
            new_array.append(array[n])
            n+=1
        elif i == index:
            i=index
            new_array.append(array[n])
            break
        else:
            break
    return new_array
print (remove_all_after([1, 1, 2, 2, 2, 3, 3], 2))


