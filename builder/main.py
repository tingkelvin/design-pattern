from director import Director
from concreteBuilder1 import ConcreteBuilder1

if __name__ == "__main__":
    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    product = director.build()
    product.list_parts()

    print("\n")

    print("Standard full featured product: ")
    director.build_full_featured_product()
    product = director.build()
    product.list_parts()
