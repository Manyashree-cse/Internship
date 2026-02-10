# def login(login_page):       #login_page or just page, any function name can be used 
def login(page):
    def wrapper(username,password):
        if username=="admin" and password=="1234":
            print("login successful")
            page(username,password)
            # login_page(username,password)
        else:
            print("login failed")
    return wrapper

@login
def login_page(username,password):
    print("welcome to dashboard")

login_page("admin","1234")