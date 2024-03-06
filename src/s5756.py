class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, x, y):
        return x + y

calculator = Calculator()
result = calculator.add(5, 10)
print("Result:", result)

# Bug: Calling a non-callable value
calculator = 42
result = calculator.add(5, 10)
print("Result:", result)

#adding comment to trigger commit


name = name




parser = etree.XMLParser() # Noncompliant: by default resolve_entities is set to true
tree1 = etree.parse('ressources/xxe.xml', parser)
root1 = tree1.getroot()

parser = etree.XMLParser(resolve_entities=True) # Noncompliant
tree1 = etree.parse('ressources/xxe.xml', parser)
root1 = tree1.getroot()
