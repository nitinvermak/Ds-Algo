class Node():

    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList():

    def __init__(self,head=None):
        self.head = head

    def printList(self): 
            temp = self.head 
            while (temp): 
                print (temp.data, " -> ", end = '') 
                temp = temp.next

    def printLength(self):
            temp=self.head
            count = 0
            while (temp):
                temp= temp.next
                count+=1
            print('Length = {}'.format(count))

    def arrayToLinkedList(self,arr):
        for item in arr:            
            if self.head:
                    temp = self.head
                    last = None
                    while temp:
                        last = temp
                        temp= temp.next
                    last.next = Node(item)         
            else:
                self.head = Node(item)
                print(self.head)


ll = LinkedList()

ll.arrayToLinkedList([i for i in range(20)])
ll.printList()
ll.printLength()