class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("Moves along...")

    def get_make_model(self):
        print(f"I'am a {self.make} {self.model}.")


my_car = Vehicle("Tesla", "Model 3")
print(my_car.make)
print(my_car.model)
my_car.get_make_model()
my_car.moves()

your_car = Vehicle("Audi", "v8")
your_car.get_make_model()
your_car.moves()


#! Inheritance
class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print("file along...")


class Truck(Vehicle):
    def moves(self):
        print("Truck along...")


class GolfCart(Vehicle):
    pass


cessna = Airplane("Cessna", "Random", "K532")
mack = Truck("Mack", "Ruva")
golfwagon = GolfCart("Wagon", "G200")

cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()

print("\n\n\n")
#! ploymorphism
for v in (my_car, your_car, cessna, mack, golfwagon):
    v.get_make_model()
    v.moves()
