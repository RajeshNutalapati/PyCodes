
def is_stressful(subj):
    print(subj)
    red = ['help','asap','urgent', 'HELP','ASAP','URGENT']
    if subj[-3:] == '!!!':
        print("here")
        return True
    elif subj.isupper():
        print("upper")
        return True
    elif subj in red:
        return True
    else:
        print("else")
        from collections import OrderedDict
        result = "".join(OrderedDict.fromkeys(subj))
        print("result", result)
        if result in red:
            return True
        else:
            return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    #assert is_stressful("I neeed HELP") == True, "Second"
    assert is_stressful("asap") == True, "Third"
    assert is_stressful("here!!!!") == True, "Fourth"
    assert is_stressful("URGEEEENNTTT here") == True, "Fifth"
    assert is_stressful("fbdg") == False, "Sixth"
    assert is_stressful("HE!LP") == True, "Seventh"
    print('Done! Go Check it!')