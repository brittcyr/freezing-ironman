

def make_selection(browser, matchups):
    list_of_matchups = []
    # 1. Format the input

    # A matchup is a tuple of (time, team1 %, team2 %, team1 link, team2 link)
    for matchup in matchups:
        m = [0]*5

        time_string = matchup[0]
        hour = int(time_string.split(':')[0])
        mins = int(time_string.split(':')[1][:2])
        m[0] = [hour, mins]

        p1_string = matchup[1]
        p1 = p1_string.split('%')[0]
        m[1] = p1

        p2_string = matchup[2]
        p2 = p2_string.split('%')[0]
        m[2] = p2
        m[3] = matchup[3]
        m[4] = matchup[4]
        list_of_matchups.append(m)


    # 2. Pick the matchup

    matchups = list_of_matchups

    # First prune by time
    for matchup in matchups:
        if matchup[0][0] > matchups[0][0][0]:
            # remove all matchups that arent in the same hour
            matchups.remove(matchup)
        if matchup[0][1] > matchups[0][0][1] + 15:
            # remove all matchups not within 15 minutes
            matchups.remove(matchup)

    best_odds = 0
    best_team = None
    for matchup in matchups:
        if matchup[1] > best_odds:
            best_odds = matchup[1]
            best_team = matchup[3]
        if matchup[2] > best_odds:
            best_odds = matchup[2]
            best_team = matchup[4]

    # 3. Submit the pick

#page = browser.open("http://streak.espn.go.com/createOrUpdateEntry?matchup=m22505o25208").read()

    site = "http://streak.espn.go.com/"
    site += best_team
    page = browser.open(site).read()

    return page
