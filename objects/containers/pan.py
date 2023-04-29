import math

class Pan(object):
    _volume_filled = 0  # in %
    _food = None

    def __init__(self, diameter, height, material):
        self._diameter = diameter
        self._height = height
        self._material = material 
        self._volume = self._set_volume()
        self._temperature = self._set_initial_temperature(material)

    # set pan volume
    def _set_volume(self):
        return math.pi * self._diameter

    # fill the pan
    def fill(self, food):
        # add food elements
        self._set_food_elements(food)

        # update pan food volume
        self._update_food_volume(food)

    def _set_food_elements(self, food):
        if self._food is None:
            self._food = food
        else:
            self._food = self._food.update(food)

    def _update_food_volume(self, food):
        self._volume_filled += food.volume
        if self._volume_filled > self._volume:
            rest = self._volume_filled - self._volume
            self._volume_filled = self._volume
            # self.drop(rest)

    # set temperature based on material
    def _set_initial_temperature(material):
        pass

    def _update_temperature(self):
        pass

    def cook(self):
        self._update_temperature()
        self._update_food()
        pass



    



    