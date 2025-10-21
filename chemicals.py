class Chemical:
    """
    Generic class for a particular chemical. Arbitrary. Essentially will be a container in each individual and environment object
    """
    def __init__(self, id):
        self._id = id
        self._quantity = 0

    def drain(self, quant):
        self._quantity -= quant

    def increase(self,quant):
        self._quantity += quant

    def get_id(self):
        return self._id

    def get_quantity(self):
        return self._quantity
