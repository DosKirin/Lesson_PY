# class Auto:
#     auto_name = 'LX456'
#     auto_model = 'mazda'
#     auto_year = 2008
#
#     def on_auto_start(self):
#         print(f'run engine')
#     def on_auto_stop(self):
#         print('stop')
#
# a = Auto()
# print(a)
# print(type(a))
# print(a.auto_name)
# a.on_auto_start()
# a.on_auto_stop()



class Auto:
    auto_count = 0

    def on_auto_start(self, auto_name, auto_model, auto_year):
        print('Auto run')
        self.auto_name = auto_name
        self.auto_model = auto_model
        self.auto_year = auto_year
        Auto.auto_count += 1

a = Auto()
a.on_auto_start('Mazda','CX4', 2010)
print(a.auto_name)
print(a.auto_count)

a_2 = Auto()
a_2.on_auto_start('Tesla', 'Model_S', 2021)
print(a_2.auto_name)
print(a_2.auto_count)

