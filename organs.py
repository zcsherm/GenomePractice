import numpy as np
import random
import utilities



READ_LENGTH = 8
def organ_constructor(genome, start_pos):
    """
    Looks at the genome on receiving an instruction to build an organ and handles the construction of an appropriate organ
    :return: None
    """
    type, start_pos = read_genome(genome, start_pos, 1)
    subtype, start_pos = read_genome(genome, start_pos, 1)
    if False in (type, subtype):
        return False
    return TYPES[type+subtype](genome, start_pos)

def read_genome(self, genome, start_pos, length=READ_LENGTH):
    try:
        read_bits = genome[start_pos:start_pos+length]
    except:
        return False, False
    return read_bits, start_pos+length

class Organ:

    def __init__(self, genome, start_pos):
        self._id = utilities.generate_id()
        def read(length=READ_LENGTH):
            print(genome, start_pos, length)
            return read_genome(genome, start_pos, length)
        self.r = read
        self.get_parameters(genome, start_pos)

    def read(self,length):
        pass


    def get_parameters(self, genome, start_pos):
        pass

class InternalOrgan(Organ):
    pass

class ExternalOrgan(Organ):
    pass

class InternalChemicalOrgan(InternalOrgan):
    pass

class InternalRegulatorOrgan(InternalOrgan):
    pass

class ExternalExecutionOrgan(ExternalOrgan):
    pass

class ExternalSensoryOrgan(ExternalOrgan):
    def get_parameters(self, genome, start_pos):
        initial_read_values = [
            ("_sense_target", 2),
            ("_output_loc", 2),
            ("_strength", 6),
            ("_size", 8),
            ('_direction', 3),
            ("_tiles", 5),
            ("_efficiency", 6),
            ("_quantity", 6)
        ]
        for val in initial_read_values:
            if start_pos is not False:
                print(val)
                value, start_pos = self.r(val[1])
                setattr(self, val[0], value)

        self._activation_cmds = set()

        if self._sense_target ==  'chemicals':
            r=random.randint(0,8)
            self._chemical_targ = r

        for quantity in range(self._quantity):
            rand = random.randint(0,64)
            self._activation_cmds.add(bin(rand))

        while start_pos is not False:
            pass
TYPES= {
    0b00:InternalChemicalOrgan,
    0b01:InternalRegulatorOrgan,
    0b10:ExternalExecutionOrgan,
    0b11:ExternalSensoryOrgan
}

SENSE_TYPES= {
    0b0: 'energy',
    0b1: 'chemicals',
    0b10: 'environment',
    0b11: 'location'
}

OUTPUT_LOCATIONS = {
    0b00: 'blood',
    0b01: 'environment',
    0b10: 'register',
    0b11: 'genome'
}
genes = 103932984209842346264574564524
s = ExternalSensoryOrgan(genes, 0)