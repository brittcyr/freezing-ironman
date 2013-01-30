import optparse
import login
import parse_page
from make_selection import make_selection

def streak_for_cash():

    parser = optparse.OptionParser("usage%proj -u <username> \
            -p <password>")
    parser.add_option('-u', dest='username', type='string', \
            help='ESPN.com username')
    parser.add_option('-p', dest='password', type='string', \
            help='ESPN.com password')

    (options, args) = parser.parse_args()
    username = options.username
    password = options.password

    (browser, streak_page) = login.get_streak_page(username, password)
    matchups = parse_page.get_matchups(streak_page)

    if 'Your Pending Pick' in streak_page or len(matchups) == 0:
        # we currently have a pick right now and need to wait
        print 'PICK IS PENDING'
        return

    result_page = make_selection(browser, matchups)

    if 'Your Pending Pick' in result_page:
        print 'SUCCESS'
    else:
        print 'FAILURE'

if __name__ == '__main__':
    streak_for_cash()
