def  removeNodes(head, x):
    while head and head.val>x:
        print head.val
        head = head.next
    curr = head
    while curr:
        if curr.next and curr.next.val>x:
            print curr.val
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head