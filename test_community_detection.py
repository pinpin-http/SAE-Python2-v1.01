from community_detection import *


tab_amis0 = lecture_reseau("files/Communaute0.csv")
tab_amis1 = lecture_reseau("files/Communaute1.csv")
tab_amis2 = lecture_reseau("files/Communaute2.csv")
tab_amis3 = lecture_reseau("files/Communaute3.csv")
tab_amis4 = lecture_reseau("files/Communaute4.csv")

network0 = create_network(tab_amis0)
network1 = create_network(tab_amis1)
#les autres network prennent trop de temps a se créer


###############################################################################################################################################################

def test_create_network(list_of_friends):
    gen_dico_dico_reseau = dico_reseau(list_of_friends)
    gen_dico_create_network = create_network(list_of_friends)
    
    assert gen_dico_dico_reseau == gen_dico_create_network, (" la fonction create_network ne genere pas le bon dico ")

if 1 == 1:    
    test_create_network(tab_amis0)
    test_create_network(tab_amis1)
    print('test create_network(): OK')


###############################################################################################################################################################

def test_get_people(network):
    liste = list(network.keys())
    liste_get_people = get_people(network)

    assert liste_get_people == liste, ("La fonction get_people ne retourne pas correctement les utilisateurs du reseau")

if 1 == 1:
    test_get_people(network0)
    test_get_people(network1)
    print("test get_people() : OK")

###############################################################################################################################################################

def test_are_friends(network,network1):
    
    assert are_friends(network,"Alice","Bob") == True
    assert are_friends(network,"Alice","Charlie") == False
    assert are_friends(network1,"Rufino","Mady") == True
    assert are_friends(network1,"Rufino","olavi") == False
    print("test are_friends(): OK")

test_are_friends(network0,network1)

###############################################################################################################################################################

def test_all_his_friends(network):
    assert all_his_friends(network, "Alice", ["Bob","Dominique"]) == True
    assert all_his_friends(network, "Alice", ["Bob","Charlie"]) == False
    print("test all_his_friends(): OK")

test_all_his_friends(network0)

###############################################################################################################################################################

def test_is_a_community(network, group):
    assert is_a_community(network0,['Alice','Bob','Charlie','dominique']) == False
    assert is_a_community(network0,['Alice','Bob','dominique']) == True
    assert is_a_community(network0,['Bob','Charlie']) == True
    
    print("test is_a_community(): OK")

###############################################################################################################################################################

def test_find_community(network, network1):
    assert find_community(network,["Alice","Bob","Charlie","Dominique"]) == ['Alice', 'Bob', 'Dominique']
    assert find_community(network1,['Faizel','Barbra', 'Placide', 'Rufino', 'Barbra', 'Björn', 'Olavi']) == ['Faizel', 'Barbra', 'Rufino', 'Olavi']
    
    print("test find_community(): OK")

test_find_community(network,network1)

###############################################################################################################################################################
def test_order_by_decreasing_popularity():
    assert order_by_decreasing_popularity(network1,['Faizel','Barbra','Placide','Rufino']) == ['Barbra', 'Rufino', 'Placide', 'Faizel']
    assert order_by_decreasing_popularity(network0,['Alice','Bob','Charlie','Dominique']) == ['Bob', 'Alice', 'Dominique', 'Charlie']
    
    print("test order_by_decreasing_popularity(): OK")

test_order_by_decreasing_popularity()

###############################################################################################################################################################

def test_find_community_by_decreasing_popularity():
    assert find_community_by_decreasing_popularity(network0) == ['Bob', 'Alice', 'Dominique']
    assert find_community_by_decreasing_popularity(network1) ==['Barbra', 'Vittorio', 'Rufino', 'Mady']
    
    print("test find_community_by_decreasing_popularity(): OK")

test_find_community_by_decreasing_popularity()

###############################################################################################################################################################
def test_find_community_from_person():
    assert find_community_from_person(network0,'Bob') == ['Bob', 'Alice', 'Dominique']
    assert find_community_from_person(network1,'Barbra') == ['Barbra', 'Vittorio', 'Rufino', 'Mady']
    assert find_community_from_person(network1,'Vittorio') == ['Vittorio', 'Barbra', 'Rufino', 'Louis', 'Olavi']
    assert find_community_from_person(network0,'Alice') == ['Alice', 'Bob', 'Dominique']
    
    print('test find_community_from_person(): OK')


test_find_community_from_person()



###############################################################################################################################################################
def test_find_max_community():
    assert find_max_community(network0) == ['Alice', 'Bob', 'Dominique']
    assert find_max_community(network1) == ['Vittore', 'Vittorio', 'Barbra', 'Cloe', 'Mady']
    print("test find_max_community(): OK")

test_find_max_community()

###############################################################################################################################################################

print('END')

