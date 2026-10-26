class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"

class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
   
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.key}: {self.value}"

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.data[index]

        if self.data[index] is None:
            self.data[index] = Node(key, value)
            return

        while current:
            if current.key == key:
                current.value = value
                return

            if current.next is None:
                break

            current = current.next

        current.next = Node(key, value)

    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def print_table(self):
        for i in range(len(self.data)):
            current = self.data[i]
            if current is None:
                print(f"Index {i}: Empty")
            else:
                contacts = []
                while current is not None:
                    contacts.append(str(current.value))
                    current = current.next
                for i in range(len(contacts)):
                    print(f"Index {i}: " +  " - ".join(contacts))

# Contact Class test
contact_1 = Contact("Riley", "123-456-7890")
print(contact_1)
print()

# Node Class test
node_1 = Node(contact_1.name, contact_1)
print(node_1.key)
print(node_1.value)
print(node_1.next)
print()

# HashTable Class test
table = HashTable(10)
table.print_table()
print()
table.insert("John", Contact("John", "909-876-1234"))
table.insert("Rebecca", Contact("Rebecca", "111-555-0002"))
table.print_table()
contact = table.search("John")
print("Search result:", contact)
print()
table.insert("Amy", Contact("Amy", "111-222-3333"))
table.insert("May", Contact("May", "222-333-1111"))
table.print_table()