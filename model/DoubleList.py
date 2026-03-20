from typing import TypeVar, Generic, Optional

from model.Node import Node

T = TypeVar('T')

class DoubleList(Generic[T]):
    
    def __init__(self):
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None
        self.size: int = 0

    def add(self,value:T):
        newNode=Node(value)

        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            newNode.previous=self.tail
            self.tail.next=newNode
            self.tail=newNode
        
        self.size+=1
        return True
    
    def remove(self,o:object):
        aux=self.head

        if self.head is None:
            return False
        
        while aux != None:
            if aux.getValue()==o:
                if aux==self.head and self.head.next==None:
                    self.head=None
                    self.tail=None
                    
                elif aux==self.head:
                    self.head=self.head.next
                    self.head.setPrevious(None)
                    
                elif aux==self.tail:
                    self.tail=self.tail.previous
                    self.tail.setNext(None)
                    
                else:
                    aux.previous.next=aux.next
                    aux.next.previous=aux.previous
                
                aux.next=None
                aux.previous=None
                self.size-=1
                return True
            aux=aux.next
        return False
        
    def contains(self, o:object):
        if o is None:
            raise ValueError("la lista no permite datos nulos")
        aux = self.head
        while aux is not None:
            if aux.value==o: 
                return True
            aux = aux.next
            
        return False
        
    def isEmpty(self): 
        return self.size == 0