from bottle import route, run, get, post, request, static_file
import twitterapi
import WebpageFormatter

@get('/index') # or @route('/login')
def index():
    return '''
        <form action="/userinput" method="post">
            User1 Twitter Handle: <input name="user1twittername" type="text" />
            User2 Twitter Handle: <input name="user2twittername" type="text" />
            <input value="Submit" type="submit" />
        </form>
    '''

@post('/userinput')
def index():
	user1twitterinfo = twitterapi.getAPIInfo(request.forms.get('user1twittername'));
	user2twitterinfo = twitterapi.getAPIInfo(request.forms.get('user2twittername'));
	return WebpageFormatter.getFormattedWebpage(user1twitterinfo, user2twitterinfo);
	
@route('/html/:path#.+#', name='html')
def static(path):
    return static_file(path, root='html')

run(host='localhost', port=8080, debug=True)