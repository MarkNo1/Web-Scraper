from subito import *

# For example
# Copy the firt link of the result of your search
main_url = 'https://www.subito.it/annunci-lazio/affitto/camere-posti-letto/roma/roma/?pe=500'

subito = Subito(main_url, 2)

subito.gathering_data()

print(subito.records)
