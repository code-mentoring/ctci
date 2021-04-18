from singly_linkedlist import *

def get_empty_list():
    return SinglyLinkedList()

def evaluate(expect, actual):
    print({True: "Pass.", False: "FAIL!!!"} [expect==actual] +" -- "+ f"Expect {expect}, actual {actual}.")