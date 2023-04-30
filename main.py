from Company import Company
from Item import Item
from Customer import Customer
from RegCustomer import RegCustomer
from Order import Order
from OrderedItem import OrderedItem

def main():
    company = Company("First Company")

    # company product items
    item1 = Item("item1", 10)
    item2 = Item("item2", 12)
    item3 = Item("item3", 8)
    item4 = Item("item4", 10)
    item5 = Item("item5", 90)

    company.addItem(item1)
    company.addItem(item2)
    company.addItem(item3)
    company.addItem(item4)
    company.addItem(item5)

    #created customers
    cust1 =  Customer("General Customer")
    rcust1 =  RegCustomer("RegCustomer", 10)

    #orders for customer 1
    order1 = Order()
    order1.addOrderedItem( OrderedItem(item5, 1))
    order1.addOrderedItem( OrderedItem(item2, 4))

    order2 =  Order()
    order2.addOrderedItem( OrderedItem(item3, 4))
    order2.addOrderedItem( OrderedItem(item4, 3))

    #Adding orders to customer
    cust1.addOrder(order1)
    cust1.addOrder(order2)

    #orders for customer 2
    order21 =  Order()
    order21.addOrderedItem( OrderedItem(item5, 1))
    order21.addOrderedItem( OrderedItem(item2, 4))

    order22 =  Order()
    order22.addOrderedItem( OrderedItem(item3, 4))
    order22.addOrderedItem( OrderedItem(item4, 3))
    #Adding order to reg customer
    rcust1.addOrder(order21)
    rcust1.addOrder(order22)

    #add customers to company
    company.addCustomer(cust1)
    company.addCustomer(rcust1)

    print(f'Customer details : {company.getCustomers()}')

    print(f'Total worth of all orders: {company.getTotalWorthOfOrdersPlaced()}')



main()
