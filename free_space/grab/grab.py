
with open("data.txt", "r") as f:
    for line in f:
        type = line.split("(")[0]
        scoreHome = line.split("_")[2]
        scoreAway = line.split("_")[3].split("(")[0]
        m = f"addResulter(EOutcomeType.{type}, new CorrectScoreResulter(Period.FULLTIME, {scoreHome}, {scoreAway}));"
        print(m)
