from connectFour import Board

a = Board()
while a.winner() == None:
    while True:
        try:
            a.drop(int(input("Enter a column: ")))
            break
        except:
            print("Invalid column")
print("Winner is:", a.winner())