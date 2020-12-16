def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if len(digits) == 0:
        return []

    result = [""]
    digit_map = {
    "0": "0",
    "1": "1",
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
    }

    for digit in digits:
        tmp_list = []
        for chr in digit_map[digit]:
            for str in result:
                tmp_list.append(str+chr)
        result = tmp_list
    return result

print(letterCombinations(digits = "23"))