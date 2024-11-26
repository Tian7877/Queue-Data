class Queue:
    def __init__(self):
        self.items =[]

    def enqueue(self,data):
        self.items.append(data)

    def dequeue(self,data):
        n = data - 1 
        if self.is_empty():
            return "Antrian Kosong"
        return self.items.pop(n)
    
    def peek(self):
        if self.is_empty():
            return "Antrian Kosong"
        return self.items[0]
    
    def is_empty(self):
        return len(self.items)==0

    def size(self):
        return len(self.items)
    
    def all(self):
        return self.items


def display_menu():
    print("\nMain Menu:")
    print("==========================================================================")
    print("1. Tambahkan Antrian")
    print("2. Hapus Dari Antrian")
    print("3. Lihat Antrian Terdepan")
    print("4. Check Antrian Kosong ")
    print("5. Lihat Size Antrian")
    print("6. Exit")
    print("==========================================================================")



def main():
    queue = Queue()
    
    while True:
        display_menu()
        try:
            choice = int(input("Pilih Menu : "))
        except ValueError:
            print("Invalid Input, Pilihan Opsi 1-6 ")
            continue
        
        if choice == 1:
            data = input("Masukkan Data: ")
            if data in queue.all():
                print("Data Sudah Ada")
            else:
                queue.enqueue(data)
                print(f"'{data}' Data Tersimpan")
        elif choice == 2:
            if not queue.is_empty():
                print(f"Pilih Indeks Antrian Yang akan di hapus Dari ==> {queue.all()}")
                data = int(input("Indeks Ke- "))
                if data >= queue.size():
                    print("Nilai Indeks Diluar Data")
                    break
                result = queue.dequeue(data)
                print(result)
            else :
                data = 0
                result = queue.dequeue(0)
                print(result)
        elif choice == 3:
            result = queue.peek()
            if not queue.is_empty() :
                print(f"Tampilan Antrian Pertama: {result}")
                print(f"Di Dalam list Antrian ===> {queue.all()}")
            else :
                print(f"Antrian Kosong")
        elif choice == 4:
            if queue.is_empty():
                print("Antrian Kosong")
            else:
                print("Antrian Tidak Kosong")
        elif choice == 5:
            print(f"Jumlah Antrian : {queue.size()}")
        elif choice == 6:
            print("Goodbye !")
            break
        else:
            print("Invalid Opsi, Silahkan Piih Opsi Valid")

if __name__ == "__main__":
    main()
