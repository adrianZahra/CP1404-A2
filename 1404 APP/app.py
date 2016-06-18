from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from ItemList import Item_vault
from Item import Item_info
from kivy.properties import StringProperty

class ItemsForHireApp(App):

    status_text = StringProperty()

    def build(self):
        self.bagOfHolding = Item_vault("items.csv")
        # Window.size = (350, 700)
        self.title = "Items For Hire"
        self.root = Builder.load_file('gui.kv')
        self.button_creator()
        self.status_text = "Choose a button function on the left"
        return self.root

    def press_add(self):
        self.root.ids.popup.open()

    def press_cancel(self):
        self.clear_text_feilds()
        self.root.ids.popup.dismiss()


    def in_changer(self, buttons_name):
        name = buttons_name.text
        for testitem in self.bagOfHolding.item_list:
            if testitem.name == name:
                testitem.in_out = "out"
                print(testitem.name, testitem.in_out)
                self.status_text = "{} has been selected for hire".format(testitem.name)

    def out_changer(self, buttons_name):
        name = buttons_name.text
        for testitem in self.bagOfHolding.item_list:
            if testitem.name == name:
                testitem.in_out = "in"
                print(testitem.name, testitem.in_out)
                self.status_text = "{} has been selected to be returned".format(testitem.name)


    def clear_grid(self):
        self.root.ids.entriesBox.clear_widgets()

    def list_hired_items(self):
        self.status_text = "Choose items you wish to hire then select Confirm"
        self.clear_grid()
        for printing_items in self.bagOfHolding.item_list:
            if printing_items.in_out == "in":
                item_button = Button(text=printing_items.name)
                item_button.bind(on_release=self.in_changer)
                item_button.background_color = (0,1,0,2)
                self.root.ids.entriesBox.add_widget(item_button)


    def list_returned_items(self):
        self.status_text = "Choose items you wish to return then select Confirm"
        self.clear_grid()
        for printing_items in self.bagOfHolding.item_list:
            if printing_items.in_out == "out":
                item_button = Button(text=printing_items.name)
                item_button.bind(on_release=self.out_changer)
                item_button.background_color = (1,0,0,2)
                self.root.ids.entriesBox.add_widget(item_button)

    def button_creator(self):
        self.status_text = "Choose a button function on the left"
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
        self.bagOfHolding.item_list.append(Item_info(Item_Name_Catch.replace(" ", ""), Item_Description_Catch.replace(" ", ""), Item_Price_Catch, "in"))
        item_button = Button(text=Item_Name_Catch)
        item_button.background_color = (0,1,0,2)
        self.root.ids.entriesBox.add_widget(item_button)
        self.clear_text_feilds()
        self.root.ids.popup.dismiss()

    def clear_text_feilds(self):
        self.root.ids.Item_Name_Catch.text = " "
        self.root.ids.Item_Description_Catch.text = " "
        self.root.ids.Item_Price_Catch.text = " "

    def exit_program(self):
        file_write = open("items.csv", "w")
        for set_items in self.bagOfHolding.item_list:
            print(set_items)
            write_stuff = str(set_items)
            file_write.write(write_stuff.strip("( )").replace(" ", ",").replace("$", " ").strip() + "\n")
        quit()


ItemsForHireApp().run()
