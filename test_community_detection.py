from community_detection import *

amis = lecture_reseau("files/Communaute1.csv")
dico_res = create_network(amis)

def test_create_network():
    assert dico_res == dico_reseau(amis)
    print("Test 1 passed !")

def test_get_people():
    assert get_people(dico_res) == personnes_reseau(amis)
    print("Test 2 passed !")

def test_are_friends():
    assert are_friends(dico_res, "Barbra", "Cloe")
    assert not are_friends(dico_res, "Mady", "Illtyd")
    print("Test 3 passed !")

def test_all_his_friends():
    assert all_his_friends(dico_res, "Mady", ['Idelle', 'Rufino', 'Vittore', 'Jakob', 'Giedrius', 'Barbra'])
    assert not all_his_friends(dico_res, "Mady", ['Barbra', 'Kirsa', 'Louis', 'Olavi', 'Placide'])
    print("Test 4 passed !")

def test_is_a_community():
    assert is_a_community(dico_res, ['Mady', 'Rufino', 'Vittorio', 'Barbra'])
    assert is_a_community(dico_res, ['Björn', 'Rufino', 'Mady'])
    assert not is_a_community(dico_res, ["Cloe", "Idelle", "Mady", "Björn", "Marwa"])
    print("Test 5 passed !")

def test_order_by_decreasing_popularity():
    assert order_by_decreasing_popularity(dico_res, ["Mady"]) == ["Mady"]
    assert order_by_decreasing_popularity(dico_res, ['Giedrius', 'Mady', 'Kirsa', 'Vittore']) == ['Mady', 'Vittore', 'Giedrius', 'Kirsa']
    print("Test 6 passed !")


print(order_by_decreasing_popularity(dico_res, ['Giedrius', 'Mady', 'Kirsa', 'Vittore']))