import http.cookiejar
import urllib
import urllib3
import configparser

# set these to whatever your fb account is


config = configparser.ConfigParser()
config.read('souperssl.cfg')
fb_username = config['login']['user']
fb_password  = config['login']['passwd']
myurl = config['login']['myurl']


class WebGamePlayer(object):

    def __init__(self, login, password):
        """ Start up... """
        self.login = login
        self.password = password

        self.cj = http.cookieJar()
        self.opener = urllib2.build_opener(
            urllib2.HTTPRedirectHandler(),
            urllib2.HTTPHandler(debuglevel=0),
            urllib2.HTTPSHandler(debuglevel=0),
            urllib2.HTTPCookieProcessor(self.cj)
        )
        self.opener.addheaders = [
            ('User-agent', ('Mozilla/4.0 (compatible; MSIE 6.0; '
                           'Windows NT 5.2; .NET CLR 1.1.4322)'))
        ]

        # need this twice - once to set cookies, once to log in...
        self.loginToFacebook()
        self.loginToFacebook()

    def loginToFacebook(self):
        """
        Handle login. This should populate our cookie jar.
        """
        login_data = urllib.urlencode({
            'SWEUserName' : self.login,
            'SWEPassword' : self.password,
        })
        response = self.opener.open(myurl, login_data)
        return ''.join(response.readlines())