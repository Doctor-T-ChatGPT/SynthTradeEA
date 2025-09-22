from SynthTradeEA.core import ping

def test_ping():
    assert ping() == "synthtradeea:ok"
