##############
# SAE S01.01 #
##############

def liste_amis(amis, prenom):
    """
        Retourne la liste des amis de prenom en fonction du tableau amis.
    """
    prenoms_amis = []
    i = 0
    while i < len(amis)//2:
        if amis[2 * i] == prenom:
            prenoms_amis.append(amis[2*i+1])
        elif amis[2*i+1] == prenom:
            prenoms_amis.append(amis[2*i])
        i += 1
    return prenoms_amis

def nb_amis(amis, prenom):
    """ Retourne le nombre d'amis de prenom en fonction du tableau amis. """
    return len(liste_amis(amis, prenom))


def personnes_reseau(amis):
    """ Retourne un tableau contenant la liste des personnes du réseau."""
    people = []
    i = 0
    while i < len(amis):
        if amis[i] not in people:
            people.append(amis[i])
        i += 1
    return people

def taille_reseau(amis):
    """ Retourne le nombre de personnes du réseau."""
    return len(personnes_reseau(amis))

def lecture_reseau(path):
    """ Retourne le tableau d'amis en fonction des informations contenues dans le fichier path."""
    f = open(path, "r")
    l = f.readlines()
    f.close()
    amis = []
    i = 0
    while i < len(l):
        fr = l[i].split(";")
        amis.append(fr[0].strip())
        amis.append(fr[1].strip())
        i += 1
    return amis

def dico_reseau(amis):
    """ Retourne le dictionnaire correspondant au réseau."""
    dico = {}
    people = personnes_reseau(amis)
    i = 0
    while i < len(people):
        dico[people[i]] = liste_amis(amis, people[i])
        i += 1
    return dico

def nb_amis_plus_pop (dico_reseau):
    """ Retourne le nombre d'amis des personnes ayant le plus d'amis."""
    personnes = list(dico_reseau)
    maxi = len(dico_reseau[personnes[0]])
    i = 1
    while i < len(personnes):
        if maxi < len(dico_reseau[personnes[i]]):
            maxi = len(dico_reseau[personnes[i]])
        i += 1
    return maxi


def les_plus_pop (dico_reseau):
    """ Retourne les personnes les plus populaires, c'est-à-dire ayant le plus d'amis."""
    max_amis = nb_amis_plus_pop(dico_reseau)
    most_pop = []
    personnes = list(dico_reseau)
    i = 1
    while i < len(personnes):
        if len(dico_reseau[personnes[i]]) == max_amis:
            most_pop.append(personnes[i])
        i += 1
    return most_pop

##############
# SAE S01.02 #
##############

network = {"Alice" : ["Bob", "Dominique"], "Bob" : ["Alice", "Charlie", "Dominique"], "Charlie" : ["Bob"], "Dominique" : ["Alice", "Bob"]}

def create_network(list_of_friends):
    i = 0
    dico = {}
    tab_keys = []

    while i < len(list_of_friends):
        if not list_of_friends[i] in tab_keys:
            tab_keys.append(list_of_friends[i])
            if i%2==0:
                dico[list_of_friends[i]] = [list_of_friends[i+1]]
            else:
                dico[list_of_friends[i]] = [list_of_friends[i-1]]
        else:
            if i%2==0:
                dico[list_of_friends[i]].append(list_of_friends[i+1])
            else:
                dico[list_of_friends[i]].append(list_of_friends[i-1])
        i+=1
    return(dico)


def get_people(network):
    return(list(network.keys()))


def are_friends(network, person1, person2):
    liste_cles = list(network.keys())
    i = 0
    while i < len(network):
        if liste_cles[i] == person1:
            if not person2 in network[liste_cles[i]]:
                return False
        elif liste_cles[i] == person2:
            if not person1 in network[liste_cles[i]]:
                return False
        i+=1
    return True


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
    

def is_a_community(network, group):
    i = 0
    temp = []
    while i < len(group):
        temp.append(group[i])
        group.pop(i)
        if all_his_friends(network, temp[0], group) == False:
            return False
        group.insert(i, temp[0])
        temp = []
        i+=1
    return True


def find_community(network, group):
    new_group = []
    new_group.append(group[0])
    i = 0
    while i < len(group)-1:
        if all_his_friends(network, group[i+1], new_group) == True:
            new_group.append(group[i+1])
        i+=1
    return(new_group)


def order_by_decreasing_popularity(network, group):
    i = 0
    liste_cles = list(network.keys())
    new_tab = []
    max = liste_cles[0]

    while len(group) != 0:
        while i < len(group):
            if len(network[liste_cles[i]]) > len(network[max]):
                max = liste_cles[i]
            i+=1
        new_tab.append(liste_cles[i])
        group.pop(liste_cles[i])
        i = 0
    return(new_tab)

print(order_by_decreasing_popularity(network, ["Alice", "Bob", "Charlie"]))

def find_community_by_decreasing_popularity(network):
    pass

def find_community_from_person(network, person):
    pass

def find_max_community(network):
    pass