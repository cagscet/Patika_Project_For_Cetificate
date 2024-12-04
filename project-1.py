# 1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği
# gibi, non-scalar verilerden de oluşabilir. Örnek olarak:
#
# input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
#
# output: [1,'a','cat',2,3,'dog',4,5]

def flatted_list(nested_list):
    flatted = []
    for item in nested_list:
        if isinstance(item,list):
            flatted.extend(flatted_list(item))
        else:
            flatted.append(item)
    return flatted

nested = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
result = flatted_list(nested)
print(result)