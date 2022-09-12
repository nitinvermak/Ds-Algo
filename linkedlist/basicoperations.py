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


my_list = LinkedList()
my_list.head = Node(1)
a=Node(2)
my_list.head.next =a
b=Node(3)
a.next = b
c=Node(4)
b.next = c




my_list.printList()

my_list.printLength()
 