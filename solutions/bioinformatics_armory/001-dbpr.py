"""Solution for Bioinformatics Armory Problem ID: DBPR

Problem Title: Introduction to Protein Databases
Link: http://rosalind.info/problems/dbpr
"""

import requests
import re

go_pattern = re.compile("^DR\s+GO")
go_process_pattern = re.compile("^DR\s+GO; GO:.+?; P:(.+?);")

input_path = "data/rosalind_dbpr.txt"
input_file = open(input_path, "r")
uniprot_id = input_file.readline().rstrip()
input_file.close()

url = "http://www.uniprot.org/uniprot/" + uniprot_id + ".txt"
response = requests.get(url)
response_lines = response.text.split("\n")

go_lines = [l for l in response_lines if go_pattern.search(l)]
go_process_lines = [l for l in go_lines if go_process_pattern.search(l)]

processes = []
for go_process_line in go_process_lines:
    process = go_process_pattern.search(go_process_line).group(1)
    processes.append(process)

print("\n".join(processes))
