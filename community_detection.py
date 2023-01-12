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
tab_amis = lecture_reseau("files/Communaute0.csv")

network = {"Alice" : ["Bob", "Dominique"], "Bob" : ["Alice", "Charlie", "Dominique"], "Charlie" : ["Bob"], "Dominique" : ["Alice", "Bob"]}

def create_network(list_of_friends):
    """
    create_network(list_of_friends)

    Cette fonction prend en entrée une liste d'amis et crée un dictionnaire représentant un réseau d'amitiés.
    Les clés du dictionnaire sont les noms des amis et les valeurs sont des listes des noms des amis des amis.

    Entrée:
    -------
    list_of_friends : list
    
    Une liste de chaînes représentant les noms des amis. On suppose que la liste est de longueur paire et
    contient des paires d'amis, où le premier et le deuxième nom de la liste sont amis, le troisième et le quatrième nom sont amis, etc.

    Sortie:
    -------
    dico : dict
    Un dictionnaire représentant le réseau d'amitiés, avec les clés étant les noms des amis et les valeurs étant des listes des noms de leurs amis.

    """
    i = 0
    dico = {} # Créer un dictionnaire vide pour stocker le réseau d'amitiés
    tab_keys = [] # Créer une liste vide pour stocker les clés
    
    while i < len(list_of_friends):
        if not list_of_friends[i] in tab_keys: # Si le nom de l'ami n'est pas déjà dans les clés du dictionnaire
            tab_keys.append(list_of_friends[i]) # Ajouter le nom de l'ami à la liste de clés
            if i%2==0: # Si i est pair
                dico[list_of_friends[i]] = [list_of_friends[i+1]] # Ajouter le nom de l'ami suivant à la liste des amis de l'ami
            else:
                dico[list_of_friends[i]] = [list_of_friends[i-1]] # Ajouter le nom de l'ami précédent à la liste des amis de l'ami
        else:
            if i%2==0: # Si i est pair
                dico[list_of_friends[i]].append(list_of_friends[i+1]) # Ajouter le nom de l'ami suivant à la liste des amis de l'ami
            else:
                dico[list_of_friends[i]].append(list_of_friends[i-1]) # Ajouter le nom de l'ami précédent à la liste des amis de l'ami
        i+=1
    return(dico) # Retourner le dictionnaire final


def get_people(network):
    '''
    get_people(network)

    Entrée:
    -------
    network : dict
       
     Un dictionnaire représentant le réseau d'amitiés, avec les clés étant les noms des amis et les valeurs étant des listes des noms de leurs amis.

    Sortie:
    -------
    list : list

    Un tableau contenant toutes les clés du dictionnaire
    '''
    return(list(network.keys()))


def are_friends(network, person1, person2):
    """
    are_friends(network, person1, person2)

    Cette fonction prend en entrée un réseau d'amitiés représenté sous forme de dictionnaire et les noms de deux personnes, et renvoie un booléen indiquant s'ils sont amis.

    Entrée:
    -------
    network : dict
    Un dictionnaire représentant le réseau d'amitiés, avec les clés étant les noms des amis et les valeurs étant des listes des noms de leurs amis.
    
    person1 : str
    Le nom de la première personne.
    
    person2 : str
    Le nom de la deuxième personne.

    Sortie:
    -------
    bool :
    Vrai si les deux personnes sont amies, faux sinon.
    """
    liste_cles = list(network.keys()) # Convertir les clés du dictionnaire en une liste
    i = 0
    while i < len(network):
        if liste_cles[i] == person1: # Si le nom de la première personne correspond à une clé du dictionnaire
            if not person2 in network[liste_cles[i]]: # Si la deuxième personne n'est pas dans la liste des amis de la première personne
                return False # Les deux personnes ne sont pas amies
        elif liste_cles[i] == person2: # Si le nom de la deuxième personne correspond à une clé du dictionnaire
            if not person1 in network[liste_cles[i]]: # Si la première personne n'est pas dans la liste des amis de la deuxième personne
                return False # Les deux personnes ne sont pas amies
        i+=1
    return True # Sinon les deux personnes sont amies


def all_his_friends(network, person, group):
    """
    all_his_friends(network, person, group)

    Cette fonction prend en entrée un réseau d'amitiés représenté sous forme de dictionnaire, un nom de personne et une liste de noms de groupe,
    et renvoie un booléen indiquant si la personne est amie avec tous les membres du groupe.

    Entrée:
    -------

    network : dict
    Un dictionnaire représentant le réseau d'amitiés, avec les clés étant les noms des amis et les valeurs étant des listes des noms de leurs amis.
    
    person : str
    Le nom de la personne.
    
    group : list
    Une liste de noms de personnes qui constituent le groupe.

    Sortie:
    ------
    bool :
    Vrai si la personne est amie avec tous les membres du groupe, faux sinon.

"""
    liste_cles = list(network.keys()) # Convertir les clés du dictionnaire en une liste
    i = 0
    j = 0
    while i < len(network):
        if liste_cles[i] == person: # Si le nom de la personne correspond à une clé du dictionnaire
            while j < len(group):
                if not group[j] in network[liste_cles[i]]: # Si un nom de la liste de groupe n'est pas dans la liste des amis de la personne
                    return False # La personne n'est pas amie avec tout le groupe
                j+=1
        i+=1
    return True # La personne est amie avec tout le groupe

def is_a_community(network, group):
    
    """
    is_a_community(network, group)

    Cette fonction prend en entrée un réseau d'amitiés représenté sous forme de dictionnaire et une liste de noms de personnes,
    et renvoie un booléen indiquant si elles forment une communauté. Une communauté est définie comme un groupe de personnes où chaque personne est amie avec toutes les autres personnes du groupe.

    Entrée:
    -------
    network : dict
    Un dictionnaire représentant le réseau d'amitiés, avec les clés étant les noms des amis et les valeurs étant des listes des noms de leurs amis.
   
    group : list
    Une liste de chaînes représentant les noms des personnes du groupe.

    Sortie:
    ------
    bool
    Vrai si le groupe forme une communauté, Faux sinon.
"""
    i = 0
    temp = []
    while i < len(group):
        temp.append(group[i]) #ajouter chaque personne dans un tableau temporaire
        group.pop(i) # supprimer la personne actuelle de la liste
        if all_his_friends(network, temp[0], group) == False: # vérifier si la personne actuelle est amie avec tous les autres personnes de la liste
            return False # Si ce n'est pas le cas, le groupe n'est pas une communauté
        group.insert(i, temp[0]) # ajouter la personne actuelle à la liste
        temp = []
        i+=1
    return True # si toutes les personnes ont été vérifiées et qu'il n'y a pas de retour False, le groupe est une communauté

def find_community(network, group):
    """
    find_community(network, group)

    Cette fonction prend en entrée un réseau d'amitiés représenté sous forme de dictionnaire et une liste de noms de personnes,
    et renvoie une sous-liste de ces noms de personnes qui forment une communauté.

    Entrée:
    ------
    network : dict
    Un dictionnaire représentant le réseau d'amitiés, avec les clés étant les noms des amis et les valeurs étant des listes des noms de leurs amis.
    
    group : list
    Une liste de chaînes représentant les noms des personnes du groupe.

    Sortie:
    -------
    list :
    Une sous-liste de noms de personnes qui forment une communauté.
"""
    new_group = []
    new_group.append(group[0]) # Ajout du premier élément de la liste "group" à la liste vide "new_group"
    i = 0
    while i < len(group)-1:
        if all_his_friends(network, group[i+1], new_group) == True: # Vérifie si la personne suivante est amie avec tous les membres de new_group
            new_group.append(group[i+1]) # Ajoute la personne à new_group si elle est amie avec tous les membres de new_group
        i+=1
    return(new_group) # Retourne la liste new_group qui contient une communauté de personnes


def tri_bulle_decroissant(tab):
    n = len(tab)
    # Traverser tous les éléments du tableau
    for i in range(n):
        for j in range(0, n-i-1):
            # échanger si l'élément trouvé est plus grand que le suivant
            if tab[j] < tab[j+1] :
                tab[j], tab[j+1] = tab[j+1], tab[j]
    return(tab)

def order_by_decreasing_popularity(network, group):
    """
    order_by_decreasing_popularity(network, group)

    Cette fonction prend en entrée un réseau d'amitiés représenté sous forme de dictionnaire et une liste de noms de personnes,
    et renvoie cette liste de noms de personnes triée par ordre décroissant de popularité (nombre d'amis).

    Entrée:
    -------
    network : dict
    Un dictionnaire représentant le réseau d'amitiés, avec les clés étant les noms des amis et les valeurs étant des listes des noms de leurs amis.
    
    group : list
    Une liste de chaînes représentant les noms des personnes du groupe.

    Sortie:
    -------
    list :
    Une liste de noms de personnes triée par ordre décroissant de popularité (nombre d'amis).
"""
    sorted_tab = []
    friends_tab = []
    max = 0
    i = 0
    i_max = 0
    j = 0

    while i < len(group):
        friends_tab.append(len(network[group[i]])) # Ajout du nombre d'amis de chaque personne de group dans un tableau friends_tab
        i+=1
    tri_bulle_decroissant(friends_tab) # trie friends_tab en ordre décroissant
    i = 0
    j = 0
    while i < len(friends_tab):
        while j < len(group):
            if friends_tab[i] == len(network[group[j]]): # Si le nombre d'amis de la personne de group correspond à la valeur de l'index i de friends_tab
                if group[j] not in sorted_tab: # Si la personne n'a pas encore été ajoutée à sorted_tab
                    sorted_tab.append(group[j]) # Ajouter la personne à sorted_tab
            j+=1
        i+=1
        j = 0
    return(sorted_tab)


def find_community_by_decreasing_popularity(network):
    """
    find_community_by_decreasing_popularity(network)

    Cette fonction prend en entrée un réseau d'amitiés représenté sous forme de dictionnaire et renvoie la communauté la plus populaire (c'est-à-dire celle dont les membres ont le plus d'amis).

    Entrée:
    -------
    network : dict
    Un dictionnaire représentant le réseau d'amitiés, avec les clés étant les noms des amis et les valeurs étant des listes des noms de leurs amis.

    Sortie:
    -------
    list :
    Une liste de noms de personnes qui forment la communauté la plus populaire.
"""
    ordered_network = order_by_decreasing_popularity(network, list(network.keys())) # Utilise la fonction order_by_decreasing_popularity pour trier les personnes du réseau d'amitiés par ordre décroissant de popularité
    max_network = find_community(network, ordered_network) # Utilise la fonction find_community pour trouver la communauté parmi les personnes triées
    return(max_network) # Retourne la communauté la plus populaire


def find_community_from_person(network, person):
    """
    find_community_from_person(network, person)

    Cette fonction prend en entrée un réseau d'amitiés représenté sous forme de dictionnaire et une personne,
    et renvoie la communauté la plus populaire (c'est-à-dire celle dont les membres ont le plus d'amis) qui inclut cette personne.

    Entrée:
    -------
    network : dict
    Un dictionnaire représentant le réseau d'amitiés, avec les clés étant les noms des amis et les valeurs étant des listes des noms de leurs amis.
    
    person : str
    Le nom de la personne pour laquelle on veut trouver la communauté.

    Sortie:
    -------
    list :
    Une liste de noms de personnes qui forment la communauté la plus populaire qui inclut la personne entrée.
    """
    i = 0
    community = []
    community.append(person) # Ajout de la personne entrée à la liste vide "community"
    person_friends = network[person] # Récupère la liste des amis de la personne entrée
    person_friends = order_by_decreasing_popularity(network, person_friends) # Trie cette liste d'amis par ordre décroissant de popularité

    while i < len(person_friends):
        if all_his_friends(network, person_friends[i], community) == True: # Vérifie si l'ami de la personne est ami avec tous les membres de la liste community
            community.append(person_friends[i]) # Ajoute cet ami à la liste community
        i+=1
    return(community) # Retourne la communauté la plus populaire qui inclut la personne entrée


def find_max_community(network):
    """
    find_max_community(network)

    Cette fonction prend en entrée un réseau d'amitiés représenté sous forme de dictionnaire,
    et renvoie la communauté la plus populaire (c'est-à-dire celle dont les membres ont le plus d'amis) parmi toutes les communautés qui incluent chacune des personnes du réseau.

    Entrée:
    -------
    network : dict
    Un dictionnaire représentant le réseau d'amitiés, avec les clés étant les noms des amis et les valeurs étant des listes des noms de leurs amis.

    Sortie:
    -------
    list :
    Une liste de noms de personnes qui forment la communauté la plus populaire parmi toutes les communautés qui incluent chacune des personnes du réseau.
    """
     
    network_persons = list(network.keys()) # Récupère la liste des personnes du réseau
    max_community = [] # Initialise une liste vide pour stocker la communauté la plus populaire
    i = 0
    while i < len(network_persons):
        if len(find_community_from_person(network, network_persons[i])) > len(max_community): # Vérifie si la longueur de la communauté trouvée pour la personne en cours est plus grande que celle de la communauté actuelle
            max_community = find_community_from_person(network, network_persons[i]) # Si c'est le cas, remplace la communauté actuelle par celle trouvée pour la personne en cours
        i+=1
    return(max_community) # Retourne la communauté la plus populaire
