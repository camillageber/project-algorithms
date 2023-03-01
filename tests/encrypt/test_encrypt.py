from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():

    assert encrypt_message("pipoca", 9) == "acopip"

    assert encrypt_message("pipoca", -1) == "acopip"

    assert encrypt_message("pipoca", 2) == "acop_ip"

    assert encrypt_message("chocolate", 4) == "etalo_cohc"

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("hello", "world")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(00, 00)
