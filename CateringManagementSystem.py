# coding=utf-8


class Orders:
    def __init__(self):
        pass

    @staticmethod
    def set_global():
        global priceofserves1, priceofserves2, priceofserves3, priceofserves4, \
            priceofserves5, typeofservice1, typeofservice2, typeofservice3, typeofservice4, typeofservice5, \
            type_of_service, price_of_serves, amount_of_client
        priceofserves1 = 0.0
        priceofserves2 = 0.0
        priceofserves3 = 0.0
        priceofserves4 = 0.0
        priceofserves5 = 0.0
        typeofservice1 = ' '
        typeofservice2 = ' '
        typeofservice3 = ' '
        typeofservice4 = ' '
        typeofservice5 = ' '
        type_of_service = ' '
        price_of_serves = 0.0
        amount_of_client = 0
        return priceofserves1, priceofserves2, priceofserves3, priceofserves4, priceofserves5, \
               typeofservice1, typeofservice2, typeofservice3, typeofservice4, typeofservice5

    @staticmethod
    def order_other_servces(typeofmenu, type_of_service, price_of_serves, discount, amount_of_client,
                            priceofmenue,
                            typeofservice1, typeofservice2, typeofservice3, typeofservice4, typeofservice5,
                            priceofserves1, priceofserves2, priceofserves3, priceofserves4, priceofserves5,
                            discountcount):
        print('\n'.join([
            "|----Type of services----|",
            "|1]Tent: RM400 per one unit (10ft)",
            "[2]Chairs: RM100 for 50 chairs",
            "[3]Tables: RM80 for 10 tables",
            "[4]Table cloths: RM20 for 10 table cloths",
            "[5]Private room: RM2000 from 50 people to 150",
            "===>Select service (Or press 'Enter' to checkout)",
        ]))
        service = raw_input()
        orders = Orders()
        if service == '1':
            try:
                units_in = float(raw_input("===>How many units you need?\n"))
                typeofservice1 = 'Tent'
                priceofserves1 = 400.0 * units_in
                print("--->It will cost: Rm{}  Type of service {}--|".format(priceofserves1, typeofservice1))
            except ValueError:
                print "\nError!\n"
                absentinput = raw_input()
                orders.order_other_servces(typeofmenu, type_of_service, price_of_serves, discount, amount_of_client,
                                           priceofmenue,
                                           typeofservice1, typeofservice2, typeofservice3, typeofservice4,
                                           typeofservice5,
                                           priceofserves1, priceofserves2, priceofserves3, priceofserves4,
                                           priceofserves5, discountcount)
        if service == '2':
            try:
                units_in = float(raw_input("===>How many set of chairs you need?\n"))
                typeofservice2 = 'Chairs'
                priceofserves2 = 100.0
                priceofserves2 *= units_in
                print("--->It will cost: Rm{}  Type of service {}--|".format(priceofserves2, typeofservice2))
            except ValueError:
                print "\nError!\n"
                absentinput = raw_input()
                orders.order_other_servces(typeofmenu, type_of_service, price_of_serves, discount, amount_of_client,
                                           priceofmenue,
                                           typeofservice1, typeofservice2, typeofservice3, typeofservice4,
                                           typeofservice5,
                                           priceofserves1, priceofserves2, priceofserves3, priceofserves4,
                                           priceofserves5, discountcount)
        if service == '3':
            try:
                units_in = float(raw_input("===>How many set of tables you need?\n"))
                typeofservice3 = 'Tables'
                priceofserves3 = 80.0 * units_in
                print("--->It will cost: Rm{}  Type of service {}--|".format(priceofserves3, typeofservice3))
            except ValueError:
                print "\nError!\n"
                absentinput = raw_input()
                orders.order_other_servces(typeofmenu, type_of_service, price_of_serves, discount, amount_of_client,
                                           priceofmenue,
                                           typeofservice1, typeofservice2, typeofservice3, typeofservice4,
                                           typeofservice5,
                                           priceofserves1, priceofserves2, priceofserves3, priceofserves4,
                                           priceofserves5, discountcount)
        if service == '4':
            try:
                units_in = float(raw_input("===>How many set of chairs you need?\n"))
                typeofservice4 = 'Table cloths'
                priceofserves4 = 20.0 * units_in
                print("--->It will cost: Rm{}  Type of service {}--|".format(priceofserves4, typeofservice4))
            except ValueError:
                print "\nError!\n"
                absentinput = raw_input()
                orders.order_other_servces(typeofmenu, type_of_service, price_of_serves, discount, amount_of_client,
                                           priceofmenue,
                                           typeofservice1, typeofservice2, typeofservice3, typeofservice4,
                                           typeofservice5,
                                           priceofserves1, priceofserves2, priceofserves3, priceofserves4,
                                           priceofserves5, discountcount)
        if service == '5':
            try:
                print ("===>How many person come?(For each additional person RM30)")
                typeofservice5 = 'Private room'
                units_in = int(raw_input())
                if units_in < 50:
                    print(
                        "----'ERROR'----\n" + "We provide this service from 50 person to 150\n" + "press 'Enter'to continue...")
                    absent_input = raw_input()
                    orders.order_other_servces(typeofmenu, type_of_service, price_of_serves, discount, amount_of_client,
                                               priceofmenue,
                                               typeofservice1, typeofservice2, typeofservice3, typeofservice4,
                                               typeofservice5,
                                               priceofserves1, priceofserves2, priceofserves3, priceofserves4,
                                               priceofserves5, discountcount)
                if 50 <= units_in <= 150:
                    units_in = 150
                    priceofserves5 = 2000
                    amount_of_client += units_in
                    print("--->It will cost: Rm{}  Type of service {}--|".format(priceofserves5, typeofservice5))
                    orders.count_all(typeofmenu, priceofmenue, discount, amount_of_client,
                                 priceofserves1, priceofserves2, priceofserves3, priceofserves4, priceofserves5,
                                 typeofservice1, typeofservice2, typeofservice3, typeofservice4, typeofservice5,
                                 discountcount)
                # count extra customers
                if units_in >= 151:
                    units_in -= 150
                    priceofserves5 = (30 * units_in) + 2000.0
                    amount_of_client += units_in + 150
                    print("--->It will cost: Rm{}  Type of service {}--|".format(priceofserves5, typeofservice5))
                    orders.count_all(typeofmenu, priceofmenue, discount, amount_of_client,
                                     priceofserves1, priceofserves2, priceofserves3, priceofserves4, priceofserves5,
                                     typeofservice1, typeofservice2, typeofservice3, typeofservice4, typeofservice5,
                                     discountcount)
                if service != '1' or service != '2' or service != '3' or service != '4' or service != '5' or service != '6':
                    orders.order_other_servces(typeofmenu, type_of_service, price_of_serves, discount, amount_of_client,
                                               priceofmenue,
                                               typeofservice1, typeofservice2, typeofservice3, typeofservice4,
                                               typeofservice5,
                                               priceofserves1, priceofserves2, priceofserves3, priceofserves4,
                                               priceofserves5, discountcount)
            except:
                print("----'ERROR'----\n" + "press 'Enter'to continue...")
                absent_input = raw_input()
                orders.order_other_servces(typeofmenu, type_of_service, price_of_serves, discount, amount_of_client,
                                           priceofmenue, typeofservice1, typeofservice2, typeofservice3, typeofservice4, \
                                           typeofservice5, priceofserves1, priceofserves2, priceofserves3, priceofserves4, \
                                           priceofserves5, discountcount)

        orders.count_all(typeofmenu, priceofmenue, discount, amount_of_client,
                         priceofserves1, priceofserves2, priceofserves3, priceofserves4, priceofserves5,
                         typeofservice1, typeofservice2, typeofservice3, typeofservice4, typeofservice5, discountcount)

    '''
        Count Discount
    '''

    # A static method does not receive an implicit first argument.
    @staticmethod
    def cout_discount(typeofmenu, priceofmenue, amount_of_client):
        global orders, discount, discountcount, priceofserves1, priceofserves2, \
            priceofserves3, priceofserves4, priceofserves5, typeofservice1, typeofservice2, \
            typeofservice3, typeofservice4, typeofservice5
        orders = Orders()
        orders.set_global()
        if 26 <= amount_of_client <= 50:
            priceofmenue *= amount_of_client
            discountcount = priceofmenue * 10 / 100
            priceofmenue -= discountcount
            discount = "10%"

        elif 51 <= amount_of_client <= 100:
            priceofmenue *= amount_of_client
            discountcount = priceofmenue * 15 / 100
            priceofmenue -= discountcount
            discount = "15%"

        elif amount_of_client >= 100:
            priceofmenue *= amount_of_client
            discountcount = priceofmenue * 20 / 100
            priceofmenue -= discountcount
            discount = "20%"

        elif 0 <= amount_of_client <= 10:
            priceofmenue *= amount_of_client
            discountcount = 0.0
            discount = "0%"

        elif 11 <= amount_of_client <= 25:
            priceofmenue *= amount_of_client
            discountcount = priceofmenue * 5 / 100
            priceofmenue -= discountcount
            discount = "5%"
        orders.count_all(typeofmenu, priceofmenue, discount, amount_of_client,
                         priceofserves1, priceofserves2, priceofserves3, priceofserves4, priceofserves5,
                         typeofservice1, typeofservice2, typeofservice3, typeofservice4, typeofservice5, discountcount)

    '''
    Count Price of menu and Service's
    '''

    # A static method does not receive an implicit first argument.
    @staticmethod
    def count_all(typeofmenu, priceofmenue, discount, amount_of_client,
                  priceofserves1, priceofserves2, priceofserves3, priceofserves4, priceofserves5,
                  typeofservice1, typeofservice2, typeofservice3, typeofservice4, typeofservice5, discountcount):
        # count string of services
        type_of_service = typeofservice1 + typeofservice2 + typeofservice3 + typeofservice4 + typeofservice5
        # count total price of srvices
        priceofserves = priceofserves1 + priceofserves2 + priceofserves3 + priceofserves4 + priceofserves5

        if priceofmenue == ' ':
            priceofmenue = 0.0
            total_price = priceofserves + priceofmenue
        else:
            total_price = priceofserves + priceofmenue
        priceofserves = 0.0
        print("|---Your order.---|\n|Type of menu: {}  \n|Amount of customers: {} \n|Type of service: {}"
              " \n|Total price: {} \n|Discount: RM{} ".format(typeofmenu, int(amount_of_client), type_of_service,
                                                              total_price, discount))
        print('\n'.join([
            "|Press [1] To select another services...",
            "|Press [2] Proceed to checkout ...",
            "|Press [3] Proceed to cancel ...",
        ]))
        check_input = raw_input()
        if check_input == '1':
            orders = Orders()
            orders.order_other_servces(typeofmenu, type_of_service, priceofserves, discount, amount_of_client,
                                       priceofmenue,
                                       typeofservice1, typeofservice2, typeofservice3, typeofservice4, typeofservice5,
                                       priceofserves1, priceofserves2, priceofserves3, priceofserves4, priceofserves5,
                                       discountcount)
        elif check_input == '2':
            payment_module = PaymentModule()
            payment_module.show_menu(total_price, typeofmenu, type_of_service, amount_of_client, discount,
                                     discountcount)
        elif check_input == '3':
            cms.main_menu()
        else:
            orders = Orders()
            orders.count_all(typeofmenu, priceofmenue, discount, amount_of_client,
                             priceofserves1, priceofserves2, priceofserves3, priceofserves4, priceofserves5,
                             typeofservice1, typeofservice2, typeofservice3, typeofservice4, typeofservice5,
                             discountcount)


class OrderMenu:
    def __init__(self):
        pass

    # A static method does not receive an implicit first argument.
    @staticmethod
    def show_menu():
        global typeofmenu, priceofmenue
        typeofmenu = " "
        priceofmenue = 0.0
        ordermenu = OrderMenu()
        print('\n'.join([
            "|----Type of menu----|",
            "|[B] Breakfast (Charge per head: RM20.00)",
            "|---- Include ---->>>\n"
            "|-Nasi lemak",
            "|-Fried noodles,",
            "|-Roti chanain",
            "|-Fried noodles",
            "|-Pasta",
            "|-Hot drink",
            "|[L]Lunch (Charge per head: RM30.00)",
            "|---- Include ---->>>\n"
            "|-Chicken Chop",
            "|-Steamed Fish",
            "|-Salad",
            "|-Fried Rice",
            "|-Soft Drink",
            "|[BQ]BBQ (Charge per head: RM60.00)",
            "|---- Include ---->>>\n"
            "|-Sausages with sauteed onions",
            "|-Beef burgers with sauteed onions",
            "|-Minted Lamb Kebabs",
            "|-Potato salad",
            "|[AT]Afternoon Teas (Charge per head: RM15.50)",
            "|---- Include ---->>>\n"
            "|-Assorted sandwiches",
            "|-Prawn vol au vents",
            "|-Smoked salmon canapes",
            "|-Fresh cream scones with jam",
            "|-Cream and strawberries",
        ]))
        print('Select menu: ')
        module_select = raw_input()
        if module_select == 'B' or module_select == 'b':
            typeofmenu = "Breakfast"
            priceofmenue = 20.00

        elif module_select == 'L' or module_select == 'l':
            typeofmenu = "Lunch"
            priceofmenue = 30.00

        elif module_select == 'BQ' or module_select == 'bq':
            typeofmenu = "BBQ"
            priceofmenue = 60.00

        elif module_select == 'AT' or module_select == 'at':
            typeofmenu = "Afternoon Teas"
            priceofmenue = 15.50
        else:
            ordermenu.show_menu()
        try:
            amount_of_client = float(raw_input('Enter amount of client: '))

            discount1 = Orders()
            discount1.cout_discount(typeofmenu, priceofmenue, amount_of_client)
        except ValueError:
            print "\nThat wasn't a number!\n"
            absentinput = raw_input()
            ordermenu.show_menu()
        return typeofmenu, priceofmenue


class OrderModule:
    def __init__(self):
        pass

    # A static method does not receive an implicit first argument.
    @staticmethod
    def show_menu():
        global typeofmenu, type_of_service, price_of_serves, discount, amount_of_client, priceofmenue, \
            typeofservice1, typeofservice2, typeofservice3, typeofservice4, typeofservice5, \
            priceofserves1, priceofserves2, priceofserves3, priceofserves4, priceofserves5
        typeofmenu = ' '
        priceofserves1 = 0.0
        priceofserves2 = 0.0
        priceofserves3 = 0.0
        priceofserves4 = 0.0
        priceofserves5 = 0.0
        typeofservice1 = ' '
        typeofservice2 = ' '
        typeofservice3 = ' '
        typeofservice4 = ' '
        typeofservice5 = ' '
        type_of_service = ' '
        price_of_serves = 0.0
        amount_of_client = 0
        discount = ' '
        priceofmenue = ' '
        discountcount = 0.0
        '''
        Strings joined by new line are more elegant
        than multiple `print` statements
        '''
        print('\n'.join([
            "|----Order Module----",
            "|[F]Place orders for food",
            "|[S]Place orders for other services",
            "|[M]Return to Main Menu",
        ]))
        module_select = raw_input()
        if module_select == 'f' or module_select == 'F':
            ordermenu = OrderMenu()
            ordermenu.show_menu()
        elif module_select == 's' or module_select == 'S':
            order = Orders()
            order.order_other_servces(typeofmenu, type_of_service, price_of_serves, discount, amount_of_client,
                                      priceofmenue,
                                      typeofservice1, typeofservice2, typeofservice3, typeofservice4, typeofservice5,
                                      priceofserves1, priceofserves2, priceofserves3, priceofserves4, priceofserves5,
                                      discountcount)
        elif module_select == 'm' or module_select == 'M':
            cms.main_menu()
        else:
            print('\n'.join([
                '|----Please, select a correct module----|',
                '|-------Press "Enter" to continue-------|',
            ]))
            module_select = raw_input()
            cms.main_menu()


class ReportModule:
    def __init__(self):
        pass

    # A static method does not receive an implicit first argument.
    @staticmethod
    def show_report():
        report = ReportModule()
        print('\n'.join([
            "|----Report Module----",
            "|[I]Display the invoice for order made",
            "|[S]Display the summary of orders and payments made ",
            "|[M]Return to Main Menu",
        ]))
        module_select = raw_input()
        if module_select == 'm' or module_select == 'M':
            cms.main_menu()
        elif module_select == 's' or module_select == 'S':
            report.display_summary()
        elif module_select == 'i' or module_select == 'I':
            display_invoice()
        else:
            report.show_report()

    # A static method does not receive an implicit first argument.
    @staticmethod
    def display_summary():
        global report_module
        report_module = ReportModule()
        try:
            with open("Bills.txt", 'r') as fin:
                print fin.read()
                absent_input = (raw_input("Press 'Enter' to continue...\n"))
                report_module.show_report()
        except IOError:
            absent_input = (raw_input("|----File was not founded----|\n|----Press 'Enter' to continue...----|\n"))
            report_module.show_report()
            # A static method does not receive an implicit first argument.


def display_invoice():
    Id_input = (raw_input("Enter ID of order\n")).strip()
    try:
        f = open("Bills.txt", "r")
        print_rows = False
        for idline in f:
            if idline.strip() == Id_input:
                print_rows = True
                continue
            if print_rows:
                if idline.startswith("["):
                    print idline
                else:
                    break
        if not print_rows:
            absent_input = (raw_input("|----Order was not founded----|\n|----    Press 'Enter' to continue...----|\n"))
            report_module = ReportModule()
            report_module.show_report()
    except IOError:
        absent_input = (raw_input("|----File was not founded----|\n|----    Press 'Enter' to continue...----|\n"))
        report_module = ReportModule()
        report_module.show_report()
    absent_input = (raw_input("|----Press 'Enter' to continue...----|\n"))
    report_module = ReportModule()
    report_module.show_report()

class CMS:
    def __init__(self):
        pass

    # A static method does not receive an implicit first argument.
    @staticmethod
    def main_menu(total_price=None, type_of_menu=None, amount_of_customers=None, type_of_service=None,
                  discount=None, discountcount=None):
        print('\n'.join([
            "|----Welcome to Catering Management System----|", "|",
            "|[O]Order", "|[R]Report", "|[P]Payment", "|[E]Exit",
            "|", "|----Select module----",
        ]))

        module_select = raw_input()

        # If user selected exit, be sure to close app
        # straight away, without further unnecessary processing
        if module_select == 'e' or module_select == 'O':
            print('Goodbye!')
            import sys
            sys.exit(0)
        elif module_select == 'o' or module_select == 'O':
            ordermodule = OrderModule()
            ordermodule.show_menu()
        elif module_select == 'r' or module_select == 'R':
            reportmodule = ReportModule()
            reportmodule.show_report()
        elif module_select == 'p' or module_select == 'P':
            paymentmodule = PaymentModule()
            paymentmodule.show_menu(total_price, type_of_menu, type_of_service, amount_of_customers, discount,
                                    discountcount)
        else:
            print('\n'.join([
                '|----Please, select a correct module----|',
                '|-------Press "Enter" to continue-------|',
            ]))
            module_select = raw_input()
            cms.main_menu()
        '''
        When the Python interpreter reads a source file, it executes all
        of the code found in it.
            Before executing the code, it will define a few special variables.For example,
        if the python interpreter is running that module (the source file) as
        the main program, it sets the special __name__ variable to have a value
        "__main__".If this file is being imported from another module, __name__
        will be set to the module's name.
        '''
        '''
        Перед исполнением, программа определяет несколько специальных переменных.
        если интерпретатор запускает файл как основную программу, он
        выставляет особую переменную __name__ в значение "__main__".
        '''


# Starter
if __name__ == "__main__":
    cms = CMS()
    cms.main_menu()


class PaymentModule:
    def __init__(self):
        pass

    # A static method does not receive an implicit first argument.
    @staticmethod
    def show_menu(total_price, type_of_menu, type_of_service, amount_of_customers, discount, discountcount):
        global payment_module
        payment_module = PaymentModule()
        print('\n'.join([
            "||----Payment Module----|",
            "|[T]Display total amount to be paid",
            "|[P]Make payment",
            "|[M]Return to Main Menu",
        ]))
        module_select = raw_input()
        if module_select == 'T' or module_select == 't':
            payment_module.display_total_amaunt(total_price, type_of_menu, type_of_service, amount_of_customers,
                                                discount)
        elif module_select == 'P' or module_select == 'p':
            payment_module.write_list(total_price, type_of_menu, type_of_service, amount_of_customers,
                                      discount, discountcount)
        elif module_select == 'm' or module_select == 'M':
            cms.main_menu()
        else:
            payment_module.show_menu(total_price, type_of_menu, type_of_service, amount_of_customers,
                                     discount, discountcount)
        return total_price, type_of_menu, type_of_service, amount_of_customers, discount

    # A static method does not receive an implicit first argument.
    @staticmethod
    def display_total_amaunt(total_price, type_of_menu, type_of_service, amount_of_customers, discount):

        print ("|Total price: {}\n |Type of menu: {}\n |Type of service: {}\n |Amount of customers:\n {} |Discount: {}".format(
            total_price, type_of_menu, type_of_service, int(amount_of_customers),
            discount + "\n|----Press 'Enter' to continue...----|"))
        absent_input = raw_input()
        payment_module = PaymentModule()
        payment_module.show_menu(total_price, type_of_menu, type_of_service, amount_of_customers, discount,
                                 discountcount)

    # A static method does not receive an implicit first argument.
    @staticmethod
    def write_list(total_price, type_of_menu, type_of_service, amount_of_customers, discount, discountcount):
        global bill_List
        '''
            Write data to file
        '''
        # to check current time and date
        from time import gmtime, strftime
        time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        # create list of data
        from random import randint
        OderId = (randint(1, 9000))
        # nested list
        bill_List = [OderId,
                     ['Total price:', total_price],
                     ['Type of menu:', type_of_menu],
                     ['Type of service:', type_of_service],
                     ['Amount of customers:', str(amount_of_customers)],
                     ['Discount:', discount, '= RM', discountcount],
                     ['Time:', time], '\t']
        try:
            # Open a file in write mode
            f = open('Bills.txt', 'a')
            for item in bill_List:
                f.write("%s\n" % item)
            # Close opend file
            f.close()
            print ("|-----File was successfully saved------|\n")
            try:
                print (
                    "|-----Your order------|\n" + "|-Order ID: {}\n |-Total price: {}\n |-Type of menu: {}\n |-Type of "
                                                  "service: {}\n |-Amount of customers: {}\n |-Discount: {} = RM{}".format(
                        OderId, total_price, type_of_menu, type_of_service, int(amount_of_customers), discount,
                        discountcount))
            except Exception:
                print ("ERROR ORDER IS ABSENT")
            print ("|-----Press 'Enter' to continue------|\n")
            absent_input = raw_input()
            cms.main_menu()
        except EOFError:
            print ("ERROR")
            cms.main_menu()



