from parser import Parser
from uk_parser import UKParser


string1 = "Contact us via 111-222-4444 or kaynlourence1210@gmail.com"
string2 = "Contact us via +1-111-222-4444 or kaynlourence1210@gmail.com"
parser1 = Parser(string1)
print(parser1.parser())

parser2 = UKParser(string2)
print(parser2.parser())
