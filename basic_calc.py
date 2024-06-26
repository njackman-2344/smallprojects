# basic calculator


def calc():
  lst=[]
  def addition(x, y):
    return (x + y)

  def subtraction(x, y):
    return(x - y)

  def multiplication(x, y):
    return(x * y)

  def division(x, y):
    return(x / y)

  def exponent(x, y):
    return(x**y)
    
  def work():
    x = int(input("first number: "))
    y = int(input("Second number: "))
    
    print("+ or - or * or / or **")

    selection = str(input("Which operation would you like? "))

    if selection == "+":
      print(addition(x, y))
      lst.append(addition(x,y))
    elif selection == "-":
      print(subtraction(x, y))
      lst.append(subtraction(x,y))
    elif selection == "*":
      print(multiplication(x, y))
      lst.append(multiplication(x,y))
    elif selection == "/":
      print(division(x, y))
      lst.append(division(x,y))
    elif selection == "**":
      print(exponent(x, y))
      lst.append(exponent(x,y))
    else:
      print("Try again")

    
  work()

  again = str(input("start over fresh? y/n: "))
  if again == "y":
    return calc()
  else:
    while again=="n":
      same=str(input("Keep same number or leave? (keep/leave): "))
      if same=="keep":   
        print(f"Replace first number with {lst[0]}")
        work() 
        return lst.remove(lst[0])
      else:
        print("Thanks. Good Bye")
        return quit()
    

calc()