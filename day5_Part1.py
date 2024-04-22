file = open("input.txt")
content = file.read()
content_list = content.split("\n")

seatID = []
for line in content_list:
    if len(line) == 10 and line.isalpha(): 
     change = str.maketrans({"F":"0", "B":"1", "L":"0", "R":"1"})
     new_line = line.translate(change)
     row_bi = new_line[0:7]
     col_bi = new_line[7:10]
     row = int(row_bi,2)
     col = int(col_bi,2)
     ID = (row*8) + col
     seatID.append(ID)
print(max(seatID))
