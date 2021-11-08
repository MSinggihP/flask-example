class Karyawan:
    nama_kantor = 'Digital Skola Data Engineer'

    def __init__(self, nama, umur, nomor_hp):
        self.nama = nama
        self._umur = umur
        self.__nomor_hp = nomor_hp
    
    def nomor_hp(self):
        return self.__nomor_hp

    @property
    def nomor_hp(self):
        return self.__nomor_hp

    @nomor_hp.setter
    def nomor_hp(self, nomor_hp):
        self.__nomor_hp = nomor_hp