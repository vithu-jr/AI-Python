class Dog:

    def __init__(self, name):
        self.name = name
    
    def display(self):
        print(self.name)
    
    def update(self, Updated_name):
        self.name = Updated_name

dog_1 = Dog('Tommy')
dog_1.display()
dog_1.update('dobby')
dog_1.display()