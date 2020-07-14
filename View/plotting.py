from PyQt5.QtWidgets import QSizePolicy
import matplotlib
import mplfinance as mpf

matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
# import plotly.graph_objects as go


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        # fig = go.Figure()
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass


class PlotCanvas(MyMplCanvas):

    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)

    def compute_initial_figure(self):
        self.axes.grid(True)
        self.axes.plot([0], [0], 'r')

    def update_figure(self, data=[]):
        self.axes.cla()
        self.axes.grid(True)
        self.axes.plot(data['Close'])
        # self.axes.plot(data['<OPEN>'])
        self.draw()

class PlotCanvas2(MyMplCanvas):

    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)

    def compute_initial_figure(self):
        self.axes.grid(True)
        self.axes.plot([0], [0], 'r')

    def update_figure(self, data=[]):
        self.axes.cla()
        # self.axes.grid(True)
        # self.axes.plot(data['<CLOSE>'])
        # self.axes.plot(data['<OPEN>'])
        mpf.plot(data, type='candle', volume=True)

        self.draw()