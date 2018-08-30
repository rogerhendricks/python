from kivy.app import App

from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout):
	def __init__(self, **kwargs):
		super(LoginScreen, self).__init__(**kwargs)
		#add two colums to the window
		self.cols = 2
		
		
		# added a label widget
		self.add_widget(Label(text="Username"))
		#create a text input
		self.username = TextInput(multiline=False)
		# show the widget
		self.add_widget(self.username)
		
		
		# add a label widget
		self.add_widget(Label(text="Password"))
		# crete a text unput
		self.password = TextInput(password=True, multiline=False)
		# display the widget
		self.add_widget(self.password)


class KivyApp(App):
	def build(self):
		return LoginScreen()

if __name__ == '__main__':
	KivyApp().run()
