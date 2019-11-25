import datetime

def ask_for_user_exit(spell: str):
    print("Cannot find spell {0} on the primary and secondary sites. "
          "Continue program? (Y/n)".format(spell))
    in1 = input(">>> ")
    if in1.lower() != "y":
        print("Exiting...")
        exit(-1)

def get_timestamp() -> str:
    # Ref: https://stackoverflow.com/a/28147286
    t = datetime.datetime.now().replace(microsecond=0).isoformat()
    return t
