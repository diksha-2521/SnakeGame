from turtle import Turtle
import os


class Scoreboard(Turtle):
    def __init__(self, has_walls):
        super().__init__()
        self.score = 0
        self.has_walls = has_walls
        self.color("white")
        self.penup()
        self.hideturtle()

        # Ensure high score file exists
        if not os.path.exists("data.txt"):
            with open("data.txt", "w") as data:
                data.write("walls:0\ninfinite:0\n")

        self.high_scores = self.load_high_scores()
        self.high_score = self.high_scores["walls"] if has_walls else self.high_scores["infinite"]


        self.score_update()

    def load_high_scores(self):
        scores = {"walls": 0, "infinite": 0}
        try:
            with open("data.txt") as data:
                for line in data:
                    mode, value = line.strip().split(":")
                    scores[mode] = int(value)
        except Exception:
            pass
        return scores

    def save_high_scores(self):
        with open("data.txt", "w") as data:
            data.write(f"walls:{self.high_scores['walls']}\n")
            data.write(f"infinite:{self.high_scores['infinite']}\n")


    def score_update(self):
        self.goto(0, 265)
        self.clear()
        mode_text = "Walls" if self.has_walls else "Infinite"
        self.write(
            f"{mode_text} Mode | Score: {self.score} High Score: {self.high_score}",
            align="center",
            font=("Courier", 18, "normal"),
        )



    def reset(self):
        if self.score > self.high_score:
            if self.has_walls:
                self.high_scores["walls"] = self.score
            else:
                self.high_scores["infinite"] = self.score
            self.save_high_scores()
            self.high_score = self.score
        self.score = 0
        self.score_update()

    def high_score_reset(self):
        if self.score > self.high_score:
            if self.has_walls:
                self.high_scores["walls"] = self.score
            else:
                self.high_scores["infinite"] = self.score
            self.save_high_scores()
            self.high_score = self.score
        self.score_update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align="center", font=("Courier", 24, "normal"))


    def add(self):
        self.score += 1
        self.clear()
        self.score_update()
