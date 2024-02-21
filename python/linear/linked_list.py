from typing import Self


class SingleLinkedNode[T]:
    def __init__(self, data: T, next_node: Self | None = None):
        self.data = data
        self.next_node = next_node


class DoublyLinkedNode[T](LinkedNode):
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
        self.head_node = LinkedNode(data[0])
        for datum in data[1:]:
            self.insert(datum)

    def __repr__(self) -> str:
        string_rep = ""
        current_node = self.head_node
        while current_node is not None:
            string_rep += f"{current_node.data}, "
            current_node = current_node.next_node
        return f"linked list with values: {string_rep}"

    def __getitem__(self, *args, **kwargs) -> T:
        pass

    def insert(self, datum: T) -> None:
        """Inserts data at the front of the list"""
        new_node = LinkedNode(datum)
        new_node.next_node = self.head_node
        self.head_node = new_node


linky1 = SingleLinkedList[str]("Hello", "There", "Linked")
linky1.insert("List")

print(linky1)
