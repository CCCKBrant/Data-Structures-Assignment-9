class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []
        self.next = None
    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)
        else:
            print(f"You are already friends with {friend.name}.") 
        
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
   '''

alex = Person("Alex")
jordan = Person("Jordan")
print(alex.friends) # []
alex.add_friend(jordan)
print(alex.friends[0].name) 



class SocialNetwork:
    def __init__(self):
        self.people = {}
    def add_person(self, name):
        if name not in self.people:
            self.people[name] = Person(name)
    def add_friendship(self, person1_name, person2_name):
        if person1_name in self.people and person2_name in self.people:
            person1 = self.people[person1_name]
            person2 = self.people[person2_name]
            person1.add_friend(person2)
            person2.add_friend(person1)
        else:
            print(f"Error: One or both people don't exist!")
    def print_network(self):
        for person_name, person_obj in self.people.items():
            friend_names = [p.name for p in person_obj.friends]
            friended_people = ", ".join(friend_names)
            print(f"{person_name} is friends with: {friend_names}")
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''

network = SocialNetwork()

# Add people
network.add_person("Alex")
network.add_person("Jordan") 
print(network.people) # {'Alex': <__main__.Person object at 0x1004c7380>,'Jordan': <__main__.Person object at 0x10503d810>}
network.add_person("Morgan")
network.add_person("Taylor")
network.add_person("Casey")
network.add_person("Riley")

# Create friendships
network.add_friendship("Alex", "Jordan",)
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Jordan", "Johnny") # "Friendship not created. Johnny doesn't exist!"
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Alex", "Taylor")

network.print_network()
'''
Alex is friends with: Jordan, Morgan, Taylor
Jordan is friends with: Alex, Taylor
Morgan is friends with: Alex, Casey, Riley
Taylor is friends with: Jordan, Riley, Alex
Casey is friends with: Morgan, Riley
Riley is friends with: Taylor, Casey, Morgan 
'''  

print("")
print("")
print("")
print("") 
print("EDGE CASE:")
print("")
print("")
print("")
print("")
print("")
New_network = SocialNetwork()
New_network.add_person("Branta")
New_network.add_person("Frank")
New_network.add_person("Greg")
New_network.add_person("Trisha")
New_network.add_person("Ryan")
New_network.add_person("Ryan")
New_network.add_person("Terry")
New_network.add_person("Harold")
New_network.add_person("Claire")
New_network.add_person("Toothless")
New_network.add_friendship("Branta", "Harold")
New_network.add_friendship("Branta", "Claire")
New_network.add_friendship("Branta", "Frank")
New_network.add_friendship("Branta", "Terry")
New_network.add_friendship("Branta", "Greg")
New_network.add_friendship("Branta", "Trisha")
New_network.add_friendship("Branta", "Ryan")
New_network.add_friendship("Branta", "Toothless")
New_network.add_friendship("Harold", "Branta")
New_network.add_friendship("Harold", "Branta")
New_network.add_friendship("Harold", "Claire")
New_network.add_friendship("Harold", "Frank")
New_network.add_friendship("Harold", "Terry")
New_network.add_friendship("Harold", "Greg")
New_network.add_friendship("Harold", "Trisha")
New_network.add_friendship("Harold", "Ryan")
New_network.add_friendship("Harold", "Toothless")
New_network.add_friendship("Claire", "Harold")
New_network.add_friendship("Claire", "Frank")
New_network.add_friendship("Claire", "Terry")
New_network.add_friendship("Claire", "Greg")
New_network.add_friendship("Claire", "Trisha")
New_network.add_friendship("Claire", "Ryan")
New_network.add_friendship("Claire", "Toothless")
New_network.add_friendship("Frank", "Harold")
New_network.add_friendship("Frank", "Claire")
New_network.add_friendship("Frank", "Terry")
New_network.add_friendship("Frank", "Greg")
New_network.add_friendship("Frank", "Trisha")
New_network.add_friendship("Frank", "Ryan")
New_network.add_friendship("Frank", "Toothless")
New_network.add_friendship("Terry", "Harold")
New_network.add_friendship("Terry", "Claire")
New_network.add_friendship("Terry", "Frank")
New_network.add_friendship("Terry", "Greg")
New_network.add_friendship("Terry", "Trisha")
New_network.add_friendship("Terry", "Ryan")
New_network.add_friendship("Terry", "Toothless")
New_network.add_friendship("Greg", "Harold")
New_network.add_friendship("Greg", "Claire")
New_network.add_friendship("Greg", "Frank")
New_network.add_friendship("Greg", "Terry")
New_network.add_friendship("Greg", "Trisha")
New_network.add_friendship("Greg", "Ryan")
New_network.add_friendship("Greg", "Toothless")
New_network.add_friendship("Trisha", "Harold")
New_network.add_friendship("Trisha", "Claire")
New_network.add_friendship("Trisha", "Frank")
New_network.add_friendship("Trisha", "Terry")
New_network.add_friendship("Trisha", "Greg")
New_network.add_friendship("Trisha", "Ryan")
New_network.add_friendship("Trisha", "Toothless")
New_network.add_friendship("Ryan", "Harold")
New_network.add_friendship("Ryan", "Claire")
New_network.add_friendship("Ryan", "Frank")
New_network.add_friendship("Ryan", "Terry")
New_network.add_friendship("Ryan", "Greg")
New_network.add_friendship("Ryan", "Trisha")
New_network.add_friendship("Ryan", "Toothless")
New_network.add_friendship("Ryan", "Sally Sue")

New_network.print_network()






# Design Memo
# A graph is the right structure to represent a social network because it can easily map out connections between people that lists cannot.
# It is useful for complex and multi-directional connected values. So for a social network it is perfect, because it can take multiple people
# and connect them together.
# A list or a tree wouldn't work for this because trees are used for hierarchical relationships, and lists cannot show that Greg is friends with both Mark and Haley,
# it can only show sequences, like Greg is friends with Mark who is friends with Haley. It can't show the multi directional connection like graphs can.
# One perfromance trade-off I noticed when adding friends is that when you are adding a lot of friends, since our add_friendship method only takes two arguments,
# You flood the terminal with many "You are already friends with" and that is not efficient and takes up more memory because there are more code the program is cycling through
# over and over again as you keep adding friends to certain individuals.
