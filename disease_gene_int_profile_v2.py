# Use the data provided in the attached file for addressing the following questions

# Part 1: Central genes of the network
# Part 2: Identify top five diseases with similar disease-gene interaction profile


###############################################################################################
##############################  disease-gene interaction ######################################
###############################################################################################

print "disease-gene interaction"

print "Part 1: Central genes of the network"
print "Pending"

#read file disease_Gene_Net.txt
f = open('disease_Gene_Net.txt', 'r')

genSymbol = []
diseaseName = []
for row in f.readlines()[1:]:
    items = row.split('\t')
    genSymbol.append(items[0])
    dName = items[1]
    itm = dName.split('\n')
    diseaseName.append(itm[0])

#Recuperation genes liste sorted par ordre alphabetique
geneList = set(genSymbol[1:50])


def fonc1(liste):
    """Compte les elements de la liste en retournant une liste de listes:
       [..., [element, nombre], ...]
    """
    return [[k, liste.count(k)] for k in set(liste)]

lliste = fonc1(genSymbol[0:50])
numList = []
for elem in lliste:
	numList.append(elem[1])

#Central gene of the network in a dictionnary
dic1 = {}
dic1.update(zip(geneList,numList))


print "Done!"




print "Part 2: Identify top five diseases with similar disease-gene interaction profile"


newGL = []
newDN = []

#For each disease-> One gene
#Some genes have several diseases in the same line
#Decomposition
print "Part 2 Step 1"
print "Pending"
for gene in range(0,len(diseaseName)):
	for elem in range(0,len(diseaseName)):
		if elem == gene:
			it = diseaseName[elem].split(', ')
			for i in it:
				newGL.append(genSymbol[gene])
				newDN.append(i)

print len(newGL), len(newDN)
print "Done!"

print "Part 2 Step 2"
print "Pending"
nGL = []
nDN = []

tmp = 0
for i in range(0,len(newDN)):
	if newDN[i] not in nDN:
		#Does not exist
		nDN.append(newDN[i])
		nGL.append(list())
		for j in range(0,len(newGL)):
			#For a given disease
			if newDN[j]==newDN[i] and newGL[j] not in nGL[tmp]:
				nGL[tmp].append(newGL[j])
		tmp+=1
print "Done!"

print "Part 2 Step 3"
print "Pending"
geneCount = []
for i in range(0,len(nGL)-1):
	geneCount.append(len(nGL[i]))
print len(geneCount)
print "Done!"

print "Part 2 Step 4"
dic2 = {}
for i in range(0,len(geneCount)-1):
    dic2[nDN[i]] = geneCount[i]
print 'dic2 =',dic2

import operator
sorted_diseases = sorted(dic2.items(), key=operator.itemgetter(1))
top5 = sorted_diseases[-5:]
print top5

print "Done!"















