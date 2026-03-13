# Estrutura de Dados

Implementação de estruturas de dados em Python.

## Estruturas implementadas

### Lista Encadeada (Linked List)

Lista encadeada simples composta por nós (`Node`) que armazenam um valor e uma referência para o próximo nó.

**Métodos disponíveis:**

| Método | Descrição |
|---|---|
| `insert_beginning(elem)` | Insere um elemento no início da lista |
| `insert_end(elem)` | Insere um elemento no final da lista |
| `remove(value)` | Remove o primeiro nó com o valor informado |
| `search(value)` | Retorna o nó com o valor informado |
| `print_list()` | Imprime todos os elementos da lista |
| `size()` | Retorna o número de elementos da lista |
| `is_empty()` | Retorna `True` se a lista estiver vazia |

**Exceções:**

- `IndexError("list is empty")` — lançada ao tentar operar em uma lista vazia
- `ValueError("value not found in the list")` — lançada quando o valor não é encontrado

## Requisitos

- Python 3.12.10

## Como executar os testes

```bash
python -m unittest discover -s tests
```

## Estrutura do projeto

```
estrutura-de-dados/
├── node.py               # Classe Node
├── linked_list.py        # Classe LinkedList
└── tests/
    ├── test_node.py      # Testes da classe Node
    └── test_linked_list.py  # Testes da classe LinkedList
```
