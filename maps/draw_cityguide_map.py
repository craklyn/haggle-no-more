import os
import folium
from folium.plugins import MarkerCluster

bangkok_markets = os.path.join('chatuchat_market.json')
#antarctic_ice_shelf_topo = os.path.join('data', 'antarctic_ice_shelf_topo.json')

m = folium.Map(
#    location=[13.752300, 100.539668],
    location=[13.752876, 100.494256],
#    tiles='Stamen Toner',
    zoom_start=15
)

#popup = 'Must be on top of the choropleth'

folium.GeoJson(
    bangkok_markets,
    name='geojson',
    style_function = lambda feature : dict(
    color='green',
    weight=3,
    opacity=1.0)
).add_to(m)

marker_cluster = MarkerCluster().add_to(m)


folium.Marker(
      location=[13.7448942, 100.5407246],
      popup="1823 Tea Lounge",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.723825, 100.516682],
      popup="A&J Silver",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.748129, 100.584818],
      popup="A-One Bangkok Hotel",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7305395, 100.5331244],
      popup="AGEHA Cafe Bar",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7046547, 100.4917476],
      popup="AVANI Riverside Bangkok Hotel",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7269524, 100.575397],
      popup="Akbar Restaurant",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7264026, 100.5758309],
      popup="Akko Trading Co.",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.740192, 100.6301241],
      popup="American Eagle",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7467681, 100.5354125],
      popup="American Eagle Outfitters",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.719883, 100.568162],
      popup="An An Lao",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7406028, 100.5418178],
      popup="Anantara Bangkok Hotel - Siam",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7046547, 100.4917476],
      popup="Anantara Bangkok Resort - Riverside",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7444755, 100.5299018],
      popup="Anne Bra",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7367377, 100.5387143],
      popup="Apinara",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7240256, 100.5160595],
      popup="Arisra Gallery",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.742094, 100.545348],
      popup="Artur Restaurant Steaks Seafood Martini",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7391137, 100.5502297],
      popup="Baan Glom Gig Restaurant",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7051756, 100.5033803],
      popup="Baan Khanitha - Asiatique",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7367621, 100.5629454],
      popup="Baan Khanitha - Soi Sukhumvit 23",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.6723745, 100.5343614],
      popup="Baan Klang Nam 2",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7478475, 100.5559355],
      popup="Baan Nakatani",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7264292, 100.5770606],
      popup="Baccara Bar",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.8399858, 100.5853348],
      popup="Ban Dokmai",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7454544, 100.5351788],
      popup="Banana Mobile",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7317002, 100.5691267],
      popup="Banana Republic",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7462276, 100.5398188],
      popup="Banana Store - Central World",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7898474, 100.5743191],
      popup="Banana Store - It Fortune Town",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.723195, 100.5803311],
      popup="Bangkok Marriott Hotel - Sukhumvit",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7457087, 100.5396561],
      popup="Bata - Central World",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.717463, 100.568238],
      popup="Bata - Lotus Rama IV",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.72288, 100.5195006],
      popup="Belle's Room",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7474444, 100.5389145],
      popup="Bershka - Central World",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7461578, 100.531427],
      popup="Bi Chalai",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7171989, 100.5187233],
      popup="Blue Elephant Cooking School",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7044608, 100.5346896],
      popup="Boon Tong Kee Restaurant",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7321857, 100.5693282],
      popup="Boots",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.669979, 100.6346465],
      popup="Bossini",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.919202, 100.6018656],
      popup="Burger King",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7203853, 100.5158907],
      popup="Cafe Ice",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7239092, 100.5238222],
      popup="Café De Laos",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7462276, 100.5398188],
      popup="Calvin Klein Jeans",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7299763, 100.5683468],
      popup="Canali",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.747109, 100.535273],
      popup="Canali Boutique",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.744632, 100.534788],
      popup="Chai Gold Label",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7467024, 100.5347688],
      popup="Charles & Keith - Siam Center",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7377149, 100.5602023],
      popup="Charles & Keith - Terminal 21",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7410466, 100.507639],
      popup="Charoenchai",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.711127, 100.509074],
      popup="Chatrium Hotel - Riverside",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.71899, 100.521924],
      popup="Chef Man",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7462276, 100.5398188],
      popup="China White",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7405693, 100.56293],
      popup="Chockchai Steak House",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7459231, 100.5346924],
      popup="Christian Dior",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7356178, 100.5610236],
      popup="CityPoint Hotel",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.815815, 100.560972],
      popup="Coach - Central Plaza Ladprao",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.760449, 100.537955],
      popup="Coach - King Power Complex",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.723033, 100.5786331],
      popup="Column Bangkok",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7489706, 100.5224156],
      popup="Crabtree & Evelyn",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.746545, 100.535151],
      popup="Crazy Step - Siam Paragon",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7672111, 100.4438725],
      popup="Crazy Step - The Circle Ratchapruk",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.746252, 100.535022],
      popup="Curated",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7462276, 100.5398188],
      popup="Da+Pp",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.802254, 100.549212],
      popup="Dairy Queen",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.744632, 100.534788],
      popup="Dapper Access",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7452525, 100.5407919],
      popup="Della Spiga",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7317147, 100.5656087],
      popup="Det-5 Restaurant & Bar",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7467681, 100.5354125],
      popup="Dolce & Gabbana",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7393451, 100.5827828],
      popup="Dong E",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7193884, 100.5907502],
      popup="Doo Rae Korean Restaurant",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.6571362, 100.6428215],
      popup="Dusit Princess Srinakarin Hotel",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7286635, 100.5384786],
      popup="Dusit Thani Bangkok",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7532, 100.546699],
      popup="Eastin Hotel Makkasan Bangkok",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7462276, 100.5398188],
      popup="Ecco",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7300597, 100.568665],
      popup="Emporium",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7300597, 100.568665],
      popup="Emporium Food Hall",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.730755, 100.568772],
      popup="Emporium Suites by Chatrium",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7324271, 100.5698741],
      popup="Emquartier Co.",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.817879, 100.560036],
      popup="Erawan Diamond",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.6632337, 100.4379],
      popup="Esprit",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.746775, 100.535477],
      popup="Fendi",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7216375, 100.5723362],
      popup="Firehouse",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.825953, 100.6792529],
      popup="Fly Now Iii",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7311589, 100.5696869],
      popup="Flynow",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7234009, 100.5362533],
      popup="Fraser Suites - Urbana Sathorn",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7319703, 100.5696853],
      popup="Fuji",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.744647, 100.533193],
      popup="Fuku Intown",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7454544, 100.5351788],
      popup="Gap",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7779988, 100.5317418],
      popup="Gems Gallery International",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7319703, 100.5696853],
      popup="Go! Ape",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7181257, 100.5906494],
      popup="Golden Tulip - Mandison Suites",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7534697, 100.5716639],
      popup="Golden Tulip - Sovereign",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7373528, 100.5604447],
      popup="Gourmet Market",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7435228, 100.5404889],
      popup="Grand Hyatt - Erawan",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7217245, 100.7863529],
      popup="Great Residence Hotel",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7589435, 100.5660458],
      popup="Greyhound Café",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.815815, 100.560972],
      popup="Gyu Ichi Yakiniku Restaurant",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.719089, 100.585289],
      popup="Hakone",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.729459, 100.5334522],
      popup="Hanamachi Japanese BBQ Restaurant",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7303298, 100.5163785],
      popup="Hanaya Japanese Restaurant",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7847004, 100.5435337],
      popup="Hanazen",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7439571, 100.5463333],
      popup="Hardcover: The Art Book Shop At BACC",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.743642, 100.544122],
      popup="Have A Zeed By Steak Lao",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7462524, 100.5328635],
      popup="Ho La La Bijouterie",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7305728, 100.5332675],
      popup="Hock Shark Fins",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7288959, 100.5276704],
      popup="Hokkaido Restaurant Surawong",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7380203, 100.5627357],
      popup="Honmono Sushi Japanese Restaurant Thonglor13",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7338737, 100.5459692],
      popup="Hotel Indigo Bangkok",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7391757, 100.5578256],
      popup="Hotel Sofitel Bangkok - Sukhumvit",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7409472, 100.5090749],
      popup="Hua Seng Hong Restaurant",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7448942, 100.5407246],
      popup="Hugo Boss - Gaysorn Plaza",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.746503, 100.53528],
      popup="Hugo Boss - Siam Paragon",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7174091, 100.5180392],
      popup="IL Bognoese",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7241271, 100.5343346],
      popup="Indigo Bar & Restaurant",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7742972, 100.5256833],
      popup="James Tailor Bangkok",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.6823797, 100.6005459],
      popup="Jaspal Central Plaza West Gate",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7502027, 100.5394533],
      popup="Jeffer Restaurant",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7330385, 100.5296776],
      popup="Jeffer Steak Chamchuri",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.8282131, 100.5678679],
      popup="Jelly Bunny",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7397409, 100.5545474],
      popup="Jidori cuisine Ken",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7409209, 100.5402006],
      popup="Jim Thompson",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7469677, 100.5342249],
      popup="Jim Thompson - Siam Paragon",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7289054, 100.568047],
      popup="Karmakamet Diner",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.6970857, 100.6064949],
      popup="Khing Klao",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7658856, 100.496894],
      popup="Khinlom Chomsaphan Restaurant",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7412827, 100.5585223],
      popup="Kingston Suites",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7397618, 100.555849],
      popup="Kinnaree Gourmet Thai Restaurant and Bar",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7324271, 100.5698741],
      popup="Kinokuniya Bookstore",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7465865, 100.5391192],
      popup="Kinokuniya Bookstores",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7816515, 100.5759717],
      popup="Korean Restaurant Drum BBQ",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7233378, 100.5199486],
      popup="Kowloon Restaurant",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7293025, 100.51635],
      popup="Kwau Je Ngau",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.723961, 100.528528],
      popup="L'Atelier de Joël Robuchon - Bangkok",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.817879, 100.560036],
      popup="Laem Cha-Reon Seafood",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7462524, 100.5328635],
      popup="Lalalove",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.746863, 100.521371],
      popup="Lalama by Naraya",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7238768, 100.5802293],
      popup="Le Dalat Restaurant",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7144824, 100.5460086],
      popup="Le Petit Zinc",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7462276, 100.5398188],
      popup="Lee Cafe - CentralWorld Plaza",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7439889, 100.5404494],
      popup="Lee Cafe - Ploenchit Road",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7462276, 100.5398188],
      popup="Lesnereides Paris",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.746518, 100.539221],
      popup="Life",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.74655, 100.532238],
      popup="Loft",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7212299, 100.5832454],
      popup="Louis Vuitton",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.738843, 100.549267],
      popup="Lyon",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7094561, 100.538557],
      popup="M Krub - Mahanakorn Cube",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7373388, 100.5605976],
      popup="MIX Restaurant & Bar - Terminal 21",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7329396, 100.5627747],
      popup="Maitria Hotel Sukhumvit 18 – A Chatrium Collection",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7395857, 100.5415977],
      popup="Man Kitchen By Chef Man",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7462276, 100.5398188],
      popup="Massimo Dutti - Central World",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7207594, 100.5858464],
      popup="Massimo Dutti - Emquartier",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7287236, 100.5339106],
      popup="Matoi Sushi",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7448942, 100.5407246],
      popup="Max Mara",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.741604, 100.541049],
      popup="Mesamis cafe",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7552281, 100.5044604],
      popup="Methavalai Sorndaeng",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7213511, 100.51702],
      popup="Mezzaluna",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7462524, 100.5328635],
      popup="Missile",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7300189, 100.5342535],
      popup="Mizu",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7473065, 100.5399331],
      popup="Momo Paradise",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7452007, 100.5337818],
      popup="NYX",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.746863, 100.521371],
      popup="Nai Chan",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.746863, 100.521371],
      popup="Naraya",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7449783, 100.556249],
      popup="Nest",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7416662, 100.5851713],
      popup="ONCE Social Bar & Cafe - Thonglor 10",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7458872, 100.5319025],
      popup="Oakley Shop",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7158366, 100.5868025],
      popup="Oasis Spa Bangkok - Sukhumvit 31",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7783765, 100.4756755],
      popup="Ootoya Restaurant",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7439979, 100.5413947],
      popup="Oriental Drincess",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7300202, 100.5466364],
      popup="Oriental Residence Bangkok",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.756226, 100.5679618],
      popup="P.T Town Co.",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7475372, 100.5171362],
      popup="Paragon Food Hall",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7267784, 100.5398394],
      popup="Paris Bangkok Restaurant",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7353059, 100.562753],
      popup="Park Plaza Bangkok - Soi 18",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.745198, 100.540774],
      popup="Paste Bangkok",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7278439, 100.5322542],
      popup="Patty's Fiesta",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7472309, 100.5416779],
      popup="Pedro",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7414135, 100.5475404],
      popup="Plaza Athénée Bangkok - A Royal Méridien Hotel",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.9440535, 100.6127981],
      popup="Ploen Seafood Restaurant",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.758509, 100.565122],
      popup="Projector 108",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.743959, 100.546509],
      popup="Pronto Central Embassy",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7462276, 100.5398188],
      popup="Pull & Bear",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7427775, 100.55283],
      popup="Ramez",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.74261, 100.541989],
      popup="Renaissance Bangkok Ratchaprasong Hotel",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7448942, 100.5407246],
      popup="Riedel Wine Bar & Cellar",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.762009, 100.493069],
      popup="Riva Surya",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7462524, 100.5328635],
      popup="Rotsaniyom",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7397618, 100.555849],
      popup="Royal Express Bangkok",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.783314, 100.501562],
      popup="Royal River Hotel Bangkok",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7250373, 100.5631972],
      popup="Ruan Mallika",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7218285, 100.56295],
      popup="Ruan Thapthim",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7410044, 100.5912811],
      popup="Saigon Recipe Restaurant",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7302884, 100.5688205],
      popup="Salvatore Ferragamo",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7467681, 100.5354125],
      popup="Scintilla Gioielli",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7604353, 100.5427028],
      popup="Seasons Siam Hotel",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7373276, 100.5590521],
      popup="Sheraton Grande Sukhumvit",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7474322, 100.5269608],
      popup="Siam@Siam Design Hotel",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7469677, 100.5342249],
      popup="Signor Sassi",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7208381, 100.7371051],
      popup="Sinsuvarn Airport Suite",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7046547, 100.4917476],
      popup="Sizzler",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.741266349306, 100.54055991131],
      popup="Sriracha Moda",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7467024, 100.5347688],
      popup="Starbucks",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7324271, 100.5698741],
      popup="Superdry",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.815815, 100.560972],
      popup="Superdry",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7844201, 100.576131],
      popup="Swissôtel - Le Concorde",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7310496, 100.5689734],
      popup="TWG Tea - Emporium Retail",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7459231, 100.5346924],
      popup="TWG Tea - Siam Paragon",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7453458, 100.4990936],
      popup="Tai Seng Heng Gold Shop",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7317681, 100.5691047],
      popup="Ted Baker",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.8165279, 100.6849005],
      popup="Terrace 61",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7168818, 100.5234004],
      popup="Thai Wah Tower II",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7462276, 100.5398188],
      popup="Thann Central World",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.747003, 100.539414],
      popup="The Adjective",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.728531, 100.580999],
      popup="The Coffee Club",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7080738, 100.6045071],
      popup="The Landmark Bangkok",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7428689, 100.5479714],
      popup="The Okura Prestige Bangkok",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7230199, 100.5109079],
      popup="The Peninsula Bangkok",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7465362, 100.5324365],
      popup="The Selected",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7482456, 100.5427172],
      popup="The St. Regis Bangkok",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7351536, 100.5631719],
      popup="The Westin Grande Sukhumvit Bangkok",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7457139, 100.5396645],
      popup="Thnk Store",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7467681, 100.5354125],
      popup="Tod's Siam Paragon",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.744866, 100.5297873],
      popup="Tokyu Department Store",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7268908, 100.5753967],
      popup="Torajiro Japanese Restaurant",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7459231, 100.5346924],
      popup="Tsuruha Thailand",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.718589, 100.54634],
      popup="U Sathorn Bangkok",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7319476, 100.5679988],
      popup="UFM Fuji Super",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7282073, 100.5350609],
      popup="Up to Yuu",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7381527, 100.5602511],
      popup="Urban360",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7265538, 100.5159744],
      popup="V .R.S . Silver",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7582449, 100.5662566],
      popup="Victoria's Secret",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.746863, 100.521371],
      popup="Villains SF - Siam Paragon",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7055615, 100.5445086],
      popup="Vino di Zanotti",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7254752, 100.5259119],
      popup="W Bangkok",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7351412, 100.5679982],
      popup="Whisgars",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7053237, 100.597564],
      popup="Wine Connection",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.725468, 100.5258914],
      popup="Wine Connection Bistro",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7398319, 100.5490027],
      popup="Witch's British",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7462276, 100.5398188],
      popup="Women's Secret",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7462276, 100.5398188],
      popup="Zara - Central World",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.73134, 100.569742],
      popup="Zara - Emquartier",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7459231, 100.5346924],
      popup="Zara - Siam Paragon",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7450385, 100.5533387],
      popup="Zenith Sukhumvit Hotel",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7342379, 100.5826251],
      popup="diVino - Food & Wine",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7602561, 100.5382335],
      popup="déjà vu",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.734132, 100.582323],
      popup="iBeat",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.7462276, 100.5398188],
      popup="iStudio by Copperwired",
      icon=folium.Icon(color='green', icon='shopping-cart'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.800497, 100.58311],
      popup="Bangkok Bank and Foreign Exchange Center",
      icon=folium.Icon(color='black', icon='credit-card'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.800497, 100.54311],
      popup="BANGKOK BANK AND FOREIGN EXCHANGE CENTER",
      icon=folium.Icon(color='black', icon='credit-card'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.736778, 100.56206],
      popup="CITIBANK",
      icon=folium.Icon(color='black', icon='credit-card'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.736808, 100.56203],
      popup="Interchange 21",
      icon=folium.Icon(color='black', icon='credit-card'),
    ).add_to(marker_cluster)

folium.Marker(
      location=[13.736808, 100.56203],
      popup="Interchange 21",
      icon=folium.Icon(color='black', icon='credit-card'),
    ).add_to(marker_cluster)

#folium.TopoJson(
#    open(antarctic_ice_shelf_topo),
#    'objects.antarctic_ice_shelf',
#    name='topojson'
#).add_to(m)

#folium.LayerControl().add_to(m)

m

