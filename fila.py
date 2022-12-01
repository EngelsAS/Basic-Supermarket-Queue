class Node:

  def __init__(self, data):

    self.data = data
    self.next = None


class Fila:

  def __init__(self):
    self.first = None
    self.last = None

  def insere(self, data):

    new_node = Node(data)

    if self.first == None:
      self.first = new_node
      self.last = new_node
    else:
      self.last.next = new_node
      self.last = new_node

  def remove(self):

    if self.first == None:
      print("A lista está vazia")
      return

    self.first = self.first.next
    print("Cliente removido da fila")

  def imprimir(self):

    contents = self.first

    if contents == None:
      print("a lista está vazia")
      return

    while contents != None:
      print(contents.data)
      contents = contents.next

    print("---------------")

