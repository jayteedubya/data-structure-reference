from typing import Self


class SingleLinkedNode[T]:
    def __init__(self, data: T, next_node: Self | None = None):
        self.data = data
        self.next_node = next_node


class DoubleLinkedNode[T](SingleLinkedNode):
    def __init__(
        self,
        data: T,
        next_node: Self | None = None,
        prev_node: Self | None = None,
    ):
        super().__init__(data, next_node)
        self.prev_node = prev_node


class SingleLinkedList[T]:
    def __init__(self, *data: T) -> None:
        self.head_node = SingleLinkedNode(data[0])
        for datum in data[1:]:
            self.insert(datum)

    def __repr__(self) -> str:
        string_rep = ""
        current_node = self.head_node
        while current_node is not None:
            string_rep += f"{current_node.data}, "
            current_node = current_node.next_node
        return f"linked list with values: {string_rep}"

    def __getitem__(self, i) -> T:
        iterations = 0
        current_node = self.head_node
        while current_node is not None and iterations < i:
            iterations += 1
            current_node = current_node.next_node
        if current_node is None:
            raise IndexError("Index out of range! ")
        return current_node.data

    def insert(self, datum: T) -> None:
        """Inserts data at the front of the list"""
        new_node = SingleLinkedNode(datum)
        new_node.next_node = self.head_node
        self.head_node = new_node

    def append(self, datum: T) -> None:
        """Inserts data and the end of the list"""
        new_node = SingleLinkedNode(datum)
        current_node = self.head_node
        while current_node.next_node is not None:
            current_node = current_node.next_node
        current_node.next_node = new_node


class DoubleLinkedList[T]:
    def __init__(self, *data: T) -> None:
        self.head_node = DoubleLinkedNode(data[0])
        self.tail_node = None
        for datum in data[1:]:
            self.insert(datum)

    def __repr__(self) -> str:
        string_rep = ""
        current_node = self.head_node
        while current_node is not None:
            string_rep += f"{current_node.data}, "
            current_node = current_node.next_node
        return f"linked list with values: {string_rep}"

    def insert(self, datum: T) -> None:
        new_node = DoubleLinkedNode(
            datum, next_node=self.head_node, prev_node=self.head_node.prev_node
        )
        if self.head_node is not None:
            self.head_node.prev_node = new_node
            new_node.next_node = self.head_node
            self.head_node = new_node
        if self.tail_node is None:
            self.tail_node = new_node

    def append(self, datum: T) -> None:
        new_node = DoubleLinkedNode(datum, prev_node=self.tail_node)
        self.tail_node.next_node = new_node
        self.tail_node = new_node


if __name__ == "__main__":

    linky1 = SingleLinkedList[str]("List", "Linked", "Single", "There")
    linky1.insert("Hello")
    linky1.append("!")

    print(f"Single Linked List: {linky1}")
    print(f"linky at index 2: {linky1[3]}")

    linky2 = DoubleLinkedList[str]("Hello", "There", "Double", "Linked")
    linky2.insert("List")
    # linky2.append("Backwards")

    print(f"Double Linked List: {linky2}")
