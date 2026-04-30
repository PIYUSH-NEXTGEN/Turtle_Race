from turtle import Turtle, Screen
import random
import time  # --- NEW: For animation delays ---


# --- NEW: Scoreboard Class ---
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 180)
        self.color("black")
        self.round = 1
        self.scores = {}  # leaderboard
        self.update_display()

    def update_display(self):
        self.clear()
        leaderboard_text = " | ".join([f"{k}:{v}" for k, v in self.scores.items()])
        self.write(f"Round: {self.round}   {leaderboard_text}", align="center", font=("Arial", 12, "bold"))

    def update_score(self, winner):
        if winner not in self.scores:
            self.scores[winner] = 0
        self.scores[winner] += 1
        self.round += 1
        self.update_display()


race = False
screen = Screen()
screen.setup(width=500, height=450)

# --- NEW: Create scoreboard ---
scoreboard = Scoreboard()

# --- NEW: Leader display ---
leader_label = Turtle()
leader_label.hideturtle()
leader_label.penup()
leader_label.goto(-30, 150)
leader_label.color("black")
leader_label.write("Leader:", align="left", font=("Arial", 12, "bold"))

leader_display = Turtle()
leader_display.hideturtle()
leader_display.penup()
leader_display.goto(30, 150)
leader_display.color("black")
current_leader = None  # --- NEW: Track current leader to avoid unnecessary updates ---

# --- NEW: Function to update leader ---
def update_leader():
    if t_list:
        max_x = max(t.xcor() for t in t_list)
        leaders = [t for t in t_list if t.xcor() == max_x]
        if len(leaders) == 1:
            leader_name = leaders[0].name
        else:
            leader_name = "Tie"
        global current_leader
        if leader_name != current_leader:
            current_leader = leader_name
            leader_display.clear()
            leader_display.write(f"{leader_name}", align="left", font=("Arial", 12, "bold"))

# --- NEW: Turtle data with names and colors ---
turtles_data = [
    ("Speedy", "blue"),
    ("Flash", "red"),
    ("Bolt", "magenta"),
    ("Zoom", "orange"),
    ("Dash", "black"),
    ("Swift", "green"),
    ("Rapid", "cyan"),
    ("Quick", "violet")
]

positions = [100, 70, 40, 10, -20, -50, -80, -110]

while True:  # --- NEW: Loop for multiple rounds ---

    names = [name for name, color in turtles_data]
    user = screen.textinput(title="Make your bet",
                            prompt=f"Which turtle will win? {names}: ")

    if not user:
        break  # exit if user cancels

    user = user.strip().title()
    if user not in names:
        print("Invalid name entered!")
        continue
    else:
        race = True
        current_leader = None  # --- NEW: Reset current leader for new round ---

    # --- RESET turtles every round ---
    t_list = []
    for i, (name, color) in enumerate(turtles_data):
        t = Turtle(shape="turtle")
        t.penup()
        t.color(color)
        t.name = name
        t.goto(x=-230, y=positions[i])
        t.write(name, align="left", font=("Arial", 10, "normal"))
        t_list.append(t)

    finish_line = Turtle()
    finish_line.hideturtle()
    finish_line.penup()
    finish_line.goto(230, 125)
    finish_line.right(90)
    finish_line.pendown()
    finish_line.pensize(4)
    for _ in range(12):
        finish_line.forward(10)
        finish_line.penup()
        finish_line.forward(10)
        finish_line.pendown()

    if race:
        while race:
            for turtle in t_list:
                if turtle.xcor() > 230:
                    race = False
                    winning_name = turtle.name

                    # --- NEW: Update scoreboard ---
                    scoreboard.update_score(winning_name)

                    # --- NEW: Celebration animation ---
                    turtle.color("gold")  # change winner turtle color to gold
                    for _ in range(36):  # spin 36 times
                        turtle.right(10)
                        time.sleep(0.05)  # slight delay for spinning effect

                    if winning_name == user:
                        print(f"🎉 Congrats! '{winning_name}' won!")
                    else:
                        print(f"😢 You lost. Winner: '{winning_name}'")

                    break

                turtle.forward(random.randint(0, 10))
                update_leader()  # --- NEW: Update leader after each move ---

    # --- CLEANUP turtles for next round ---
    for t in t_list:
        t.clear()  # clear the name
        t.hideturtle()
    leader_display.clear()  # --- NEW: Clear leader display ---

screen.exitonclick()

