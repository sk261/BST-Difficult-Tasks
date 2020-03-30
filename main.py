import bst


helpMessage = \
"""
/help               print help message
/load <filename>    loads the file into a binary search tree
/save <filename>    saves the binary search tree into a file
/view               prints the binary search tree
/q or /exit         ends the program
<task of the day>   If you enter in a task of the day, we'll traverse the tree and find it's relative difficulty
"""

affirmations = ["yes", "1", "y", "ye", "mhm", "yep", 1]


print("Welcome to Shay's BST Difficult Task Analyzer. If you need help, enter /help")

currentBST = None
while True:
    print("Enter in your next task (as an active verb): ")
    i = input().strip()
    if i[0] == "/":
        command = i.split(' ')[0][1:].lower()
        param = " ".join(i.split(" ")[1:])
        if command == "help":
            print(helpMessage)
        elif command == "save":
            if not currentBST is None:
                currentBST.saveArr(param)
            continue
        elif command == "load":
            currentBST = bst.BinarySearchNode(file=param)
            continue
        elif command == "view":
            print(currentBST)
            continue
        elif command in ["q", "exit"]:
            quit()
    else:
        if currentBST is None:
            currentBST = bst.BinarySearchNode(data=i)
            print("This is a good start! What else do you plan to do today?")
        else:
            marker = currentBST
            while True:
                print("Is it harder than " + marker.data + "?")
                j = input().strip().lower()
                if j in affirmations:
                    if marker.right is None:
                        marker.right = bst.BinarySearchNode(data=i)
                        break
                    else:
                        marker = marker.right
                        continue
                print("Is it easier than " + marker.data + "?")
                j = input().strip().lower()
                if j in affirmations:
                    if marker.left is None:
                        marker.left = bst.BinarySearchNode(data=i)
                        break
                    else:
                        marker = marker.left
                        continue
                print("Okay, then I'll add " + marker.data + " and " + i + " together.")
                marker.data = marker.data + " or " + i
                break

            print("Added to your tree! What else do you plan to do today?")