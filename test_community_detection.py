from community_detection import *

amis_comm1 = lecture_reseau("files/Communaute1.csv")
amis_comm2 = lecture_reseau("files/Communaute2.csv")
dico_res_comm1 = create_network(amis_comm1)
dico_res_comm2 = create_network(amis_comm2)

def test_create_network():
    assert dico_res_comm1 == dico_reseau(amis_comm1)
    assert dico_res_comm1 == dico_reseau(amis_comm2)
    print("Test 1 passed !")

def test_get_people():
    assert get_people(dico_res_comm1) == personnes_reseau(amis_comm1)
    assert get_people(dico_res_comm2) == personnes_reseau(amis_comm2)
    print("Test 2 passed !")

def test_are_friends():
    assert are_friends(dico_res_comm1, "Barbra", "Cloe")
    assert not are_friends(dico_res_comm1, "Mady", "Illtyd")
    print("Test 3 passed !")

def test_all_his_friends():
    assert all_his_friends(dico_res_comm1, "Mady", ['Idelle', 'Rufino', 'Vittore', 'Jakob', 'Giedrius', 'Barbra'])
    assert not all_his_friends(dico_res_comm1, "Mady", ['Barbra', 'Kirsa', 'Louis', 'Olavi', 'Placide'])
    print("Test 4 passed !")

def test_is_a_community():
    assert is_a_community(dico_res_comm1, ['Mady', 'Rufino', 'Vittorio', 'Barbra'])
    assert is_a_community(dico_res_comm1, ['Björn', 'Rufino', 'Mady'])
    assert not is_a_community(dico_res_comm1, ["Cloe", "Idelle", "Mady", "Björn", "Marwa"])
    print("Test 5 passed !")

def test_order_by_decreasing_popularity():
    assert order_by_decreasing_popularity(dico_res_comm1, ["Mady"]) == ["Mady"]
    assert order_by_decreasing_popularity(dico_res_comm1, ['Giedrius', 'Mady', 'Kirsa', 'Vittore']) == ['Mady', 'Vittore', 'Giedrius', 'Kirsa']
    print("Test 6 passed !")

def test_find_community_by_decreasing_popularity():
    assert find_community_by_decreasing_popularity(dico_res_comm1) == ['Barbra', 'Vittorio', 'Rufino', 'Mady']
    print("Test 7 passed !")