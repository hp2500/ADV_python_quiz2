from media_feed import *
import sys


def test_play_media(): 
    """
    Test whether playing media adds it to the feed.
    """
    
    Mov = Movie("Fight Club", 1999)
    Son = Song("Hello", 1999, "MM", "Nope", 1)
    Pod = Podcast("JRE", 2022, 200, "Dumb Shit")
    
    usr = User("Heinrich")
    
    usr.play(Pod)
    usr.play(Mov)
    usr.play(Son)
    
    # assert that three different media types can be added 
    assert len(usr.feed) == 3
    
    # assert that time stamp is added 
    assert usr.feed[0].timestamp != None

    
def test_common_media(): 
    """
    Test whether whether common media can be found between two users. 
    """
    
    Mov = Movie("Fight Club", 1999)
    Son = Song("Hello", 1999, "MM", "Nope", 1)
    Pod = Podcast("JRE", 2022, 200, "Dumb Shit")
    Pod2 = Podcast("Lex Fridman", 2022, 200, "Smart Shit")

    
    usr = User("Heinrich")
    
    usr.play(Pod)
    usr.play(Mov)
    
    usr2 = User("Julian")
    usr2.play(Son)
    usr2.play(Mov)
    usr2.play(Pod2)


    common = usr.common_media(usr2)
    
    # assert that users have one piece of content in common
    assert len(common) == 1
    
    
def test_render_feed():
    """
    Test whether render_feed produces correct string.
    """
    
    Mov = Movie("Fight Club", 1999)
    Son = Song("Hello", 1999, "MM", "Nope", 1)
    Pod = Podcast("JRE", 2022, 200, "Dumb Shit")
    
    usr = User("Heinrich")
    
    usr.play(Mov)
    usr.play(Son)
    usr.play(Pod)
    
    rendered_string = usr.render_feed()
    
    # assert corretness of rendered string
    assert rendered_string == (f'JRE (2022), 200, Dumb Shit, {usr.feed[0].timestamp}\n'
                               f'Hello (1999), MM, Nope, 1, {usr.feed[1].timestamp}\n'
                               f'Fight Club (1999), {usr.feed[2].timestamp}\n')
    
    
