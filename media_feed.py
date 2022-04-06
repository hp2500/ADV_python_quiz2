from datetime import datetime

class Movie: 
    """
    Instance represents an individual Movie. 
    """
    
    def __init__(self, name, year, timestamp=None):
         
        self.name = name
        self.year = year
        self.timestamp = timestamp
        
    def __str__(self):
        
        str_str = (f"{self.name} "
                   f"({self.year}), " 
                   f"{self.timestamp}" 

                  )
        
        return str_str
        
        
    def __repr__(self):
        
        repr_str = (f'<Media(name="{self.name}", year="{self.year}")>')

        return repr_str

    
class Song:
    """
    Instance represents an individual Song. 
    """
    
    def __init__(self, name, year,  artist, album, track, timestamp=None,):
        self.name = name
        self.year = year
        self.artist = artist
        self.album = album
        self.track = track
        self.timestamp = timestamp


        
    def __str__(self):
        
        str_str = (f"{self.name} "
                   f"({self.year}), "
                   f"{self.artist}, " 
                   f"{self.album}, " 
                   f"{self.track}, "
                   f"{self.timestamp}")
        
        return str_str
        
        
    def __repr__(self):
        
        repr_str = (f'<Media(name="{self.name}", year="{self.year}", artist="{self.artist}", album="{self.album}", track="{self.track}", timestamp="{self.timestamp}")>')

        return repr_str
    
    
class Podcast:
    """
    Instance represents an individual Podcast. 
    """
    
    def __init__(self, name, year, ID, ep_name, timestamp=None,):
        self.name = name
        self.year = year
        self.ID = ID
        self.ep_name = ep_name
        self.timestamp = timestamp

    def __str__(self):
        
        str_str = (f"{self.name} "
                   f"({self.year}), "
                   f"{self.ID}, " 
                   f"{self.ep_name}, " 
                   f"{self.timestamp}" 
                  )
        
        return str_str
        
        
    def __repr__(self):
        
        repr_str = (f'<Media(name="{self.name}", year="{self.year}", ID="{self.ID}", ep_name="{self.ep_name}", timestamp="{self.timestamp}")>')

        return repr_str
            

class User:
    """
    Instance a user with a unique feed.
    """
    
    def __init__(self, name): 
        
        self.feed = []
        self.name = name
        
        
    def __str__(self):
        
        str_str = ""
        
        for i in self.feed: 
            
            str_str = str_str+i.__str__()+"\n"
        
        return str_str
    
    
    def play(self, media):
        """Add piece of media content to feed."""
        
        now = datetime.now()
        timestamp = now.strftime("%m/%d/%Y, %H:%M:%S")
        
        setattr(media, "timestamp", timestamp)
        
        self.feed.insert(0, media)
        
    def render_feed(self):
        """Print user's media feed."""
                
        return str(self)
        
        
    def common_media(self, other):
        """Compare user's media feed with other user and print common content."""
        
        return list(set(self.feed).intersection(other.feed))
        