"""
Gives rules for genes that govern biochemistry properties. These produce constructs which are grouped together into an 'organ', each gene governs a potential reaction, monitors for a specific chemical, or affects the global attributes of the organ.
"""

"""
Notes:
Possible activation functions: x, x^2, sqrt(x^a) [0<a<1], 1/(1+e^(-ax+.5a) , [sigmoid centered on .5], sqrt(A^(-Bx)) [1.2<A<5] [A<B<5B], -(1/(1+e^(-ax+.5a))+1 [inverse sigmoid], 1-x, 1-x^2

Possible types:
Receptors: Adjusts parameters of Organ based on concentration of chemical, each has an activation function that determines output
Emittors: Releases a given chemical based on a current parameter of the organ (rate, health, size)
Reactions: Converts chemicals into other chemicals, supports equations of multiple chemicals with varying coefficients
Processing: How quickly each chemical is broken down by or accumulated in the organ
Absorption rates:
Initialcondition: HOw much of a chemical is present at birth, and the cost of reproduction
"""
class BioChemGene:
    def __init__(self, organ):
        self._organ = organ

    def set_activation(self, function):
        self._activation_function = function
        
class Receptor(BioChemGene):
    """
    I'm thinking that this gets passed in class methods for the organ, and adjusts the params by calling those functions
    """
    def set_parameter(self, parameter):
        self._parameter = parameter

    def set_chemical(self, chemical):
        self._chemical = chemical

    
