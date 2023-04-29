class Food(object):
    def __init__(self):
        # self._elements = Elements()
        pass

    def update(self, food):
        if self.elements is None:
            self.elements = food.elements
        else:
            self.elements = self.elements + food.elements

    class Elements(object):
        def __init__(self, element_weight_s):
            self._element_weight_s = element_weight_s