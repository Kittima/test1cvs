import random
def generate_list():
    alist = [x for x in range(random.randint(-10, 10)) ]
    assert len(alist) > 0, "A generated list is empty!"
    assert sum(alist) >= 0, "the Sum of a generated list of number is less than zero!!" 
    return alist
    
    
""" 
print a generated list
"""
def printIt():
    mylist = generate_list()
    print( mylist )    
    
def main():
    """business logic for when running this module as the primary one!"""
    printIt()

"""
If this script file is called, run main() directly
""" 
if __name__ == '__main__':
    print( "Test printIt():" )
    main()