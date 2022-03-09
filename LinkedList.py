# Trabalhando com lista encadeada em Python

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next
        else:
            nodes.append("None")
            return " -> ".join(nodes)

    def __iter__(self):
        node = self.head

        while node is not None:
            yield node
            node = node.next

    def len_list(self):
        len = 0
        node = self.head

        while node is not None:
            node = node.next
            len += 1
        else:
            return len

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
        else:
            for current_node in self:
                pass
            else:
                current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("A lista está vazia")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node com '%s' não encontrado" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("A lista está vazia")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return

            prev_node = node

        raise Exception("Node com '%s' não encontrado" % target_node_data)

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("A lista está vazia")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next
                return

            prev_node = node

        raise Exception("Node com '%s' não encontrado" % target_node_data)

    def get_node(self, position):
        if self.head is None:
            raise Exception("A lista está vazia")

        if position > self.len_list() or position < 1:
            raise Exception("Indice maior que o tamanho da lista ou menor que 1")

        for index, node in enumerate(self, start=1):
            if index == position:
                return self.print_node(node)

    def reverse_list(self):
        if self.head is None:
            raise Exception("A lista está vazia")

        prev = None
        current_node = self.head

        while current_node is not None:
            next = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next
        else:
            self.head = prev

    def print_list(self):
        if self.head is None:
            raise Exception("A lista está vazia")

        for node in self:
            print(node.data, end=" ")

    def print_node(self, node):
        print(node.data, end=" ")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


print("Inicializando uma lista")
llist = LinkedList(["Ana", "Maria", "João"])
print(llist)

print("Adiconando node no começo")
llist.add_first(Node("Nathalia"))
print(llist)

print("Adiconando node no fim")
llist.add_last(Node("Marcos"))
print(llist)

print("Adicionando node depois de um node especifico")
llist.add_after("Maria", Node("Carlos"))
print(llist)

print("Adicionando node antes de um node especifico")
llist.add_before("Maria", Node("Amanda"))
print(llist)

print("Removendo um node especifico")
llist.remove_node("Maria")
print(llist)

print("Acessando um node especifico")
llist.get_node(1)  # posicao 1
print()

print("Revertendo a lista")
llist.reverse_list()
print(llist)
