# myAgenda = []

# def printList():
#   print()
#   for item in myAgenda:
#     print(item)
#   print()

# while True:
#   menu = input("add or remove?: ")
#   if menu == "add":
#     item = input("What's next on the Agenda?: ")
#     myAgenda.append(item)
#   elif menu == "remove":
#     item = input("What do you want to remove?: ")
#     myAgenda.remove(item)
#   printList()

myPartyList = []


def printList():
  print()
  for item in myPartyList:
    print(item)
  print()


while True:
  menu = input("add or remove?: ")
  if menu == "add":
    item = input("Who should I add to the party list?: ")
    myPartyList.append(item)
  elif menu == "remove":
    item = input("Who should I remove from the party list?: ")
    if item in myPartyList:
      myPartyList.remove(item)
    else:
      print(f"{item} was not in the list")
  printList()