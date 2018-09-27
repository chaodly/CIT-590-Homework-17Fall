def main():
    players = [] # a list
    d = {} # for every football player create a dictionary
    
    infile = open('football.txt', 'r')
    
    for line in infile:
        line_s = line.strip()
        ls = line_s.split(",")
        d["First Name"] = ls[0]
        d["Last Name"] = ls[1]
        d["Position"] = ls[2]
        d["Team"] = ls[3]
        players.append(d)
    infile.close()

## If you want to use the "with" command, the above code would change to:
##    with open('football.txt', 'r') as infile:
##        lines = infile.readlines()
##        for line in lines:
##            line_s = line.strip()
##            ls = line_s.split(",")
##            d["First Name"] = ls[0]
##            d["Last Name"] = ls[1]
##            d["Position"] = ls[2]
##            d["Team"] = ls[3]
##            players.append(d)

    print(players)    

main()
