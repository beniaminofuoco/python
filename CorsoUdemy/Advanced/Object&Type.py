class MyClass:
    pass

if __name__ == "__main__":
    # Creo un instanza della classe MyClass
    myObj = MyClass()
    print()
    print("Verifichiamo che myObj è un istanza di MyClass isinstance(myObj,MyClass) :  ",isinstance(myObj,MyClass))
    #True

    print()
    print("Verifichiamo che MyClass è un istanza di object isinstance(MyClass,object) :  ", isinstance(MyClass, object))
    # True

    print()
    print("Verifichiamo che myObj è un istanza di object isinstance(myObj,object) :  ", isinstance(myObj, object))
    # True

    print()
    print("Verifichiamo che MyClass è un istanza di type isinstance(MyClass,type) :  ", isinstance(MyClass, type))
    # True

    print()
    print("Verifichiamo che myObj è un istanza di type isinstance(myObj,type) :  ", isinstance(myObj, type))
    # False

    print()
    print("Verifichiamo che object è un istanza di object isinstance(object,object) :  ", isinstance(object, object))
    # True

    print()
    print("Verifichiamo che type è un istanza di type isinstance(type,type) :  ", isinstance(type, type))
    # True

    print()
    print("Verifichiamo che object è un istanza di type isinstance(object,type) :  ", isinstance(object, type))
    # True

    print()
    print("Verifichiamo che type è un istanza di object isinstance(type,object) :  ", isinstance(type, object))
    # True