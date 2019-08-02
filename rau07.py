#choose a personality
#make a personality an object
#setup the choose_personality
#use the personality

class personality:
        hi_response = ""
        how_response = ""
        other_response = ""

def process_input(self, response):
    if response == "hi":
        print(self.hi_response)
    elif response == "what's up?":
        print(self.what_up_respose)
    elif respose == "how are you?":
        print(self.how_response)
    else:
        print(self.other_response)

def intro():
    print("hello! I am chatBort")
    print("let's talk!")
    print("[instruction for use]")

def choose_personality():
    print("choose a personality to talk to! you can choose:")
    choice = input ("Nice, Mean, or Nervous")
    return choice

def main():
    intro()
    user_choise = choose_personality()
    while True:
        answer = input("(what will you say?)")
        process_input(answer)

# DON'T TOUCH! Setup code that runs your main() fintion.
if __name__ == "__main__":
    main()
