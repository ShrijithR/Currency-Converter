from .Dictionaries import one_nine, ten_teen, twty_nty
from .support import Attrs

class Paise(Attrs):
    """Define method to check if the paise part of the argument
    is present, and return the converted string if it does"""
    def get_paise(self):    
        self.paise = ''
        #Check if paise amount is given, else catch index error
        try:
            if int(self.split_list[1]) != 0:
                self.paise = ' '+ self.split_list[1] +'/100'
        except IndexError:
            pass
        return self.paise

class Single_double(Attrs): 
    def convert(self):
        """Converts the single and double digit numbers"""
        if self.amount == 0:
            return
        if self.length == 1:
            return one_nine[self.amount]
        if self.num_list[0] == 1:
            return ten_teen[self.amount]
        if not self.num_list[1] == 0:
            return ' '.join((twty_nty[self.num_list[0]], 
            one_nine[self.num_list[1]] ))
        
        return twty_nty[self.num_list[0]]

class Hundreds(Attrs):
    def convert(self):
        """Converts three digit numbeRs"""
        if self.amount == 0:
            return    
        
        if self.length < 3:
            self.singleDouble = Single_double(self.amount)
            return self.singleDouble.convert()
        self.last_two_digits = int(''.join(self.num_str[1:]))
        self.singleDouble = Single_double(self.last_two_digits)
        
        if self.singleDouble.convert():
            return (
                ' '.join((
                    one_nine[self.num_list[0]], 'Hundred', 'and', 
                    self.singleDouble.convert()
                ))
            )
        return (
            ' '.join((
                one_nine[self.num_list[0]], 'Hundred'
            ))
        )

class Thousand(Attrs):    
    def convert(self):
        """Converts four and five digit numbeRs"""
        if self.amount == 0:
            return 
        if self.length <= 3:
            self.hundreds = Hundreds(self.amount)
            return self.hundreds.convert()
        
        self.last_three_digits = int(''.join(self.num_str[-3:]))
        self.singleDouble = Single_double(self.num_list[0])
        self.hundreds = Hundreds(self.last_three_digits)
        
        if self.length == 4:
            if self.hundreds.convert():
                return (
                ' '.join((
                self.singleDouble.convert(), 'Thousand', 
                self.hundreds.convert()
                    ))
                )
            return (
                ' '.join((
                self.singleDouble.convert(), 'Thousand'
                ))
            )
        self.singleDouble = Single_double(int(''.join(self.num_str[:2])))
        
        if self.hundreds.convert():
            return (
            ' '.join((
            self.singleDouble.convert(), 'Thousand', 
            self.hundreds.convert()
                ))
            )
        return (
            ' '.join((
            self.singleDouble.convert(), 'Thousand'
            ))
        )

class Lakh(Attrs):
    def convert(self):
        """Converts six digit numbeRs"""
        if self.amount == 0:
            return
        
        if self.length <= 5:
            self.thousand = Thousand(self.amount)
            return self.thousand.convert()
        
        self.last_five_digits = int(''.join(self.num_str[-5:]))
        self.thousand = Thousand(self.last_five_digits)
        self.singleDouble = Single_double(self.num_list[0])
        
        if self.thousand.convert():
            return (
            ' '.join((
            self.singleDouble.convert(), 'Lakh', 
            self.thousand.convert()
                ))
            )
        
        return (
            ' '.join((
            self.singleDouble.convert(), 'Lakh'
            ))
        )