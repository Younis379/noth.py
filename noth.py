#modules are used to better organize our code,we break up our code into multiple files each file is called module should contain all functions classes which are related ,then we can import a module into another module .
#or you can write import converter,but then you have to specify your function

import converter
from converter import lbs_to_kg
print(lbs_to_kg(70))

