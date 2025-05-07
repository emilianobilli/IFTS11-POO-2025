

class Cuenta(object):
    def __init__(self,nro_cuenta, nombre, saldo, estado_cuenta,edad):
        self.nro_cuenta = nro_cuenta
        self.nombre = nombre
        self.saldo = saldo
        self.estado_cuenta = estado_cuenta
        self.edad = edad 
        pass
    def ingresarMonto(self,montoIngreso):
        self.saldo = self.saldo + montoIngreso
        return None
    def retirarmonto(self,montoRetirar):
        if self.saldo >= montoRetirar:
            self.saldo = self.saldo - montoRetirar
        else:
            return(print("monton ingresado mayor a saldo"))
        return None
    def mostrarDatos(self):
        return(print(self.nombre, "nro de cuenta", self.nro_cuenta, "estado:", self.estado_cuenta,"monto", self.saldo))
class CuentaEstudiante(Cuenta):
    def ingresarMonto(self, montoIngreso):
        return super().ingresarMonto(montoIngreso)
    def retirarmonto(self, montoRetirar):
        return super().retirarmonto(montoRetirar)
    def mostrarDatos(self):
        return super().mostrarDatos()
class CuentaMenor(Cuenta):
    def ingresarMonto(self, montoIngreso):
        return super().ingresarMonto(montoIngreso)
    def retirarmonto(self, montoRetirar):
        return super().retirarmonto(montoRetirar)
    def mostrarDatos(self):
        return super().mostrarDatos()
class CuentaMayor(Cuenta):
    def ingresarMonto(self, montoIngreso):
        return super().ingresarMonto(montoIngreso)
    def retirarmonto(self, montoRetirar):
        return super().retirarmonto(montoRetirar)
    def mostrarDatos(self):
        return super().mostrarDatos()
    def mayoriaDeEdad(self):
        if self.edad > 17:
            return(print("La persona",self.nombre,"es mayor de edad"))
        else:
            return(print("La persona",self.nombre,"es menor de edad"))

if __name__ == "__main__":
    a = CuentaMayor(490000,"carlos",1200,"activo",19)
    a.ingresarMonto(500)
    a.mostrarDatos()
    a.retirarmonto(300)
    a.mostrarDatos()
    a.mayoriaDeEdad()    
    b = CuentaMenor(490000,"carlos",200,"activo",19)
    b.ingresarMonto(300)
    b.mostrarDatos()
    b.retirarmonto(600)
    b.mostrarDatos()
    c= CuentaEstudiante(490006,"carlos",200,"activo",19)
    c.ingresarMonto(300)
    c.mostrarDatos()
    c.retirarmonto(100)
    c.mostrarDatos()
