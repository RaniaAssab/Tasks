# Use the data provided in the attached file for addressing the following questions

# Part 1: Central genes of the network
# Part 2: Identify top five diseases with similar disease-gene interaction profile


###############################################################################################
##############################  disease-gene interaction ######################################
###############################################################################################

import operator
import csv

print "###############################################################################################"
print "##############################  disease-gene interaction ######################################"
print "###############################################################################################"


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


print "Part 1: Central genes of the network"
print "Pending"


def fonc1(liste):
    """Compte les elements de la liste en retournant une liste de listes:
       [..., [element, nombre], ...]
    """
    return [[k, liste.count(k)] for k in set(liste)]

#Recuperation genes liste sorted alphabeticaly
lliste = fonc1(genSymbol)
geneList = []
numList = []
for elem in lliste:
	geneList.append(elem[0])
	numList.append(elem[1])


#Central genes of the network in a dictionnary
dic1 = {}
dic1.update(zip(geneList,numList))

w = csv.writer(open("output.csv", "w"))
for key, val in dic1.items():
	w.writerow([key, val])

print "Done!"

print "There are ",len(geneList)," central genes in the network."
print "They are reported in output.csv"



print "Part 2: Identify top five diseases with similar disease-gene interaction profile"


#For each disease-> One gene
#Some genes have several diseases in the same line
#Decomposition
print "Part 2 Step 1"
print "Pending"
newGL = []
newDN = []

for gene in range(0,len(diseaseName)):
	for elem in range(0,len(diseaseName)):
		if elem == gene:
			it = diseaseName[elem].split(', ')
			for i in it:
				newGL.append(genSymbol[gene])
				newDN.append(i)

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
print "Done!"


print "Part 2 Step 4"
dic2 = {}
for i in range(0,len(geneCount)-1):
    dic2[nDN[i]] = geneCount[i]

sorted_diseases = sorted(dic2.items(), key=operator.itemgetter(1))
top5 = sorted_diseases[-5:]
print "Done!"

print "The top 5 diseases are : \n"
for i in reversed(range(len(top5))):
	print len(top5)-i,": ", top5[i][0], " -> ",top5[i][1] ," genes \n"
















