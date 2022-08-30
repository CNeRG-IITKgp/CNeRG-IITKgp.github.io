import csv

INFILE = 'CNeRG Datasets - Datasets.csv'
OUTFILE = 'datasets_table'

with open(INFILE) as fp:
    rdr = csv.reader(fp)
    head = next(rdr)
    data = list(rdr)

html = []
# prepare data
for row in data:
    

    links = row[3].split(',')
    if len(links) > 1:
        tmp = []
        for i, line in enumerate(links):
            tmp.append('<a href=' + line.strip() + '>Link %d</a>'%(i + 1))
        row[3] = ', '.join(tmp)
    else:
        row[3] = '<a href=' + row[3].strip() + '>Link</a>'
    

    row = [x.replace('\n', ' ') for x in row]

    tmp = '<tr> <td>' +  '</td> <td>'.join(row) + '</td> </tr>'
    html.append(tmp)


# print to file
with open(OUTFILE, 'w') as fo:
    fo.write('\n'.join(html))