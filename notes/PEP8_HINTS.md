### Underscores
1. **_var**  
``Single underscores - name is meant for internal use. ``   
**Note!** If you use a wildcard import(*) to import all names from the module,  
Python will not import names with a leading underscore  
(unless the module defines an __all__ list that overrides this behavior)
2. **var_**  
``a single trailing underscore (postfix) is used by convention to avoid naming conflicts with Python keywords.``
3. **__var**  
``A double underscore prefix causes the Python interpreter to rewrite the   
attribute name in order to avoid naming conflicts in subclasses.``  
_``class Test:  ``   
     ``def __init__(self):``  
        ``self.foo = 11``
        ``self._bar = 23``
        ``self.__baz = 23``  
``t = Test()``_
``dir(t)``  
>>['_Test__baz', '__class__', '__delattr__', '__dict__', '__dir__',
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__',
 '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
 '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
 '__weakref__', '_bar', 'foo']
>
>
