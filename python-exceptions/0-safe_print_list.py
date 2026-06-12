def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except Exception as e:  # هنا نمسك أي خطأ ونعطيه اسم e
            print("\n[خطأ]: نوع الخطأ هو:", type(e).__name__)
            print("[رسالة الخطأ]:", e)
            break
    print("")
    return count
