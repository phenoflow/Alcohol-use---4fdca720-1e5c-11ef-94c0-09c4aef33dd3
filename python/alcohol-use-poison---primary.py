# A. John, S. Rees, 2024.

import sys, csv, re

codes = [{"code":"U4091","system":"readv2"},{"code":"U209y","system":"readv2"},{"code":"U1A91","system":"readv2"},{"code":"U4095","system":"readv2"},{"code":"U1A9.","system":"readv2"},{"code":"U4092","system":"readv2"},{"code":"U409z","system":"readv2"},{"code":"U2091","system":"readv2"},{"code":"U4097","system":"readv2"},{"code":"U2094","system":"readv2"},{"code":"U1A93","system":"readv2"},{"code":"U4096","system":"readv2"},{"code":"U1A9z","system":"readv2"},{"code":"U4093","system":"readv2"},{"code":"U2095","system":"readv2"},{"code":"U1A90","system":"readv2"},{"code":"U1A95","system":"readv2"},{"code":"U409.","system":"readv2"},{"code":"U1A97","system":"readv2"},{"code":"U1A94","system":"readv2"},{"code":"U4094","system":"readv2"},{"code":"U209.","system":"readv2"},{"code":"U1A96","system":"readv2"},{"code":"U4090","system":"readv2"},{"code":"U2096","system":"readv2"},{"code":"U2090","system":"readv2"},{"code":"U209z","system":"readv2"},{"code":"U1A92","system":"readv2"},{"code":"U2092","system":"readv2"},{"code":"U409y","system":"readv2"},{"code":"SLH3.","system":"readv2"},{"code":"U1A9y","system":"readv2"},{"code":"U2097","system":"readv2"},{"code":"U2093","system":"readv2"},{"code":"X652","system":"readv2"},{"code":"X45","system":"readv2"},{"code":"X655","system":"readv2"},{"code":"X455","system":"readv2"},{"code":"Y157","system":"readv2"},{"code":"X452","system":"readv2"},{"code":"X453","system":"readv2"},{"code":"X651","system":"readv2"},{"code":"Y155","system":"readv2"},{"code":"Y156","system":"readv2"},{"code":"X459","system":"readv2"},{"code":"X450","system":"readv2"},{"code":"X659","system":"readv2"},{"code":"Y151","system":"readv2"},{"code":"Y154","system":"readv2"},{"code":"Y152","system":"readv2"},{"code":"X650","system":"readv2"},{"code":"Y15","system":"readv2"},{"code":"Y158","system":"readv2"},{"code":"X658","system":"readv2"},{"code":"X657","system":"readv2"},{"code":"X656","system":"readv2"},{"code":"X653","system":"readv2"},{"code":"Y159","system":"readv2"},{"code":"Y153","system":"readv2"},{"code":"X65","system":"readv2"},{"code":"X454","system":"readv2"},{"code":"X457","system":"readv2"},{"code":"X456","system":"readv2"},{"code":"X654","system":"readv2"},{"code":"Y150","system":"readv2"},{"code":"X458","system":"readv2"},{"code":"X451","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('alcohol-use-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["alcohol-use-poison---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["alcohol-use-poison---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["alcohol-use-poison---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
