import hashlib

#print(hashlib.algorithms_available)

def hashing_hardcoded():
    hash_obj = hashlib.md5(b'Hello, Python!')
    print("Hex string representing the hash:",hash_obj.hexdigest())
    print("sequence of bytes representing the hash:",hash_obj.digest())

# recieving input and enconding it, (hash function only accepts a sequence of bytes as param)

def recieving_input():
    mystring = input("Enter the string to hash:")
    hash_obj2 = hashlib.md5(mystring.encode())
    print(hash_obj2.hexdigest())

hashing_hardcoded()
recieving_input()






