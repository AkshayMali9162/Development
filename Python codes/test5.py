class DoubleLinkedCasing(object):
    def __init__(self,value):
        self.value = value
        self.next_value =  None
        self.prev_value = None


a = DoubleLinkedCasing(1)
b = DoubleLinkedCasing(2)
c = DoubleLinkedCasing(3)


a.next_value = b
b.prev_value  = a

b.next_value = c
c.prev_value = b


