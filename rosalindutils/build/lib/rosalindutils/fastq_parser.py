from rosalindutils.fastq_read import FastqRead

class FastqParser(object):

    def __init__(self, input_path):
        self.input_path = input_path

    def parse_fastq(self):
        input_file = open(self.input_path, "r")
        all_read_objs = []
        all_lines_in_read = []

        for l in input_file:
            line = l.rstrip()
            
            if len(all_lines_in_read) == 4:
                all_read_objs.append(FastqRead(all_lines_in_read))
                all_lines_in_read = []

            all_lines_in_read.append(line)

        all_read_objs.append(FastqRead(all_lines_in_read))

        return all_read_objs

    def convert_fastq_to_fasta(read):
        new_header = re.sub("^@", ">", read[0])
        new_seq = read[1]

        return new_header + new_seq
