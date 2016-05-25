from kivy.app import App
from kivy.lang import Builder


class ItemsForHireApp(App):
    def __init__(self, **kwargs):

        super(ItemsForHireApp, self).__init__(**kwargs)
        self.items_list = []
        in_file = open("items.csv", "r")
        for line in in_file:
            item_match = line.strip().replace(" ", "").split(",")
            name = item_match[0]
            description = item_match[1]
            price = item_match[2]
            hired = item_match[3]

            self.items_list.append((item_match[0], item_match[1], item_match[2], item_match[3]))

    def build(self):
        # Window.size = (350, 700)
        self.title = "Items For Hire"
        self.root = Builder.load_file('gui.kv')
        return self.root

    def press_add(self):
        self.root.ids.popup.open()

    def press_cancel(self):
        self.root.ids.popup.dismiss()

    def press_save(self):
        self.root.ids.popup.dismiss()

    def show_all_items(self):
        # this is the function that prints all items in the list
        print("All items on file (* indicates item is currently out):")
        item_count_number = -1
        for printing_items in self.items_list:
            if len(printing_items[3]) == 3:
                item_count_number += 1
                print("{0} = {1} = ${2} *".format(item_count_number, printing_items[0:2], printing_items[2]))
            else:
                item_count_number += 1
                print("{0} = {1} = ${2}".format(item_count_number, printing_items[0:2], printing_items[2]))


ItemsForHireApp().run()
