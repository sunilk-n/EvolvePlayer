class CommandParams:
    def __init__(self, func, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.func = func

    def __call__(self, *args, **kwargs):
        if len(self.args) == 1:
            self.func(self.args[0])
        elif len(self.args) == 2:
            self.func(self.args[0], self.args[1])
        elif len(self.args) == 3:
            self.func(self.args[0], self.args[1], self.args[2])