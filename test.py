def create_network(list_of_friends):
    i = 0
    dico = {}
    tab_keys = []

    while i < len(list_of_friends):
        if i%2==0:
            dico[list_of_friends[i]].append(list_of_friends[i+1])
        else:
            dico[list_of_friends[i]].append(list_of_friends[i-1])
        if not list_of_friends[i] in tab_keys:
            tab_keys.append(list_of_friends[i])
        i+=1
    return(dico)

print(create_network(["Alice", "Bob", "Dominique", "Alice"]))