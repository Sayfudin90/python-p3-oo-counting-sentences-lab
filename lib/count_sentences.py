class MyString:
    def __init__(self, value=''):
        """Initialize a MyString object with a string value. Default is empty string."""
        self._value = ''
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")
    
    @property
    def value(self):
        """Get the string value."""
        return self._value
    
    @value.setter
    def value(self, new_value):
        """Set the string value, ensuring it's a string."""
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")
    
    def is_sentence(self):
        """Return True if the value ends with a period, False otherwise."""
        return self.value.endswith('.')
    
    def is_question(self):
        """Return True if the value ends with a question mark, False otherwise."""
        return self.value.endswith('?')
    
    def is_exclamation(self):
        """Return True if the value ends with an exclamation mark, False otherwise."""
        return self.value.endswith('!')
    
    def count_sentences(self):
        """
        Count the number of sentences in the value.
        Sentences end with '.', '?', or '!'.
        """
        if not self.value:
            return 0
        
        # Replace all sentence-ending punctuation with a period
        normalized = self.value
        for char in ['!', '?']:
            normalized = normalized.replace(char, '.')
        
        # Split by periods and count non-empty entries
        sentences = [s.strip() for s in normalized.split('.')]
        
        # Filter out empty strings
        sentences = [s for s in sentences if s]
        
        return len(sentences)