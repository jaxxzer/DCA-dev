
from optparse import OptionParser

parser = OptionParser()
parser.add_option("--in", dest="infile", help="Input file")
parser.add_option("--out", dest="outfile", default="log_x.csv", help="Output file")
(options,args) = parser.parse_args()

f = open(options.infile, "r")

lines = f.readlines()

f.close()

o = open(options.outfile, "w")
for line in lines:
    s = line.split('\t')
    id = s[0]

    o.write(str(s[1]))
    for i in range(0,int(id)+1):
        o.write('\t')
    o.write(str(s[2]))

o.close()
    
