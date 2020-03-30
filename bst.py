class BinarySearchNode:
    def __init__(self, data = None, file = None, arr = None):
        self.data = data
        self.left = None
        self.right = None

        if not arr is None:
            self._buildFromArr(arr)


        if file is None:
            return
        
        f = open(file, "r")
        file_raw = f.read()
        f.close()
        values = file_raw.split("\n")
        self._buildFromArr(values)

    def _buildFromArr(self, arr):
        data = arr.pop(0)
        level = len(data.split('\t'))
        self.data = data.split("\t").pop(-1)
        pieces = []
        for i in range(2):
            if len(arr) > 0:
                if level < len(arr[0].split("\t")):
                    pieces.append(BinarySearchNode(arr = arr))
        for n in pieces:
            if n.data[0] == "-":
                n.data = n.data[1:]
                self.left = n
            else:
                self.right = n

    def saveArr(self, file, level = 0, isLeft = False):
        pfile = file
        if level == 0:
            f = open(file, "w")
            pfile = f

        tabs = ""
        for i in range(level):
            tabs += "\t"
        if isLeft:
            tabs += "-"
        
        pfile.write(tabs + self.data + "\n")
        if not self.left is None:
            self.left.saveArr(pfile, level + 1, True)
        if not self.right is None:
            self.right.saveArr(pfile, level + 1, False)

        if level == 0:
            f.close()

    def __str__(self):
        return self.toString()
    
    def toString(self, level = 0, isLeft = False):
        tabs = ""
        for i in range(level):
            tabs += "\t"
        if isLeft:
            tabs += "-"
        
        ret = tabs + self.data + "\n"
        if not self.left is None:
            ret += self.left.toString(level + 1, True)
        if not self.right is None:
            ret += self.right.toString(level + 1, False)
        if level == 0:
            ret = ret[:-1]
        return ret