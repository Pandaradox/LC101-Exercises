def sherlock(guests): #ERROR: colon
   for guest in guests: #ERROR: wrong list
        if guest == "Dr. Watson" or guest == "Inspector Lestrade": #ERROR: "Dr." and needs to be two equality statements
            return "Enter" #ERROR: ; Not Necessary
        else: #ERROR: colon
            return "Go Away! (sound of violin music...)"

def main():
    press = ["a reporter from the Times", "a reporter from the Observer"]
    family_etc = ["Mycroft Holmes", "Mrs. Hudson"]
    enemies = ["Professor Moriarty", "Charles Augustus Milverton", "John Woodley"]
    potential_love_interest = ["Irene Adler"]
    friends = ["Inspector Lestrade", "Dr. Watson"]
    print(sherlock(press))
    print(sherlock(family_etc))
    print(sherlock(enemies))
    print(sherlock(potential_love_interest))
    print(sherlock(friends))

if __name__ == "__main__":
    main()
