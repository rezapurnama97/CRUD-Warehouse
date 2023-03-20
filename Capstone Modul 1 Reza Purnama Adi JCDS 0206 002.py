itemData =[
    {
        "Item Code" : "RZ101",
        "Item Name" : "Lif Boi",
        "Category" : "Alat Mandi",
        "Stock" : 28,
        "Price/Item" : 10000},
     {
        "Item Code" : "RZ102",
        "Item Name" : "Sampo Klir",
        "Category" : "Alat Mandi",
        "Stock" : 36,
        "Price/Item" : 15000},
    {
        "Item Code" : "RZ103",
        "Item Name" : "Kolgate",
        "Category" : "Alat Mandi",
        "Stock" : 33,
        "Price/Item" : 12000},
    {
        "Item Code" : "RZ201",
        "Item Name" : "Skintifik ",
        "Category" : "Skin Care",
        "Stock" : 40,
        "Price/Item" : 20000},
    {
        "Item Code" : "RZ202",
        "Item Name" : "The Ordinary ",
        "Category" : "Skin Care",
        "Stock" : 32,
        "Price/Item" : 25000}
]

line = ("=")*80

def mainMenu():
    print(line)
    print("-                           Data Gudang Mas Reza                               -")
    print(line)
    print(" ")
    print("""MAIN MENU
1. Read Item data
2. Create Item data
3. Update Item data
4. Delete Item data
5. Exit Program
    
input num 1-5: """)
    mainMenuInput = input("Input : ")
    if mainMenuInput.isdigit():
        if int(mainMenuInput) == 1:
            readData()
        elif int(mainMenuInput) == 2:
            createData()
        elif int(mainMenuInput) == 3:
            updateData()
        elif int(mainMenuInput) == 4:
            deleteDataItem()
        elif int(mainMenuInput) == 5:
            print("terima Kasih")
            global run
            run = 0
    else :
        print("\n")
        print("Please Put Available Number")
        mainMenu()


def readData():
    print(line)
    print("-                                MENU READ DATA                                -")
    print(line)
    print("""
1. Show all item
2. Find item
3. Back to Main Menu
    
input num 1-3""")
    readDataInput = input("Input: ")
    if readDataInput.isdigit():
        if int(readDataInput) == 1:
            print(line)
            print("-                             MENU SHOW ALL ITEM DATA                             -")
            print(line)
            showData()
        elif int(readDataInput) == 2:
            print("-                             MENU FIND ITEM DATA                             -")
            print(line)
            findData()
        elif int(readDataInput) == 3:
            mainMenu()
        else :
            print("Please put available number")
            readData()
    else:
        readData()
    readData()

def showData():
    print("|Item Code\t| Item Name\t\t| Category\t\t| Stock\t| Price|")
    for i in range(len(itemData)):
            print(f"""|{itemData[i]["Item Code"]}\t\t| {itemData[i]["Item Name"]}\t\t| {itemData[i]["Category"]}\t\t| {itemData[i]["Stock"]} \t| {itemData[i]["Price/Item"]}|""")
    print("\n")

def findData():
    itemCode= input("Input Item Code: ").upper()
    for i in range(len(itemData)):
        if itemCode == itemData[i]["Item Code"]:
            print("|Item Code\t| Item Name\t\t| Category\t\t| Stock\t| Price/item\t|")
            print(f"""|{itemData[i]["Item Code"]}\t\t| {itemData[i]["Item Name"]}\t\t| {itemData[i]["Category"]}\t\t| {itemData[i]["Stock"]} \t| {itemData[i]["Price/Item"]}\t|""")
            print("\n")
            break
        elif (i == len(itemData)-1):
            print("\n-                                Data is not available                                -")
            print("\n")   

def createData():
    print(line)
    print("-                             MENU CREATE DATA                             -")
    print(line)
    print("1. Add Item")
    print("2. Back to Main Menu""")
    createDataInput= input("Input 1-2: ")
    if createDataInput.isdigit():
        if int(createDataInput) == 1:
            print(line)
            print ("-                             ADD DATA                             -")
            addData()
        elif int(createDataInput) == 2:
            mainMenu()
        else:
            print("Please input available option (1-2)")
            createData()
    else:
        print("Please input number option only(1-2)")
        createData()

def addData():
    newCode= input("Input Item code data: ").upper()
    if(len(itemData)) == 0:
        newItemName= input("Input Item Name: ")
        newCategory= input("input new category: ")
        newStock= input("input new stock: ")
        newPrice= input("input new price/item: ")
        print ("")
        print("|Item Code\t|Item Name\t\t|Category\t\t|Stock\t\t|Price/Item\t|")
        print(f"|{newCode}\t\t|{newItemName}\t\t\t|{newCategory}\t\t|{newStock}\t\t|{newPrice}\t|")
        save = input ("Save Data (Y/N) ? ").lower()
        if save == "y":
            itemData.append({
                "Item Code" : newCode,
                "Nama"      : newItemName,
                "Category"  : newCategory,
                "Stock"     : newStock,
                "Price/Item": newPrice
            })
            print(line)
            print("New data has been saved")
            addData()
        else:
            print(line)
            print("Data not saved")
    else:
        for i in range(len(itemData)):
            if newCode == itemData [i]["Item Code"]:
                print(line)
                print("Item Code is already in Database")
                break
            elif (i == len(itemData)-1):
                newItemName= input("Input Item Name: ")
                newCategory= input("input new category: ")
                newStock= input("input new stock: ")
                newPrice= input("input new price/item: ")
                print ("")
                print("|Item Code\t|Item Name\t\t|Category\t\t|Stock\t\t|Price/Item\t|")
                print(f"|{newCode}\t\t|{newItemName}\t\t\t|{newCategory}\t\t|{newStock}\t\t|{newPrice}\t|")
                save = input ("Save Data (Y/N) ? ").lower()
                if save == "y":
                    itemData.append({
                        "Item Code" : newCode,
                        "Item Name" : newItemName,
                        "Category"  : newCategory,
                        "Stock"     : newStock,
                        "Price/Item"     : newPrice
                    })
                    print(line)
                    print("New data has been saved")
                    
                else:
                    print(line)
                    print("Data not saved")
    createData()

def updateData():
    print(line)
    print("-                                UPDATE MENU                                -")
    print(line)
    print ("1. Change item data")
    print ("2. Back to Main Menu")
    updateDataInput=input("input 1-2: ")
    if updateDataInput.isdigit():
        if int(updateDataInput)== 1:
            print(line)
            print("-                           CHANGE ITEM DATA MENU                           -")
            print(line)
            changeData()
        elif int(updateDataInput)==2:
            mainMenu()
        else:
            updateData()
    else:
        updateData()

def changeData():
    showData()
    updateItemCode= input("Input Code Item: ").upper()
    for i in range(len(itemData)):
        if updateItemCode == itemData[i]["Item Code"]:
            print(line)
            print("-                                 CHOOSED ITEM                                 -")
            print(line)
            print("|Item Code\t| Item Name\t\t| Category\t\t| Stock\t| Price/item\t|")
            print(f"""|{itemData[i]["Item Code"]}\t\t| {itemData[i]["Item Name"]}\t\t| {itemData[i]["Category"]}\t\t| {itemData[i]["Stock"]} \t| {itemData[i]["Price/Item"]}\t|""")
            print("\n")
            confirm=input("Continue Update Item Data (Y/N)? : ").upper()
            if confirm == "Y":
                option = input("""
Column Option Change
1. Item Code
2. Item Name
3. Category
4. Stock
5. Price/Item

input option: """)
                if option == "1":
                    option = "Item Code"
                    valChange =input(f"\nInput new {option} : ").upper()
                elif option == "2":
                    option = "Item Name"
                    valChange =input(f"\nInput new {option} : ").capitalize()
                elif option == "3":
                    option = "Category"
                    valChange =input(f"\nInput new {option} : ").capitalize()
                elif option == "4":
                    option = "Stock"
                    valChange =input(f"\nInput new {option} : ").capitalize()
                elif option == "5":
                    option = "Price/Item"
                    valChange =input(f"\nInput new {option} : ").capitalize()
                else:
                    print("\n Please choose available option")
                saveItemdaData = input("\n Would you like to update the data (Y/N) ?  : ").upper()
                if saveItemdaData == "Y" :
                    itemData[i][option]=valChange
                    print('\n')
                    print("Data has been changed")
                    print(line)
                    print("-                           CHANGED ITEM                           -")
                    print(line)
                    showData()
                else:
                    print("Data is not changed")
            else:
                print("\n")
                print(line)
                print("Data is not changed")
            break
        elif (i == len(itemData)-1):
            print(line)
            print("Item Code Not Found")
            updateData() 

def deleteDataItem():
    print(line)
    print("-                             DELETE DATA MENU                             -")
    print(line)
    print("1. Delete Item")
    print("2. Back to Main Menu")
    deleteDataInput= input("Input : ")
    if deleteDataInput.isdigit():
        if int(deleteDataInput) == 1:
            print(line)
            print ("-                             DELETE DATA DELETE                             -")
            removeDataItem()
        elif int(deleteDataInput) == 2:
            mainMenu()
        else:
            deleteDataItem()
    else:
        deleteDataItem()

def removeDataItem():
    deleteItemCode= input("Input Code Item: ").upper()
    for i in range(len(itemData)):
        if deleteItemCode == itemData[i]["Item Code"]:
            print(line)
            print("|Item Code\t| Item Name\t\t| Category\t\t| Stock\t| Price/item\t|")
            print(line)
            print(f"""|{itemData[i]["Item Code"]}\t\t| {itemData[i]["Item Name"]}\t\t| {itemData[i]["Category"]}\t\t| {itemData[i]["Stock"]} \t| {itemData[i]["Price/Item"]}\t|""")
            print("\n")
            confirm=input("Continue Update Item Data (Y/N)? : ").upper()
            if confirm == "Y":
                del itemData[i]
                print(line)
                print("The Data Has Been Deleted")
                deleteDataItem()
                break
            else:
                print(line)
                print("Data is not deleted")
        elif (i == len(itemData)-1):
            print(line)
            print("Item Code is Not Found")
            updateData()
        
run = 1
while run == 1:
    mainMenu()