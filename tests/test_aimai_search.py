from aimai_search import AimaiSearch


def test_aimai_search():
    a = AimaiSearch(["あいまい検索", "kensaku", "傑作"])

    assert a.search_best("kensaku") == ("kensaku", 100.0)

    terms, _ = zip(*a.search("kensaku"))
    assert terms == ("kensaku", "あいまい検索", "傑作")

    terms, _ = zip(*a.search("kensaku", limit=1))
    assert terms == ("kensaku",)

    terms, _ = zip(*a.search("kensaku", limit=2))
    assert terms == ("kensaku", "あいまい検索")

    a = AimaiSearch(["カツカレー", "カツ丼", "カルテット"])
    assert a.search_best("cultet curry")[0] == "カツカレー"
    assert a.search_best("katsu kare")[0] == "カツカレー"
    assert a.search_best("katsu don")[0] == "カツ丼"
    assert a.search_best("quartet")[0] == "カルテット"
    assert a.search_best("karutetto")[0] == "カルテット"
