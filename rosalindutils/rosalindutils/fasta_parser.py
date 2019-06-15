class FastaParser(object):

    def __init__(self, input_file):
        self.input_file = input_file

    def parse_fasta(self):

        sequence_obj = {"header": None, "sequence": ""}
        all_sequence_objs = []

        with open(self.input_file, "r") as infile:
            sequence_obj["header"] = infile.readline().rstrip()[1:]

            for line in infile:
                lr = line.rstrip()

                if (lr.startswith(">")):
                    all_sequence_objs.append(sequence_obj)
                    sequence_obj = {"header": lr[1:], "sequence": ""}
                else:
                    sequence_obj["sequence"] += lr

            all_sequence_objs.append(sequence_obj)

        return all_sequence_objs
