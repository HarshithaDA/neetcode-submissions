class CountSquares:

    def __init__(self):
        self.ptscount = defaultdict(int)
        self.pts = []
        

    def add(self, point: List[int]) -> None:
        # add point count to hashmap
        # store counts of each of the points with a hashmap
        self.ptscount[tuple(point)] += 1
        self.pts.append(point)
        

    def count(self, point: List[int]) -> int:
        # how many squares are we able to make with this new input query point and our original points in our list
        res = 0
        
        # height and width has to be equal for square
        # check if two diagonal points (x,y) & (px,py) can form a square -> if above condition statisfies
        # check if there exists a top left & bottom right points - (x,py) and (px, y)

        px, py = point

        # iterate thru list
        for x, y in self.pts:
            if (abs(py-y) != abs(px-x)) or x == px or y == py:
                # its not a square if area not postive and h&b not equal
                # if they are stacked on top also - skip thru this point
                continue

            # these are diagonal poitns
            # check if there exists a top left & bottom right points - (x,py) and (px, y)
            res += self.ptscount[(x,py)] * self.ptscount[(px, y)] 

        return res


            



