from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from ItemList import Item_vault
from Item import Item_info

class ItemsForHireApp(App):

    """
    def __init__(self, **kwargs):

        super(ItemsForHireApp, self).__init__(**kwargs)
        self.items_list = []
        in_file = open("items.csv", "r")
        for line in in_file:
            item_match = line.strip().replace(" ", "").split(",")
            name = item_match[0]
            description = item_match[1]
            price = item_match[2]

            self.items_list.append((item_match[0], item_match[1], item_match[2], item_match[3]))"""



    def build(self):
        self.bagOfHolding = Item_vault("items.csv")
        # Window.size = (350, 700)
        self.title = "Items For Hire"
        self.root = Builder.load_file('gui.kv')
        self.button_creator()
        return self.root

    def press_add(self):
        self.root.ids.popup.open()

    def press_cancel(self):
        self.clear_text_feilds()
        self.root.ids.popup.dismiss()


    def testchange(self):
        for testitems in self.bagOfHolding.item_list:
            print(testitems.in_out[0:])

    def clear_grid(self):
        self.root.ids.entriesBox.clear_widgets()

    def hire_items(self):
        self.clear_grid()
        for printing_items in self.bagOfHolding.item_list:
            if printing_items.in_out == "in":
                item_button = Button(text=printing_items.name)
                item_button.background_color = (0,1,0,2)
                self.root.ids.entriesBox.add_widget(item_button)

    def return_items(self):
        self.clear_grid()
        for printing_items in self.bagOfHolding.item_list:
            if printing_items.in_out == "out":
                item_button = Button(text=printing_items.name)
                item_button.background_color = (1,0,0,2)
                self.root.ids.entriesBox.add_widget(item_button)

    def button_creator(self):
        self.clear_grid()
        for printing_items in self.bagOfHolding.item_list:
            if printing_items.in_out == "out":
                item_button = Button(text=printing_items.name)
                item_button.background_color = (1,0,0,2)
                self.root.ids.entriesBox.add_widget(item_button)
            else:
                item_button = Button(text=printing_items.name)
                item_button.background_color = (0,1,0,2)
                self.root.ids.entriesBox.add_widget(item_button)


    def save_item(self, Item_Name_Catch, Item_Description_Catch, Item_Price_Catch):
        self.bagOfHolding.item_list.append(Item_info(Item_Name_Catch, Item_Description_Catch, Item_Price_Catch, "in"))
        item_button = Button(text=Item_Name_Catch)
        item_button.background_color = (0,1,0,2)
        self.root.ids.entriesBox.add_widget(item_button)
        self.clear_text_feilds()
        self.root.ids.popup.dismiss()

    def clear_text_feilds(self):
        self.root.ids.Item_Name_Catch.text = " "
        self.root.ids.Item_Description_Catch.text = " "
        self.root.ids.Item_Price_Catch.text = " "






ItemsForHireApp().run()
