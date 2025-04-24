from homework3 import Solution, list_to_linked_list, linked_list_to_list

def test_add_two_numbers():
    s = Solution()

    # Test Case 1
    l1 = list_to_linked_list([2, 4, 3])
    l2 = list_to_linked_list([5, 6, 4])
    result = linked_list_to_list(s.addTwoNumbers(l1, l2))
    assert result == [7, 0, 8], f"Expected [7, 0, 8], but got {result}"

    # Test Case 2
    l1 = list_to_linked_list([0])
    l2 = list_to_linked_list([0])
    result = linked_list_to_list(s.addTwoNumbers(l1, l2))
    assert result == [0], f"Expected [0], but got {result}"

    # Test Case 3
    l1 = list_to_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = list_to_linked_list([9, 9, 9, 9])
    result = linked_list_to_list(s.addTwoNumbers(l1, l2))
    assert result == [8, 9, 9, 9, 0, 0, 0, 1], f"Expected [8, 9, 9, 9, 0, 0, 0, 1], but got {result}"

    print("All test cases passed!")

if __name__ == "__main__":
    test_add_two_numbers()
