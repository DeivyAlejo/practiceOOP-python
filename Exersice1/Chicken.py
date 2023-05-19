class Chicken:
    def __init__(self, name="Nancy", happy = True, alive = True, hearts = 4, food = 0.1):
        self.name = name
        self.happy = happy
        self.alive = alive
        self.hearts = hearts
        self.food = food
        
    def feed(self, food_amount):
        if self.alive:
            self.food += food_amount
            if self.food > 2:
                self.alive = False
            
            if self.hearts <= 3:
                self.hearts += 1

    def play(self, Chicken):
        if self.alive and Chicken.alive:
            self.happy = True
            Chicken.happy = True

    def hit(self):
        if self.alive:
            self.happy = False
            self.hearts -= 1
            if self.hearts < 1:
                self.alive = False

    def get_eggs(self):
        if self.alive:
            if self.food > 0.25:
                self.food -= 0.25
                if self.happy:
                    self.happy = False
                    return 2
                return 1
    
    def __repr__(self):
        return f"Chicken(name = {self.name}, happy = {self.happy}, alive = {self.alive}, hearts = {self.hearts}, food = {self.food})"

    def __str__(self):
        return f"Chicken({self.name} is happy = {self.happy}, alive = {self.alive}, it has {self.hearts} hearts, and {self.food}kg of food)"
    
    
    
    
chicken1 = Chicken("Sandra")
chicken2 = Chicken()

print(chicken1)
chicken1.feed(0.5)
print(chicken1)
chicken1.get_eggs()
print(chicken1)
chicken1.hit()
chicken1.hit()
chicken1.hit()
print(chicken1)
chicken2.hit()
print(chicken1)
print(chicken2)
chicken1.play(chicken2)
print(chicken1)
print(chicken2)

