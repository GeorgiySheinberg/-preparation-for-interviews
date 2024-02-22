from check_balance import check_balanced
# Сбалансированные последовательности:
string_1 = '(((([{}]))))'
string_2 = "[([])((([[[]]])))]{()}"
string_3 = '{{[()]}}'
# Несбалансированные последовательности:

string_4 = "}{}"
string_5 = "{{[(])]}}"
string_6 = "[[{())}]"
if __name__ == '__main__':
    print(check_balanced(string_1))
    print(check_balanced(string_2))
    print(check_balanced(string_3))
    print(check_balanced(string_4))
    print(check_balanced(string_5))
    print(check_balanced(string_6))
