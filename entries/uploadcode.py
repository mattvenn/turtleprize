from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts

from simplegist import Simplegist
import secrets

def test_wp():
    wp = Client(secrets.wp_url,secrets.wp_user,secrets.wp_pass)
    print(wp.call(GetPosts()))
    print(wp.call(GetUserInfo()))

def wp_upload(config):
    print("uploading media")
    wp = Client(secrets.wp_url,secrets.wp_user,secrets.wp_pass)
    # set to the path to your file

    # prepare metadata
    data = {
            'name': 'picture.jpg',
            'type': 'image/jpg',  # mimetype
    }

    # read the binary file and let the XMLRPC library encode it into base64
    with open(config['png_file'], 'rb') as img:
            data['bits'] = xmlrpc_client.Binary(img.read())

    response = wp.call(media.UploadFile(data))
    return response

def wp_post(image,config):
    print("making post")
    wp = Client(secrets.wp_url,secrets.wp_user,secrets.wp_pass)
    post = WordPressPost()
    post.title = "%s from %s" % (config['name'],config['school'])
    img_code = '<a href="%s"><img class="alignnone size-medium wp-image-8" alt="turtle pic" src="%s" width="100%%"/></a>' % ( image['url'],image['url'])
    post.content = '''
<strong>Author</strong> %s<br>
<strong>School</strong> %s<br>
%s
<strong>Code</strong><br>
[gist id=%s]
''' % (config['name'],config['school'],img_code,config['gist_id'])
    post.thumbnail = image['id']
    post.post_status = 'publish'
    post.terms_names = {
        'post_tag': ['teacher'],
        'category': ['competition entry']
    }
    response = wp.call(NewPost(post))
    print(response)

def gist_post(config):
    print("posting gist")
    GHgist = Simplegist(username=secrets.user,api_token=secrets.token)
    # creating gist and returning url, script, clone link
    desc = 'Author: %s, School: %s' % (config['name'],config['school'])
    result = GHgist.create(name='turtleprize.com competition entry', description=desc, public=1, content=config['text'])
    config['gist_id'] = result['id'] 
    print("id=" + config['gist_id'])

import pickle
config = pickle.load( open( "save.p", "rb" ) )
image = wp_upload(config)
gist_id = gist_post(config)
wp_post(image,config)
