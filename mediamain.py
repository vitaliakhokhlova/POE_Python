class Publisher:

    def __init__(self, name):
        self.name = name


class Author:

    def __init__(self, name):
        self.name = name


class Media:

    id = 0

    def __init__(self, name, price, publisher, author):
        Media.id += 1
        self.name = name
        self.price = price
        self.publisher = publisher
        self.author = author

    def __repr__(self):
        return f"id = {self.id}, name = {self.name}, price = {self.price}, publisher = {self.publisher}, author = {self.author}"

    def price_ttc(self):
        return self.price*1.2

class Book(Media):

    def __init__(self,  name, price, publisher, author, nbpage):
        super().__init__(name, price, publisher, author)
        self.nbpage = nbpage

    def get_net_price(self):
        return self.price_ttc()*1.05


if __name__ == '__main__':

    m = Media( "Nénuphares", 100000, "Huston", "Monet")
    print(m)
    print(m.name)
    print(m.price_ttc())

    b = Book( "Bible", 20, 100, "Heaven", "Dieu")
    print(b)
    print(b.get_net_price())

