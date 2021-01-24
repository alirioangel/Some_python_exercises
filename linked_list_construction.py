# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

	# para setear la cabeza si no existia 1 antes seteamos cabeza y cola
	# si ya existia una cabeza la insertamos antes de esta con insertBefore
    def setHead(self, node):
        if self.head is None:
			self.head = node
			self.tail = node
			return
		self.insertBefore(self.head, node)

	# funcion para setear la cola a partir del setHead si 
	# no existe una cola anterior (porque si no hay cola anterior tampoco
	# hay cabeza). o insertandola despues de la cola existente
    def setTail(self, node):
        if self.tail is None:
			self.setHead(node)
			return
		self.insertAfter(self.tail,node)
	
	# chequeamos que el nodo a ingresar no sea el unico nodo
	# de una lista de 1 nodo. si no es removemos sus pointers
	# por seguridad, luego seteamos los pointers next y prev del 
	# nodo que estara despues, verificando que no sea la cabeza
	# si es la cabeza la actualizamos.
    def insertBefore(self, node, nodeToInsert):
		if nodeToInsert == self.head and nodeToInsert == self.tail:
			return
		self.remove(nodeToInsert)
		nodeToInsert.prev = node.prev
		nodeToInsert.next = node
		if node.prev is None:
			self.head = nodeToInsert
		else:
			node.prev.next = nodeToInsert
		node.prev = nodeToInsert

	# chequeamos que el nodo a ingresar no sea el unico nodo
	# de una lista de 1 nodo. si no es removemos sus pointers
	# por seguridad, luego seteamos los pointers next y prev del 
	# nodo que estara antes verificando que no sea la cola 
	# si es la cola actualizar la cola.
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
			return
		self.remove(nodeToInsert)
		nodeToInsert.next = node.next
		nodeToInsert.prev = node
		if node.next is None:
			self.tail = nodeToInsert
		else:
			node.next.prev = nodeToInsert
		node.next = nodeToInsert

	# comprobamos si la posicion puesta es 1 para saber si
	# quieren añadirlo a la cabeza si no continuamos iterando
	# desde la cabeza y hasta encontrar la posicion
	# si encontramos la posicion usamos insertBefore (explicada arriba)
	# si no encontramos seteamos como Cola xq significa que esta al final 
	# o fuera de la lista
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
			self.setHead(nodeToInsert)
			return
		node = self.head
		currentPosition = 1
		while node is not None and currentPosition != position:
			node = node.next
			currentPosition += 1
		if node is not None:
			self.insertBefore(node, nodeToInsert)
		else:
			self.setTail(nodeToInsert)
			
	# nos situamos en la cabeza (inicio de la lista)
	# iteramos hasta que el node sea None
	# creamos un valor temporal (nodeToRemove) = al nodo 
	# que estamos iterando, comprobamos que el valor del nodo
	# sea el valor que requerimos eliminar, si es
	# llamamos remove (explicado abajo)
    def removeNodesWithValue(self, value):
        node = self.head
		while node is not None:
			nodeToRemove = node
			node = node.next
			if nodeToRemove.value == value:
				self.remove(nodeToRemove)
		
	# verificamos que no sea la cabeza o la cola
	# si son las actualizamos con los valores prev o next
	# respectivamente. luego procedemos a utilizar
	# el updateNodePointers (explicado abajo)
    def remove(self, node):
        if node == self.head:
			self.head = self.head.next
		if node == self.tail:
			self.tail = self.tail.prev
		self.updateNodePointers(node)

		
	# nos posicionamos en la cabeza (inicio de la lista)
	# iteramos hasta conseguir el valor o hasta que se acabe
	# la lista. si conseguimos el valor regresaremos true
	# si no lo conseguimos regresara false
    def containsNodeWithValue(self, value):
        node = self.head
		while node is not None and node.value != value :
			node = node.next
		return node is not None
	
	
	# Funcion helper para eliminar de manera segura
	# los pointers de un nodo ejemplo:
	# 1 -> 2 -> 3 si removemos el 2
	# node.prev(1).next = 2 lo sobreescribimos por el node.next = 3
	# node.next(3).prev = 2 lo sobreescribimos por el node.prev = 1
	# cortamos ambos nodos y removemos node.next y prev = None
	def updateNodePointers(self, node):
		if node.prev is not None:
			node.prev.next = node.next
		if node.next is not None:
			node.next.prev = node.prev
		node.next = None
		node.prev = None
