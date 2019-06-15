class FastqRead(object):

    def __init__(self, lines):
        self.header = lines[0]
        self.seq = lines[1]
        self.spacer = lines[2]
        self.quality = lines[3]
