from simulator import SoFIFASimulator
from pytest import raises, CaptureFixture

def test_invalid_team():
    """
        Tests to ensure that a KeyError is raised 
        when an unsupported team is requested within the simulator.
    """
    with raises(KeyError):
        SoFIFASimulator("Chelsea", "bayern").run_simulator()

def test_string_manipulation(capfd: CaptureFixture):
    """
        Tests to ensure that the simulator will still run
        even with capitalization inconsistencies as long as
        supported teams are requested by the user.
    """
    SoFIFASimulator("aRSeNaL", "CHELSEA").run_simulator()
    out: str = capfd.readouterr()[0]
    assert len(out) > 0