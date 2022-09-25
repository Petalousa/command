

BAR_WIDTH = 30

class Commander:
    def __init__(self):
        self.exit_warning = None
        pass


    # generic function to continually diplay a menu
    # display_menu should print options
    # handle_menu should deal with user input
    # handle_menu should return True/False
    def run_menu(self, display_menu, handle_menu):
        run = True
        while run:
            display_menu()
            run = handle_menu()

    def print_bar(self, width=BAR_WIDTH):
        print('='*width)


    def display_main(self):
        self.print_bar()
        print("--MAIN MENU--")
        print("1. ")
        print("2. ")
        print("3. ")
        print("0. quit")


    def handle_main(self):
        _in = input(">")

        if _in == "0":
            if self.exit_warning == None:
                return False
            else:
                self.print_bar()
                print(self.exit_warning)
                _in = input("do you still wish to exit? (y/n) >")
                if _in.lower() == 'y':
                    return False
                if _in.lower() == '0':
                    return False

        elif _in == "1":
            self.exit_warning = "You have unsaved changes"
            print("unsaved changes.")
        elif _in == "2":
            self.exit_warning = None
            print("saved changes.")
            pass
        elif _in == "3":
            pass

        return True

    def start(self):
        self.run_menu(self.display_main,self.handle_main)


c = Commander()
c.start()