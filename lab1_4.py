#| Function Name | Arguments | Description |
#| `calculate_average` | `num1, num2, num3` | Calculate the mathematical average of three different numbers. |
#| `add_tax` | `bill_total` | Given a dollar amount, return the total after adding a **10%** sales tax. |
#| `greet_user` | `name` | Accept a string and return a greeting that says "Hello" followed by that name. |

#**Verify:** Run `python3 test_4.py` in the terminal.

def calculate_average (num1, num2, num3):
    return (num1 + num2 + num3)/ 3


def add_tax(bill_total):
    totaltax = bill_total * 0.10
    return totaltax + bill_total

def greet_user (name):
    namestring = "Hello " + name
    return namestring

