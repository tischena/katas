from needless_chaos import needless_chaos_func, results_array

def test_needless_chaos():
    results_array.clear()

    assert needless_chaos_func(5, 3) # 2
    assert needless_chaos_func(10, 7) # 2 or 3
    print(needless_chaos_func(5, 1)) # 2 or 3 or 4