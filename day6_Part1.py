file = open("input.txt")
content = file.read()
content_list = content.split("\n\n")

def countDis(str):
 
    # Stores all distinct characters
    s = set(str)
 
    # Return the size of the set
    return len(s)

ans = 0
for i in content_list:
    if "\n" in i:
        count = countDis(i) - 1
    else:
        count = countDis(i)
    ans += count
print(ans)