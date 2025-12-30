import random


class RockPaperScissors:
    def __init__(self) -> None:
        self.gametable = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        """
        (0,0) → tabuleiro[0][0]
        (0,1) → tabuleiro[0][1]
        (0,2) → tabuleiro[0][2]
        
        (1,0) → tabuleiro[1][0]
        (1,1) → tabuleiro[1][1]
        (1,2) → tabuleiro[1][2]
        
        (2,0) → tabuleiro[2][0]
        (2,1) → tabuleiro[2][1]
        (2,2) → tabuleiro[2][2]
        """
        self.coordinates_table = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
        ]

    def get_rnd_coordinates(self) -> list[int]:
        return [random.randint(0, 2), random.randint(0, 2)]

    def render_table(self):
        for line in self.gametable:
            print(line)

    def render_coordinates_table(self):
        for line in self.coordinates_table:
            print(line)

    def cpu_play(self):
        cpu_play = self.get_rnd_coordinates()
        # print(cpu_play)
        x_axis, y_axis = cpu_play
        print("x_axis:", x_axis)
        print("y_axis:", y_axis)
        self.gametable[x_axis][y_axis] = 1

    def computer_move(self):
        print("\nComputer Round: ")
        self.render_table()
        self.cpu_play()
        self.render_table()
        # TODO: colocar um check pra ver se ja ta preenchido o tabuleiro na coordenada

    def person_play(self):
        self.render_coordinates_table()
        person_play = input(
            "Insert coordinates via comma separated values e.g. 0,0 (x,y): "
        )
        prs_play_lst = person_play.split(",")
        print(prs_play_lst)
        x_axis, y_axis = prs_play_lst
        print(x_axis)
        print(y_axis)
        # TODO: colocar um check pra ver se ja ta preenchido o tabuleiro na coordenada

    def player_move(self):
        print("\nPlayer Round: ")
        self.render_table()
        self.cpu_play()
        self.render_table()
        # TODO: completar a jogada do player

    def start(self):
        self.computer_move()
        self.person_play()


if __name__ == "__main__":
    game = RockPaperScissors()
    game.start()
