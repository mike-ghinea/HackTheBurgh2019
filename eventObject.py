class venueObject:
  def __init__(self, json):
    self.name = json['name']
    self.code = json['code']
    self.description = json['description']
    self.address = json['address']
    self.post_code = json['post_code']
    self.phone = json['phone']
    self.email = json['email']
    self.disabled_desc = json['disabled_description']
    self.has_booking_over_phone = json['has_booking_over_phone']
    self.has_booking_over_card = json['has_booking_over_card']
    self.has_booking_over_web = json['has_booking_over_web']
    self.box_office_opening = json['box_office_opening']
    self.box_office_fringe = json['box_office_fringe']
    self.has_bar = json['has_bar']
    self.has_cafe = json['has_cafe']
    self.cafe_description = json['cafe_description']    
    self.web_address = json['web_address']
    self.position = json['position']

class discounts:
  def __init__(self, json):
    self.friends = json['friends'] 
    self.group = json['group']
    self.passport = json['passport']
    self.schools = json['schools']
    self.two_for_one = json['two_for_one']

  def __repr__(self):
    discounts_available = ""

    if self.friends == True:
      discounts_available += 'friends '
    if self.group == True:
      discounts_available += 'group '
    if self.passport == True:
      discounts_available += 'passport '    
    if self.schools == True:
      discounts_available += 'schools '
    if self.two_for_one == True:
      discounts_available += 'two_for_one '

    if len(discounts_available) == 0:
      return "None"
    else:
      return discounts_available

class eventObject:
  def __init__(self, json):
    self.age_category = json['age_category']
    self.artist       = json['artist']
    self.artist_type  = json['artist_type']
    self.code         = json['code']
    self.country      = json['country']
    self.description  = json['description']
    self.discounts    = discounts(json['discounts'])
    self.description_teaser = json['description_teaser']
    self.festival     = json['festival']
    self.festival_id  = json['festival_id']
    self.genre        = json['genre']
    self.genre_tags   = json['genre_tags']
    self.latitude     = json['latitude']
    self.longitude    = json['longitude']
    self.non_english  = json['non_english']
    self.performances = json['performances']
    self.venue        = venueObject(json['venue'])
    self.website      = json['website']
    self.title        = json['title'] 

  def __repr__(self):
    return """
    Title       : %s
    Age Category: %s
    Arist       : %s
    Country     : %s
    Description : %s
    Festival    : %s

    Discounts   : %s
    """%(self.title, self.age_category, self.artist, self.country, self.description_teaser, self.festival, self.discounts)