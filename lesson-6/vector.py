class Vector:
    def __init__(self, *args):
        self.coords = list(args)
        # print(self.coords)

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, index):
        print('Executing for index:', index)
        return self.coords[index]

    def __iter__(self):
        print('Inside __iter__ method')
        coords = self.coords.copy()
        for coor in coords:
            yield coor

# v1 = Vector(1, 2)
# print("lenght v1:", len(v1))  # 2
v2 = Vector(1, 2, 5, 7, 9, 4, 2)
# print(v2[1:3])

for i in v2:
    print(i)