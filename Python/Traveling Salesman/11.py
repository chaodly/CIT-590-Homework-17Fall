import math
def read_cities(file_name):
    '''Read in the cities from the given file_name, \
       and return them as a list of four-tuples: \
       [(state, city, latitude, longitude), ...] \
       Use this as your initial road_map, that is, \
       the cycle Alabama → Alaska → Arizona → ... → Wyoming → Alabama.'''
    cities = [] # a list contains all the cities
    
    infile = open ("C:\\Users\\nizhe\\Desktop\\2017Fall\\CIT-590\\HW4\\" + file_name, 'r')
    
    with open(file_name) as file_object:
        lines = file_object.readlines()
        
    for line in lines:
        line_s = line.strip() # delete blank space
        cities.append(line_s.split('\t')) # use '\t' as a seperator
        # at this moment, cities is a long list, whose components are all short lists, \
        # containing information of each state

    city_info_list = [] # a new list used for containing 4-tuples
    
    for city in cities:
        # city is the short list, which contains information of each city,
        # e.g. ['Alabama', 'Montgomery', '32.361538', '-86.279118']
        
        city_info = (city[0],city[1],city[2],city[3])
        city_info_list.append(city_info)

    return city_info_list
    

def print_cities(road_map):
    '''Prints a list of cities, along with their locations. \
       Print only one or two digits after the decimal point.'''
    road_map = read_cities(file_name)
    city_info_s_list = []
    for i in range(len(road_map)):
        road_map[i] = road_map[i][1:]
        # road_map is a list, contains tuples,such as ('Montgomery', '32.361538', '-86.279118')
        a = road_map[i][1]
        b = road_map[i][2]
        city_info_s = (road_map[i][0], round(float(a),2),round(float(b),2))
        city_info_s_list.append(city_info_s)
    print (city_info_s_list)
    
file_name = 'city-data.txt'
road_map = read_cities(file_name)
print_cities(road_map)
