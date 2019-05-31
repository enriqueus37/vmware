# To get log file:
#   git log > log.txt

def parserFunction(file_name):
    log_file = open(file_name, "r")
    productivity = {}

    for line in log_file:
        line_parsed = line.split(" ")
        if line_parsed[0] == "Author:":
            author_name = line_parsed[1] + " " + line_parsed[2].rstrip()
            if author_name in productivity:
                productivity[author_name] += 1
            else:
                productivity[author_name] = 1

    #print(productivity)
    x = lambda y: "commits" if y > 1 else "commit"
    for author in productivity:
        print(author, "made", productivity[author], x(productivity[author]), "in total.")



if __name__ == "__main__":
    file_name = input("Enter file name: ")
    parserFunction(file_name)
