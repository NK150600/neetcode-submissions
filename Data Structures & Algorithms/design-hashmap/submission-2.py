class Node:
    def __init__(self,key,value):
        self.key_val = [key,value]
        self.next = None

class MyHashMap:

    def __init__(self):
        self.hashmap = [Node(0,0) for i in range(10**4)]

    def put(self, key: int, value: int) -> None:
        curr = self.hashmap[key % len(self.hashmap)]

        while curr.next:
            if curr.next.key_val[0] == key:
                curr.next.key_val[1] = value
                return
            curr = curr.next
        curr.next = Node(key,value)

    def get(self, key: int) -> int:
        curr = self.hashmap[key % len(self.hashmap)]

        while curr.next:
            if curr.next.key_val[0] == key:
                return curr.next.key_val[1]
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        curr = self.hashmap[key % len(self.hashmap)]

        while curr.next:
            if curr.next.key_val[0] == key:
                curr.next = curr.next.next
                return
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)