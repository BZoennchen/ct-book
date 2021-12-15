class Memory():
    def __init__(self, size=1024):
        self.ERROR_CODE = -1
        self.SUCCESS_CODE = -2
        self.name_to_dt = {'number': 0, 'char': 1, 'list': 2, 'addr': 3}

        self.size = size
        self.memory = [0 for _ in range(self.size)]
        self.inuse = [False for _ in range(self.size)]

    def to_data_type(self, name):
        if name in self.name_to_dt:
            return self.name_to_dt[name]
        else:
            return self.ERROR_CODE

    def calc_bytes(self, data_type):
        if data_type == self.to_data_type('number'):
            return 3
        if data_type == self.to_data_type('char'):
            return 2
        if data_type == self.to_data_type('addr'):
            return 3
        return self.ERROR_CODE

    def number_to_byte(self, number):
        return (number // 256, number % 256)

    def to_number(self, byte1, byte2):
        return byte1 * 256 + byte2

    def char_to_byte(self, char):
        return ord(char)

    def to_char(self, byte):
        return chr(byte)

    def is_valid(self, addr):
        return addr >= 0 and addr < len(self.memory)

    def is_inuse(self, addr):
        return self.inuse[addr]

    def is_free(self, addr):
        return self.is_valid(addr) and not self.is_inuse(addr)

    def unfree(self, addr, n_bytes):
        for i in range(n_bytes):
            if self.is_valid(addr+i):
                self.inuse[addr+i] = True
            else:
                return self.ERROR_CODE
        return self.SUCCESS_CODE

    def malloc(self, n_bytes):
        addr = 0
        count = 0
        for b in self.inuse:
            if not b:
                count += 1
            else:
                addr += count + 1
                count = 0
            if count == n_bytes:
                if self.unfree(addr, n_bytes):
                    return addr
                else:
                    return self.ERROR_CODE
        return self.ERROR_CODE

    def mfree(self, addr, n_bytes):
        for i in range(n_bytes):
            if self.is_valid(addr+i):
                self.inuse[addr+i] = False
            else:
                return self.ERROR_CODE
        return self.SUCCESS_CODE

    def calc_list_bytes(self, addr):
        m = self.to_number(self.memory[addr+1], self.memory[addr+2])
        n_bytes_element = self.calc_bytes(self.memory[addr+3]) - 1
        return 4 + m * n_bytes_element

    def alloc(self, data_type, value):
        n_bytes = self.calc_bytes(data_type)
        if n_bytes == self.ERROR_CODE:
            return self.ERROR_CODE
        addr = self.malloc(n_bytes)
        if addr != self.ERROR_CODE:
            self.memory[addr] = data_type
            if data_type == self.to_data_type('number') or data_type == self.to_data_type('addr'):
                byte_value = self.number_to_byte(value)
                self.memory[addr+1] = byte_value[0]
                self.memory[addr+2] = byte_value[1]
            if data_type == self.to_data_type('char'):
                self.memory[addr+1] = self.char_to_byte(value)
        return addr

    def alloc_list(self, data_type, n):
        n_bytes = 4 + (self.calc_bytes(data_type)-1) * n
        if data_type == self.to_data_type('list'):
            return self.ERROR_CODE

        # 1. alloc memory
        addr = self.malloc(n_bytes)

        # 2. initalize meta data (data type of the list and its elements and length of the list)
        self.memory[addr] = self.to_data_type('list')
        n_bytes = self.number_to_byte(n)
        self.memory[addr+1] = n_bytes[0]
        self.memory[addr+2] = n_bytes[1]
        self.memory[addr+3] = data_type
        return addr

    def free(self, addr):
        if self.is_valid(addr):
            data_type = self.memory[addr]
            if data_type == self.to_data_type('list'):
                n_bytes = self.calc_list_bytes(addr)
            else:
                n_bytes = self.calc_bytes(data_type)
            return self.mfree(addr, n_bytes)
        return self.ERROR_CODE

    def read_number(self, addr):
        return self.to_number(self.memory[addr+1], self.memory[addr+2])

    def add(self, addr1, addr2):
        number1 = self.read_number(addr1)
        number2 = self.read_number(addr2)
        value = (number1 + number2) % (256**2)
        addr = self.alloc(self.to_data_type('number'), value)
        return addr

    def list_len(self, addr):
        return self.to_number(self.memory[addr+1], self.memory[addr+2])

    def set_list_value(self, addr, index, value):
        data_type = self.memory[addr+3]
        m = self.calc_bytes(data_type)-1
        mem_addr = addr + 4 + (m * index)
        if data_type == self.to_data_type('number') or data_type == self.to_data_type('addr'):
            byte_value = self.number_to_byte(value)
            self.memory[mem_addr] = byte_value[0]
            self.memory[mem_addr+1] = byte_value[1]
            return self.SUCCESS_CODE
        elif data_type == self.to_data_type('char'):
            self.memory[mem_addr] = self.char_to_byte(value)
            return self.SUCCESS_CODE
        else:
            return self.ERROR_CODE

    def get_list_value(self, addr, index):
        data_type = self.memory[addr+3]
        m = self.calc_bytes(data_type)-1
        #print(f"bytes: {m}")
        #print(f"addr: {addr}")
        mem_addr = addr + 4 + (m * index)
        if data_type == self.to_data_type('number') or data_type == self.to_data_type('addr'):
            return self.to_number(self.memory[mem_addr], self.memory[mem_addr+1])
        elif data_type == self.to_data_type('char'):
            return self.to_char(self.memory[mem_addr])
        else:
            return self.ERROR_CODE

    def char_to_str(self, addr):
        return self.to_char(self.memory[addr+1])

    def number_to_str(self, addr):
        return str(self.to_number(self.memory[addr+1], self.memory[addr+2]))

    def list_to_str(self, mylist):
        output = "["
        length = self.list_len(mylist)
        element_data_type = self.memory[mylist+3]

        for i in range(length):
            value = self.get_list_value(mylist, i)
            if element_data_type == self.to_data_type('addr'):
                output += self.mem_to_string(value)
            elif element_data_type == self.to_data_type('char'):
                output += value
            elif element_data_type == self.to_data_type('number'):
                output += str(value)
            if i < length-1:
                output += ", "
        output += "]"
        return output

    def mem_to_string(self, addr):
        output = ""
        if self.is_valid(addr) and self.inuse[addr]:
            data_type = self.memory[addr]
            if data_type == self.to_data_type('char'):
                output += self.char_to_str(addr)
            elif data_type == self.to_data_type('number'):
                output += self.number_to_str(addr)
            elif data_type == self.to_data_type('list'):
                output += self.list_to_str(addr)
            elif data_type == self.to_data_type('addr'):
                new_addr = self.read_number(addr)
                output += self.mem_to_string(new_addr)
        return output

    def new_primitive_list(self, values, data_type):
        length = len(values)
        mylist = self.alloc_list(data_type, length)

        # fill list
        for i in range(length):
            self.set_list_value(mylist, i, values[i])
        return mylist

    def get_data_type(self, value):
        if type(value) == int:
            return self.to_data_type('number')
        if type(value) == str:
            if len(value) == 1:
                return self.to_data_type('char')
            else:
                return self.to_data_type('list')

    def new_list(self, values):
        length = len(values)
        mylist = self.alloc_list(self.to_data_type('addr'), length)

        for i in range(length):
            element_data_type = self.get_data_type(values[i])
            if element_data_type in [self.to_data_type('number'), self.to_data_type('char')]:
                addr = self.alloc(element_data_type, values[i])
            else:
                addr = self.new_list(values[i])
            self.set_list_value(mylist, i, addr)
        return mylist
