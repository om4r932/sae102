from community_detection import *

amis_comm1 = lecture_reseau("files/Communaute1.csv")
amis_comm2 = lecture_reseau("files/Communaute2.csv")
dico_res_comm1 = create_network(amis_comm1)
dico_res_comm2 = create_network(amis_comm2)

def test_create_network():
    assert dico_res_comm1 == dico_reseau(amis_comm1)
    assert dico_res_comm2 == dico_reseau(amis_comm2)
    print("Test 1 passed !")

def test_get_people():
    assert get_people(dico_res_comm1) == personnes_reseau(amis_comm1)
    assert get_people(dico_res_comm2) == personnes_reseau(amis_comm2)
    print("Test 2 passed !")

def test_are_friends():
    assert are_friends(dico_res_comm1, "Barbra", "Cloe")
    assert are_friends(dico_res_comm2, "Olavi", "Vibol")
    assert not are_friends(dico_res_comm1, "Mady", "Illtyd")
    assert not are_friends(dico_res_comm2, "Marwa", "Lalie")
    print("Test 3 passed !")

def test_all_his_friends():
    assert all_his_friends(dico_res_comm1, "Mady", ["Idelle", "Rufino", "Vittore", "Jakob", "Giedrius", "Barbra"])
    assert all_his_friends(dico_res_comm2, "Ilies", ["Séverin", "Petru", "Christ", "Placide"])
    assert not all_his_friends(dico_res_comm1, "Vittore", ["Cloe", "Rufino", "Olavi", "Björn", "Mady"])
    assert not all_his_friends(dico_res_comm1, "Kirsa", ["Cloe", "Rufino", "Olavi", "Björn", "Mady"])
    print("Test 4 passed !")

def test_is_a_community():
    assert is_a_community(dico_res_comm1, ["Mady", "Rufino", "Vittorio", "Barbra"])
    assert is_a_community(dico_res_comm2, ["Dragan", "Cain", "Petru"])
    assert not is_a_community(dico_res_comm1, ["Cloe", "Idelle", "Mady", "Björn", "Marwa"])
    assert not is_a_community(dico_res_comm2, ["Illtyd", "Finn", "Placide", "Giedrius", "Stéphanie"])
    print("Test 5 passed !")

def test_find_community():
    assert find_community(dico_res_comm1, ["Idelle", "Mady", "Idelle", "Teodor"]) == ["Idelle", "Mady"]
    assert find_community(dico_res_comm1, ["Mady", "Rufino", "Olavi"]) == ["Mady", "Rufino"]
    assert find_community(dico_res_comm2, ["Shayla", "Évike", "Simo", "Idelle"]) == ["Shayla"]
    assert find_community(dico_res_comm2, ["Silviu", "Chatzkel", "Shirine", "Gordon"]) == ["Silviu"]
    print("Test 6 passed !")

def test_order_by_decreasing_popularity():
    assert order_by_decreasing_popularity(dico_res_comm1, ["Mady"]) == ["Mady"]
    assert order_by_decreasing_popularity(dico_res_comm1, ["Giedrius", "Mady", "Kirsa", "Vittore"]) == ["Mady", "Giedrius", "Vittore", "Kirsa"]
    assert order_by_decreasing_popularity(dico_res_comm2, ["Zayneb"]) == ["Zayneb"]
    assert order_by_decreasing_popularity(dico_res_comm2, ["Grwn", "Amadeo", "Cloe", "Pavao"]) == ["Pavao", "Amadeo", "Grwn", "Cloe"]
    print("Test 7 passed !")

def test_find_community_by_decreasing_popularity():
    assert find_community_by_decreasing_popularity(dico_res_comm1) == ["Rufino", "Mady", "Vittorio", "Barbra"]
    assert find_community_by_decreasing_popularity(dico_res_comm2) == ["Dragan", "Cain", "Petru"]
    print("Test 8 passed !")

def test_find_community_from_person():
    assert find_community_from_person(dico_res_comm1, "Idelle") == ["Idelle", "Mady"]
    assert find_community_from_person(dico_res_comm1, "Giedrius") == ["Giedrius", "Rufino", "Mady", "Vittorio"]
    assert find_community_from_person(dico_res_comm2, "Zayneb") == ["Zayneb"]
    assert find_community_from_person(dico_res_comm2, "Mady") == ["Mady", "Cain", "Petru"]
    print("Test 9 passed !")

def test_find_max_community():
    assert find_max_community(dico_res_comm1) == ["Barbra", "Rufino", "Mady", "Vittorio"]
    assert find_max_community(dico_res_comm2) == ['Mady', 'Cain', 'Petru']
    print("Test 10 passed !")
