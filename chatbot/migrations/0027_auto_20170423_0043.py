# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-23 05:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0026_auto_20170422_1710'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatters',
            options={'ordering': ['username']},
        ),
        migrations.AlterField(
            model_name='chatters',
            name='location',
            field=models.CharField(choices=[(b'0', b'Birmingham, ALABAMA'), (b'1', b'Dothan, ALABAMA'), (b'2', b'Huntsville, ALABAMA'), (b'3', b'Mobile, ALABAMA'), (b'4', b'Montgomery, ALABAMA'), (b'5', b'Anchorage, ALASKA'), (b'6', b'Aniak, ALASKA'), (b'7', b'Barrow, ALASKA'), (b'8', b'Bethel, ALASKA'), (b'9', b'Cordova, ALASKA'), (b'10', b'Deadhorse / Prudhoe Bay, ALASKA'), (b'11', b'Dillingham, ALASKA'), (b'12', b'Fairbanks, ALASKA'), (b'13', b'Galena, ALASKA'), (b'14', b'Gustavus, ALASKA'), (b'15', b'Homer, ALASKA'), (b'16', b'Hoonah, ALASKA'), (b'17', b'Juneau, ALASKA'), (b'18', b'Kenai, ALASKA'), (b'19', b'Ketchikan, ALASKA'), (b'20', b'King Salmon, ALASKA'), (b'21', b'Kodiak, ALASKA'), (b'22', b'Kotzebue, ALASKA'), (b'23', b'Nome, ALASKA'), (b'24', b'Petersburg, ALASKA'), (b'25', b'Sitka, ALASKA'), (b'26', b"St. Mary's, ALASKA"), (b'27', b'Unalakleet, ALASKA'), (b'28', b'Unalaska, ALASKA'), (b'29', b'Valdez, ALASKA'), (b'30', b'Wrangell, ALASKA'), (b'31', b'Yakutat, ALASKA'), (b'32', b'Bullhead City, ARIZONA'), (b'33', b'Flagstaff, ARIZONA'), (b'34', b'Grand Canyon / Tusayan, ARIZONA'), (b'35', b'Mesa, ARIZONA'), (b'36', b'Page, ARIZONA'), (b'37', b'Peach Springs 1G4, ARIZONA'), (b'38', b'Phoenix, ARIZONA'), (b'39', b'Tucson, ARIZONA'), (b'40', b'Yuma, ARIZONA'), (b'41', b'Fayetteville, ARKANSAS'), (b'42', b'Fort Smith, ARKANSAS'), (b'43', b'Little Rock, ARKANSAS'), (b'44', b'Texarkana, ARKANSAS'), (b'45', b'Arcata / Eureka, CALIFORNIA'), (b'46', b'Bakersfield, CALIFORNIA'), (b'47', b'Burbank, CALIFORNIA'), (b'48', b'Carlsbad, CALIFORNIA'), (b'49', b'Chico, CALIFORNIA'), (b'50', b'Crescent City, CALIFORNIA'), (b'51', b'Fresno, CALIFORNIA'), (b'52', b'Long Beach, CALIFORNIA'), (b'53', b'Los Angeles, CALIFORNIA'), (b'54', b'Mammoth Lakes, CALIFORNIA'), (b'55', b'Modesto, CALIFORNIA'), (b'56', b'Monterey, CALIFORNIA'), (b'57', b'Oakland, CALIFORNIA'), (b'58', b'Ontario, CALIFORNIA'), (b'59', b'Palm Springs, CALIFORNIA'), (b'60', b'Redding, CALIFORNIA'), (b'61', b'Sacramento, CALIFORNIA'), (b'62', b'San Diego, CALIFORNIA'), (b'63', b'San Francisco, CALIFORNIA'), (b'64', b'San Jose, CALIFORNIA'), (b'65', b'San Luis Obispo, CALIFORNIA'), (b'66', b'Santa Ana, CALIFORNIA'), (b'67', b'Santa Barbara, CALIFORNIA'), (b'68', b'Santa Maria, CALIFORNIA'), (b'69', b'Santa Rosa, CALIFORNIA'), (b'70', b'Stockton, CALIFORNIA'), (b'71', b'Aspen, COLORADO'), (b'72', b'Colorado Springs, COLORADO'), (b'73', b'Denver, COLORADO'), (b'74', b'Durango, COLORADO'), (b'75', b'Eagle, COLORADO'), (b'76', b'Grand Junction, COLORADO'), (b'77', b'Gunnison, COLORADO'), (b'78', b'Hayden, COLORADO'), (b'79', b'Montrose, COLORADO'), (b'80', b'Hartford, CONNECTICUT'), (b'81', b'New Haven, CONNECTICUT'), (b'82', b'Daytona Beach, FLORIDA'), (b'83', b'Fort Lauderdale, FLORIDA'), (b'84', b'Fort Myers, FLORIDA'), (b'85', b'Gainesville, FLORIDA'), (b'86', b'Jacksonville, FLORIDA'), (b'87', b'Key West, FLORIDA'), (b'88', b'Melbourne, FLORIDA'), (b'89', b'Miami, FLORIDA'), (b'90', b'Orlando, FLORIDA'), (b'91', b'Panama City Beach, FLORIDA'), (b'92', b'Pensacola, FLORIDA'), (b'93', b'Punta Gorda, FLORIDA'), (b'94', b'Sarasota / Bradenton, FLORIDA'), (b'95', b'St. Augustine, FLORIDA'), (b'96', b'St. Petersburg/Clearwater, FLORIDA'), (b'97', b'Tallahassee, FLORIDA'), (b'98', b'Tampa, FLORIDA'), (b'99', b'Valparaiso, FLORIDA'), (b'100', b'West Palm Beach, FLORIDA'), (b'101', b'Albany, GEORGIA'), (b'102', b'Atlanta, GEORGIA'), (b'103', b'Augusta, GEORGIA'), (b'104', b'Brunswick, GEORGIA'), (b'105', b'Columbus, GEORGIA'), (b'106', b'Savannah, GEORGIA'), (b'107', b'Valdosta, GEORGIA'), (b'108', b'Hilo, Hawaii, HAWAII'), (b'109', b'Honolulu, Oahu, HAWAII'), (b'110', b'Kahului, Maui, HAWAII'), (b'111', b'Kailua-Kona, Hawaii, HAWAII'), (b'112', b'Kaunakakai, Molokai, HAWAII'), (b'113', b'Lanai City, Lanai, HAWAII'), (b'114', b'Lihue, Kauai, HAWAII'), (b'115', b'Boise, IDAHO'), (b'116', b'Hailey, IDAHO'), (b'117', b'Idaho Falls, IDAHO'), (b'118', b'Lewiston, IDAHO'), (b'119', b'Pocatello / Arbon Valley, IDAHO'), (b'120', b'Twin Falls, IDAHO'), (b'121', b'Belleville, ILLINOIS'), (b'122', b'Bloomington / Normal, ILLINOIS'), (b'123', b'Champaign / Urbana, ILLINOIS'), (b'124', b'Chicago, ILLINOIS'), (b'125', b'Chicago, ILLINOIS'), (b'126', b'Marion, ILLINOIS'), (b'127', b'Moline, ILLINOIS'), (b'128', b'Peoria, ILLINOIS'), (b'129', b'Quincy, ILLINOIS'), (b'130', b'Rockford, ILLINOIS'), (b'131', b'Springfield, ILLINOIS'), (b'132', b'Evansville, INDIANA'), (b'133', b'Fort Wayne, INDIANA'), (b'134', b'Indianapolis, INDIANA'), (b'135', b'South Bend, INDIANA'), (b'136', b'Cedar Rapids, IOWA'), (b'137', b'Des Moines, IOWA'), (b'138', b'Dubuque, IOWA'), (b'139', b'Sioux City, IOWA'), (b'140', b'Waterloo, IOWA'), (b'141', b'Garden City, KANSAS'), (b'142', b'Manhattan, KANSAS'), (b'143', b'Wichita, KANSAS'), (b'144', b'Cincinnati/Covington, KENTUCKY'), (b'145', b'Lexington, KENTUCKY'), (b'146', b'Louisville, KENTUCKY'), (b'147', b'Owensboro, KENTUCKY'), (b'148', b'Paducah, KENTUCKY'), (b'149', b'Alexandria, LOUISIANA'), (b'150', b'Baton Rouge, LOUISIANA'), (b'151', b'Lafayette, LOUISIANA'), (b'152', b'Lake Charles, LOUISIANA'), (b'153', b'Monroe, LOUISIANA'), (b'154', b'New Orleans, LOUISIANA'), (b'155', b'Shreveport, LOUISIANA'), (b'156', b'Bangor, MAINE'), (b'157', b'Bar Harbor, MAINE'), (b'158', b'Portland, MAINE'), (b'159', b'Presque Isle, MAINE'), (b'160', b'Rockland, MAINE'), (b'161', b'Baltimore / Glen Burnie, MARYLAND'), (b'162', b'Salisbury, MARYLAND'), (b'163', b'Hagerstown, MARYLAND'), (b'164', b'Boston, MASSACHUSETTS'), (b'165', b'Hyannis, MASSACHUSETTS'), (b'166', b'Nantucket, MASSACHUSETTS'), (b'167', b'Provincetown, MASSACHUSETTS'), (b'168', b'Vineyard Haven, MASSACHUSETTS'), (b'169', b'Worcester, MASSACHUSETTS'), (b'170', b'Alpena, MICHIGAN'), (b'171', b'Beaver Island 6Y8 Welke Airport P-N, MICHIGAN'), (b'172', b'Detroit / Romulus, MICHIGAN'), (b'173', b'Escanaba, MICHIGAN'), (b'174', b'Flint, MICHIGAN'), (b'175', b'Grand Rapids, MICHIGAN'), (b'176', b'Hancock / Calumet, MICHIGAN'), (b'177', b'Iron Mountain / Kingsford, MICHIGAN'), (b'178', b'Kalamazoo / Battle Creek, MICHIGAN'), (b'179', b'Lansing, MICHIGAN'), (b'180', b'Marquette / Gwinn, MICHIGAN'), (b'181', b'Muskegon, MICHIGAN'), (b'182', b'Pellston, MICHIGAN'), (b'183', b'Saginaw, MICHIGAN'), (b'184', b'Sault Ste. Marie, MICHIGAN'), (b'185', b'Traverse City, MICHIGAN'), (b'186', b'Bemidji, MINNESOTA'), (b'187', b'Brainerd, MINNESOTA'), (b'188', b'Duluth, MINNESOTA'), (b'189', b'Hibbing, MINNESOTA'), (b'190', b'International Falls, MINNESOTA'), (b'191', b'Minneapolis, MINNESOTA'), (b'192', b'Rochester, MINNESOTA'), (b'193', b'St. Cloud, MINNESOTA'), (b'194', b'Columbus / West Point / Starkville, MISSISSIPPI'), (b'195', b'Gulfport / Biloxi, MISSISSIPPI'), (b'196', b'Hattiesburg / Laurel, MISSISSIPPI'), (b'197', b'Jackson, MISSISSIPPI'), (b'198', b'Columbia, MISSOURI'), (b'199', b'Joplin, MISSOURI'), (b'200', b'Kansas City, MISSOURI'), (b'201', b'Springfield, MISSOURI'), (b'202', b'St. Louis, MISSOURI'), (b'203', b'Billings, MONTANA'), (b'204', b'Bozeman, MONTANA'), (b'205', b'Butte, MONTANA'), (b'206', b'Great Falls, MONTANA'), (b'207', b'Helena, MONTANA'), (b'208', b'Kalispell, MONTANA'), (b'209', b'Missoula, MONTANA'), (b'210', b'Grand Island, NEBRASKA'), (b'211', b'Kearney, NEBRASKA'), (b'212', b'Lincoln, NEBRASKA'), (b'213', b'Omaha, NEBRASKA'), (b'214', b'Scottsbluff, NEBRASKA'), (b'215', b'Boulder City, NEVADA'), (b'216', b'Elko, NEVADA'), (b'217', b'Las Vegas, NEVADA'), (b'218', b'Reno, NEVADA'), (b'219', b'NEW, NEVADA'), (b'220', b'Lebanon, NEVADA'), (b'221', b'Manchester, NEVADA'), (b'222', b'Portsmouth, NEVADA'), (b'223', b'NEW, NEVADA'), (b'224', b'Atlantic City, NEVADA'), (b'225', b'Trenton, NEVADA'), (b'226', b'Newark, NEVADA'), (b'227', b'NEW, NEVADA'), (b'228', b'Albuquerque, NEVADA'), (b'229', b'Farmington, NEVADA'), (b'230', b'Hobbs, NEVADA'), (b'231', b'Roswell, NEVADA'), (b'232', b'Santa Fe, NEVADA'), (b'233', b'NEW, NEVADA'), (b'234', b'Albany, NEVADA'), (b'235', b'Binghamton, NEVADA'), (b'236', b'Buffalo, NEVADA'), (b'237', b'Elmira / Corning, NEVADA'), (b'238', b'Islip, NEVADA'), (b'239', b'Ithaca, NEVADA'), (b'240', b'New York, NEVADA'), (b'241', b'Newburgh, NEVADA'), (b'242', b'Niagara Falls, NEVADA'), (b'243', b'Plattsburgh, NEVADA'), (b'244', b'Rochester, NEVADA'), (b'245', b'Syracuse, NEVADA'), (b'246', b'Watertown, NEVADA'), (b'247', b'White Plains, NEVADA'), (b'248', b'Asheville, NORTH CAROLIN'), (b'249', b'Charlotte, NORTH CAROLIN'), (b'250', b'Fayetteville, NORTH CAROLIN'), (b'251', b'Greensboro, NORTH CAROLIN'), (b'252', b'Greenville, NORTH CAROLIN'), (b'253', b'Jacksonville, NORTH CAROLIN'), (b'254', b'New Bern, NORTH CAROLIN'), (b'255', b'Raleigh, NORTH CAROLIN'), (b'256', b'Wilmington, NORTH CAROLIN'), (b'257', b'Bismarck, NORTH DAKOT'), (b'258', b'Dickinson, NORTH DAKOT'), (b'259', b'Fargo, NORTH DAKOT'), (b'260', b'Grand Forks, NORTH DAKOT'), (b'261', b'Minot, NORTH DAKOT'), (b'262', b'Williston, NORTH DAKOT'), (b'263', b'Akron / Canton, OHIO'), (b'264', b'Cincinnati, OHIO'), (b'265', b'Cleveland, OHIO'), (b'266', b'Columbus, OHIO'), (b'267', b'Dayton, OHIO'), (b'268', b'Toledo, OHIO'), (b'269', b'Youngstown / Warren, OHIO'), (b'270', b'Lawton, OKLAHOMA'), (b'271', b'Oklahoma City, OKLAHOMA'), (b'272', b'Tulsa, OKLAHOMA'), (b'273', b'Eugene, OREGON'), (b'274', b'Klamath Falls, OREGON'), (b'275', b'Medford, OREGON'), (b'276', b'North Bend, OREGON'), (b'277', b'Portland, OREGON'), (b'278', b'Redmond, OREGON'), (b'279', b'Allentown, PENNSYLVANIA'), (b'280', b'Erie, PENNSYLVANIA'), (b'281', b'Harrisburg / Middletown, PENNSYLVANIA'), (b'282', b'Latrobe, PENNSYLVANIA'), (b'283', b'Philadelphia, PENNSYLVANIA'), (b'284', b'Pittsburgh, PENNSYLVANIA'), (b'285', b'State College, PENNSYLVANIA'), (b'286', b'Wilkes-Barre / Scranton, PENNSYLVANIA'), (b'287', b'Williamsport, PENNSYLVANIA'), (b'288', b'Block Island / New Shoreham, RHODE ISLAN'), (b'289', b'Providence / Warwick, RHODE ISLAN'), (b'290', b'Westerly, RHODE ISLAN'), (b'291', b'Charleston, SOUTH CAROLIN'), (b'292', b'Columbia, SOUTH CAROLIN'), (b'293', b'Florence, SOUTH CAROLIN'), (b'294', b'Greer, SOUTH CAROLIN'), (b'295', b'Hilton Head Island, SOUTH CAROLIN'), (b'296', b'Myrtle Beach, SOUTH CAROLIN'), (b'297', b'Aberdeen, SOUTH DAKOT'), (b'298', b'Pierre, SOUTH DAKOT'), (b'299', b'Rapid City, SOUTH DAKOT'), (b'300', b'Sioux Falls, SOUTH DAKOT'), (b'301', b'Bristol / Johnson City / Kingsport, TENNESSEE'), (b'302', b'Chattanooga, TENNESSEE'), (b'303', b'Knoxville, TENNESSEE'), (b'304', b'Memphis, TENNESSEE'), (b'305', b'Nashville, TENNESSEE'), (b'306', b'Abilene, TEXAS'), (b'307', b'Amarillo, TEXAS'), (b'308', b'Austin, TEXAS'), (b'309', b'Beaumont / Port Arthur, TEXAS'), (b'310', b'Brownsville, TEXAS'), (b'311', b'College Station, TEXAS'), (b'312', b'Corpus Christi / Kingsville, TEXAS'), (b'313', b'Dallas, TEXAS'), (b'314', b'Del Rio, TEXAS'), (b'315', b'El Paso, TEXAS'), (b'316', b'Fort Hood / Killeen / Temple, TEXAS'), (b'317', b'Harlingen, TEXAS'), (b'318', b'Houston, TEXAS'), (b'319', b'Laredo, TEXAS'), (b'320', b'Longview, TEXAS'), (b'321', b'Lubbock, TEXAS'), (b'322', b'McAllen, TEXAS'), (b'323', b'Midland, TEXAS'), (b'324', b'San Angelo, TEXAS'), (b'325', b'San Antonio, TEXAS'), (b'326', b'Tyler, TEXAS'), (b'327', b'Waco, TEXAS'), (b'328', b'Wichita Falls, TEXAS'), (b'329', b'Provo, UTAH'), (b'330', b'Salt Lake City, UTAH'), (b'331', b'St. George / Beaver, UTAH'), (b'332', b'Wendover, UTAH'), (b'333', b'Burlington, VERMONT'), (b'334', b'Charlottesville, VIRGINIA'), (b'335', b'Lynchburg, VIRGINIA'), (b'336', b'Newport News, VIRGINIA'), (b'337', b'Norfolk, VIRGINIA'), (b'338', b'Richmond, VIRGINIA'), (b'339', b'Roanoke, VIRGINIA'), (b'340', b'Staunton / Waynesboro / Harrisonburg, VIRGINIA'), (b'341', b'Washington, D.C. / Arlington County, VIRGINIA'), (b'342', b'Bellingham, WASHINGTON'), (b'343', b'Friday Harbor, WASHINGTON'), (b'344', b'Pasco, WASHINGTON'), (b'345', b'Port Angeles, WASHINGTON'), (b'346', b'Pullman / Moscow, Idaho, WASHINGTON'), (b'347', b'Seattle, WASHINGTON'), (b'348', b'Spokane, WASHINGTON'), (b'349', b'Walla Walla, WASHINGTON'), (b'350', b'Wenatchee, WASHINGTON'), (b'351', b'Yakima, WASHINGTON'), (b'352', b'Charleston, WEST VIRGINI'), (b'353', b'Clarksburg, WEST VIRGINI'), (b'354', b'Huntington, WEST VIRGINI'), (b'355', b'Lewisburg, WEST VIRGINI'), (b'356', b'Morgantown, WEST VIRGINI'), (b'357', b'Appleton, WISCONSIN'), (b'358', b'Eau Claire, WISCONSIN'), (b'359', b'Green Bay, WISCONSIN'), (b'360', b'La Crosse, WISCONSIN'), (b'361', b'Madison, WISCONSIN'), (b'362', b'Milwaukee, WISCONSIN'), (b'363', b'Mosinee, WISCONSIN'), (b'364', b'Rhinelander, WISCONSIN'), (b'365', b'Casper, WYOMING'), (b'366', b'Cheyenne, WYOMING'), (b'367', b'Cody, WYOMING'), (b'368', b'Gillette, WYOMING'), (b'369', b'Jackson, WYOMING'), (b'370', b'Riverton, WYOMING'), (b'371', b'Rock Springs, WYOMING'), (b'372', b'Sheridan, WYOMING'), (b'373', b'Pago Pago, Tutuila, AMERICAN SAMO'), (b'374', b'Agana / Tamuning, GUAM'), (b'375', b'Obyan, Saipan Island, NORTHERN MARIANA'), (b'376', b'Rota Island, NORTHERN MARIANA'), (b'377', b'Aguadilla, PUERTO RIC'), (b'378', b'Ceiba, PUERTO RIC'), (b'379', b'Ponce, PUERTO RIC'), (b'380', b'San Juan / Carolina, PUERTO RIC'), (b'381', b'Vieques, PUERTO RIC'), (b'382', b'U.S., PUERTO RIC'), (b'383', b'Charlotte Amalie, St. Thomas, PUERTO RIC'), (b'384', b'Christiansted, St. Croix, PUERTO RIC')], max_length=3),
        ),
    ]
