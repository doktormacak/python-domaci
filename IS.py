''''

Program pravi IS marketa za automobile. Sadrzi automobile i neke bitne karakteristike za lako pretrazivanje automobila.
Takodje nam daje informacije o auto placevima i auto otpadima gdje moze lako naci zeljeni automobil i djelove za iste.
Informacije iz IS-a su stavljene u "Automobili.txt".


''''






ListaAutomobili = []


class Automobili:

    def __init__(self, id, brend, model, godiste, kilometraza, kubikaza, cijena, lokacija_automobila):
        self.id = id
        self.brend = brend
        self.model = model
        self.godiste = godiste
        self.kilometraza = kilometraza
        self.kubikaza = kubikaza
        self.cijena = cijena
        self.lokacija_automobila = lokacija_automobila

        src1 = {
            'ID': self.id,
            'Brend': self.brend,
            'Model': self.model,
            'Godiste': self.godiste,
            'Kilometraza': self.kilometraza,
            'Kubikaza': self.kubikaza,
            'Cijena': self.cijena,
            'Lokacija_automobila': self.lokacija_automobila
        }

        ListaAutomobili.append(src1)


    def __repr__(self):
        return f'Naziv automobila: {self.brend}, {self.model}. Cijena automobila: {self.cijena}, na lokaciji: {self.lokacija_automobila}'



ListaAutoPlaceva = []


class Auto_placevi:


    def __init__(self, id, ime, lokacija_placa, telefon, automobili_na_placu):
        self.id = id
        self.ime = ime
        self.lokacija_placa = lokacija_placa
        self.telefon = telefon
        self.automobili_na_placu = automobili_na_placu

        src2 = {
            'ID' : self.id,
            'Ime' : self.ime,
            'Lokacija_placa' : self.lokacija_placa,
            'Telefon' : self.telefon,
            'Automobili_na_placu' : self.automobili_na_placu

        }

        ListaAutoPlaceva.append(src2)

    def __repr__(self):
        return f'Naziv auto placa: {self.ime}. Lokacija placa: {self.lokacija_placa}, broj telefona: {self.telefon}'


ListaAutoDjelova = []


class Auto_djelovi:


    def __init__(self, id, ime, lokacija, telefon, djelovi_na_otpadu):
        self.id = id
        self.ime = ime
        self.lokacija = lokacija
        self.telefon = telefon
        self.djelovi_na_otpadu = djelovi_na_otpadu


        src3 = {
            'ID' : self.id,
            'Ime' : self.ime,
            'Lokacija' : self.lokacija,
            'Telefom' : self.telefon,
            'Djelovi_na_otpadu' : self.djelovi_na_otpadu
        }

        ListaAutoDjelova.append(src3)

    def __repr__(self):
        return f'Naziv Auto djelova: {self.ime}. Lokacija: {self.lokacija} i broj telefona: {self.telefon}'


automobil1 = Automobili(1,'Aston Martin', 'Vanquish', 2003, 13000, 5935, 79000, 'Budva')
automobil2 = Automobili(2, 'BMW', '330ci', 2003, 120000, 3000, 9800, 'Podgorica')
automobil3 = Automobili(3, 'De Tomaso', 'Pantera', 1978, 47000, 58000, 108000, 'Cetinje')


plac1 = Auto_placevi(1, 'Auto Ventura' , 'Cetinje' , '+3826855441', 'polovni i novi automobili' )
plac2 = Auto_placevi(2, 'Cars PG', 'Podgorica', '+38267535665' , 'polovni automobili')


otpad1 = Auto_djelovi(1, 'Auto djelovi PG', 'Podgorica', '+3827744220', 'polovni djelovi')



f = open("Automobili.txt", 'a')
f.write(str(ListaAutomobili))
f.write("\n")
f.write(str(ListaAutoPlaceva))
f.write("\n")
f.write(str(ListaAutoDjelova))
f.close
