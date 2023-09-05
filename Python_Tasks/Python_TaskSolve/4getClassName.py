class Trello:
    
    def name(self,name):
        return name
    
t=Trello()

print(t.__class__.__name__)

# or u can use:
print(type(t).__name__)