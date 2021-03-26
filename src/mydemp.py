class LinkedListNode:
    #initializer funciton
    def __init__(self,value):
        self.value=value
        self.next=None
    


def insert_at_head(linked_list,new_value): #recieve the head and new insert
    #create a new link list node
    new_node=LinkedListNode(new_value)
    new_node.next=linked_list
    # linked_list.next=None
    return new_node #since we cant assigned to linked_list which is outside fun
     
def insert_at_tail(linked_list_tail,new_value):#pass tail
    new_node=LinkedListNode(new_value)
    linked_list_tail.next = new_node
    return  new_node
    
def print_list(start_node): #
    curr_node=start_node
    while(curr_node is not None):
        print(curr_node.value)
        curr_node=curr_node.next

#init code head and tail
#note here head is the linked_list
linked_list=LinkedListNode(6)
tail=linked_list #saving the original head so we can access tail when more nodes are inserted

linked_list= insert_at_head(linked_list,5)
tail=insert_at_tail(tail,8)
# head.next=LinkedListNode(7)
# head.next.next=LinkedListNode(5)
# insert_node(head,7)
# insert_node(head,5)

# print(head)
# print(head.value)
# print(head.next.value)
# print(head.next.next.value)
print_list(linked_list)
