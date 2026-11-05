import random

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.funny_guy = False


class GameManager:


    def __init__(self):
        self.players = {}

    def add_player(self, player):
        self.players[player.name] = player

    def print_players(self):
        player_count = 1
        for player_name, player in self.players.items():
            print(f"Player: {player_count}, Name: {player_name}, Score: {player.score}")
            player_count += 1

    def roundsToPlay(self,rounds):
        self.rounds = rounds
        return self.rounds

    def gameState(self, rounds):
        self.state = 0
        self.rounds = rounds
        while self.state < self.rounds:
            print(f"Round {self.state + 1} of {self.rounds}")
            game_par = random.randint(3, 5)
            print(f"Hole {self.state + 1} is Par {game_par} ")
            for player_name,player in self.players.items():
                score = int(input(f"Enter strokes for {player_name}: "))
                roundResult = self.determine_performance(game_par, score, player)
                if player.funny_guy:
                    print(f"{player_name} completed the hole in {score} strokes....{roundResult}")
                    score = 10
                    player.score += score
                else:
                    print(f"{player_name} completed the hole in {score} strokes.\n {player_name}'s score this round is a {roundResult}.\n")
                    player.score += score - game_par
                player.funny_guy = False
            self.state += 1
            for player_name, player in self.players.items():
                print(f"{player_name}'s total score after round {self.state} is {player.score}.")
            input("Press Enter to continue to the next round...\n")

   
    def determine_performance(self, par, strokes,player):
        while True:
            if strokes <= 0:
                player.funny_guy = True
                return("Yeah Sure...+10 has been added to your score..funny guy")
            elif par - 4 == strokes:
                return("Condor")
            elif par - 3 == strokes:
                if par == 3:
                    return("Hole in One!")
                else:
                    return("Albatross")
            elif par - 2 == strokes:
                return("Eagle")
            elif par - 1 == strokes:
                return("Birdie")
            elif strokes == par:
                return("Par")
            elif par +1 == strokes:
                return("Bogey")
            elif par + 2 == strokes:
                return("Double Bogey")
            elif par + 3 == strokes:
                return("Triple Bogey")
            else:
                return("+" + str(strokes - par))
        