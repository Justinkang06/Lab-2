import Lab2

print("Test_Lab2")

# Test for find_min_max()
def test_find_min_max():
    temperature_list = [10, 20, 30, 40, 50]
    result = Lab2.find_min_max(temperature_list)
    assert result == [10, 50]

# Test for calc_average()
def test_calc_average():
    temperature_list = [10, 20, 30, 40, 50]
    result = Lab2.calc_average(temperature_list)
    expected = 30
    assert result == expected

# Test for calc_median_temperature() with odd number of items
def test_calc_median_temperature_odd():
    temperature_list = [10, 20, 30, 40, 50]
    result = Lab2.calc_median_temperature(temperature_list)
    expected = 30
    assert result == expected

# Test for calc_median_temperature() with even number of items
def test_calc_median_temperature_even():
    temperature_list = [10, 20, 30, 40]
    result = Lab2.calc_median_temperature(temperature_list)
    expected = (20 + 30) / 2
    assert result == expected
