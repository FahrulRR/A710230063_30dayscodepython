import sys
from PyQt5 import QtWidgets
from kasir import Ui_MainWindow  # Mengimpor kelas dari file kasir.py

class KasirApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(KasirApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Menghubungkan sinyal klik ke slot tambahBarang
        self.ui.pushButtonTambahBarang.clicked.connect(self.tambahBarang)
        self.total_harga = 0.0
        self.ui.tableWidgetBarang.setRowCount(0)
        self.ui.tableWidgetBarang.setColumnCount(3)
        self.ui.tableWidgetBarang.setHorizontalHeaderLabels(['Nama Barang', 'Harga Barang', 'Jumlah Barang'])

    def tambahBarang(self):
        # Mengambil data dari input
        nama_barang = self.ui.lineEditNamaBarang.text()
        harga_barang = float(self.ui.lineEditHargaBarang.text())
        jumlah_barang = int(self.ui.lineEditJumlahBarang.text())
        total_harga_barang = harga_barang * jumlah_barang

        # Menambahkan baris baru ke tabel
        rowPosition = self.ui.tableWidgetBarang.rowCount()
        self.ui.tableWidgetBarang.insertRow(rowPosition)
        self.ui.tableWidgetBarang.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(nama_barang))
        self.ui.tableWidgetBarang.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(f'{harga_barang:.2f}'))
        self.ui.tableWidgetBarang.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(str(jumlah_barang)))

        # Mengupdate total harga
        self.total_harga += total_harga_barang
        self.ui.labelTotalHarga.setText(f'Total Harga: {self.total_harga:.2f}')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = KasirApp()
    window.show()
    sys.exit(app.exec_())
