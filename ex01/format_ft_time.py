from time import time
import datetime
today = time()
dayformat = datetime.date.today().strftime("%b %d %Y")
print("Seconds since January 1, 1970:", "{:,}".format(today), "or ", "{:e}".format(today), " in scientific notation\n",dayformat, sep='')