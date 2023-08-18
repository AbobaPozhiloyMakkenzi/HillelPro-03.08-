team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Kevin", "age": 17, "number": 12},
]


def show_players(players):
    player_list = []
    for i in players:
        try:
            player_list.append(i)
        except Exception as e:
            raise print(e)
    return player_list


def add_player(num, name, age):
    team.append({"name": name, "age": age, "number": num})


def remove_player(players, num):
    for idx, i in reversed(list(enumerate(players))):
        print(idx, i)
        if i["number"] == num:
            team.pop(idx)


def main():
    print(show_players(team))

    add_player(num=17, name="Cris", age=31)
    add_player(num=17, name="Dave", age=44)
    add_player(num=17, name="Batista", age=44)
    print(show_players(team))
    remove_player(players=team, num=17)
    print(show_players(team))


if __name__ == "__main__":
    main()
else:
    raise SystemExit("This module in only for running")
