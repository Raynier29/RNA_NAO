import random

class Perceptron:
    def __init__(self,input_number,step_size=0.1):
        self._ins = input_number # Número de parámetros de entrada

    # Seleccionamos pesos aleatorios
        self._w = [random.random() for _ in range(input_number)]
        self._eta = step_size # La tasa de convergencia

    def predict(self,inputs):
        # Producto punto de entrada y pesos
        weighted_average = sum(w*elm for w,elm in zip(self._w,inputs))
        #print(weighted_average)
        if weighted_average > 0:

            return 1
        return 0

    def train(self,inputs,ex_output):
        output = self.predict(inputs)
        error = ex_output - output
        # El error es la diferencia entre la salida correcta y la esperada
        if error != 0:
            self._w = [w+self._eta*error*x for w,x in
            zip(self._w,inputs)]
        return error
