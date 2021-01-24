########################################################################### 
# Crearemos una funcion auxiliar que permita evaluar                      #
# si la resta del target y el valor del nodo actual es                    #
# menor que la resta entre el target y el valor de nodo anterior          #
# adicionalmente chequearemos si el target es mayor que el nodo entonces  #
# quiere decir que el siguiente nodo es el de la derecha                  #
# si es menor entonces el siguiente nodo es el de la izquierda            #
###########################################################################
def findClosestValueInBst(tree, target): 
    return findClosestValueInBstHelper(tree, target, tree.value);

def findClosestValueInBstHelper(tree,target,closest):
	currentNode = tree
	while currentNode is not None:
		if abs(target - closest) > abs(target - currentNode.value):
			closest = currentNode.value
		if target > currentNode.value:
			currentNode = currentNode.right
		elif target < currentNode.value:
			currentNode = currentNode.left
		else:
			break
	return closest

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
