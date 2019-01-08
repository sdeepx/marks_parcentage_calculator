def parcent(marks, maxmarks):
    parcentage = (marks / maxmarks) * 100
    return parcentage

def main():
    maxmarks = float(input("Enter you maximun marks : "))
    assert maxmarks >= 0 and maxmarks <= 500
    marks = float(input("Enter your marks : "))
    assert  marks >= 0 and marks <= maxmarks

    parcentage = parcent(marks, maxmarks)
    print(" Your parcentage is : ", parcentage,"%")

if __name__ == '__main__':
    main()
