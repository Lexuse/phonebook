# import data_generation as dg
import user_interface as ui
import crud


# dg.start() # генерация базы контактов
crud.init_data_base('base_phone.csv')
ui.ls_menu()
