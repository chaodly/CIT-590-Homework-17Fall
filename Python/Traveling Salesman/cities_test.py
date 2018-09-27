import unittest
from cities import *

class Testcitites(unittest.TestCase):

    def test_sed(self):
        a = ('Montgomery', 32.36, -86.28)
        b = ('Harrisburg', 40.27, -76.88)
        c = ('Hartford', 41.77, -72.68)
        self.assertEqual(sed(a, b), 12.29)
        self.assertEqual(sed(b, c), 4.46)
        self.assertEqual(sed(a, c), 16.54)
        
    def test_compute_total_distance(self):
        road_map = [('Montgomery', 32.36, -86.28), ('Harrisburg', 40.27, -76.88),
                    ('Hartford', 41.77, -72.68),('Montpelier', 44.27, -72.57),
                    ('Boston', 42.24, -71.03), ('Jefferson City', 38.57, -92.19),
                    ('Lincoln', 40.81, -96.68), ('Atlanta', 33.76, -84.39),
                    ('Indianapolis', 39.79, -86.15), ('Topeka', 39.04, -95.69),
                    ('Baton Rouge', 30.46, -91.14), ('Denver', 39.74, -104.98),
                    ('Columbus', 39.96, -83.0), ('Annapolis', 38.97, -76.5),
                    ('Trenton', 40.22, -74.76),('Albany', 42.66, -73.78),
                    ('Lansing', 42.73, -84.55), ('Springfield', 39.78, -89.65),
                    ('Columbia', 34.0, -81.03), ('Nashville', 36.16, -86.78),
                    ('Charleston', 38.35, -81.63),('Providence', 41.82, -71.42),
                    ('Richmond', 37.54, -77.46), ('Dover', 39.16, -75.53),
                    ('Raleigh', 35.77, -78.64), ('Augusta', 44.32, -69.77),
                    ('Helana', 46.6, -112.03), ('Boise', 43.61, -116.24),
                    ('Carson City', 39.16, -119.75), ('Pierre', 44.37, -100.34),
                    ('Jackson', 32.32, -90.21), ('Concord', 43.22, -71.55),
                    ('Madison', 43.07, -89.38), ('Tallahassee', 30.45, -84.27), 
                    ('Oklahoma City', 35.48, -97.53), ('Des Moines', 41.59, -93.62),
                    ('Phoenix', 33.45, -112.07), ('Salt Lake City', 40.75, -111.89),
                    ('Olympia', 47.04, -122.89), ('Salem', 44.93, -123.03),
                    ('Sacramento', 38.56, -121.47), ('Juneau', 58.3, -134.42),
                    ('Honolulu', 21.31, -157.83), ('Cheyenne', 41.15, -104.8),
                    ('Frankfort', 38.2, -84.86), ('Little Rock', 34.74, -92.33),
                    ('Austin', 30.27, -97.75), ('Bismarck', 48.81, -100.78),
                    ('Santa Fe', 35.67, -105.96), ('Saint Paul', 44.95, -93.09)]
        self.assertEqual(compute_total_distance(road_map), 649.22)
    def test_swap_cities(self):
        road_map = [('Montgomery', 32.36, -86.28), ('Harrisburg', 40.27, -76.88),
                    ('Hartford', 41.77, -72.68),('Montpelier', 44.27, -72.57),
                    ('Boston', 42.24, -71.03), ('Jefferson City', 38.57, -92.19),
                    ('Lincoln', 40.81, -96.68), ('Atlanta', 33.76, -84.39),
                    ('Indianapolis', 39.79, -86.15), ('Topeka', 39.04, -95.69),
                    ('Baton Rouge', 30.46, -91.14), ('Denver', 39.74, -104.98),
                    ('Columbus', 39.96, -83.0), ('Annapolis', 38.97, -76.5),
                    ('Trenton', 40.22, -74.76),('Albany', 42.66, -73.78),
                    ('Lansing', 42.73, -84.55), ('Springfield', 39.78, -89.65),
                    ('Columbia', 34.0, -81.03), ('Nashville', 36.16, -86.78),
                    ('Charleston', 38.35, -81.63),('Providence', 41.82, -71.42),
                    ('Richmond', 37.54, -77.46), ('Dover', 39.16, -75.53),
                    ('Raleigh', 35.77, -78.64), ('Augusta', 44.32, -69.77),
                    ('Helana', 46.6, -112.03), ('Boise', 43.61, -116.24),
                    ('Carson City', 39.16, -119.75), ('Pierre', 44.37, -100.34),
                    ('Jackson', 32.32, -90.21), ('Concord', 43.22, -71.55),
                    ('Madison', 43.07, -89.38), ('Tallahassee', 30.45, -84.27), 
                    ('Oklahoma City', 35.48, -97.53), ('Des Moines', 41.59, -93.62),
                    ('Phoenix', 33.45, -112.07), ('Salt Lake City', 40.75, -111.89),
                    ('Olympia', 47.04, -122.89), ('Salem', 44.93, -123.03),
                    ('Sacramento', 38.56, -121.47), ('Juneau', 58.3, -134.42),
                    ('Honolulu', 21.31, -157.83), ('Cheyenne', 41.15, -104.8),
                    ('Frankfort', 38.2, -84.86), ('Little Rock', 34.74, -92.33),
                    ('Austin', 30.27, -97.75), ('Bismarck', 48.81, -100.78),
                    ('Santa Fe', 35.67, -105.96), ('Saint Paul', 44.95, -93.09)]
        new_road_map = [('Harrisburg', 40.27, -76.88),('Montgomery', 32.36, -86.28), 
                    ('Hartford', 41.77, -72.68),('Montpelier', 44.27, -72.57),
                    ('Boston', 42.24, -71.03), ('Jefferson City', 38.57, -92.19),
                    ('Lincoln', 40.81, -96.68), ('Atlanta', 33.76, -84.39),
                    ('Indianapolis', 39.79, -86.15), ('Topeka', 39.04, -95.69),
                    ('Baton Rouge', 30.46, -91.14), ('Denver', 39.74, -104.98),
                    ('Columbus', 39.96, -83.0), ('Annapolis', 38.97, -76.5),
                    ('Trenton', 40.22, -74.76),('Albany', 42.66, -73.78),
                    ('Lansing', 42.73, -84.55), ('Springfield', 39.78, -89.65),
                    ('Columbia', 34.0, -81.03), ('Nashville', 36.16, -86.78),
                    ('Charleston', 38.35, -81.63),('Providence', 41.82, -71.42),
                    ('Richmond', 37.54, -77.46), ('Dover', 39.16, -75.53),
                    ('Raleigh', 35.77, -78.64), ('Augusta', 44.32, -69.77),
                    ('Helana', 46.6, -112.03), ('Boise', 43.61, -116.24),
                    ('Carson City', 39.16, -119.75), ('Pierre', 44.37, -100.34),
                    ('Jackson', 32.32, -90.21), ('Concord', 43.22, -71.55),
                    ('Madison', 43.07, -89.38), ('Tallahassee', 30.45, -84.27), 
                    ('Oklahoma City', 35.48, -97.53), ('Des Moines', 41.59, -93.62),
                    ('Phoenix', 33.45, -112.07), ('Salt Lake City', 40.75, -111.89),
                    ('Olympia', 47.04, -122.89), ('Salem', 44.93, -123.03),
                    ('Sacramento', 38.56, -121.47), ('Juneau', 58.3, -134.42),
                    ('Honolulu', 21.31, -157.83), ('Cheyenne', 41.15, -104.8),
                    ('Frankfort', 38.2, -84.86), ('Little Rock', 34.74, -92.33),
                    ('Austin', 30.27, -97.75), ('Bismarck', 48.81, -100.78),
                    ('Santa Fe', 35.67, -105.96), ('Saint Paul', 44.95, -93.09)]
        self.assertEqual(swap_cities(road_map, 0, 1), (new_road_map, 663.86))
    def test_find_best_cycle(self):
        road_map = [('Montgomery', 32.36, -86.28), ('Harrisburg', 40.27, -76.88), \
                    ('Hartford', 41.77, -72.68), ('Montpelier', 44.27, -72.57), \
                    ('Boston', 42.24, -71.03), ('Jefferson City', 38.57, -92.19), \
                    ('Lincoln', 40.81, -96.68), ('Atlanta', 33.76, -84.39), \
                    ('Indianapolis', 39.79, -86.15), ('Topeka', 39.04, -95.69), \
                    ('Baton Rouge', 30.46, -91.14), ('Denver', 39.74, -104.98), \
                    ('Columbus', 39.96, -83.0), ('Annapolis', 38.97, -76.5), \
                    ('Trenton', 40.22, -74.76), ('Albany', 42.66, -73.78), \
                    ('Lansing', 42.73, -84.55), ('Springfield', 39.78, -89.65), \
                    ('Columbia', 34.0, -81.03), ('Nashville', 36.16, -86.78), \
                    ('Charleston', 38.35, -81.63), ('Providence', 41.82, -71.42), \
                    ('Richmond', 37.54, -77.46), ('Dover', 39.16, -75.53), \
                    ('Raleigh', 35.77, -78.64), ('Augusta', 44.32, -69.77), \
                    ('Helana', 46.6, -112.03), ('Boise', 43.61, -116.24), \
                    ('Carson City', 39.16, -119.75), ('Pierre', 44.37, -100.34), \
                    ('Jackson', 32.32, -90.21), ('Concord', 43.22, -71.55), \
                    ('Madison', 43.07, -89.38), ('Tallahassee', 30.45, -84.27), \
                    ('Oklahoma City', 35.48, -97.53), ('Des Moines', 41.59, -93.62), \
                    ('Phoenix', 33.45, -112.07), ('Salt Lake City', 40.75, -111.89), \
                    ('Olympia', 47.04, -122.89), ('Salem', 44.93, -123.03), \
                    ('Sacramento', 38.56, -121.47), ('Juneau', 58.3, -134.42), \
                    ('Honolulu', 21.31, -157.83), ('Cheyenne', 41.15, -104.8), \
                    ('Frankfort', 38.2, -84.86), ('Little Rock', 34.74, -92.33), \
                    ('Austin', 30.27, -97.75), ('Bismarck', 48.81, -100.78), \
                    ('Santa Fe', 35.67, -105.96), ('Saint Paul', 44.95, -93.09)]
        self.assertEqual(find_best_cycle(road_map), \
                         ([('Montpelier', 44.27, -72.57), ('Augusta', 44.32, -69.77), \
                           ('Boston', 42.24, -71.03), ('Providence', 41.82, -71.42), \
                           ('Harrisburg', 40.27, -76.88), ('Atlanta', 33.76, -84.39), \
                           ('Tallahassee', 30.45, -84.27), ('Montgomery', 32.36, -86.28), \
                           ('Jefferson City', 38.57, -92.19), ('Saint Paul', 44.95, -93.09), \
                           ('Madison', 43.07, -89.38), ('Springfield', 39.78, -89.65), \
                           ('Indianapolis', 39.79, -86.15), ('Columbus', 39.96, -83.0), \
                           ('Charleston', 38.35, -81.63), ('Columbia', 34.0, -81.03), \
                           ('Raleigh', 35.77, -78.64), ('Richmond', 37.54, -77.46), \
                           ('Annapolis', 38.97, -76.5), ('Dover', 39.16, -75.53), \
                           ('Trenton', 40.22, -74.76), ('Hartford', 41.77, -72.68), \
                           ('Concord', 43.22, -71.55), ('Albany', 42.66, -73.78), \
                           ('Lansing', 42.73, -84.55), ('Bismarck', 48.81, -100.78), \
                           ('Helana', 46.6, -112.03), ('Boise', 43.61, -116.24), \
                           ('Salt Lake City', 40.75, -111.89), ('Santa Fe', 35.67, -105.96), \
                           ('Oklahoma City', 35.48, -97.53), ('Topeka', 39.04, -95.69), \
                           ('Lincoln', 40.81, -96.68), ('Des Moines', 41.59, -93.62), \
                           ('Pierre', 44.37, -100.34), ('Cheyenne', 41.15, -104.8), \
                           ('Denver', 39.74, -104.98), ('Carson City', 39.16, -119.75), \
                           ('Sacramento', 38.56, -121.47), ('Salem', 44.93, -123.03), \
                           ('Olympia', 47.04, -122.89), ('Juneau', 58.3, -134.42), \
                           ('Honolulu', 21.31, -157.83), ('Phoenix', 33.45, -112.07), \
                           ('Austin', 30.27, -97.75), ('Baton Rouge', 30.46, -91.14), \
                           ('Jackson', 32.32, -90.21), ('Little Rock', 34.74, -92.33), \
                           ('Nashville', 36.16, -86.78), ('Frankfort', 38.2, -84.86)], 348.96))
unittest.main()
