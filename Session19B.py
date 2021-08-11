# Monkey Patching

class Theme:

    def show_theme(self):
        print("~~~~~~~~~~~~~~~~~~")
        print("Welcome to MyApp")
        print("Primary Color: BLACK")
        print("~~~~~~~~~~~~~~~~~~")


def show_customized_theme():
    print("########################")
    print("This is MyApp")
    print("Have a Great Day ahead :)")
    print("Primary Color: WHITE")
    print("########################")


def main():

    theme1 = Theme()
    print("theme1.show_theme before is:", theme1.show_theme)

    # Monkey Patching :) | Use Reference to Object and not the Class
    # Reference Copy
    theme1.show_theme = show_customized_theme
    print("theme1.show_theme now is:", theme1.show_theme)
    theme1.show_theme()

    theme2 = Theme()
    theme2.show_theme() # ?


if __name__ == '__main__':
    main()