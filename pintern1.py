import json, collections, time
global bots
bots = []

def bot_detection(input_file_path):

#Define variables and open the file
    log = open(input_file_path, 'r')
    multiple_actions = False
    repeat_actions = False
    access = {}
    action = []
    timestamp = []
    count_chocula = []

#pull needed info from file
    for use in log:
        access = json.loads(use)
        user = access["user"]

#search log for username & add actions and timestamps to list
        if user in line:
            action.append(access["action"])
            timestamp.append(access["timestamp"])
            act = collections.Counter(action)

#Look for frequency
            time = 15*60
            timestamp.sort()
            #print timestamp
            #print multiple_actions
            for i in range(len(timestamp)):
                for h in range(i+1, len(timestamp)):
                    count_chocula = cmp(i, h)
            """CC should be an evaluation compating each value with the ones around it in the list.
            Can't quite figure out how to compare them all to a 360 range.
            Stack overflow recommended intertools?"""

            if count_chocula >= 15:
                multiple_actions = True
            else:
                multiple_actions = False

#Look for duplicate actions
            if {k:v for (k,v) in act.items() if v>=7}:
                repeat_actions = True
            else:
                repeat_actions = False

#Sort to bot and add user if needed
            if multiple_actions = True and repeat_actions = True:
                bots.append(user)
    log.close()
    bots.sort()

bot_detection(filepath)
print("The following users have been declared as bots: ", bots)

