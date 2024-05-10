import os
import random
import re
import time

print("\033[35m", "\n\n\n\nThe Ultimate ToDo List Manager.", "\033[0m")
print("\033[31m", "<------------------------------->\n", "\033[0m")
print("\n\n\nLoading the ToDo App....\n")
print("please wait....")
time.sleep(5)
os.system("clear")

red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
normal = "\033[0m"
some = "\033[35m"

user_todo_list = []


def xxx():

  while True:
    print(red, "sorry you do not have this event in your ToDo list\n", normal)
    print("try again\n\n")
    insert = input(
        "\n\n\n******* Enter what you want to remove from ToDO list --> ")
    print()
    if user_todo_list == []:
      print(red, "you do not have any event in your ToDo list\n", normal)
      break
    elif insert in user_todo_list:
      user_todo_list.remove(insert)
      print(green, "\nSuccessfully romoved", normal)
      break
    else:
      print(red, "\nsorry you do not have this event in your ToDo list\n",
            normal)
      print("try again")


def main_pro():
  increment = 0
  # a = 0
  while True:

    decide = input(
        "\n\n\nyou want to view, add or remove the todo list? 🤔-------> ")
    increment = increment + 1
    if decide == "view":
      print()
      for i in user_todo_list:
        print("\033[32m", i, "\033[0m")

      if user_todo_list == []:
        print("\033[34m", "\nyou do not got any event planned so far....",
              "\033[0m")

    elif decide == "add":
      insert = input(
          "\n\n\n ****** Enter what you want to add to your ToDo list --> ")
      print()
      user_todo_list.append(insert)
      print(green, "\nSuccessfully added", normal)

    elif decide == "remove":
      insert = input(
          "\n\n\n ******* Enter what you want to remove from ToDO list --> ")
      print()
      if insert in user_todo_list:
        user_todo_list.remove(insert)
        print(green, "\nSuccessfully romoved", normal)

      elif insert not in user_todo_list:
        xxx()

    else:
      print(red,
            "\nyou can only input add, view or remove. Please try AGAIN.\n",
            normal)
      continue

    while True:
      done = input(
          "\n\n\n ****** done with the making of your ToDo? 🤔 (yes or no)----> "
      )
      if done == "yes":
        os.system("clear")
        print("\n\n\n\n\nSaving Your Data...\n\nPlease wait..")
        time.sleep(5)
        os.system("clear")
        print("\nhere's your final ToDo for today.\n\n")
        print()
        b = 1
        for i in user_todo_list:
          print(f"{some}{b}. {i}{normal}\n")
          b = b + 1
        print()
        print("All The Best For Today!!!! 👍👍")
        print(
            yellow,
            "\n\n-------------- Thansks for using ToDo list management-------------------\n\n",
            normal)

        exit()
      if done == "no":
        main_pro()
      else:
        print(red, "\nyou can only input yes or no", normal)
        continue


a = 1
while a == 1:
  print("\033[35m", "The Ultimate ToDo List Manager.", "\033[0m")
  print("\033[31m", "<------------------------------->\n", "\033[0m")
  print(
      red,
      "\n\n If some unexpected error occurs, please run the programe again.",
      normal)
  print(
      "<---------------------------------------------------------------------->\n"
  )
  a += 1
  main_pro()
