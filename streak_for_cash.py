#!/usr/bin/python
import optparse
import login
import parse_page
from make_selection import make_selection

def streak_for_cash():
    # Parse the username and password
    parser = optparse.OptionParser("usage%proj -u <username> \
            -p <password>")
    parser.add_option('-u', dest='username', type='string', \
            help='ESPN.com username')
    parser.add_option('-p', dest='password', type='string', \
            help='ESPN.com password')

    (options, args) = parser.parse_args()
    username = options.username
    password = options.password


    # Login
    (browser, streak_page) = login.get_streak_page(username, password)


    # Get the matchups
    matchups = parse_page.get_matchups(streak_page)

    # Check if there are any matchups to choose from
    if len(matchups) == 0:
        # we currently have a pick right now and need to wait
        print 'PICK IS PENDING'
        return

    # Make the pick
    result_page = make_selection(browser, matchups)

    if 'Your Pending Pick' in result_page:
        print '<html>'
        print parse_page.get_matchup(result_page)
        print '</html>'
    else:
        print 'FAILURE'

if __name__ == '__main__':
    streak_for_cash()
