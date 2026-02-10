def admin_only(dashboard):
    def wrapper(username):
        if username=="admin":
            print("hi manya")
            dashboard(username)
        else:
            print("access denied")
    return wrapper

@admin_only
def dashboard(username):
    print("welcom to dashboard")
dashboard("admin")