
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window



class ItemsForHireApp(App):
    def build(self):
        #Window.size = (350, 700)
        self.title = "Items For Hire"
        self.root = Builder.load_file('gui.kv')
        return self.root

    def press_add(self):
       self.root.ids.popup.open()

    def press_cancel(self):
        self.root.ids.popup.dismiss()

    def press_save(self):
        self.root.ids.popup.dismiss()








ItemsForHireApp().run()
