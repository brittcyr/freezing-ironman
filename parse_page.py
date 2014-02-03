from BeautifulSoup import BeautifulSoup

def get_matchups(page):
    soup = BeautifulSoup(page)

    # A matchup is a tuple of (time, team1 %, team2 %, team1 link, team2 link)
    matchups = []

    for matchup_div in soup.findAll("div", { "class":"matchup-container" }):
        try:
            table = matchup_div.findAll("table", {"class":"mg-gametableQ"})

            if not table:
                continue

            table = table[0]

            time_tag = table.findAll("div", {"class":"matchupDate"})[0]
            time_unformatted = str(time_tag.findAll(text=True)[0])

            team1_percent_tag = table.findAll("td", {"class":"mg-column6 wpw"})[0]
            team1_percent_tag = team1_percent_tag.findAll("span", {"class":"wpw"})[0]
            team1_percent_unformatted = str(team1_percent_tag.findAll(text=True)[0])

            team2_percent_tag = table.findAll("td", {"class":"mg-column6 wpw"})[1]
            team2_percent_tag = team2_percent_tag.findAll("span", {"class":"wpw"})[0]
            team2_percent_unformatted = str(team2_percent_tag.findAll(text=True)[0])

            team1_link_tag = table.findAll("td", {"class":"mg-column8 pick borderRight "})[0]
            team1_link_tag = team1_link_tag.findAll("a", {"class":"mg-check mg-checkEmpty"})[0]
            team1_link_unformatted = str(list(team1_link_tag.attrs[3])[1])

            team2_link_tag = table.findAll("td", {"class":"mg-column8 pick borderRight  last"})[0]
            team2_link_tag = team2_link_tag.findAll("a", {"class":"mg-check mg-checkEmpty"})[0]
            team2_link_unformatted = str(list(team2_link_tag.attrs[3])[1])

            matchups.append((time_unformatted, team1_percent_unformatted, \
                   team2_percent_unformatted, team1_link_unformatted,  \
                   team2_link_unformatted))
        except Exception as e:
            # This is where we look at a link already past due
            continue

    return matchups

def get_matchup(page):
    soup = BeautifulSoup(page)
    matchup = soup.find("table", { "class":"mg-gametableQ mg-gametableQYlw" })
    return matchup
