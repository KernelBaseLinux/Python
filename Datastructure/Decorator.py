def WraperFunc(Function):
    def DataCollector(A , b):
        data = A + b
        return data
    return DataCollector

@WraperFunc
def data(A, b):
    return;

A = 10
b = 6
print("Addition_Value: ",data(A,b))
