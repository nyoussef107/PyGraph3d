class Polygon():
    def __init__(self, pts, color, distance):
        self.points = pts
        self.color = color
        self.distance = distance

    def sort_polygons(poly_list):
        "ignore this"
        is_sorted = False
        while not is_sorted:
            is_sorted = True
            for i in range(len(poly_list) - 1):
                if (poly_list[i].distance < poly_list[i + 1].distance):
                    poly_list[i + 1], poly_list[i] = poly_list[i], poly_list[i + 1]
                    is_sorted = False           
        
