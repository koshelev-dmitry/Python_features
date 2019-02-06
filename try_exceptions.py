def foo(var):
    try:
        print(var)
        # 1 + print(var)
    except:
        1 + print('Why do you print me?') + 1
    else:
        1 + print('Why do you print me?') + 1
    finally:
        return


print(foo("Hello"))


"""
>> Why do you print me? 
no raise of errors
"""
