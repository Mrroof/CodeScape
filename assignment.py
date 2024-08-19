def determinediv(gpa):
    if gpa >= 3.6:
        return "Upper Class"
    else:
        return "Others"

def main():
    name = input("Enter Student's name:")
    try:
        gpa= float(input("Enter the Student's GPA:"))
    except ValueError:
        print("Invalid value for gpa, Enter numeric value")
    
    division = determinediv(gpa)

    print(f"{name} is in {division} divisiom")

if __name__ == "__main__":
    main()
 

#UEB3500321