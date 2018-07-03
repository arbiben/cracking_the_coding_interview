from animal_shelter import animal_shelter, Dog, Cat

a = animal_shelter()
a.enqueue(Dog("rick"))
a.enqueue(Cat("bick"))
a.enqueue(Cat("nick"))
a.enqueue(Dog("lick"))
a.enqueue(Dog("pick"))
a.enqueue(Cat("wick"))
a.enqueue(Dog("sick"))

print(a.dequeue_any())
print(a.dequeue_any())
print(a.dequeue_any())

print(a.dequeue_dog())
print(a.dequeue_cat())
