from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from random import randint

class Quiz(App):
    pass


class MainWidget(GridLayout):

    neighbors = {
        'q': ['w', 'a'],
        'w': ['q', 'e', 's'],
        'e': ['w', 'd'],
        'a': ['q', 's', 'z'],
        's': ['w', 'a','d','x'],
        'd': ['e', 's','c'],
        'z': ['a', 'x'],
        'x': ['z', 's', 'c'],
        'c': ['x', 'd'],

    }

    def neigh(self, widget, id):
        widget.background_color = self.change_color(widget.background_color)
        for i in self.neighbors[id]:
            for j in i:
                widget.parent.ids[j].background_color = self.change_color(widget.parent.ids[j].background_color)


    def start(self,widget):
        for i in widget.parent.ids:
            widget.parent.ids[i].background_color = self.random_color()

    def change_color(self, color):
        if color == [0, 0, 1, 1.0]:
            return (1, 0, 0)
        elif color == [1, 0, 0, 1.0]:
            return (0, 0, 1)

    def random_color(self):
        if randint(0, 1):
            return (0, 0, 1)
        else:
            return (1, 0, 0)

if __name__ == '__main__':
    Quiz().run()




