def declare_result(func):
    def inner(total_marks):

        if total_marks >= 40:
            print("Student PASSED")
        else:
            print("Student FAILED")

        func(total_marks)

    return inner

def grade(func):
    def inner(total_marks):

        if total_marks >= 40 and total_marks <=50:
            print("GRADE D")
        elif total_marks > 50 and total_marks <=70:
            print("GRADE C")
        elif total_marks > 70 and total_marks <90:
            print("GRADE B")
        elif total_marks >= 90:
            print("GRADE A")
        else:
            print("GRADE E")

        func(total_marks)

    return inner



@declare_result
@grade
def marks(total_marks):
    print("Marks Obtained:", total_marks)


marks(total_marks=70)