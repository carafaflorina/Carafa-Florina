#1) lista initiala
initial_list=[7,8,9,2,3,1,4,10,5,6]

#2)lista in ordine crescatoare
list_ascendingOrder=initial_list.copy()
list_ascendingOrder.sort()
print(list_ascendingOrder)

#3)lista in ordine descrscatoare
list_descendingOrder=list_ascendingOrder.copy()
list_descendingOrder.reverse()
print(list_descendingOrder)

#4)lista doar cu numerele pare
list_elementePare=list_ascendingOrder.copy()
print(list_elementePare[1::2])

#5)lista doar cu numerele impare
list_elementeImpare=list_ascendingOrder.copy()
print(list_elementeImpare[0::2])

#6)lista cu elementele multiplu al lui 3
list_elementeMultipluDe3=list_ascendingOrder.copy()
print(list_elementeMultipluDe3[2::3])


list_elementeMultipluDe3_2=[]
for i in list_ascendingOrder:
    if i%3==0:
        list_elementeMultipluDe3_2.append(i)
        
        
print(list_elementeMultipluDe3_2)
   

        
    
