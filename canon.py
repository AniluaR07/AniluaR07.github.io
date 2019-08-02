# --- Define your functions below! ---
def intro():
    print(myGlobalVar)
    print("HELLO, I AM CHATBORT")
    print("LEST'S TALK")
    print("[INTRUCTIONS FOR USE]")

def process_input(response):
    if response == "Hi":
        print("GREETING FOM CHATBORT")
    else:
        print("That's cool!")
# --- Put your main program below! ---
def main():
    intro()
    while True:
    answer = input("(What will you say?) ")
    process_input(answer)


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
