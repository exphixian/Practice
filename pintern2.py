import re
global largest_urls
largest_urls = []

def analyze_requests(log_path):
#Define variables
    global largest_urls
    log = open(log_path, 'r')

#Pull necessary information from files (Remove gifs, keep all GETs w/ 200)
    for line in log:
        if "Get" in line and "200" in line and not "gif" in line:
            largest_urls.append(line.split()[-1])
            largest_urls.append(line.split()[6])
        largest_urls = [(largest_urls[i], largest_urls[i+1])
                        for i in range(0, len(largest_urls), 2)]

#Determine average processing time for each URL

#Sort in decreasing value & check for 15 longest processing URLs
    largest_urls.sort(reverse = True)
    while True:
        if len(largest_urls) > 15:
            largest_urls.pop
        elif len(largest_urls) < 15:
            print("There are only %s URLs that qualify." % (len(largest_urls)))
            break
        else:
            break

    log.close()

analyze_requests()
print("The URLs currently taking the most processing time are: ")
for i in range(0,15):
    print(i+1, '.', largest_urls[i][1], " at ", largest_urls[i][0], " seconds.")
