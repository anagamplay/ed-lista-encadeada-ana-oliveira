from linked_list import LinkedList

def main():
    ll = LinkedList()

    print("=== Inserindo no início ===")
    ll.insert_beginning(3)
    ll.insert_beginning(2)
    ll.insert_beginning(1)
    ll.print_list()

    print("\n=== Inserindo no final ===")
    ll.insert_end(4)
    ll.insert_end(5)
    ll.print_list()

    print(f"\nTamanho: {ll.size()}")
    print(f"Está vazia: {ll.is_empty()}")

    print("\n=== Buscando valor 3 ===")
    node = ll.search(3)
    print(f"Encontrado: {node.data}")

    print("\n=== Removendo valor 3 ===")
    ll.remove(3)
    ll.print_list()

    print(f"\nTamanho após remoção: {ll.size()}")

if __name__ == "__main__":
    main()
