from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts

details = {
    'url' : 'http://turtleprize.com/xmlrpc.php',
    'user' : "entryrobot",
    'pass' : "$jx9ajsD",
    }

def test_wp():
    wp = Client(details['url'],details['user'],details['pass'])
    print(wp.call(GetPosts()))
    print(wp.call(GetUserInfo()))

def wp_upload(code):
    print("uploading media")
    wp = Client(details['url'],details['user'],details['pass'])
    # set to the path to your file

    # prepare metadata
    data = {
            'name': 'picture.jpg',
            'type': 'image/jpg',  # mimetype
    }

    # read the binary file and let the XMLRPC library encode it into base64
    with open(code['png_file'], 'rb') as img:
            data['bits'] = xmlrpc_client.Binary(img.read())

    response = wp.call(media.UploadFile(data))
    return response

def wp_post(image,code):
    print("making post")
    wp = Client(details['url'],details['user'],details['pass'])
    post = WordPressPost()
    post.title = "%s from %s" % (code['name'],code['school'])
    img_code = '<a href="%s"><img class="alignnone size-medium wp-image-8" alt="turtle pic" src="%s" width="100%%"/></a>' % ( image['url'],image['url'])
    post.content = '''
<strong>Author</strong> %s<br>
<strong>School</strong> %s<br>
%s
<strong>Code</strong><br>
<pre class="dontquote prettyprint">
%s
</pre>
''' % (code['name'],code['school'],img_code,code['text'])
    #post.thumbnail = image['id']
    post.post_status = 'publish'
    post.terms_names = {
        'post_tag': ['teacher'],
        'category': ['competition entry']
    }
    response = wp.call(NewPost(post))
    print(response)

import pickle
code = pickle.load( open( "save.p", "rb" ) )
image = wp_upload(code)
wp_post(image,code)
