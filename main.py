from data_puller import DataPuller
from form_bot import DataEntry

data_extractor = DataPuller()
rents = data_extractor.get_rent_list()
form_bot = DataEntry()
for rent in rents:
    form_bot.fill_form(rent)


