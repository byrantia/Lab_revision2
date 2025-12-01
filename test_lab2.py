import main as lab

def test_find_min_max():
    data = [0.51,2,3.4,12.3,421]
    actual_result = [0.51,421]

    result = lab.find_min_max(data)

    assert result == actual_result

def test_average():
    data = [1,2,3]

    actual = 2

    result = lab.cal_averge(data)

    assert result == actual


def test_median():
    data = [1.2,32.1,12]

    result = 12

    test = lab.cal_median(data)

    assert test == result