from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo

details = {
    'url' : 'http://turtleprize.com/xmlrpc.php',
    'user' : "entryrobot",
    'pass' : "$jx9ajsD",
    }

def test_wp():
    wp = Client(details['url'],details['user'],details['pass'])
    print(wp.call(GetPosts()))
    print(wp.call(GetUserInfo()))

def wp_post():
    wp = Client(details['url'],details['user'],details['pass'])
    post = WordPressPost()
    post.title = 'My new title'
    post.content = 'This is the body of my new post.'
    post.terms_names = {
        'post_tag': ['test', 'teacher'],
        'category': ['entries']
    }
    wp.call(NewPost(post))

wp_post()
test_wp()
