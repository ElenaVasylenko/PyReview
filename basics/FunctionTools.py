
# PROPERTY , get, set. del added automaticly to object. Function could be used as a variable


class Thing:
    def __init__(self, my_word):
        self._word = my_word
    @property
    def word(self):
        return self._word
print(Thing('ok').word)

t = Thing('no')
print(t._word)
### 'ok'