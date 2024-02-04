class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList[T]:
    def __init__(self, *args: T) -> None:
        pass

    def __repr__(self) -> str:
        pass

    def __getitem__(self, *args, **kwargs) -> T:
        pass


linky = LinkedList[str]()
