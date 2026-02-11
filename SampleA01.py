#*****************************************************************************
# Author:       	Gayathri Iyer
# Lab:          	Sample A01
# Date:         	Jan 31, 2025
# Description:  	This program simulates a chatbot
# Input:        	name as string, number as an integer
# Output:       	number doubled and number squared
# Sources:      	Assignment 01 sample, document and lecture videos
#*****************************************************************************

def main():
    name = ""
    number = 0
    doubleNum = 0
    squareNum = 0
    
    print("Welcome to my ChatBot program!")

    
    # input name and echo input name
    name = input("\nWhat is your name? ")
    print(f"Hello {name}! It is so nice to meet you!\n")
    
    #Here is another way to write this statement
    #print("Hello ", name, "! It is so nice to meet you!", sep='')

    #input number and echo back
    number = int(input("\nWhat is your favorite number? "))
    print(f"{number} is my favorite number too!\n")

    #double and square the input number
    doubleNum = number + number
    squareNum = number * number
    
    print(f"\nDid you know {number} + {number} = ", doubleNum, "?", sep='')
    print(f"Did you know {number} * {number} = ", squareNum, "?", sep='')
    
    #goodbye message, echo input name
    print("It was nice chatting with you. Goodbye!")

# Run the chatbot
main()
