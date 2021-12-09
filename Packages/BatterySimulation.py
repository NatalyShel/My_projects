from random import randint

class BatterySimulation:
    def __init__(self, logger):
        self.logger = logger

    def simulate_last_hour(self):
        ''' simulate battery temperature changes for the last 1 hour
            (every minute) and add loggs to logger
    '''
        for minute in range(1, 61):
            temperature = randint(20, 40)
            if temperature < 30:   
                # add logg with DEBUG level 
                self.logger.debug('{0} C'.format(temperature))
            elif temperature >= 30 and temperature <= 35:
                # add logg with WARNING level 
                self.logger.warning('{0} C'.format(temperature))
            elif temperature > 35:
                # add logg with CRITICAL level 
                self.logger.critical('{0} C'.format(temperature))
            else:
                raise Exception('Temperature out of range.')