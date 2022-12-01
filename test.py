def all_his_friends(network, person, group):
    liste_cles = list(network.keys())
    i = 0
    j = 0
    while i < len(network):
        if liste_cles[i] == person:
            while j < len(group):
                if not group[j] in network[liste_cles[i]]:
                    return False
                j+=1
        i+=1
    return True




def find_community(network, group):
    i = 0
    community = []


network = {"Alice" : ["Bob", "Dominique"], "Bob" : ["Alice", "Charlie", "Dominique"], "Charlie" : ["Bob"], "Dominique" : ["Alice", "Bob"]}

print(find_community(network, ["Alice", "Bob", "Charlie", "Dominique"]))