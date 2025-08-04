# The Decorator Pattern lets you dynamically add behavior to an object without modifying its original class.

# Instead of using a big inheritance tree, you "wrap" the object with decorators that add new functionality.


class Texteditor:
    def write(self):
        return "Writing text"

class Textdecorator:  # Base decorator class
    def __init__(self,editor):
        self.editor = editor
    def write(self):
        return self.editor.write()  # Delegates the call to the wrapped editor object
    
class Bolddecorator(Textdecorator): # Concrete Decorator class; for adding bold functionality
    def write(self):
        return f"<b>{self.editor.write()}</b>"
    
class Italicdecorator(Textdecorator): # Concrete Decorator class; for adding italic functionality
    def write(self):
        return f"<i>{self.editor.write()}</i>"


text = Bolddecorator(Texteditor())
print(text.write())  # Output: <b>Writing text</b>
text = Italicdecorator(Texteditor())
print(text.write())  # Output: <i><b>Writing text</b></i>
# This demonstrates the Decorator Pattern where we can add new functionality (bold, italic) to an existing object (text editor) without modifying its structure.


"""class coffee:
    def cost(self):
        return 5  

class coffeedecorator: # Base decorator class for coffee
    def __init__(self, coffee):
        self.coffee = coffee
    def cost(self):
        return self.coffee.cost()

class milkdecorator(coffeedecorator): # Decorator for adding milk functionality
    def cost(self):
        return self.coffee.cost() + 2  # Adds cost of milk
    
class espressodecorator(coffeedecorator): # Decorator for adding espresso functionality
    def cost(self):
        return self.coffee.cost + 5

class sugardecorator(coffeedecorator): # Decorator for adding sugar functionality
    def cost(self):
        return self.coffe.cost() + 1
    
order = coffee()
print(order.cost())  # Output: 5
order = espressodecorator(milkdecorator(sugardecorator(order)))
print(f"Order for coffee with one espresso shot with milk and sugar is ${order.cost()}")  # Output: 8 (5 + 2 + 1)
# This demonstrates how we can dynamically add functionality (milk, sugar, espresso) to the coffee object without changing its original class."""