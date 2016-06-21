"""Adrian Zahra, 21/06/2016, https://github.com/adrianZahra/CP1404-A2.git"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.button import Button

from Item import Item_info
from ItemList import Item_vault


class ItemsForHireApp(App):
    status_text = StringProperty()

    def build(self):
        # this function creates and startes the app
        # it fist calls the Item_vault class and passes in the CSV file as a paramater
        # it also calls the button_creator fucntion so it can imediatly display all the items as widgets in the app
        self.item_Info_Holder = Item_vault("items.csv")
        # Window.size = (350, 700)
        self.title = "Items For Hire"
        self.root = Builder.load_file('gui.kv')
        self.button_creator()
        self.no_items_check()
        return self.root


    def no_items_check(self):
        # this function was designed so that the information text will know if there are items or no items in a csv file
        # if the item holder contain no objects then its length will be 0 triggering the no items message
        if len(self.item_Info_Holder.item_list) == 0:
            self.status_text = "There are currently no items or no item file was found.\n You can still add new items and a new file will be made upon saving and exiting"
        else:
            self.status_text = "Choose a button function on the left"

    # the following two functions work with the popup so you can open and close it when nesecary
    def press_add(self):
        self.root.ids.popup.open()

    def press_cancel(self):
        self.clear_text_feilds()
        self.root.ids.popup.dismiss()

    def in_changer(self, buttons_name):
        # the folowing function is used to change the status of an item from "in" to "out"
        # it takes in the name of the button as a parameter and ckeck if the buttons name matches the name of an item
        # when the item is located it then changes its in_out status to "out" and displays the name of the object that has been selected
        name_Search = buttons_name.text
        for found_Item in self.item_Info_Holder.item_list:
            if found_Item.name == name_Search:
                found_Item.in_out = "out"
                print(found_Item.name, found_Item.in_out)
                self.status_text = "{} has been selected for hire".format(found_Item.name)

    def out_changer(self, buttons_name):
        # the folowing function is used to change the status of an item from "out" to "in"
        # it takes in the name of the button as a parameter and ckeck if the buttons name matches the name of an item
        # when the item is located it then changes its in_out status to "in" and displays the name of the object that has been selected
        name_Search = buttons_name.text
        for found_Item in self.item_Info_Holder.item_list:
            if found_Item.name == name_Search:
                found_Item.in_out = "in"
                print(found_Item.name, found_Item.in_out)
                self.status_text = "{} has been selected to be returned".format(found_Item.name)


    def clear_grid(self):
        # this function is general pourpose and is called when the grid needs to be cleared of its items for repopulation
        self.root.ids.entriesBox.clear_widgets()

    def list_in_stock(self):
        # this function was created to list all the items that are in stock
        # when one of the in stock items are clicked it calls the in_changer function
        # this function will only display items whos hire status are "in"
        self.status_text = "Choose items you wish to hire on the right then select Confirm"
        self.clear_grid()
        for printing_items in self.item_Info_Holder.item_list:
            if printing_items.in_out == "in":
                item_button = Button(text=printing_items.name)
                item_button.bind(on_release=self.in_changer)
                item_button.background_color = (0, 1, 0, 2)
                self.root.ids.entriesBox.add_widget(item_button)


    def list_out_stock(self):
        # this function was created to list all the items that are out of stock
        # when one of the in stock items are clicked it calls the out_changer function
        # this function will only display items whos hire status are "out"
        self.status_text = "Choose items you wish to return on the right then select Confirm"
        self.clear_grid()
        for printing_items in self.item_Info_Holder.item_list:
            if printing_items.in_out == "out":
                item_button = Button(text=printing_items.name)
                item_button.bind(on_release=self.out_changer)
                item_button.background_color = (1, 0, 0, 2)
                self.root.ids.entriesBox.add_widget(item_button)


    def button_creator(self):
        # this function was made to list every item
        # it makes use of an if statement with an "in" or "out" check
        # items are then coded so a user know which items are in or out ofS stock
        self.clear_grid()
        for printing_items in self.item_Info_Holder.item_list:
            self.no_items_check()
            if printing_items.in_out == "out":
                item_button = Button(text=printing_items.name)
                item_button.background_color = (1, 0, 0, 2)
                self.root.ids.entriesBox.add_widget(item_button)
            else:
                item_button = Button(text=printing_items.name)
                item_button.background_color = (0, 1, 0, 2)
                self.root.ids.entriesBox.add_widget(item_button)



    def save_item(self, Item_Name_Catch, Item_Description_Catch, Item_Price_Catch):
        # this function is used to take inupt collected from the popup and adds it to the class as another item object
        # it also creates and adds the new items widget button
        # it takes in the new items name condition and price from the popup as input parameters ad are then appended as a object just like in the Item_Valt class
        self.item_Info_Holder.item_list.append(
            Item_info(Item_Name_Catch.replace(" ", ""), Item_Description_Catch.replace(" ", ""), Item_Price_Catch,
                      "in"))
        item_button = Button(text=Item_Name_Catch)
        item_button.background_color = (0, 1, 0, 2)
        self.root.ids.entriesBox.add_widget(item_button)
        self.clear_text_feilds()
        self.root.ids.popup.dismiss()
        self.button_creator()


    def clear_text_feilds(self):
        # this fucntion is called upon exit of the popup it makes sure all feilds are empty for the next item to be entered
        self.root.ids.Item_Name_Catch.text = " "
        self.root.ids.Item_Description_Catch.text = " "
        self.root.ids.Item_Price_Catch.text = " "

    def exit_program(self):
        # this function was designed to write previous and new items back into the csv so they can be reopend and used again
        # the function makes use of a for loop to make each line of the text file for 1 item
        # it then modifies the string to match CSV standards
        # when this has occurred then program will then close with the help of quit()
        file_write = open("items.csv", "w")
        for set_items in self.item_Info_Holder.item_list:
            print(set_items)
            write_items = str(set_items)
            file_write.write(write_items.strip("( )").replace(" ", ",").replace("$", " ").strip() + "\n")
        quit()


ItemsForHireApp().run()
