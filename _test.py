
import dearpygui.dearpygui as dpg


dpg.create_context()
dpg.setup_dearpygui()
dpg.create_viewport()
dpg.show_viewport()



def exitting(sender=None, app_data=None, user_data=None):
    print("exiting...")

dpg.set_exit_callback(exitting, user_data='hi')

dpg.start_dearpygui()
dpg.destroy_context()