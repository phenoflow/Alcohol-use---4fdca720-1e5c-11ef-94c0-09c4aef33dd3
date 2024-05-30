# A. John, S. Rees, 2024.

import sys, csv, re

codes = [{"code":"E014.","system":"readv2"},{"code":"SM021","system":"readv2"},{"code":"SM030","system":"readv2"},{"code":"SM002","system":"readv2"},{"code":"E2300","system":"readv2"},{"code":"SM03.","system":"readv2"},{"code":"SM03z","system":"readv2"},{"code":"E230.","system":"readv2"},{"code":"SM031","system":"readv2"},{"code":"SM0..","system":"readv2"},{"code":"Eu100","system":"readv2"},{"code":"SyuG0","system":"readv2"},{"code":"SM011","system":"readv2"},{"code":"SM0y.","system":"readv2"},{"code":"E230z","system":"readv2"},{"code":"SM0z.","system":"readv2"},{"code":"T51","system":"readv2"},{"code":"T519","system":"readv2"},{"code":"T512","system":"readv2"},{"code":"T518","system":"readv2"},{"code":"T513","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('alcohol-use-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["alcohol-use-intoxication---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["alcohol-use-intoxication---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["alcohol-use-intoxication---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
