from solution import most_frequent_item_count
import codewars_test as test

@test.describe("Example tests")
def test_group():
    test.assert_equals(most_frequent_item_count([3, -1, -1]), 2, "didn't work for [3, -1, -1]")
    test.assert_equals(most_frequent_item_count([3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]), 5, "didn't work for [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]")
    test.assert_equals(most_frequent_item_count([]), 0, "didn't work for []")
    test.assert_equals(most_frequent_item_count([9]), 1, "didn't work for [9]")
