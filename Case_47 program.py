def main():
    n = int(input("Number of teams: "))
    teams = {}
    for _ in range(n):
        name = input("Team name: ").strip()
        teams[name] = {"points": 0, "gf": 0, "ga": 0}

    matches = int(input("Number of matches: "))
    for i in range(matches):
        a = input(f"Match {i + 1} home team: ").strip()
        b = input("Away team: ").strip()
        if a not in teams or b not in teams or a == b:
            print("Invalid team selection; match ignored.")
            continue
        ga = int(input("Home goals: "))
        gb = int(input("Away goals: "))
        if ga < 0 or gb < 0:
            print("Negative goals are invalid; match ignored.")
            continue
        teams[a]["gf"] += ga
        teams[a]["ga"] += gb
        teams[b]["gf"] += gb
        teams[b]["ga"] += ga
        if ga > gb:
            teams[a]["points"] += 3
        elif gb > ga:
            teams[b]["points"] += 3
        else:
            teams[a]["points"] += 1
            teams[b]["points"] += 1

    ranking = sorted(teams.items(),
                     key=lambda item: (-item[1]["points"],
                                       -(item[1]["gf"] - item[1]["ga"]),
                                       item[0].lower()))
    print("\nRANK  TEAM                 PTS  GF  GA  GD")
    for rank, (name, stat) in enumerate(ranking, 1):
        gd = stat["gf"] - stat["ga"]
        print(f"{rank:<5} {name:<20} {stat['points']:<4} {stat['gf']:<3} {stat['ga']:<3} {gd}")

if __name__ == "__main__":
    main()
