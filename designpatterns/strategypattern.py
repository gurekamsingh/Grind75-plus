# abstract class
class TextFormatter:
    def format(self, text):
        raise NotImplementedError

# concrete classes implementing the abstract class
class UpperCaseFormatter(TextFormatter):
    def format(self, text):
        return text.upper()

class LowerCaseFormatter(TextFormatter):
    def format(self, text):
        return text.lower()   

# Context class that uses the strategy 
class TextEditor:
    def __init__(self, formatter: TextFormatter):
        self.formatter = formatter

    def publish(self, text):
        return self.formatter.format(text)
    
# Example usage

editor = TextEditor(UpperCaseFormatter())
print(editor.publish("hi my name is Gurekam"))

editor = TextEditor(LowerCaseFormatter())
print(editor.publish("hi my name is Gurekam"))

# Basically instead of using if else or switch statements to determine how to format text, 
# we used strategy pattern to encapsulate the formatting logic in separate classes. 
# This makes it easy to add new formatting strategies without modifying the existing code. 