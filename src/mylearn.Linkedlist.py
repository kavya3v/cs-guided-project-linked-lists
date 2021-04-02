#create linkedlist
class LinkedListNode:
    def __init__(self,value):
        self.value=value
        self.next=None

x=LinkedListNode("X")
y=LinkedListNode("Y")
z=LinkedListNode("Z")
x.next=y
y.next=z
# print(a.value)
#insert at head
def insert_at_head(head_of_list):
    new_node=LinkedListNode("new")
    new_node.next =  head_of_list
    return new_node
#so we can save the head - return from function
# head = insert_at_head(x)

#insert at tail
def insert_at_tail(linked_list):
    new_node = LinkedListNode("t")
    linked_list.next = new_node
    return new_node

#so we can save the tail
# tail = insert_at_tail(b)

#print the list
def print_list(linked_list):
    curr_node = linked_list
    while(curr_node is not None):
        print(curr_node.value)
        curr_node = curr_node.next
# print(print_list(head))

#delete this node
def delete_this_node(del_node):
    #we copy the next nodes value to delnode
    next_node = del_node.next
    del_node.value = next_node.value
    del_node.next = next_node.next
# delete_this_node(b)
# print(print_list(head))

#reverse a node !!!!!!!!!
print(print_list(x))
def reverse_node(l):
    prev_node = None
    curr_node = l
    next_node = l.next
    while(curr_node is not None):
        next_node = curr_node.next
        #shift the pointers
        curr_node.next = prev_node
        #swap
        prev_node = curr_node
        curr_node = next_node
        
    return prev_node
    

#merge two linked list
arra=[1,2,3,]
arrb=[4,5]
def merge_list(l1,l2):
    dummyList = LinkedListNode("*")
    curr_node = dummyList
    while (curr_node is not None):
        if l1 is None:
            curr_node.next = l2
            return dummyList.next
        if l2 is None:
            curr_node.next = l1
            return dummyList.next
        if l1.value < l2.value:
            curr_node.next = l1
            l1=l1.next
        else:
            curr_node.next = l2
            l2=l2.next
        #move on
        curr_node = curr_node.next
    return dummyList.next
        
    
#insert into the sorted array
#[] #insert at head[2,3] # #insert at tail
#insert inbetween [5,9,10] #8
def insert_intosorted(l,value):
    new_node = LinkedListNode(value)
    if l == None:
        return new_node
    if value <= l.value
        #insert as head
        new_node.next = l
        return new_node
    #loop thru the nodes and insert when value less than node value
    #if value is not less than any of the nodes value - then insert as tail
    curr_node = l
    while(curr_node is not None):
        if curr_node.next is None:
            #insert at tail
            curr_node.next = new_node
            break

        if(value) <= curr_node.next.value:
            new_node.next = curr_node.next
            curr_node.next = new_node
            break
        #move on 
        curr_node = curr_node.next
    return l 
        












