aibeA = {1,2,3,4,5}
aibeB= {1,2,3,4,5,7,8,11}

aibeA.update(aibeB) #cia yra updarinama sena aibe
print(aibeA)
#pasalinimo budai
# aibeA.remove(5)#pasalina aelementa
# aibeA.discard(6)# jeigu nera elemento tai nemeta klaidos tiesiog nieko nesalina
aibeA.pop()

print(aibeA)
aibeA.clear()#visiskai isvalo aibe
print(aibeA)