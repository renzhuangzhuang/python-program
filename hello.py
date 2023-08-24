def testlist(value_list):
    return value_list.append("end")


if __name__ == "__main__":
    list_test = [value for value in range(1,11)]
    print(list_test)

    print("++++++++++")
    testlist(list_test)
    print(list_test)
