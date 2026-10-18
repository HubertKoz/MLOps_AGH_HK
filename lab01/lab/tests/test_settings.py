import pytest
from pydantic import ValidationError
from settings import Settings


def test_settings_ok():
    # podanie wiadomosci wprost
    s = Settings(ENVIRONMENT="test", APP_NAME="Lab1-test", ASDF="secret")
    assert s.ENVIRONMENT == "test"
    assert s.APP_NAME == "Lab1-test"


def test_settings_bad_env():
    # niepoprawne środowisko
    with pytest.raises(ValidationError):
        Settings(ENVIRONMENT="asdf", APP_NAME="Lab1-asdf", ASDF="secret")
