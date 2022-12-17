has_high_income = True
has_good_credit = True
if has_good_credit and  has_high_income:
    print("allowed ")


if has_high_income and not has_good_credit:
    print("allowed")


if has_high_income or has_good_credit:
    print("allowed")

if has_high_income or not has_good_credit:
    print("allowed")

if not has_high_income and has_good_credit:
    print("allowed")
#and:both must be true or false
#or:at least one must be true or false