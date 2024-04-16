class Négyzet:
    def __init__(self, oldal_hossz):
        self.oldal_hossz = oldal_hossz

    def kerület(self):
        eredmény = 4 * self.oldal_hossz
        return f"A négyzet kerülete {eredmény}."

    def terület(self):
        eredmény = self.oldal_hossz ** 2
        return f"A négyzet területe {eredmény}."