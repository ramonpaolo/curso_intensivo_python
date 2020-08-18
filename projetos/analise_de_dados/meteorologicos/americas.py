from pygal_maps_world.maps import World

py = World()
py.add("America do Norte", ["ca", "mx", "us"])
py.add("Ameria Central", {"bz": 100, "cr":1, "gt":1, "hn":1, "ni":2})
py.add("America do Sul", ["ar", ("br", 10002), "bo", "cl", "co"])
py.render_to_file("americas.svg")