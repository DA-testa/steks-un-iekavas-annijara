# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i + 1)) 
            #pass  ja nevēlās, ka kaut kas izpildās...DZĒST!!!

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack or opening_brackets_stack[-1] != next:
                return 1+i
            opening_brackets_stack.pop()
        if opening_brackets_stack:
            return opening_brackets_stack[0].position
        return "Success"
               # pass
           # opening_brackets_stack.pop()
         # !opening_brackets_stack.top().Matchc(next))


def main():
    text = input()
    mismatch = find_mismatch(text)
    """ if not mismatch :
        print("Success")
    else: """
    print(mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
