# Zhengchao Ni
# 73173892

import math
import random
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
        city_info_s = (road_map[i][0], round(float(a),2),round(float(b),2)) # change into standard form
        city_info_s_list.append(city_info_s)
    # print (city_info_s_list) # a list contains tuples, ('Montgomery', '32.36', '-86.27')
    return city_info_s_list
    
def sed(a, b):
    # I just suppose the data from the txt is the coordinate of a city (ignore the physic)
    # I know that represents the longitude and latitude of a city
    # whose distance cannot be calculated simply by Euclidean formula
    ''' compute the standard Euclidean distance, a and b can be 3-element tuples'''
    return round(math.sqrt((a[-1] - b[-1]) ** 2 + (a[-2] - b[-2]) ** 2), 2)

def compute_total_distance(road_map):
    '''Returns, as a floating point number, \
       the sum of the distances of all the connections in the road_map. \
       Remember that it's a cycle, so that (for example) in the initial road_map, \
       Wyoming connects to Alabama. \
       Note: The Earth is not flat so Euclidean distance will not be \
       the actual *physical* distance between two cities but, \
       as usual, let’s ignore physics.'''
    total_distance = 0
    for i in range(0, len(road_map) - 1):
        total_distance += sed(road_map[i], road_map[i + 1])
    total_distance += sed(road_map[0], road_map[-1])
    return total_distance

def swap_cities(road_map, index1, index2):
    '''Take the city at location index1 in the road_map, \
       and the city at location index2, swap their positions in the road_map, \
       compute the new total distance, and return the tuple (new_road_map, new_total_distance). \
       Allow the possibility that index1=index2, and handle this case correctly.'''
    temp = road_map[index1]
    road_map[index1] = road_map[index2]
    road_map[index2] = temp
    
    new_total_distance = compute_total_distance(road_map)
    # print ('new road map: ',road_map)
    # print ('new distance: ', new_total_distance)
    new_road_map = road_map
    return (new_road_map, new_total_distance)
    
def find_best_cycle(road_map):
    '''Using swap_cities, find the swap that reduces the total distance by the biggest amount. \
       Repeat until you have performed 1000 swaps or \
       until no swap can further decrease the total distance. \
       This algorithm is called hill climbing, and your solution is a local optimum.'''
    original_total_distance = compute_total_distance(road_map)
    total_distance = original_total_distance
    new_total_distance = 0
    new_distance_list = []
    i = 0
    j = 0
    # fix road_map[0], test which swap (road_map[0] with road_map[i]) reduce the most
    # then fix road_map[1], then road_map[2]...until road_map[50]
    
    for m in range(50):
        for index1 in range(len(road_map)):
            for index2 in range(len(road_map)):
                new_road_map, new_total_distance = swap_cities(road_map, index1, index2)
                if new_total_distance < total_distance:
                    i, j = index1, index2
                    total_distance = new_total_distance
                swap_cities(road_map, index1, index2)
                # just compare, not truly swap, so change back to the original list
                
            swap_cities(road_map, i, j) # real swap is here
            
    return new_road_map, round(total_distance, 2)

def print_map(road_map):
    '''Prints, in an easily understandable format, the cities and their connections, \
       along with the cost for each connection and the total cost.'''
    for i in range (0, len(road_map) - 1):
        distance = sed(road_map[i], road_map[i+1])
        distance = round(distance, 2)
        print ('*[' + str(road_map[i][0]) + ']*' + '----' + '(' + 'distance: '+ \
               str(distance) + ')' + '---->', end = '')
    print (('*[' + str(road_map[-1][0]) + ']*' + '----' + '(' + 'distance: ' + str(distance) + ')'\
            + '---->' + '*[' + str(road_map[0][0]) + ']*'))
def main():
    '''Reads in and prints out the city data, then creates the "best" cycle and prints it out.'''
    
    global file_name
    file_name = 'city-data.txt'
    road_map = read_cities(file_name)
    road_map = print_cities(road_map)
    # up to now, read the file and print it in a standard form
    r_min = [] # minimum road_map
    d_min = [] # minimum distance
    for i in range(3):
        random.shuffle(road_map)
        [new_road_map, new_distance] = find_best_cycle(road_map)
        r_min.append([new_road_map, new_distance])
    flag = 0
    if r_min[0][1] > r_min[1][1]:
        if r_min[1][1] > r_min[2][1]:
            d_min = r_min[2][1]
            flag = 2
        else:
            d_min = r_min[1][1]
            flag = 1
    else:
        d_min = r_min[0][1]
        flag = 0
    print ('The total distance is: ', d_min)
    print ('========================================= Map =========================================')
    print_map(r_min[flag][0])
    print ('=======================================================================================')

if __name__ == '__main__':
    main()
    
