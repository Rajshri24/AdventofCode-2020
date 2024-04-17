file = open("test.txt")
content = file.read()
content_list = content.split("\n\n")

ans = 0

for line in content_list:
    valid = [0, 0, 0, 0, 0, 0, 0]
    fields = 0
    if (line.count(":")==8) or (line.count(":")==7 and line.find("cid")==-1):
        pos_byr = line.find("byr")+len("byr")+1
        pos_iyr = line.find("iyr")+len("iyr")+1
        pos_eyr = line.find("eyr")+len("eyr")+1
        pos_hgt = line.find("hgt")+len("hgt")+1
        pos_hcl = line.find("hcl")+len("hcl")+1
        pos_ecl = line.find("ecl")+len("ecl")+1
        pos_pid = line.find("pid")+len("pid")+1
        pos_cid = line.find("cid")+len("cid")+1

        byr = int(line[pos_byr:pos_byr+4])
        if byr >= 1920 and byr <= 2002:
            valid[0] = 1

        iyr = int(line[pos_iyr:pos_iyr+4])
        if iyr >= 2010 and iyr <= 2020:
            valid[1] = 1

        eyr = int(line[pos_eyr:pos_eyr+4])
        if eyr >=2020 and eyr <= 2030:
            valid[2] = 1


        if line.find("cm") != -1:
            pos_cm = line.find("cm")
            if (pos_cm-pos_hgt > 0) and (pos_cm-pos_hgt < 4):
                hgt_cm = int(line[pos_hgt:pos_cm])
                if hgt_cm >= 150 and hgt_cm <= 193:
                 valid[3] = 1
        elif line.find("in") != -1:
            pos_in = line.find("in")
            if (pos_in-pos_hgt > 0) and (pos_in-pos_hgt < 4):
                hgt_in = int(line[pos_hgt:pos_in])
                if hgt_in >= 59 and hgt_in <= 96:
                 valid[3] = 1
        count = 0
        if line.find("#") != -1:
            if (line[pos_hcl+1:pos_hcl+7]).isalnum() == True:
                ascii = [ord(c) for c in (line[pos_hcl+1:pos_hcl+7])]
                for i in ascii:
                    if (i>=97 and i<=102) or (i>=48 and i<=57):
                        count = count+1
                if count == 6:
                    valid[4] = 1
        
        ecl_list = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        ecl = line[pos_ecl:pos_ecl+3]
        tick = 0
        for j in ecl_list:
            if ecl == j:
                tick = tick+1
        if tick == 1:
            valid[5] = 1
        
        pid = line[pos_pid:pos_pid+9]
        ptick = 0
        if pid.isdigit() == True:
            ptick = ptick+1
        if ptick >= 1:
            valid[6] = 1
        for k in valid:
            if k == 1:
                fields = fields+1
        if fields == 7:
            ans = ans+1
print(ans)        






        

        
