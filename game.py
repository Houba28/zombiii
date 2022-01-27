class Game:
    def __init__(self):
        self.score = 0
        self.game_started = False
        self.screen_x = 1280
        self.screen_y = 720
        self.level = 1
        self.max_level = 21
        self.show_dev = False
        self.enemies = []
        self.intervals = [2000, 1500, 1000, 500, 400, 300, 200, 100, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
