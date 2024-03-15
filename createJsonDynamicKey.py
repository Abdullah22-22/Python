# import json

# # Navigation text for options
# navText = """
# 1: Wipe Data
# 2: Create Data
# 3: Exit
# """

# # Function to get user input for key-value pair
# def getInput():
#     valueList = []
#     keyList = []
#     print("To stop adding values, Enter without data")
#     while True:
#         value = input("Enter value: ")
#         if not value:
#             break
#         else:
#             try:
#                 valueList.append(value)
#             except Exception as e:
#                 print(f"ERROR: {e}")
#     for i, value in enumerate(valueList, start=1): # More sophisticated "for loop"
#         keyList.append(f"key{i}")
#     print(keyList)
#     return dict(zip(keyList, valueList))  # Create dictionary using zip

# # Function to wipe the JSON file
# def wipeData():
#     confirmation = input("Are you sure you want to wipe the JSON file? (yes/no): ")
#     if confirmation.lower() in ("yes","y"):
#         with open('data.json', 'w') as file:
#             file.write("")
#         print("JSON file wiped successfully.")
#     else:
#         print("Wipe operation aborted.")

# # Function to create or update data in the JSON file
# def createData():
#     try:
#         while True:
#             dictZip = getInput()

#             # Read existing JSON data or initialize as empty dictionary
#             try:
#                 with open('data.json', 'r') as file:
#                     existingData = json.load(file)
#             except (FileNotFoundError, json.JSONDecodeError):
#                 existingData = {}

#             # Update data with new input
#             existingData.update(dictZip)

#             # Write updated data back to the file
#             with open('data.json', 'w') as file:
#                 json.dump(existingData, file, indent=4)
#             print("JSON file updated successfully.")

#             # Ask if user wants to continue adding data
#             userInput = input("Do you want to stop (yes/no(Enter)): ")
#             if userInput.lower() in ("yes", "y"):
#                 break

#     except FileNotFoundError:
#         print("Error: JSON file not found.")
#     except PermissionError:
#         print("Error: Permission denied to write to JSON file.")
#     except OSError as e:
#         print(f"Error: {e.strerror} - {e.filename}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# # Function to handle navigation options
# def navOption():
#     while True:
#         print(navText)
#         userInput = str(input("Option: "))
#         match userInput:
#             case "1":
#                 wipeData()
#             case "2":
#                 createData()
#             case "3":
#                 print("Shutting down...")
#                 exit()
#             case _ :
#                 continue

# # Start the navigation
# navOption()

       
import json

navText = """
1: Wipe Data
2: Create Data
3: Exit
"""
def getinpu():
        keyList=[]
        valueList=[]
        while True:
                        
                value=input("enter value: ")
                if not value:
                        break
                else:
                        valueList.append(value)
        for i,value in enumerate(valueList, start=1):
                        keyList.append(f"key:{i}")
                
        return dict(zip(keyList,valueList))
def WipeData():
        wipe_input=input("if u want delet press (yes,y)")
        if wipe_input.lower() in ("yes","y"):
                with open("data.json","w")as f:
                        f.write("")
                        print("file is cler")
        else:
                print("failed")

def CreateData():
        
        while True:
                dictzip= getinpu()
                try:
                        with open ("data.json","r")as f:
                                data= json.load(f)
                except(FileNotFoundError,json.JSONDecodeError):
                        data={}
                        data.update(dictzip)
                        with open("data.json","w")as f:
                                json.dump(data,f,indent=4)
                continue_input=input("if u want stop pres(yes,y): ")
                if continue_input.lower() in ("yes","y"):
                        break
def nav():

        while True:
                print(navText)
                navText_input=str(input("enetr number:"))
                match navText_input:
                        case "1":
                                WipeData()
                        case "2":
                                CreateData()
                        case "3":
                                exit()
                        case _:
                                continue
nav()
          