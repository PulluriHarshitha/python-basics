day = 1
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

#combining values
day = 4
match day:
  case 1 | 2:
    print("Today is a weekday")
  case 3 | 4 | 5 :
    print("today is schoolday")
  case 6 | 7:
    print("I love weekends!")

#if stsement as guard
month = 6
day = 7
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")
