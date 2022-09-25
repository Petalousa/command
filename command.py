from random import randint
import json

BAR_WIDTH = 30


names = [
    "Alpha",
    "Bravo",
    "Charlie",
    "Delta",
    "Echo",
    "Foxtrot",
    "Golf",
    "Hotel",
    "Lima",
    "Mike",
    "November",
    "Oscar",
    "Papa",
    "Quebec",
    "Sierra",
    "Tango",
    "Uniform",
    "Victor",
    "Whiskey",
    "Xray",
    "Yankee"
]

def make_junk_data(width, depth):
    ret_dict = {}
    for _ in range(randint(1, width)):
        name = names[randint(0, len(names)-2)]
        if depth > 1:
            ret_dict[name] = make_junk_data(width, depth - 1)
        else:
            ret_dict[name] = []
            for _ in range(randint(0, width)):
                leaf_name = names[randint(0, len(names)-2)]
                ret_dict[name].append(leaf_name)
    return ret_dict

class Commander:
    def __init__(self):
        self.exit_warning = None
        self.json_data = make_junk_data(5, 3)
        self.path = []
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


    # NAVIGATE MENU
    def display_nav(self):
        self.print_bar()
        print("--NAV MENU--")
        current_level = self.json_data

        for x in self.path:
            print(" > ", end='')
            print(x, end='')
            current_level = current_level[x]
        print('')

        i = 1
        if isinstance(current_level, list):
            for val in current_level:
                print("  -" + val)
        else:
            self.keys = []
            for key in current_level:
                self.keys.append(key)
                print("%d. %s" % (i, key))
                i += 1

        if len(self.path) > 0:
            print("%d. %s" % (i, ".."))
        print("0. quit")


    def go_up(self):
        if len(self.path) > 0:
            self.path = self.path[:-1]


    def handle_nav(self):
        _in = input(">")

        current_level = self.json_data
        for x in self.path:
            current_level = current_level[x]

        menu_selection = None
        try:
            menu_selection = int(_in)
        except Exception:
            pass

        if menu_selection is not None:
            if isinstance(current_level, list):
                if menu_selection == 1 and len(self.path) > 0:
                    self.path = self.path[:-1]
            elif menu_selection > 0 and menu_selection <= len(self.keys):
                self.path.append(self.keys[menu_selection-1])
            elif menu_selection == (len(current_level) + 1):
                self.go_up()

        if _in == "..":
            self.go_up()

        if _in == "0":
            menu_selection = None
            self.path = []
            return False
        return True

    # MAIN MENU
    def generate_random(self):
        print("generating new data...")
        self.exit_warning = "You have unsaved changes"
        self.json_data = make_junk_data(5, 3)
        print("done!")

    def print_json(self):
        self.exit_warning = None
        self.print_bar()
        print(json.dumps(self.json_data, indent=4))

    def navigate_json(self):
        self.run_menu(self.display_nav, self.handle_nav)

    def display_main(self):
        self.print_bar()
        print("--MAIN MENU--")
        print("1. generate random data")
        print("2. print data")
        print("3. navigate")
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
            self.generate_random()
        elif _in == "2":
            self.print_json()
        elif _in == "3":
            self.navigate_json()

        return True

    def start(self):
        self.run_menu(self.display_main,self.handle_main)


c = Commander()
c.start()