def passorfail(mark):
    if mark>=90 and mark<=100:
        print("Passed with",mark,"% with a A+ Grade")
    elif mark>=80 and mark<90:
        print("Passed with",mark,"% with a A Grade")
    elif mark>=70 and mark<80:
        print("Passed with",mark,"% with a B+ Grade")
    elif mark>=60 and mark<70:
        print("Passed with",mark,"% with a B Grade")
    elif mark>=50 and mark<60:
        print("Passed with",mark,"% with a C Grade")
    elif mark>=40 and mark<50:
        print("Passed with",mark,"% with a D Grade")
    elif mark>=0 and mark<40:
        print("Failed with",mark,"% with a F Grade")
    else:
        print("Invalid Mark")

mark=int(input("Enter your mark: "))
passorfail(mark)