class Block(object):
    def __init__(self, param_list):
        self.w, self.l, self.h = param_list

    def get_width(self):
        return self.w

    def get_length(self):
        return self.l

    def get_height(self):
        return self.h

    def get_volume(self):
        return self.w * self.l * self.h

    def get_surface_area(self):
        return 2 * (self.w * self.l + self.w * self.h + self.l * self.h)
