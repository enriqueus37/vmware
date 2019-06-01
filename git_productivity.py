# This small program calculates the number of commits per Author and saves it in a dictionary.
# It then prints the number of commits per author and the name of the author.
#
# To get log file to input into program:
#   git log > log.txt
#
#
#
# I also added a second function (commented out in main) that saves the date of when the commit was made. 
# This is not very relevant in terms of productivity of the employee but I wanted to implement it since I mentioned it on the phone call.

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

def parserFunctionWithDates(file_name):        
    f = open(file_name, "r")
    productivity = {}

    for line in f:
        line_parsed = line.split(" ")
        #print(line_parsed[0])
        if line_parsed[0] == "Author:":
            author_name = line_parsed[1] + " " + line_parsed[2].rstrip()
            if author_name in productivity:
                productivity[author_name]["commits"] += 1
            else:
                productivity[author_name] = dict(commits = 1, dates = dict())
        elif line_parsed[0] == "Date:":
            #date = line_parsed[4] + " " + line_parsed[5]
            month = line_parsed[4]
            day = line_parsed[5]
            if month in productivity[author_name]["dates"]:
                if day not in productivity[author_name]["dates"][month]:
                    productivity[author_name]["dates"][month].append(day)
            else:
                productivity[author_name]["dates"][month] = [day]


    print(productivity)
    x = lambda y: "commits" if y > 1 else "commit"
    for author in productivity:
        print(author, "made", productivity[author]["commits"], x(productivity[author]["commits"]), "in total.")


if __name__ == "__main__":
    file_name = input("Enter file name: ")
    parserFunction(file_name)
    #parserFunctionWithDates(file_name)
    
