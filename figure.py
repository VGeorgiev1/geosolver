import json

class Figure:
    def __init__(self):
        self.points = {}
        self.lines = []
        self.circles = []
    def point(self, name):
        self.points[name] = {"name": name}
    def line(self, a, b, name=None):
        self.lines.append({
            "name": name,
            "a": a,
            "b": b
        })
    def circle(self, O, r):
        self.circles.append({
            "O": O,
            "r": r
        })
    def set_point(self, name, x, y):
        if(name in self.points):
            self.points[name]["x"] = x
            self.points[name]["y"] = y
    def get_data(self):
        lines = []
        for l in self.lines:
            if(l["a"] in self.points and l["b"] in self.points):
                p1 = self.points[l["a"]]
                p2 = self.points[l["b"]]
                if("x" in p1 and "x" in p2):
                    lines.append({
                        "x1":p1["x"], 
                        "x2":p2["x"], 
                        "y1":p1["y"], 
                        "y2":p2["y"]})
        circles = []
        for l in self.circles:
            if(l["O"] in self.points and l["r"] in self.points):
                p1 = self.points[l["O"]]
                p2 = self.points[l["r"]]
                if("x" in p1 and "x" in p2):
                    circles.append({"center":p1,
                        "r":p2})
        return json.dumps({
            "points": list(self.points.values()),
            "lines": lines,
            "circles": circles
        })