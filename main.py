from ast import main
from os import name

from core.gui import Gui


class Main():
    def main(self):
        Gui().startPygameLoop()



if __name__ == "__main__":
    m = Main()
    m.main()