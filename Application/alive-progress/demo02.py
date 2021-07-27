import time
from alive_progress import alive_bar, config_handler, bouncing_spinner_factory

train_spinner = bouncing_spinner_factory('2021 NLPCC please', 15, hiding=True)

config_handler.set_global(spinner=train_spinner, bar='classic')

total = 300
with alive_bar(total) as bar:  # declare your expected total
    for _ in range(total):         # iterate as usual over your items
        time.sleep(2)
        bar()                  # call after consuming one item    

