from appJar import gui
from form import form

loggedIn = False
app = gui("login")


def login(btn):
    if btn == 'login':
        usr = app.getEntry("Username")
        pw = app.getEntry("Password")

        if str(usr) == "bailey" and str(pw) == "password":
            app1 = form
            app1.form()
        else:
            print("failed")


def main():
    app.addLabelEntry("Username")
    app.addSecretLabelEntry("Password")
    app.addButton("login", login)
    app.go()


if __name__ == '__main__':
    main()
