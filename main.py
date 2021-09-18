import embedded as emb

class Products(object):

    def __init__(self, name, price, size):
        self.size = size # size of product in standart VM values
        self.price = price
        self.name = name

class Slots(object):
    _registry = []

    def __init__(self, num, x, y, product, count, status):
        self._registry.append(self)
        self.num = num # number of the slot in VM
        self.x = x # number in row of VM left to right
        self.y = y # row in VM up to down
        self.product = product # name of product placed in slot
        self.count = count # count of goods in slot
        self.status = status # status that slot is working True/False

    def use_slot(self):
        if self.count > 0:
            size = product_objects[self.product].size
            _result = emb.use(self.x, self.y, size)
            if _result == size:
                self.count -= 1
                return 'OK'
            elif _result == 0:
                self.count = 0
                return 'ERROR no product in slot'
        self.status = False
        return 'ERROR slot is broken'

product_objects = {}
slots_objects = {}

for row in emb.read_tsv('products.tsv'):
    name, price, size = row['name'], int(row['price']), int(row['size'])
    product_objects[name] = Products(name, price, size)

for row in emb.read_tsv('slots.tsv'):
    num, x, y, count, product, status = int(row['num']), int(row['x']), int(row['y']), int(row['count']), row['product'], bool(row['status'])
    slots_objects[num] = Slots(num, x, y, product, count, status)

while True:
    avaiable_nums = []
    print('look at our goods')
    for slot in Slots._registry:
        num = slot.num
        product = slot.product
        price = product_objects[product].price

        if slot.count > 0 and slot.status:
            avaiable_nums.append(num)
            print(num, product, price)
    if len(avaiable_nums) == 0:
        print('Sorry VM is empty, come back tomorrow')
        break

    while True:
        print('choose the product')
        choosen_num = int(input())
        print('\n')

        if avaiable_nums.count(choosen_num) > 0:
            product = slots_objects[choosen_num].product
            price = product_objects[product].price
            break

    print(f'you choose ---{product}--- the price is ---{price}---')

    money = 0
    while True:
        print(f'insert the money, the money avaiable is ---{money}---')
        money += int(input())
        print('\n')
        if money >= price:
            break

    res = slots_objects[choosen_num].use_slot()
    
    if res != 'OK':
        print('Sorry your product is unavaiable')
        print(f'take back your money ---{money}---')
        print('\n')
        continue

    if money > price:
        print(f'take your change ---{money - price}---')
    print(f'take your goods ---{product}---')
    print('\n')
