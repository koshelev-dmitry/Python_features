def test(var):
    try:
        print(var)
        # 1 + print(var)
    except:
        1 + print('Why do you print me?') + 1
    else:
        1 + print('Why do you print me?') + 1
    finally:
        return 'Opa 2'


print(test("Hello"))