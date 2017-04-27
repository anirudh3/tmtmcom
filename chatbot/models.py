from django.db import models

# User class for built-in authentication module
from django.contrib.auth.models import User

locations = (
        ( '0', 'Birmingham, ALABAMA'),
        ( '1', 'Dothan, ALABAMA'),
        ( '2', 'Huntsville, ALABAMA'),
        ( '3', 'Mobile, ALABAMA'),
        ( '4', 'Montgomery, ALABAMA'),
        ( '5', 'Anchorage, ALASKA'),
        ( '6', 'Aniak, ALASKA'),
        ( '7', 'Barrow, ALASKA'),
        ( '8', 'Bethel, ALASKA'),
        ( '9', 'Cordova, ALASKA'),
        ( '10', 'Deadhorse / Prudhoe Bay, ALASKA'),
        ( '11', 'Dillingham, ALASKA'),
        ( '12', 'Fairbanks, ALASKA'),
        ( '13', 'Galena, ALASKA'),
        ( '14', 'Gustavus, ALASKA'),
        ( '15', 'Homer, ALASKA'),
        ( '16', 'Hoonah, ALASKA'),
        ( '17', 'Juneau, ALASKA'),
        ( '18', 'Kenai, ALASKA'),
        ( '19', 'Ketchikan, ALASKA'),
        ( '20', 'King Salmon, ALASKA'),
        ( '21', 'Kodiak, ALASKA'),
        ( '22', 'Kotzebue, ALASKA'),
        ( '23', 'Nome, ALASKA'),
        ( '24', 'Petersburg, ALASKA'),
        ( '25', 'Sitka, ALASKA'),
        ( '26', 'St. Mary\'s, ALASKA'),
        ( '27', 'Unalakleet, ALASKA'),
        ( '28', 'Unalaska, ALASKA'),
        ( '29', 'Valdez, ALASKA'),
        ( '30', 'Wrangell, ALASKA'),
        ( '31', 'Yakutat, ALASKA'),
        ( '32', 'Bullhead City, ARIZONA'),
        ( '33', 'Flagstaff, ARIZONA'),
        ( '34', 'Grand Canyon / Tusayan, ARIZONA'),
        ( '35', 'Mesa, ARIZONA'),
        ( '36', 'Page, ARIZONA'),
        ( '37', 'Peach Springs 1G4, ARIZONA'),
        ( '38', 'Phoenix, ARIZONA'),
        ( '39', 'Tucson, ARIZONA'),
        ( '40', 'Yuma, ARIZONA'),
        ( '41', 'Fayetteville, ARKANSAS'),
        ( '42', 'Fort Smith, ARKANSAS'),
        ( '43', 'Little Rock, ARKANSAS'),
        ( '44', 'Texarkana, ARKANSAS'),
        ( '45', 'Arcata / Eureka, CALIFORNIA'),
        ( '46', 'Bakersfield, CALIFORNIA'),
        ( '47', 'Burbank, CALIFORNIA'),
        ( '48', 'Carlsbad, CALIFORNIA'),
        ( '49', 'Chico, CALIFORNIA'),
        ( '50', 'Crescent City, CALIFORNIA'),
        ( '51', 'Fresno, CALIFORNIA'),
        ( '52', 'Long Beach, CALIFORNIA'),
        ( '53', 'Los Angeles, CALIFORNIA'),
        ( '54', 'Mammoth Lakes, CALIFORNIA'),
        ( '55', 'Modesto, CALIFORNIA'),
        ( '56', 'Monterey, CALIFORNIA'),
        ( '57', 'Oakland, CALIFORNIA'),
        ( '58', 'Ontario, CALIFORNIA'),
        ( '59', 'Palm Springs, CALIFORNIA'),
        ( '60', 'Redding, CALIFORNIA'),
        ( '61', 'Sacramento, CALIFORNIA'),
        ( '62', 'San Diego, CALIFORNIA'),
        ( '63', 'San Francisco, CALIFORNIA'),
        ( '64', 'San Jose, CALIFORNIA'),
        ( '65', 'San Luis Obispo, CALIFORNIA'),
        ( '66', 'Santa Ana, CALIFORNIA'),
        ( '67', 'Santa Barbara, CALIFORNIA'),
        ( '68', 'Santa Maria, CALIFORNIA'),
        ( '69', 'Santa Rosa, CALIFORNIA'),
        ( '70', 'Stockton, CALIFORNIA'),
        ( '71', 'Aspen, COLORADO'),
        ( '72', 'Colorado Springs, COLORADO'),
        ( '73', 'Denver, COLORADO'),
        ( '74', 'Durango, COLORADO'),
        ( '75', 'Eagle, COLORADO'),
        ( '76', 'Grand Junction, COLORADO'),
        ( '77', 'Gunnison, COLORADO'),
        ( '78', 'Hayden, COLORADO'),
        ( '79', 'Montrose, COLORADO'),
        ( '80', 'Hartford, CONNECTICUT'),
        ( '81', 'New Haven, CONNECTICUT'),
        ( '82', 'Daytona Beach, FLORIDA'),
        ( '83', 'Fort Lauderdale, FLORIDA'),
        ( '84', 'Fort Myers, FLORIDA'),
        ( '85', 'Gainesville, FLORIDA'),
        ( '86', 'Jacksonville, FLORIDA'),
        ( '87', 'Key West, FLORIDA'),
        ( '88', 'Melbourne, FLORIDA'),
        ( '89', 'Miami, FLORIDA'),
        ( '90', 'Orlando, FLORIDA'),
        ( '91', 'Panama City Beach, FLORIDA'),
        ( '92', 'Pensacola, FLORIDA'),
        ( '93', 'Punta Gorda, FLORIDA'),
        ( '94', 'Sarasota / Bradenton, FLORIDA'),
        ( '95', 'St. Augustine, FLORIDA'),
        ( '96', 'St. Petersburg/Clearwater, FLORIDA'),
        ( '97', 'Tallahassee, FLORIDA'),
        ( '98', 'Tampa, FLORIDA'),
        ( '99', 'Valparaiso, FLORIDA'),
        ( '100', 'West Palm Beach, FLORIDA'),
        ( '101', 'Albany, GEORGIA'),
        ( '102', 'Atlanta, GEORGIA'),
        ( '103', 'Augusta, GEORGIA'),
        ( '104', 'Brunswick, GEORGIA'),
        ( '105', 'Columbus, GEORGIA'),
        ( '106', 'Savannah, GEORGIA'),
        ( '107', 'Valdosta, GEORGIA'),
        ( '108', 'Hilo, Hawaii, HAWAII'),
        ( '109', 'Honolulu, Oahu, HAWAII'),
        ( '110', 'Kahului, Maui, HAWAII'),
        ( '111', 'Kailua-Kona, Hawaii, HAWAII'),
        ( '112', 'Kaunakakai, Molokai, HAWAII'),
        ( '113', 'Lanai City, Lanai, HAWAII'),
        ( '114', 'Lihue, Kauai, HAWAII'),
        ( '115', 'Boise, IDAHO'),
        ( '116', 'Hailey, IDAHO'),
        ( '117', 'Idaho Falls, IDAHO'),
        ( '118', 'Lewiston, IDAHO'),
        ( '119', 'Pocatello / Arbon Valley, IDAHO'),
        ( '120', 'Twin Falls, IDAHO'),
        ( '121', 'Belleville, ILLINOIS'),
        ( '122', 'Bloomington / Normal, ILLINOIS'),
        ( '123', 'Champaign / Urbana, ILLINOIS'),
        ( '124', 'Chicago, ILLINOIS'),
        ( '125', 'Chicago, ILLINOIS'),
        ( '126', 'Marion, ILLINOIS'),
        ( '127', 'Moline, ILLINOIS'),
        ( '128', 'Peoria, ILLINOIS'),
        ( '129', 'Quincy, ILLINOIS'),
        ( '130', 'Rockford, ILLINOIS'),
        ( '131', 'Springfield IL, ILLINOIS'),
        ( '132', 'Evansville, INDIANA'),
        ( '133', 'Fort Wayne, INDIANA'),
        ( '134', 'Indianapolis, INDIANA'),
        ( '135', 'South Bend, INDIANA'),
        ( '136', 'Cedar Rapids, IOWA'),
        ( '137', 'Des Moines, IOWA'),
        ( '138', 'Dubuque, IOWA'),
        ( '139', 'Sioux City, IOWA'),
        ( '140', 'Waterloo, IOWA'),
        ( '141', 'Garden City, KANSAS'),
        ( '142', 'Manhattan, KANSAS'),
        ( '143', 'Wichita, KANSAS'),
        ( '144', 'Cincinnati/Covington, KENTUCKY'),
        ( '145', 'Lexington, KENTUCKY'),
        ( '146', 'Louisville, KENTUCKY'),
        ( '147', 'Owensboro, KENTUCKY'),
        ( '148', 'Paducah, KENTUCKY'),
        ( '149', 'Alexandria, LOUISIANA'),
        ( '150', 'Baton Rouge, LOUISIANA'),
        ( '151', 'Lafayette, LOUISIANA'),
        ( '152', 'Lake Charles, LOUISIANA'),
        ( '153', 'Monroe, LOUISIANA'),
        ( '154', 'New Orleans, LOUISIANA'),
        ( '155', 'Shreveport, LOUISIANA'),
        ( '156', 'Bangor, MAINE'),
        ( '157', 'Bar Harbor, MAINE'),
        ( '158', 'Portland, MAINE'),
        ( '159', 'Presque Isle, MAINE'),
        ( '160', 'Rockland, MAINE'),
        ( '161', 'Baltimore / Glen Burnie, MARYLAND'),
        ( '162', 'Salisbury, MARYLAND'),
        ( '163', 'Hagerstown, MARYLAND'),
        ( '164', 'Boston, MASSACHUSETTS'),
        ( '165', 'Hyannis, MASSACHUSETTS'),
        ( '166', 'Nantucket, MASSACHUSETTS'),
        ( '167', 'Provincetown, MASSACHUSETTS'),
        ( '168', 'Vineyard Haven, MASSACHUSETTS'),
        ( '169', 'Worcester, MASSACHUSETTS'),
        ( '170', 'Alpena, MICHIGAN'),
        ( '171', 'Beaver Island 6Y8 Welke Airport P-N, MICHIGAN'),
        ( '172', 'Detroit / Romulus, MICHIGAN'),
        ( '173', 'Escanaba, MICHIGAN'),
        ( '174', 'Flint, MICHIGAN'),
        ( '175', 'Grand Rapids, MICHIGAN'),
        ( '176', 'Hancock / Calumet, MICHIGAN'),
        ( '177', 'Iron Mountain / Kingsford, MICHIGAN'),
        ( '178', 'Kalamazoo / Battle Creek, MICHIGAN'),
        ( '179', 'Lansing, MICHIGAN'),
        ( '180', 'Marquette / Gwinn, MICHIGAN'),
        ( '181', 'Muskegon, MICHIGAN'),
        ( '182', 'Pellston, MICHIGAN'),
        ( '183', 'Saginaw, MICHIGAN'),
        ( '184', 'Sault Ste. Marie, MICHIGAN'),
        ( '185', 'Traverse City, MICHIGAN'),
        ( '186', 'Bemidji, MINNESOTA'),
        ( '187', 'Brainerd, MINNESOTA'),
        ( '188', 'Duluth, MINNESOTA'),
        ( '189', 'Hibbing, MINNESOTA'),
        ( '190', 'International Falls, MINNESOTA'),
        ( '191', 'Minneapolis, MINNESOTA'),
        ( '192', 'Rochester, MINNESOTA'),
        ( '193', 'St. Cloud, MINNESOTA'),
        ( '194', 'Columbus / West Point / Starkville, MISSISSIPPI'),
        ( '195', 'Gulfport / Biloxi, MISSISSIPPI'),
        ( '196', 'Hattiesburg / Laurel, MISSISSIPPI'),
        ( '197', 'Jackson, MISSISSIPPI'),
        ( '198', 'Columbia, MISSOURI'),
        ( '199', 'Joplin, MISSOURI'),
        ( '200', 'Kansas City, MISSOURI'),
        ( '201', 'Springfield MI, MISSOURI'),
        ( '202', 'St. Louis, MISSOURI'),
        ( '203', 'Billings, MONTANA'),
        ( '204', 'Bozeman, MONTANA'),
        ( '205', 'Butte, MONTANA'),
        ( '206', 'Great Falls, MONTANA'),
        ( '207', 'Helena, MONTANA'),
        ( '208', 'Kalispell, MONTANA'),
        ( '209', 'Missoula, MONTANA'),
        ( '210', 'Grand Island, NEBRASKA'),
        ( '211', 'Kearney, NEBRASKA'),
        ( '212', 'Lincoln, NEBRASKA'),
        ( '213', 'Omaha, NEBRASKA'),
        ( '214', 'Scottsbluff, NEBRASKA'),
        ( '215', 'Boulder City, NEVADA'),
        ( '216', 'Elko, NEVADA'),
        ( '217', 'Las Vegas, NEVADA'),
        ( '218', 'Reno, NEVADA'),
        ( '219', 'Lebanon, NEW HAMPSHIRE'),
        ( '220', 'Manchester, NEW HAMPSHIRE'),
        ( '221', 'Portsmouth, NEW HAMPSHIRE'),
        ( '222', 'Atlantic City, NEW JERSEY'),
        ( '223', 'Trenton, NEW JERSEY'),
        ( '224', 'Newark, NEW JERSEY'),
        ( '225', 'Albuquerque, NEW MEXICO'),
        ( '226', 'Farmington, NEW MEXICO'),
        ( '227', 'Hobbs, NEW MEXICO'),
        ( '228', 'Roswell, NEW MEXICO'),
        ( '229', 'Santa Fe, NEW MEXICO'),
        ( '230', 'Albany, NEW YORK'),
        ( '231', 'Binghamton, NEW YORK'),
        ( '232', 'Buffalo, NEW YORK'),
        ( '233', 'Elmira / Corning, NEW YORK'),
        ( '234', 'Islip, NEW YORK'),
        ( '235', 'Ithaca, NEW YORK'),
        ( '236', 'New York, NEW YORK'),
        ( '237', 'Newburgh, NEW YORK'),
        ( '238', 'Niagara Falls, NEW YORK'),
        ( '239', 'Plattsburgh, NEW YORK'),
        ( '240', 'Rochester, NEW YORK'),
        ( '241', 'Syracuse, NEW YORK'),
        ( '242', 'Watertown, NEW YORK'),
        ( '243', 'White Plains, NEW YORK'),
        ( '244', 'Asheville, NORTH CAROLINA'),
        ( '245', 'Charlotte, NORTH CAROLINA'),
        ( '246', 'Fayetteville, NORTH CAROLINA'),
        ( '247', 'Greensboro, NORTH CAROLINA'),
        ( '248', 'Greenville, NORTH CAROLINA'),
        ( '249', 'Jacksonville, NORTH CAROLINA'),
        ( '250', 'New Bern, NORTH CAROLINA'),
        ( '251', 'Raleigh, NORTH CAROLINA'),
        ( '252', 'Wilmington, NORTH CAROLINA'),
        ( '253', 'Bismarck, NORTH DAKOTA'),
        ( '254', 'Dickinson, NORTH DAKOTA'),
        ( '255', 'Fargo, NORTH DAKOTA'),
        ( '256', 'Grand Forks, NORTH DAKOTA'),
        ( '257', 'Minot, NORTH DAKOTA'),
        ( '258', 'Williston, NORTH DAKOTA'),
        ( '259', 'Akron / Canton, OHIO'),
        ( '260', 'Cincinnati, OHIO'),
        ( '261', 'Cleveland, OHIO'),
        ( '262', 'Columbus, OHIO'),
        ( '263', 'Dayton, OHIO'),
        ( '264', 'Toledo, OHIO'),
        ( '265', 'Youngstown / Warren, OHIO'),
        ( '266', 'Lawton, OKLAHOMA'),
        ( '267', 'Oklahoma City, OKLAHOMA'),
        ( '268', 'Tulsa, OKLAHOMA'),
        ( '269', 'Eugene, OREGON'),
        ( '270', 'Klamath Falls, OREGON'),
        ( '271', 'Medford, OREGON'),
        ( '272', 'North Bend, OREGON'),
        ( '273', 'Portland, OREGON'),
        ( '274', 'Redmond, OREGON'),
        ( '275', 'Allentown, PENNSYLVANIA'),
        ( '276', 'Erie, PENNSYLVANIA'),
        ( '277', 'Harrisburg / Middletown, PENNSYLVANIA'),
        ( '278', 'Latrobe, PENNSYLVANIA'),
        ( '279', 'Philadelphia, PENNSYLVANIA'),
        ( '280', 'Pittsburgh, PENNSYLVANIA'),
        ( '281', 'State College, PENNSYLVANIA'),
        ( '282', 'Wilkes-Barre / Scranton, PENNSYLVANIA'),
        ( '283', 'Williamsport, PENNSYLVANIA'),
        ( '284', 'Block Island / New Shoreham, RHODE ISLAND'),
        ( '285', 'Providence / Warwick, RHODE ISLAND'),
        ( '286', 'Westerly, RHODE ISLAND'),
        ( '287', 'Charleston, SOUTH CAROLINA'),
        ( '288', 'Columbia, SOUTH CAROLINA'),
        ( '289', 'Florence, SOUTH CAROLINA'),
        ( '290', 'Greer, SOUTH CAROLINA'),
        ( '291', 'Hilton Head Island, SOUTH CAROLINA'),
        ( '292', 'Myrtle Beach, SOUTH CAROLINA'),
        ( '293', 'Aberdeen, SOUTH DAKOTA'),
        ( '294', 'Pierre, SOUTH DAKOTA'),
        ( '295', 'Rapid City, SOUTH DAKOTA'),
        ( '296', 'Sioux Falls, SOUTH DAKOTA'),
        ( '297', 'Bristol / Johnson City / Kingsport, TENNESSEE'),
        ( '298', 'Chattanooga, TENNESSEE'),
        ( '299', 'Knoxville, TENNESSEE'),
        ( '300', 'Memphis, TENNESSEE'),
        ( '301', 'Nashville, TENNESSEE'),
        ( '302', 'Abilene, TEXAS'),
        ( '303', 'Amarillo, TEXAS'),
        ( '304', 'Austin, TEXAS'),
        ( '305', 'Beaumont / Port Arthur, TEXAS'),
        ( '306', 'Brownsville, TEXAS'),
        ( '307', 'College Station, TEXAS'),
        ( '308', 'Corpus Christi / Kingsville, TEXAS'),
        ( '309', 'Dallas, TEXAS'),
        ( '310', 'Del Rio, TEXAS'),
        ( '311', 'El Paso, TEXAS'),
        ( '312', 'Fort Hood / Killeen / Temple, TEXAS'),
        ( '313', 'Harlingen, TEXAS'),
        ( '314', 'Houston, TEXAS'),
        ( '315', 'Laredo, TEXAS'),
        ( '316', 'Longview, TEXAS'),
        ( '317', 'Lubbock, TEXAS'),
        ( '318', 'McAllen, TEXAS'),
        ( '319', 'Midland, TEXAS'),
        ( '320', 'San Angelo, TEXAS'),
        ( '321', 'San Antonio, TEXAS'),
        ( '322', 'Tyler, TEXAS'),
        ( '323', 'Waco, TEXAS'),
        ( '324', 'Wichita Falls, TEXAS'),
        ( '325', 'Provo, UTAH'),
        ( '326', 'Salt Lake City, UTAH'),
        ( '327', 'St. George / Beaver, UTAH'),
        ( '328', 'Wendover, UTAH'),
        ( '329', 'Burlington, VERMONT'),
        ( '330', 'Charlottesville, VIRGINIA'),
        ( '331', 'Lynchburg, VIRGINIA'),
        ( '332', 'Newport News, VIRGINIA'),
        ( '333', 'Norfolk, VIRGINIA'),
        ( '334', 'Richmond, VIRGINIA'),
        ( '335', 'Roanoke, VIRGINIA'),
        ( '336', 'Staunton / Waynesboro / Harrisonburg, VIRGINIA'),
        ( '337', 'Washington, D.C. / Arlington County, VIRGINIA'),
        ( '338', 'Bellingham, WASHINGTON'),
        ( '339', 'Friday Harbor, WASHINGTON'),
        ( '340', 'Pasco, WASHINGTON'),
        ( '341', 'Port Angeles, WASHINGTON'),
        ( '342', 'Pullman / Moscow, Idaho, WASHINGTON'),
        ( '343', 'Seattle, WASHINGTON'),
        ( '344', 'Spokane, WASHINGTON'),
        ( '345', 'Walla Walla, WASHINGTON'),
        ( '346', 'Wenatchee, WASHINGTON'),
        ( '347', 'Yakima, WASHINGTON'),
        ( '348', 'Charleston, WEST VIRGINIA'),
        ( '349', 'Clarksburg, WEST VIRGINIA'),
        ( '350', 'Huntington, WEST VIRGINIA'),
        ( '351', 'Lewisburg, WEST VIRGINIA'),
        ( '352', 'Morgantown, WEST VIRGINIA'),
        ( '353', 'Appleton, WISCONSIN'),
        ( '354', 'Eau Claire, WISCONSIN'),
        ( '355', 'Green Bay, WISCONSIN'),
        ( '356', 'La Crosse, WISCONSIN'),
        ( '357', 'Madison, WISCONSIN'),
        ( '358', 'Milwaukee, WISCONSIN'),
        ( '359', 'Mosinee, WISCONSIN'),
        ( '360', 'Rhinelander, WISCONSIN'),
        ( '361', 'Casper, WYOMING'),
        ( '362', 'Cheyenne, WYOMING'),
        ( '363', 'Cody, WYOMING'),
        ( '364', 'Gillette, WYOMING'),
        ( '365', 'Jackson, WYOMING'),
        ( '366', 'Riverton, WYOMING'),
        ( '367', 'Rock Springs, WYOMING'),
        ( '368', 'Sheridan, WYOMING'),
        ( '369', 'Pago Pago, Tutuila, AMERICAN SAMOA'),
        ( '370', 'Agana / Tamuning, GUAM'),
        ( '371', 'Obyan, Saipan Island, NORTHERN MARIANAS'),
        ( '372', 'Rota Island, NORTHERN MARIANAS'),
        ( '373', 'Aguadilla, PUERTO RICO'),
        ( '374', 'Ceiba, PUERTO RICO'),
        ( '375', 'Ponce, PUERTO RICO'),
        ( '376', 'San Juan / Carolina, PUERTO RICO'),
        ( '377', 'Vieques, PUERTO RICO'),
        ( '378', 'Charlotte Amalie, St. Thomas, U.S. VIRGIN ISLANDS '),
        ( '379', 'Christiansted, St. Croix, U.S. VIRGIN ISLANDS '),
        )

# Data Model for additional user information
class Chatters(models.Model):
    username = models.OneToOneField(User, related_name="one2one_user", blank=True, null=True)
    fname = models.CharField(max_length=160, blank=True)
    name = models.CharField(max_length=160, blank=True)
    lname = models.CharField(max_length=160, blank=True)
    email = models.CharField(max_length=160, blank=True)
    age = models.CharField(max_length=5, blank=True)
    image = models.ImageField(upload_to='static/img/', default='/static/img/egg.jpg')
    spotify_auth = models.CharField(max_length=430, blank=True)
    acousticness = models.FloatField(null=True, default=0)
    danceability = models.FloatField(null=True, default=0)
    energy = models.FloatField(null=True, default=0)
    instrumentalness = models.FloatField(null=True, default=0)
    key = models.FloatField(null=True, default=0)
    liveness = models.FloatField(null=True, default=0)
    loudness = models.FloatField(null=True, default=0)
    speechiness = models.FloatField(null=True, default=0)
    tempo = models.FloatField(null=True, default=0)
    time_signature = models.FloatField(null=True, default=0)
    valence = models.FloatField(null=True, default=0)
    location = models.CharField(max_length=3, choices=locations)

    def __unicode__(self):
        return 'Entry(id=' + str(self.id) + ')'

    class Meta:
        ordering = ["username"]

# Data model for tracks
class Tracks(models.Model):
    track = models.CharField(max_length=160)
    artist = models.CharField(max_length=160)
    album = models.CharField(max_length=160)
    img = models.CharField(max_length=300)
    uri = models.CharField(max_length=160)
    popularity = models.CharField(max_length=160)
    created = models.DateTimeField(default=None)
    index = models.CharField(max_length=10)
    top_tracks = models.ForeignKey(Chatters, null=True, default=None, related_name='toptracks')
    acousticness = models.FloatField(null=True, default=None)
    danceability = models.FloatField(null=True, default=None)
    energy = models.FloatField(null=True, default=None)
    instrumentalness = models.FloatField(null=True, default=None)
    key = models.FloatField(null=True, default=None)
    liveness = models.FloatField(null=True, default=None)
    loudness = models.FloatField(null=True, default=None)
    speechiness = models.FloatField(null=True, default=None)
    tempo = models.FloatField(null=True, default=None)
    time_signature = models.FloatField(null=True, default=None)
    valence = models.FloatField(null=True, default=None)

    def __unicode__(self): #Tell it to return as a unicode string
        return 'id=' + str(self.id) + ',text="' + self.track + '"'

    class Meta:
        ordering = ["created"]

# Data model for tracks
class hotTracks(models.Model):
    track = models.CharField(max_length=160)
    artist = models.CharField(max_length=160)
    album = models.CharField(max_length=160)
    img = models.CharField(max_length=300)
    uri = models.CharField(max_length=160)
    popularity = models.CharField(max_length=160)
    created = models.DateTimeField(default=None)
    index = models.CharField(max_length=10)
    acousticness = models.FloatField(null=True, default=None)
    danceability = models.FloatField(null=True, default=None)
    energy = models.FloatField(null=True, default=None)
    instrumentalness = models.FloatField(null=True, default=None)
    key = models.FloatField(null=True, default=None)
    liveness = models.FloatField(null=True, default=None)
    loudness = models.FloatField(null=True, default=None)
    speechiness = models.FloatField(null=True, default=None)
    tempo = models.FloatField(null=True, default=None)
    time_signature = models.FloatField(null=True, default=None)
    valence = models.FloatField(null=True, default=None)
    duplicates = models.FloatField(null=True, default=1.)
    location = models.CharField(max_length=3, choices=locations)

    def __unicode__(self): #Tell it to return as a unicode string
        return 'id=' + str(self.id) + ',text="' + self.track + '"'

    class Meta:
        ordering = ["duplicates"]

# Data model for artists
class Artists(models.Model):
    artist = models.CharField(max_length=160)
    uri = models.CharField(max_length=160)
    img = models.CharField(max_length=300)
    popularity = models.CharField(max_length=160)
    created = models.DateTimeField(default=None)
    index = models.CharField(max_length=10)
    top_artists = models.ForeignKey(Chatters, null=True, default=None, related_name='topartists')

    def __unicode__(self): #Tell it to return as a unicode string
        return 'id=' + str(self.id) + ',text="' + self.artist + '"'

    class Meta:
        ordering = ["created"]

# Data model for genres
class Genres(models.Model):
    genre = models.CharField(max_length=160)
    created = models.DateTimeField(default=None)
    number = models.IntegerField(default = 1)
    top_genres = models.ForeignKey(Chatters, null=True, default=None, related_name='topgenres')

    def __unicode__(self): #Tell it to return as a unicode string
        return 'id=' + str(self.id) + ',text="' + self.genre + '"'

    class Meta:
        ordering = ["-number"]

# Data model for a chat message
class Mess(models.Model):
    text = models.CharField(max_length=160)
    user = models.ForeignKey(User, default=None)
    created = models.DateTimeField(default=None)
    reality_coefficient = models.BooleanField(default=True)
    context = models.TextField(null=True, default=None)
    # con = models.CharField(max_length=100)

    def __unicode__(self): #Tell it to return as a unicode string
        return 'id=' + str(self.id) + ',text="' + self.text + '"'

    class Meta:
        ordering = ["created"]

# Data model for Search Track Returns
class SearchRes(models.Model):
    user = models.ForeignKey(User, default=None)
    track = models.CharField(max_length=160)
    artist = models.CharField(max_length=160)
    album = models.CharField(max_length=160)
    img = models.CharField(max_length=300)
    uri = models.CharField(max_length=160)
    popularity = models.CharField(max_length=160)
    created = models.DateTimeField(default=None)
    acousticness = models.FloatField(null=True, default=None)
    danceability = models.FloatField(null=True, default=None)
    energy = models.FloatField(null=True, default=None)
    instrumentalness = models.FloatField(null=True, default=None)
    key = models.FloatField(null=True, default=None)
    liveness = models.FloatField(null=True, default=None)
    loudness = models.FloatField(null=True, default=None)
    speechiness = models.FloatField(null=True, default=None)
    tempo = models.FloatField(null=True, default=None)
    time_signature = models.FloatField(null=True, default=None)
    valence = models.FloatField(null=True, default=None)

    def __unicode__(self): #Tell it to return as a unicode string
        return 'id=' + str(self.id) + ',text="' + self.track + '"'

    class Meta:
        ordering = ["created"]

# Data model for Search Artist Returns
class ArtistRes(models.Model):
    user = models.ForeignKey(User, default=None)
    artist = models.CharField(max_length=160)
    uri = models.CharField(max_length=160)
    img = models.CharField(max_length=300)
    popularity = models.CharField(max_length=160)
    created = models.DateTimeField(default=None)

    def __unicode__(self): #Tell it to return as a unicode string
        return 'id=' + str(self.id) + ',text="' + self.track + '"'

    class Meta:
        ordering = ["created"]

# Data model for Search Artist Returns
class GenreRes(models.Model):
    user = models.ForeignKey(User, default=None)
    genre = models.CharField(max_length=160)
    created = models.DateTimeField(default=None)

    def __unicode__(self): #Tell it to return as a unicode string
        return 'id=' + str(self.id) + ',text="' + self.track + '"'

    class Meta:
        ordering = ["created"]

# Data model for Search Artist Returns
class PlaylistRes(models.Model):
    user = models.ForeignKey(User, default=None)
    playlist = models.CharField(max_length=160, default='')
    img = models.CharField(max_length=300, default='')
    owner = models.CharField(max_length=160, default='')
    ownerid = models.CharField(max_length=160, default='')
    created = models.DateTimeField(default=None)
    uri = models.CharField(max_length=160, default='')
    followers = models.CharField(max_length=160, default='')
    trackcount = models.CharField(max_length=160, default='')

    def __unicode__(self): #Tell it to return as a unicode string
        return 'id=' + str(self.id) + ',text="' + self.track + '"'

    class Meta:
        ordering = ["created"]
