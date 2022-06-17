from line_protocol_parser import parse_line
with open('/home/syedasamreen/Downloads/ipmidata.txt  ', 'r') as f_obj:
    for line in f_obj:
        print(parse_line(line))