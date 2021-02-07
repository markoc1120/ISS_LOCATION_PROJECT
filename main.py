from earth import Earth
from iss import Iss
from data import Data

data = Data()
earth = Earth()
iss = Iss(earth, data)

earth.maintain_window()
