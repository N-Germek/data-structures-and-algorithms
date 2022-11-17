# from data_structures.queue import Queue
import copy


"""animal
{
animal:"cat"
}

"""


class AnimalShelter:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, animal):
        node = Node(animal)

        if self.front is None:
            self.front = node
            self.rear = node
            return self

        self.rear.next = node
        self.rear = node
        self.length += 1
        return self

    def dequeue(self, pref):

        if self.front.value["animal"] == pref:
            removed_animal = self.front.value["animal"]
            self.front = self.front.next
            self.length -= 1
            return removed_animal
        # if self.front.value["animal"] != pref:
        queue_length = copy.deepcopy(self.length)
        answer = None

        while queue_length >= 0:
            if self.front.value["animal"] == pref:
                answer = self.front.value["animal"]
                self.front = self.front.next
                self.length -= 1
                queue_length -= 1
                break
            else:
                remove = self.front.value
                dequeued_node = Node(remove)
                self.front = self.front.next
                self.rear.next = dequeued_node
                self.rear = dequeued_node
                queue_length -= 1

        for i in range(queue_length + 1):
            remove = self.front.value
            dequeued_node = Node(remove)
            self.front = self.front.next
            self.rear.next = dequeued_node
            self.rear = dequeued_node
        if self.front is None:
            raise Exception("Queue is empty.")
        return answer


class Dog:
    pass


class Cat:
    def __init__(self, value=None):
        self.value = value


class Node:
    def __init__(self, value=None, next=None):
        self .value = value
        self.next = next
