from matplotlib.axes import Axes
from matplotlib.container import BarContainer

def autolabel_err_bars(
        ax: Axes,
        barcontainer: BarContainer,
        height_multiplier: float = 1.00,
        round_n: int = 2,
        x_mod: str = 'left',
        ha: str = 'left') -> None:
    """Labels the mean of the barcontainer above the container.
    https://stackoverflow.com/questions/14270391/python-matplotlib-multiple-bars
    """

    for ix, rect in enumerate(barcontainer):

        # Height for bar
        h = rect.get_height()

        # # Calculate x based on position of bar
        # if ix == 0:
        #     x = rect.get_x(),
        # elif ix == len(barcontainer):
        #     x = rect.get_x() + rect.get_width()/2
        # # else:
        # #     x = rect.get_x() + rect.get_width()

        # Set static x
        if x_mod == 'left':
            x = rect.get_x()
        elif x_mod == 'left_center':
            x = rect.get_x() + rect.get_width()/4
        elif x_mod == 'center':
            x = rect.get_x() + rect.get_width()/2
        elif x_mod == 'right_center':
            x = rect.get_x() + 3 * rect.get_width()/4
        elif x_mod == 'right':
            x = rect.get_x() + rect.get_width()
        elif isinstance(x_mod, float):
            x = rect.get_x() + x_mod
        else:
            raise ValueError(
                'invalid :param x_mod:. Must be in options above or float.')

        # Textbox
        ax.text(
            x=x,
            y=height_multiplier*h,
            s=str(round(h, round_n)),
            ha=ha,
            va='bottom')

    return None
