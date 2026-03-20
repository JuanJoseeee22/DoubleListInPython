from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class Node(Generic[T]):

    def __init__(self,value:T):
        self.value:T=value
        self.next:Optional[Node[T]]=None
        self.previous:Optional[Node[T]]=None

    def getValue(self):
        return self.value
    
    def setValue(self,value):
        self.value=value

    def getNext(self) -> Optional[Node[T]]:
        return self.next

    def setNext(self, next: Optional[Node[T]]) -> None:
        self.next = next

    def getPrevious(self) -> Optional[Node[T]]:
        return self.previous

    def setPrevious(self, previous: Optional[Node[T]]) -> None:
        self.previous = previous
    