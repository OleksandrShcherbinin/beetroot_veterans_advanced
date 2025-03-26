# class MyClass:
#     def __hash__(self):
#         return 1
#
#
# print(hash(MyClass()))
# # print(hash(1000))
# # print(hash('hello'))
# # print(hash('hello'))
# # print(hash('hello'))
#
# my_dict = {
#     'key_1': 1, # 0: 1,
#     'key_2': 1, # 1: 1,
#     'key_3': 1, # 2: 1,
#     'key_4': 1, # 3: 1,
#     'key_5': 1  # 4: 1,
# }
#
# my_set = {'key_1', 'key_2', 'key_3'}
#
# my_frozenset = frozenset([1, 2, 3, 4, 5])
#
# from collections import Counter
#
# counter = Counter(['apple', 'orange', 'apple', 'pear', 'orange', 'grape'])
# print(counter)
#
# from collections import ChainMap
# map_1 = {'a': 1, 'b': 2}
# map_2 = {'b': 3, 'c': 4}
# chain = ChainMap(map_2, map_1)
# print(chain['a'])
# print(chain['b'])
#
#
# class Person:
#     pass
#
# print('*' * 100)
# print(hash(None))
# print(hash(None))
# print(hash(None))
# print(hash(None))
# print(hash(1000))
# print(hash(1000.00))
# print(hash('python'))
# print(hash(b'python'))
# print(hash(True))
# print(hash(False))
# # print(hash((1, 2, 3, [1, 2, 3])))
# person = Person()
# print('ID', id(person))
# person.name = 'Alex'
# print(hash(person))
# print(person.name)
#
# new_dict = {person: [1, 2, 3]}
# print(new_dict)
# from typing import Any
#
#
# def simple_hash(text: Any) -> int:
#     return sum(
#         index * ord(symbol) for index, symbol in enumerate(repr(text), start=1)
#     )


# print('*' * 100)
# print(simple_hash(3.14))
# print(simple_hash('3.14'))
# print(simple_hash(True))
# print(simple_hash('hello'))
# print(simple_hash('hello'))
# print(simple_hash('elloh'))
import hashlib


# md5_hash = hashlib.md5(b'hello')
# print(md5_hash.hexdigest())
#
# md5_hash_2 = hashlib.md5(b'hello2')
# print(md5_hash_2.hexdigest())
#
# sha_256 = hashlib.sha256(b'hello')
# print(sha_256.hexdigest())

SECRET_KEY = 'secret_key'


def store_password(password: str) -> str:
    hash_object = hashlib.sha256(SECRET_KEY.encode() + password.encode('utf-8'))
    return hash_object.hexdigest()


def verify_password(stored_password: str, input_password: str) -> bool:
    hash_object = hashlib.sha256(SECRET_KEY.encode() + input_password.encode())
    input_password_hash = hash_object.hexdigest()
    return stored_password == input_password_hash


# password = 'qwerty'
# stored_password = store_password(password)
# print(stored_password)
# if verify_password(stored_password, 'qwerty2'):
#     print('Access granted')
# else:
#     print('Wrong password')


def generate_file_hash(file_path: str) -> str:
    sha_256_hash = hashlib.sha256()
    with open(file_path, 'rb') as file:
        for byte_block in iter(lambda: file.read(4096), b''):
            sha_256_hash.update(byte_block)

    return sha_256_hash.hexdigest()


def compare_images(file_1: str, file_2: str) -> None:
    hash_1 = generate_file_hash(file_1)
    print(hash_1)
    hash_2 = generate_file_hash(file_2)
    print(hash_2)

    if hash_1 == hash_2:
        print('Files are the same')
    else:
        print('Files are different')


# compare_images('hash.png', 'files/time_complexity.png')
from simhash import Simhash


def compare_documents(doc1: str, doc2: str) -> None:
    sim_hash_1 = Simhash(doc1)
    sim_hash_2 = Simhash(doc2)

    hamming_distance = sim_hash_1.distance(sim_hash_2)
    print('Hamming distance', hamming_distance)
    if hamming_distance < 15:
        print('Document is similar')
    else:
        print('Documents are different')


document_1 = 'This is sample document that contains some text'
document_2 = 'This is sample document that some text'

# compare_documents(document_1, document_2)
import hmac

key = b'secret_key'
message = b'Hello world'

hmac_object = hmac.new(key, message, hashlib.sha256)
hash_object = hmac_object.hexdigest()
print(hash_object)

received_message = b'Hello world'
calculated_hmac = hmac.new(key, received_message, hashlib.sha256)
print(calculated_hmac.hexdigest())

if hmac.compare_digest(calculated_hmac.hexdigest().encode(), hash_object.encode()):
    print('Match')
else:
    print('Different')
