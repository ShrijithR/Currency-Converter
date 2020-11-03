import logging, re

logging.basicConfig(level = logging.DEBUG, format = '%(message)s')
logging.disable(logging.DEBUG)

class Input_Validation():
    """Creates regex attributes to check if the input is valid"""
    def __init__(self, amount):
        #Convert input into proper form
        self.num_str = ''.join(str(amount).split(','))
        #Create regex condition attributes
        self.allowed_input = re.compile(r'[^\d.,]')
        self.allowed_dot = re.compile(r'\.')
        self.allowed_decimal_limit = re.compile(r'\.\d{3,}$')
        self.allowed_Start = re.compile(r'^\d')
        self.allowed_End = re.compile(r'\d$')
        #Create a list containing the conditions
        self.condition_list = [
            self.allowed_input.search(self.num_str),  
            len(self.allowed_dot.findall(self.num_str)) > 1,
            self.allowed_decimal_limit.search(self.num_str), 
            not self.allowed_Start.search(self.num_str),
            not self.allowed_End.search(self.num_str)
        ]        
    def validate(self):
        """Returns True if the input passes through the if conditions"""        
        if [i for i in self.condition_list if i]:
            return "Invalid input"
        logging.debug("Passed regex")
        
        if float(self.num_str) < 0 or float(self.num_str) > 999999.99:
            return "Number not within the limit"
        logging.debug("Passed limit")
        
        if float(self.num_str) == 0:
            return "Rs. Zero"
        logging.debug("Passed zero")
    
        return True

class Attrs:
    """Attributes required for the convertion processes """
    def __init__(self, amount):
        self.inputValidation = Input_Validation(amount)
        self.num_str = self.inputValidation.num_str
        
        if self.inputValidation.validate() == True:
            self.split_list = self.num_str.split('.')
            self.num_list = []
            for i in self.split_list[0]:
                self.num_list.append(int(i))
            self.length = len(self.num_list)
            self.amount = int(self.split_list[0])

class Convert_Process(Attrs):    
    """Methods to concatenate the return values 
    of the convertion methods """
    
    def _return_string(self, words, paise):
        #Method used only for the purpose of concatenation
        #inside this class. 
        """Return the arguments encapsulated inside Rs and ONLY"""
        return "Rs. " + words + paise + ' ONLY'

    def get_rupee_in_words(self):
        """Calls the necessary method from equating the length
        of the amount to the key in the dictionary"""
        from .digit_functions import (
            Paise, Single_double, Hundreds, Thousand, Lakh
            )
        self.convert_dict = {
            1: Single_double, 2: Single_double, 
            3: Hundreds, 4: Thousand, 
            5: Thousand, 6: Lakh
            }
        self.paise = Paise(self.num_str)
        self.num_digit = self.convert_dict[self.length](self.amount)
        if self.amount == 0:
            return "Rs." + self.paise.get_paise() + ' ONLY'
        return self._return_string(
            self.num_digit.convert(), self.paise.get_paise()
            )

class Main_Function_Call:
    """Call the convert process after checking if the input is valid"""
    def __init__(self, amount):
        self.amount = amount
        self.input_check = Input_Validation(self.amount)
        
    def convert(self):
        """Check the validity of the input, instantiate the convert class
        and return the concatenated value"""
        if self.input_check.validate() != True:
            return self.input_check.validate()
        self.convertProcess = Convert_Process(self.amount)
        return self.convertProcess.get_rupee_in_words()
