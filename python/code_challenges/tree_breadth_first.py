from data_structures.binary_tree import BinaryTree, Node
from data_structures.queue import Queue

"""
ALGORITHM breadthFirst(root)
// INPUT  <-- root node
// OUTPUT <-- front node of queue to console

  Queue breadth <-- new Queue()
  breadth.enqueue(root)

  while ! breadth.is_empty()
    node front = breadth.dequeue()
    OUTPUT <-- front.value

    if front.left is not NULL
      breadth.enqueue(front.left)

    if front.right is not NULL
      breadth.enqueue(front.right)
      """


def breadth_first(lst):
    lst = []
    if BinaryTree() is not None:
        return lst

    while lst is None:
        node = BinaryTree(node.front)
        node.front = node
        # lst.append(node.front.value)
        lst.dequeue(node.front)
        # lst.enqueue(node.front.value)
        if lst.left is not None:
            lst.enqueue(node.left)
            # lst.append(node.left.value)
        if node.right is not None:
            lst.enqueue(node.right)
            # lst.append(node.right.value)
        lst.dequeue(node.front.value)
        return lst
    #
    #     node = Node.value
    #     front = root


    # if lst is not None:
    #     node = Queue.dequeue(front.value)
    #     lst.append(node)
    #


    #
    # while lst is not None:
    #     lst.enqueue(root.value)

    #
    # lst.enqueue()
    # node = Queue()
    # while lst is None:
    #     pass

