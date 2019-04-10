# April 9th 2019
# Rania Assab
# Tasks:
# Use the data provided in the attached file for addressing the following questions

# Part 1: Central genes of the network
# Part 2: Identify top five diseases with similar disease-gene interaction profile

# Imports
import operator
import csv
import numpy
from itertools import chain

###############################################################################################
##############################  disease-gene interaction ######################################
###############################################################################################


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
			newGL.append(genSymbol[gene])
			newDN.append(it[0])

print "Done!"


print "Part 2 Step 2"
#Genes listing for each disease
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
#Diseases sharing the highest number of genes
print "Pending"

def common_genes(dis1, dis2): 
    dis1_set = set(dis1) 
    dis2_set = set(dis2) 
    if (dis1_set & dis2_set): 
        return(dis1_set & dis2_set) 


#Initialization empty array
simScoreMatrix = numpy.zeros((len(nDN), len(nDN)), dtype=int)
print "There are ",len(nDN)," diseases reported."

#Best scores recuperation
bestScores = []
bestScorePosition1 = []
bestScorePosition2 = []
#first col disease
for i in range(0,len(nDN)):
	#I look at all diseases
	for j in range(0,len(nDN)):
		if nDN[i]!=nDN[j]:
			#Look for matches
			match = common_genes(nGL[i], nGL[j])
			#Put the score in the matrix
			if match!=None:
				simScoreMatrix[i,j] = len(match)
	bestScorePosition1.append(nDN[i])
	bestScorePosition2.append(nDN[numpy.argmax(simScoreMatrix[i])])
	bestScores.append(max(simScoreMatrix[i]))

print "Done!"


print "Part 2 Step 4"
print "Pending"


diseasesDup = []
for i in range(0,len(nDN)):
	t1 = [bestScorePosition1[i],bestScorePosition2[i]]
	tmp = [set(t1),[bestScores[i]]]
	diseasesDup.append(tmp)


#remove duplicates
def remove_duplicates(dico):
	return [i for n, i in enumerate(dico) if i not in dico[n + 1:]]

allInteractions = remove_duplicates(diseasesDup)


cleanInteractions = []
for i in range(0,len(allInteractions)):
	cleanInteractions.append(list(chain.from_iterable(allInteractions[i])))

#Sort interactions following their score
top5 = sorted(cleanInteractions, key = lambda x: int(x[2]))
top5 = top5[-5:]

print "The top 5 diseases are : \n"
for i in range(0,5):
	print 4-i+1,": ", top5[i][0], " - ",top5[i][1] , " -> ",top5[i][2] ," genes \n"

print "Done!"












