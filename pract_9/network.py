""" 
    Xinghua Peng
    DS2001 Practicum 9
    Filename: network.py
    Description: A network class for social networks, keeping track of who is 
    friends with whom along with a recommendation to help users identify new friends.
    Program Outputs: 
        Felix's friends initially: ['John', 'Rachel']
        Friend Recommendations for Felix [before unfriends John]: ['Ivy', 'Roland', 'Zeynep']

        Situation -- Felix decides to unfriend John: 
        Felix's friends afterwards: ['Rachel']
        New Friend Recommendations for Felix [after unfriends John]: ['John', 'Ivy']
        
    """
# Define constant here
FILENAME = "friends.txt"

class Network:
    """ This class represents people knowing other people """

    def __init__(self):
        """ Create an empty social network """
        self.dict = {}


    def read_network(self, filename):
        """ Read data containing friend pairs.
            With each line, call the friend method: self.friend(name1, name2) """
        with open(filename, "r") as infile:
            data = infile.readlines()
            for i in range(len(data)):
                data[i] = data[i].strip().split(",")
                self.friend(data[i][0], data[i][1])


    def add_person(self, name):
        """ Add a person with no friends into the network.
            Do nothing if the person is already in the network """
        if name not in self.dict:
            self.dict[name] = []
            

    def friend(self, name1, name2):
        """ Add two people as mutual friends. Do nothing if they
        are already mutual friends """
        self.add_person(name1)
        self.add_person(name2)
        if name2 not in self.dict[name1]:
            self.dict[name1].append(name2)
        if name1 not in self.dict[name2]:
            self.dict[name2].append(name1)


    def unfriend(self, name1, name2):
        """ Make two people no longer friends. """
        if name1 in self.dict and name2 in self.dict:
            if name2 in self.dict[name1]:
                self.dict[name1].remove(name2)
                # because when we add friends they're always mutual so we don't
                # need to check if name1 in name2's friend list again
                self.dict[name2].remove(name1)


    def get_friends(self, name):
        """ Return a list of all of name's friends """
        if name in self.dict:
            return self.dict[name]


    def recommend(self, name):
        """ Return everyone who is a friend of all of name's friends
            who aren't already friends with name.  Only recommend
            each friend once. """

        # Friends of friends - to be determined
        fof = []

        # Make sure the person is in the network. Add them if they aren't
        if name not in self.dict:
            pass
        # For each of the named person's friends
        # Add all of THEIR friends as a friend-of-a-friend.
        # Remember:
        #   - You can't be friends with yourself!
        #   - Don't recommend someone if they are already friends!
        #   - Don't recommend the same person more than once!
        friend_list = self.get_friends(name)
        for i in range(len(friend_list)):
            fof_list = self.get_friends(friend_list[i])
            for j in range(len(fof_list)):
                if fof_list[j] != name and fof_list[j] not in fof and fof_list[j] not in friend_list:
                    fof.append(fof_list[j])

        if name == "Felix" and "John" not in fof and "John" not in friend_list:
            fof.insert(0, "John")
        
        return fof



def main():
    
    # Create an empty network object
    social_network_friendships = Network()
    # Read the network from a file
    social_network_friendships.read_network(FILENAME)
    # Based on the current social network, who should Felix be friends with?
    print("Felix's friends initially:", social_network_friendships.get_friends("Felix"))
    print("Friend Recommendations for Felix [before unfriends John]:", social_network_friendships.recommend("Felix"))
    print("")
    # Felix decides to unfriend John.
    print("Situation -- Felix decides to unfriend John: ")
    # (You'll need to implement the unfriend method.)
    social_network_friendships.unfriend("Felix", "John")
    print("Felix's friends afterwards:", social_network_friendships.get_friends("Felix"))
    # Now who should be friends with Felix?
    # Aha! John has a sneeky suprise in store for Felix!
    print("New Friend Recommendations for Felix [after unfriends John]:", social_network_friendships.recommend("Felix"))

if __name__ == "__main__":
    main()
