class User():
    
    def __init__(self, user_id=None, name=None, review_count=None, average_stars=None, votes=None):
        self.user_id = user_id
        self.name = name
        self.review_count = review_count
        self.average_stars = average_stars
        self.votes = votes

    def __repr__(self):
        return "User " + str(self.name) + " (" + str(self.user_id).decode('utf-8') + ")"

class Business():
    
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
        return "Business " + self.name.decode('utf-8') #+ " (" + self.business_id.decode('utf-8') + ")"

class Review():
    
    def __init__(self, business_id=None, user_id=None, stars=None, text=None, date=None, votes=None):
        self.business_id = business_id
        self.user_id = user_id
        self.stars = stars
        self.text = text
        self.date = date
        self.votes = votes

    def __repr__(self):
        return "Review of " + str(self.business_id) + " by " + str(self.user_id)
        
class Checkin():
    
    def __init__(self, business_id=None, checkin_info=None):
        self.business_id = business_id
        self.checkin_info = checkin_info

    def __repr__(self):
        return "Checkins for " + str(self.business_id)
