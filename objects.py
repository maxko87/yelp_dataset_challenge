class YelpObject(object):

    def __str__(self):
        return self.__repr__()

    def __unicode__(self):
        return self.__unicode__()

class User(YelpObject):
    
    def __init__(self, user_id=None, name=None, review_count=None, average_stars=None, votes=None):
        self.user_id = user_id
        self.name = name
        self.review_count = review_count
        self.average_stars = average_stars
        self.votes = votes

    def __repr__(self):
        try:
            return "User " + str(self.name) + " (" + str(self.user_id).decode('utf-8') + ")"
        except:
            return "User"

class Business(YelpObject):
    
    def __init__(self, business_id=None, name=None, neighborhoods=None, average_stars=None, full_address=None, city=None, state=None, latitude=None, longitude=None, stars=None, review_count=None, categories=None, open_=None):
        self.business_id = business_id
        self.name = name
        self.neighborhoods = neighborhoods
        self.average_stars = average_stars
        self.full_address = full_address
        self.city = city
        self.state = state
        self.latitude = latitude
        self.longitude = longitude
        self.stars = stars
        self.review_count = review_count
        self.categories = categories
        self.open = open_

    def __repr__(self):
        try:
            return "Business " + str(self.name) + " (" + self.business_id.decode('utf-8') + ")"
        except:
            return "Business"

class Review(YelpObject):
    
    def __init__(self, business_id=None, user_id=None, stars=None, text=None, date=None, votes=None, get_text=True):
        self.business_id = business_id
        self.user_id = user_id
        self.stars = stars
        self.date = date
        self.votes = votes
        if get_text:
            self.text = text

    def __repr__(self):
        try:
            return "Review of " + str(self.business_id) + " by " + str(self.user_id)
        except:
            return "Review"
        
class Checkin(YelpObject):
    
    def __init__(self, business_id=None, checkin_info=None):
        self.business_id = business_id
        self.checkin_info = checkin_info

    def __repr__(self):
        try:
            return "Checkins for " + str(self.business_id)
        except:
            return "Checkin"
