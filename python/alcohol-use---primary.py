# A. John, S. Rees, 2024.

import sys, csv, re

codes = [{"code":"1B1c.","system":"readv2"},{"code":"8BAs.","system":"readv2"},{"code":"8BAw.","system":"readv2"},{"code":"136S.","system":"readv2"},{"code":"F25B.","system":"readv2"},{"code":"13Y8.","system":"readv2"},{"code":"9NN2.","system":"readv2"},{"code":"136c.","system":"readv2"},{"code":"E2502","system":"readv2"},{"code":"8G32.","system":"readv2"},{"code":"F1440","system":"readv2"},{"code":"8H7p.","system":"readv2"},{"code":"E2501","system":"readv2"},{"code":"Eu108","system":"readv2"},{"code":"Eu107","system":"readv2"},{"code":"8IEA.","system":"readv2"},{"code":"F11x0","system":"readv2"},{"code":"9k1..","system":"readv2"},{"code":"E015.","system":"readv2"},{"code":"E01..","system":"readv2"},{"code":"G312","system":"readv2"},{"code":"E244","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('alcohol-use-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["alcohol-use---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["alcohol-use---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["alcohol-use---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
