import mechanize
import cookielib

def get_streak_page(username, password):
    browser = mechanize.Browser(factory=mechanize.RobustFactory())

    # Cookie Jar
    cj = cookielib.LWPCookieJar()
    browser.set_cookiejar(cj)

    # Browser options
    browser.set_handle_equiv(True)
    browser.set_handle_gzip(True)
    browser.set_handle_redirect(True)
    browser.set_handle_referer(True)
    browser.set_handle_robots(False)

    # Follows refresh 0 but not hangs on refresh > 0
    browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

    # User-Agent (this is cheating, ok?)
    browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; \
            en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    browser.open("https://r.espn.go.com/members/login")

    browser.select_form(nr=2)

    # User credentials
    browser.form['username'] = username
    browser.form['password'] = password

    # Login
    browser.submit()

    # Go to the streak for the cash page
    page = browser.open("http://streak.espn.go.com/en/entry").read()

    return (browser, page)
