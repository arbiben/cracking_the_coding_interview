# peopel must take the dogs who have arrived first (FIFO) 
# if they want a dog - return oldest dog, if they want a car - return oldest cat
# if they don't care return whichever came first

from LinkedList import LinkedList
order = 0

class animal_shelter():
    def __init__(self):
        self.dog_queue = LinkedList()
        self.cat_queue = LinkedList()

    def enqueue(self, animal):
        if isinstance(animal, Dog):
            self.dog_queue.push(animal)
        if isinstance(animal, Cat):
            self.cat_queue.push(animal)

    def dequeue_any(self):
        dog = self.dog_queue.last()
        cat = self.cat_queue.last()
        
        if dog and cat:
            if dog.num > cat.num:
                return self.dequeue_cat()
            else:
                return self.dequeue_dog()
        
        if dog or cat:
            return self.dequeue_dog() if dog else self.dequeue_cat()

        return None
    
    def dequeue_cat(self):
        if not self.cat_queue.isEmpty():
            return self.cat_queue.dequeue().name
        
        return None
    
    def dequeue_dog(self):
        if not self.dog_queue.isEmpty():
            return self.dog_queue.dequeue().name
        
        return None

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name):
        global order
        self.num = order
        order += 1
        super().__init__(name)

class Cat(Animal):
    def __init__(self, name):
        global order
        self.num = order
        order += 1
        super().__init__(name)

