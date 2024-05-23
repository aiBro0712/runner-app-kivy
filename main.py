from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView
from kivy.uix.pagelayout import PageLayout 

class PageLayoutExample(PageLayout):
    pass

class ScrollViewExample(ScrollView):
    pass

class StackLayoutExample(StackLayout):
    # pass
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.orientation ="lr-bt"   
        for i in  range(0,100):
            i = Button(text=str(i+1),size_hint=(None,None),size =(dp(100),dp(100)) )
            self.add_widget(i)




# class GridLayoutExample(GridLayout):
#     pass

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass


class MainWidget(Widget):
    pass

class RunningApp(App):
    # def build(self):
    #     # return BoxLayoutExample()
    #     return AnchorLayout()
    pass
    
RunningApp().run()
 