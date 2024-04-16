class Négyzet:
    def __init__(self, oldal_hossz):
        self.oldal_hossz = oldal_hossz

    def kerulet(self):
        return 4 * self.oldal_hossz

    def terulet(self):
        return self.oldal_hossz ** 2