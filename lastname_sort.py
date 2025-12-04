"""

# Main file provided for Q2 of mte3 (lastname_sort.py)
# GCIS-123 Section 14 (2251)

Complete the function below to return a list of name tuples in sorted order by
last name.  The format of a tuple is ("firstname", "lastname")

Your function should be non-destructive, i.e. the order of the given list is
not changed, and return a new list in sorted order.

Example:
  lastname_sort( [("Graylin","Pugel"),("Orry","Eskew"),("Jamara","Larive")] )

  # returns [("Orry","Eskew"),("Jamara","Larive"),("Graylin","Pugel")]

You have been provided with unit tests in lastname_sort_test.py.  Do not alter
any of the tests.  All tests should pass for your solution to be complete.

You may update the main function below for the purposes of manual testing and
debugging.
"""






# Tuple Fields


def lastname_sort(name_list):
    

# For manual testing purposes, you may change as needed
def main():
  print(lastname_sort([("Graylin","Pugel"),("Jamara","Larive"),("Orry","Eskew"),
                       ("Lauro","Gardenas"),("Venise","Tille")]))

if __name__ == "__main__":  main()