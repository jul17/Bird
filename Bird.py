class Bird:
    total_amount_in_the_world = 0

    def __init__(self, name="kivi", colour="black", weight=15, country="Bali", amount_in_the_world=50):
        self.name = name
        self.colour = colour
        self.weight = weight
        self.country = country
        self.amount_in_the_world = amount_in_the_world
        Bird.total_amount_in_the_world += amount_in_the_world

    def to_string(self):
        print("Name - " + self.name + ", Colour - ", self.colour, ", Weight - ", self.weight, ", Country - ",
              self.country,
              ", Amount in the world - ", self.amount_in_the_world)

    def print_sum(self):
        print("Amount in the world - " + self.name, self.amount_in_the_world)

    @staticmethod
    def print_static_sum():
        print("Total amoumt in the wourld", Bird.total_amount_in_the_world)


if __name__ == '__main__':
    print("\n**************************\n")
    kivi = Bird()
    parrot = Bird("parrot", "red", 3.4, "Brazil")
    eagle = Bird("eagle", "brown", 34, "Spain", 300)

    kivi.to_string()
    parrot.to_string()
    eagle.to_string()

    print("\n**************************\n")
    kivi.print_sum()
    parrot.print_sum()
    eagle.print_sum()

    print("\n**************************\n")
    Bird.print_static_sum()
    print("\n**************************\n")

