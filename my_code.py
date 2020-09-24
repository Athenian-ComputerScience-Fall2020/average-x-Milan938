# Collaborators (including web sites where you got help: (enter none if you didn't need help)
# None

def avg(user_list):
    # Insert code here
    average = sum(user_list) / len(user_list)
    return average


if __name__ == '__main__':
  
    # Put the values you want to test in for x,y and z

    # Now, comment out the print statement and work on the code below
    # Remember to indent in this section
    user_list = [] # start with an empty list

    num = 0
    while num != "done":
        num = input("Enter a number to be averaged, if done type 'done' ")
        if num == "done":
            break
        num = int(num)
        user_list.append(num)

    print(avg(user_list))