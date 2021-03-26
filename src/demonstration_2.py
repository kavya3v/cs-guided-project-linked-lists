"""
Given a reference to the head node of a singly-linked list, write a function
that reverses the linked list in place. The function should return the new head
of the reversed list.

In order to do this in O(1) space (in-place), you cannot make a new list, you
need to use the existing nodes.

In order to do this in O(n) time, you should only have to traverse the list
once.

*Note: If you get stuck, try drawing a picture of a small linked list and
running your function by hand. Does it actually work? Also, don't forget to
consider edge cases (like a list with only 1 or 0 elements).*
"""
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

def reverse(head_of_list):
    # Your code here
    #local var - have the curr node as the head that passed
    prev_node=None
    curr_node=head_of_list
    next_node=head_of_list.next

    while(curr_node is not None):
        #swap the pointers
        next_node=curr_node.next

        #reverse the "next" of the curr node
        curr_node.next = prev_node

        #move all three to next link 
        # Update all pointers to move to next node
        prev_node = curr_node
        curr_node = next_node
        # next_node = next_node.next
    return prev_node

def print_list(start_node): #
    curr_node=start_node
    while(curr_node is not None):
        print(curr_node.value)
        curr_node=curr_node.next

x=LinkedListNode("x")
y=LinkedListNode("y")
z=LinkedListNode("z")

x.next = y
y.next = z

head=x
print_list(head) 


head=reverse(head) 
print("after reversing")
print_list(head)

