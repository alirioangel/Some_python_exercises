########################################################
# Solucion con recursividad, se evaluara nodo a nodo   #
# para determinar si es None, si es none y no tiene    #
# hijos de ningun lado entonces se acabo la suma       #
# y se añade al arreglo y si no es None  se sumara     #
# al total que se lleva                                #
########################################################

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums = []
	branchSumsHelper(root,0,sums)
	return sums
	
	
def branchSumsHelper(node,total,sums):
	if node is None:
		return
	newTotal = total + node.value
	if node.left is None and node.right is None:
		sums.append(newTotal)
		return
	branchSumsHelper(node.left,newTotal,sums)
	branchSumsHelper(node.right,newTotal,sums)
