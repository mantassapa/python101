aibeA = {1,2,3,4,5}
aibeB= {1,2,3,4,5,7,8,11}
print(aibeA.issubset(aibeB))
print(aibeB.issubset(aibeA)) # poaibis

#virsaibis
print(aibeB.issuperset(aibeA))
print(aibeA.issuperset(aibeB))


aibeC = {12,13,14,15} 
#ar visi skirtingi# tikrina ar visi elemenatai skirtingi
print(aibeC.isdisjoint(aibeB))

#aibiu sajunga
aibeD = aibeA.union(aibeB) #sukuria nauja aibe
print(aibeD)

#aibiu sankirtia
aibeE = aibeA.intersection(aibeB)
print(aibeE)

#skirtumas
aibeF = aibeA.difference(aibeB)
aibeG = aibeB.difference(aibeA)

print(aibeF)
print(aibeG)