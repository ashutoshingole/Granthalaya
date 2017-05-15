import Tkinter
import dimensions
import appearance
import buttons


def main():
    window = Tkinter.Tk()
    window.wm_title("Granthalaya")
    dimensions.set_dimensions(window)
    buttons.add_menu(window)
    appearance.set_appearance(window)


main()
