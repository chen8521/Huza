from PyQt5.QtWidgets import QWidget, QVBoxLayout


def setChartMode(self, args):
    mode = args
    chartwidget = self.docks['main'].widget()
    if not hasattr(chartwidget, 'myax'):
        return

    ctrol = chartwidget.myctrol
    canvas = chartwidget.mycanvas
    ctrol.mode = mode
    canvas.draw()


def setLagendEnable(self, args):
    return
    enabled = args
    chartwidget = self.docks['main'].widget()
    if not hasattr(chartwidget, 'myax'):
        return

    ax = chartwidget.myax
    canvas = chartwidget.mycanvas
    ax.get_legend().set_visible(enabled)
    canvas.draw()


def setRest(self, args):
    mode = args
    chartwidget = self.docks['main'].widget()
    if not hasattr(chartwidget, 'myax'):
        return

    ctrol = chartwidget.myctrol
    canvas = chartwidget.mycanvas
    ctrol.home()
    canvas.draw()


def setSaveFigure(self, args):
    chartwidget = self.docks['main'].widget()
    if not hasattr(chartwidget, 'myax'):
        return

    ctrol = chartwidget.myctrol
    canvas = chartwidget.mycanvas
    ctrol.save_figure()
    canvas.draw()


def rems_plot_contourf_xy(self, args):
    self.setDockName('main', f'')

    contianerWidget = QWidget(self.form)
    lay = QVBoxLayout(self.form)
    lay.setContentsMargins(0, 0, 0, 0)
    contianerWidget.setLayout(lay)

    canvas = FigureCanvas(Figure(figsize=(5, 3)))
    lay.addWidget(canvas)
    ctrol = MyNavigationToolbar2QT(canvas, self.form)
    canvas.figure.subplots_adjust(left=0.1, right=0.97, wspace=0.3, hspace=0.3)
    ax = canvas.figure.subplots()

    contianerWidget.myax = ax
    contianerWidget.myctrol = ctrol
    contianerWidget.mycanvas = canvas
    self.docks["main"].setWidget(contianerWidget)


def quxian(self, args):
    self.setDockName('main', f'曲线绘制')

    contianerWidget = QWidget(self.form)
    lay = QVBoxLayout(self.form)
    lay.setContentsMargins(0, 0, 0, 0)
    contianerWidget.setLayout(lay)

    canvas = FigureCanvas(Figure(figsize=(5, 3)))
    lay.addWidget(canvas)
    ctrol = MyNavigationToolbar2QT(canvas, self.form)
    canvas.figure.subplots_adjust(left=0.1, right=0.97, wspace=0.3, hspace=0.3)

    np.random.seed(19680801)

    dt = 0.01
    t = np.arange(0, 30, dt)
    nse1 = np.random.randn(len(t))  # white noise 1
    nse2 = np.random.randn(len(t))  # white noise 2

    # Two signals with a coherent part at 10Hz and a random part
    s1 = np.sin(2 * np.pi * 10 * t) + nse1
    s2 = np.sin(2 * np.pi * 10 * t) + nse2

    axs = canvas.figure.subplots(2, 1)
    axs[0].plot(t, s1, t, s2)
    axs[0].set_xlim(0, 2)
    axs[0].set_xlabel('time')
    axs[0].set_ylabel('s1 and s2')
    axs[0].grid(True)

    cxy, f = axs[1].cohere(s1, s2, 256, 1. / dt)
    axs[1].set_ylabel('coherence')

    contianerWidget.myax = axs[0]
    contianerWidget.myctrol = ctrol
    contianerWidget.mycanvas = canvas
    self.docks["main"].setWidget(contianerWidget)


def quxian2(self, args):
    self.setDockName('main', f'曲线绘制')

    contianerWidget = QWidget(self.form)
    lay = QVBoxLayout(self.form)
    lay.setContentsMargins(0, 0, 0, 0)
    contianerWidget.setLayout(lay)

    canvas = FigureCanvas(Figure(figsize=(5, 3)))
    lay.addWidget(canvas)
    ctrol = MyNavigationToolbar2QT(canvas, self.form)
    canvas.figure.subplots_adjust(left=0.1, right=0.97, wspace=0.3, hspace=0.3)

    from cycler import cycler
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt

    # Define a list of markevery cases and color cases to plot
    cases = [None,
             8,
             (30, 8),
             [16, 24, 30],
             [0, -1],
             slice(100, 200, 3),
             0.1,
             0.3,
             1.5,
             (0.0, 0.1),
             (0.45, 0.1)]

    colors = ['#1f77b4',
              '#ff7f0e',
              '#2ca02c',
              '#d62728',
              '#9467bd',
              '#8c564b',
              '#e377c2',
              '#7f7f7f',
              '#bcbd22',
              '#17becf',
              '#1a55FF']

    # Configure rcParams axes.prop_cycle to simultaneously cycle cases and colors.
    mpl.rcParams['axes.prop_cycle'] = cycler(markevery=cases, color=colors)

    # Create data points and offsets
    x = np.linspace(0, 2 * np.pi)
    offsets = np.linspace(0, 2 * np.pi, 11, endpoint=False)
    yy = np.transpose([np.sin(x + phi) for phi in offsets])

    # Set the plot curve with markers and a title
    ax = canvas.figure.subplots()

    for i in range(len(cases)):
        ax.plot(yy[:, i], marker='o', label=str(cases[i]))
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper right', borderaxespad=0.,shadow=True)
    ax.get_legend().set_visible(True)
    ax.set_title('Support for axes.prop_cycle cycler with markevery')

    contianerWidget.myax = ax
    contianerWidget.myctrol = ctrol
    contianerWidget.mycanvas = canvas
    self.docks["main"].setWidget(contianerWidget)

def sandian(self, args):
    self.setDockName('main', f'曲线绘制')

    contianerWidget = QWidget(self.form)
    lay = QVBoxLayout(self.form)
    lay.setContentsMargins(0, 0, 0, 0)
    contianerWidget.setLayout(lay)

    canvas = FigureCanvas(Figure(figsize=(5, 3)))
    lay.addWidget(canvas)
    ctrol = MyNavigationToolbar2QT(canvas, self.form)
    canvas.figure.subplots_adjust(left=0.1, right=0.97, wspace=0.3, hspace=0.3)

    np.random.seed(19680801)
    # some random data
    x = np.random.randn(1000)
    y = np.random.randn(1000)

    def scatter_hist(x, y, ax, ax_histx, ax_histy):
        # no labels
        ax_histx.tick_params(axis="x", labelbottom=False)
        ax_histy.tick_params(axis="y", labelleft=False)

        # the scatter plot:
        ax.scatter(x, y)

        # now determine nice limits by hand:
        binwidth = 0.25
        xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
        lim = (int(xymax / binwidth) + 1) * binwidth

        bins = np.arange(-lim, lim + binwidth, binwidth)
        ax_histx.hist(x, bins=bins)
        ax_histy.hist(y, bins=bins, orientation='horizontal')


    # definitions for the axes
    left, width = 0.1, 0.65
    bottom, height = 0.1, 0.65
    spacing = 0.005

    rect_scatter = [left, bottom, width, height]
    rect_histx = [left, bottom + height + spacing, width, 0.2]
    rect_histy = [left + width + spacing, bottom, 0.2, height]

    # start with a square Figure

    ax = canvas.figure.add_axes(rect_scatter)
    ax_histx = canvas.figure.add_axes(rect_histx, sharex=ax)
    ax_histy = canvas.figure.add_axes(rect_histy, sharey=ax)

    # use the previously defined function
    scatter_hist(x, y, ax, ax_histx, ax_histy)


    contianerWidget.myax = ax
    contianerWidget.myctrol = ctrol
    contianerWidget.mycanvas = canvas
    self.docks["main"].setWidget(contianerWidget)


def sample(self, args):
    self.setDockName('main', f'曲线绘制')

    contianerWidget = QWidget(self.form)
    lay = QVBoxLayout(self.form)
    lay.setContentsMargins(0, 0, 0, 0)
    contianerWidget.setLayout(lay)

    canvas = FigureCanvas(Figure(figsize=(5, 3)))
    lay.addWidget(canvas)
    ctrol = MyNavigationToolbar2QT(canvas, self.form)
    canvas.figure.subplots_adjust(left=0.1, right=0.97, wspace=0.3, hspace=0.3)

    # Data for plotting
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)
    ax = canvas.figure.subplots()
    ax.plot(t, s)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
           title='About as simple as it gets, folks')
    ax.grid()

    contianerWidget.myax = ax
    contianerWidget.myctrol = ctrol
    contianerWidget.mycanvas = canvas
    self.docks["main"].setWidget(contianerWidget)


def quxian3(self, args):
    self.setDockName('main', f'')

    contianerWidget = QWidget(self.form)
    lay = QVBoxLayout(self.form)
    lay.setContentsMargins(0, 0, 0, 0)
    contianerWidget.setLayout(lay)

    canvas = FigureCanvas(Figure(figsize=(5, 3)))
    lay.addWidget(canvas)
    ctrol = MyNavigationToolbar2QT(canvas, self.form)
    canvas.figure.subplots_adjust(left=0.1, right=0.97, wspace=0.3, hspace=0.3)
    ax = canvas.figure.subplots()

    year = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2018]
    population_by_continent = {
        'africa': [228, 284, 365, 477, 631, 814, 1044, 1275],
        'americas': [340, 425, 519, 619, 727, 840, 943, 1006],
        'asia': [1394, 1686, 2120, 2625, 3202, 3714, 4169, 4560],
        'europe': [220, 253, 276, 295, 310, 303, 294, 293],
        'oceania': [12, 15, 19, 22, 26, 31, 36, 39],
    }

    ax.stackplot(year, population_by_continent.values(),
                 labels=population_by_continent.keys())
    ax.legend(loc='upper left')
    ax.set_title('World population')
    ax.set_xlabel('Year')
    ax.set_ylabel('Number of people (millions)')


    contianerWidget.myax = ax
    contianerWidget.myctrol = ctrol
    contianerWidget.mycanvas = canvas
    self.docks["main"].setWidget(contianerWidget)

def heatmap(self, args):
    self.setDockName('main', f'')

    contianerWidget = QWidget(self.form)
    lay = QVBoxLayout(self.form)
    lay.setContentsMargins(0, 0, 0, 0)
    contianerWidget.setLayout(lay)

    canvas = FigureCanvas(Figure(figsize=(5, 3)))
    lay.addWidget(canvas)
    ctrol = MyNavigationToolbar2QT(canvas, self.form)
    canvas.figure.subplots_adjust(left=0.1, right=0.97, wspace=0.3, hspace=0.3)
    ax = canvas.figure.subplots()

    vegetables = ["cucumber", "tomato", "lettuce", "asparagus",
                  "potato", "wheat", "barley"]
    farmers = ["Farmer Joe", "Upland Bros.", "Smith Gardening",
               "Agrifun", "Organiculture", "BioGoods Ltd.", "Cornylee Corp."]

    harvest = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
                        [2.4, 0.0, 4.0, 1.0, 2.7, 10, 0.0],
                        [1.1, 9, 0.8, 4.3, 1.9, 4.4, 0.0],
                        [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
                        [0.7, 1.7, 5, 2.6, 2.2, 6.2, 0.0],
                        [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
                        [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]])

    im = ax.imshow(harvest,cmap = matplotlib.cm.get_cmap('jet'))

    # We want to show all ticks...
    ax.set_xticks(np.arange(len(farmers)))
    ax.set_yticks(np.arange(len(vegetables)))
    # ... and label them with the respective list entries
    ax.set_xticklabels(farmers)
    ax.set_yticklabels(vegetables)

    # Rotate the tick labels and set their alignment.

    # Loop over data dimensions and create text annotations.
    for i in range(len(vegetables)):
        for j in range(len(farmers)):
            text = ax.text(j, i, harvest[i, j],
                           ha="center", va="center", color="w")

    ax.set_title("Harvest of local farmers (in tons/year)")
    canvas.figure.colorbar(im)
    contianerWidget.myax = ax
    contianerWidget.myctrol = ctrol
    contianerWidget.mycanvas = canvas
    self.docks["main"].setWidget(contianerWidget)

def yun(self, args):
    self.setDockName('main', f'')

    contianerWidget = QWidget(self.form)
    lay = QVBoxLayout(self.form)
    lay.setContentsMargins(0, 0, 0, 0)
    contianerWidget.setLayout(lay)

    canvas = FigureCanvas(Figure(figsize=(5, 3)))
    lay.addWidget(canvas)
    ctrol = MyNavigationToolbar2QT(canvas, self.form)
    canvas.figure.subplots_adjust(left=0.1, right=0.97, wspace=0.3, hspace=0.3)
    ax = canvas.figure.subplots()

    np.random.seed(19680801)
    npts = 200
    ngridx = 100
    ngridy = 200
    x = np.random.uniform(-2, 2, npts)
    y = np.random.uniform(-2, 2, npts)
    z = x * np.exp(-x ** 2 - y ** 2)

    ax1,ax2 = canvas.figure.subplots(2, 1)

    # -----------------------
    # Interpolation on a grid
    # -----------------------
    # A contour plot of irregularly spaced data coordinates
    # via interpolation on a grid.

    # Create grid values first.
    xi = np.linspace(-2.1, 2.1, ngridx)
    yi = np.linspace(-2.1, 2.1, ngridy)
    import matplotlib.tri as tri
    # Linearly interpolate the data (x, y) on a grid defined by (xi, yi).
    triang = tri.Triangulation(x, y)
    interpolator = tri.LinearTriInterpolator(triang, z)
    Xi, Yi = np.meshgrid(xi, yi)
    zi = interpolator(Xi, Yi)

    # Note that scipy.interpolate provides means to interpolate data on a grid
    # as well. The following would be an alternative to the four lines above:
    # from scipy.interpolate import griddata
    # zi = griddata((x, y), z, (xi[None, :], yi[:, None]), method='linear')

    ax1.contour(xi, yi, zi, levels=14, linewidths=0.5, colors='k')
    cntr1 = ax1.contourf(xi, yi, zi, levels=14, cmap="RdBu_r")

    canvas.figure.colorbar(cntr1, ax=ax1)
    ax1.plot(x, y, 'ko', ms=3)
    ax1.set(xlim=(-2, 2), ylim=(-2, 2))
    ax1.set_title('grid and contour (%d points, %d grid points)' %
                  (npts, ngridx * ngridy))

    # ----------
    # Tricontour
    # ----------
    # Directly supply the unordered, irregularly spaced coordinates
    # to tricontour.

    ax2.tricontour(x, y, z, levels=14, linewidths=0.5, colors='k')
    cntr2 = ax2.tricontourf(x, y, z, levels=14, cmap="RdBu_r")

    canvas.figure.colorbar(cntr2, ax=ax2)
    ax2.plot(x, y, 'ko', ms=3)
    ax2.set(xlim=(-2, 2), ylim=(-2, 2))
    ax2.set_title('tricontour (%d points)' % npts)


    contianerWidget.myax = ax
    contianerWidget.myctrol = ctrol
    contianerWidget.mycanvas = canvas
    self.docks["main"].setWidget(contianerWidget)

def hexbin(self, args):
    self.setDockName('main', f'')

    contianerWidget = QWidget(self.form)
    lay = QVBoxLayout(self.form)
    lay.setContentsMargins(0, 0, 0, 0)
    contianerWidget.setLayout(lay)

    canvas = FigureCanvas(Figure(figsize=(5, 3)))
    lay.addWidget(canvas)
    ctrol = MyNavigationToolbar2QT(canvas, self.form)
    canvas.figure.subplots_adjust(left=0.1, right=0.97, wspace=0.3, hspace=0.3)

    np.random.seed(19680801)

    n = 100000
    x = np.random.standard_normal(n)
    y = 2.0 + 3.0 * x + 4.0 * np.random.standard_normal(n)
    xmin = x.min()
    xmax = x.max()
    ymin = y.min()
    ymax = y.max()

    axs = canvas.figure.subplots(ncols=2, sharey=True)
    ax = axs[0]
    hb = ax.hexbin(x, y, gridsize=50, cmap='inferno')
    ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax))
    ax.set_title("Hexagon binning")
    cb = canvas.figure.colorbar(hb, ax=ax)
    cb.set_label('counts')

    ax = axs[1]
    hb = ax.hexbin(x, y, gridsize=50, bins='log', cmap='inferno')
    ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax))
    ax.set_title("With a log color scale")
    cb = canvas.figure.colorbar(hb, ax=ax)
    cb.set_label('log10(N)')

    contianerWidget.myax = ax
    contianerWidget.myctrol = ctrol
    contianerWidget.mycanvas = canvas
    self.docks["main"].setWidget(contianerWidget)

def times(self, args):
    self.setDockName('main', f'')

    contianerWidget = QWidget(self.form)
    lay = QVBoxLayout(self.form)
    lay.setContentsMargins(0, 0, 0, 0)
    contianerWidget.setLayout(lay)

    canvas = FigureCanvas(Figure(figsize=(5, 3)))
    lay.addWidget(canvas)
    ctrol = MyNavigationToolbar2QT(canvas, self.form)
    canvas.figure.subplots_adjust(left=0.1, right=0.97, wspace=0.3, hspace=0.3)
    fig=  canvas.figure
    from copy import copy
    import time

    import numpy.matlib
    from matplotlib.colors import LogNorm

    axes = canvas.figure.subplots(nrows=3)

    # Make some data; a 1D random walk + small fraction of sine waves
    num_series = 1000
    num_points = 100
    SNR = 0.10  # Signal to Noise Ratio
    x = np.linspace(0, 4 * np.pi, num_points)
    # Generate unbiased Gaussian random walks
    Y = np.cumsum(np.random.randn(num_series, num_points), axis=-1)
    # Generate sinusoidal signals
    num_signal = int(round(SNR * num_series))
    phi = (np.pi / 8) * np.random.randn(num_signal, 1)  # small random offset
    Y[-num_signal:] = (
            np.sqrt(np.arange(num_points))[None, :]  # random walk RMS scaling factor
            * (np.sin(x[None, :] - phi)
               + 0.05 * np.random.randn(num_signal, num_points))  # small random noise
    )

    # Plot series using `plot` and a small value of `alpha`. With this view it is
    # very difficult to observe the sinusoidal behavior because of how many
    # overlapping series there are. It also takes a bit of time to run because so
    # many individual artists need to be generated.
    tic = time.time()
    axes[0].plot(x, Y.T, color="C0", alpha=0.1)
    toc = time.time()
    axes[0].set_title("Line plot with alpha")
    print(f"{toc - tic:.3f} sec. elapsed")

    # Now we will convert the multiple time series into a histogram. Not only will
    # the hidden signal be more visible, but it is also a much quicker procedure.
    tic = time.time()
    # Linearly interpolate between the points in each time series
    num_fine = 800
    x_fine = np.linspace(x.min(), x.max(), num_fine)
    y_fine = np.empty((num_series, num_fine), dtype=float)
    for i in range(num_series):
        y_fine[i, :] = np.interp(x_fine, x, Y[i, :])
    y_fine = y_fine.flatten()
    x_fine = np.matlib.repmat(x_fine, num_series, 1).flatten()

    # Plot (x, y) points in 2d histogram with log colorscale
    # It is pretty evident that there is some kind of structure under the noise
    # You can tune vmax to make signal more visible
    import matplotlib.pyplot as plt
    cmap = copy(plt.cm.plasma)
    cmap.set_bad(cmap(0))
    h, xedges, yedges = np.histogram2d(x_fine, y_fine, bins=[400, 100])
    pcm = axes[1].pcolormesh(xedges, yedges, h.T, cmap=cmap,
                             norm=LogNorm(vmax=1.5e2), rasterized=True)
    fig.colorbar(pcm, ax=axes[1], label="# points", pad=0)
    axes[1].set_title("2d histogram and log color scale")

    # Same data but on linear color scale
    pcm = axes[2].pcolormesh(xedges, yedges, h.T, cmap=cmap,
                             vmax=1.5e2, rasterized=True)
    fig.colorbar(pcm, ax=axes[2], label="# points", pad=0)
    axes[2].set_title("2d histogram and linear color scale")

    contianerWidget.myax = axes[0]
    contianerWidget.myctrol = ctrol
    contianerWidget.mycanvas = canvas
    self.docks["main"].setWidget(contianerWidget)


def yun2(self, args):
    self.setDockName('main', f'')

    contianerWidget = QWidget(self.form)
    lay = QVBoxLayout(self.form)
    lay.setContentsMargins(0, 0, 0, 0)
    contianerWidget.setLayout(lay)

    canvas = FigureCanvas(Figure(figsize=(5, 3)))
    lay.addWidget(canvas)
    ctrol = MyNavigationToolbar2QT(canvas, self.form)
    canvas.figure.subplots_adjust(left=0.1, right=0.97, wspace=0.3, hspace=0.3)
    ax = canvas.figure.subplots()

    from matplotlib import cm

    extent = (-3, 3, -3, 3)

    delta = 0.5
    x = np.arange(-3.0, 4.001, delta)
    y = np.arange(-4.0, 3.001, delta)
    X, Y = np.meshgrid(x, y)
    Z1 = np.exp(-X ** 2 - Y ** 2)
    Z2 = np.exp(-(X - 1) ** 2 - (Y - 1) ** 2)
    Z = Z1 - Z2

    norm = cm.colors.Normalize(vmax=abs(Z).max(), vmin=-abs(Z).max())

    cset1 = ax.contourf(
        X, Y, Z, 40,
        norm=norm)
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_xticks([])
    ax.set_yticks([])

    contianerWidget.myax = ax
    contianerWidget.myctrol = ctrol
    contianerWidget.mycanvas = canvas
    self.docks["main"].setWidget(contianerWidget)

def td(self, args):
    self.setDockName('main', f'')

    contianerWidget = QWidget(self.form)
    lay = QVBoxLayout(self.form)
    lay.setContentsMargins(0, 0, 0, 0)
    contianerWidget.setLayout(lay)

    canvas = FigureCanvas(Figure(figsize=(5, 3)))
    lay.addWidget(canvas)
    ctrol = MyNavigationToolbar2QT(canvas, self.form)
    canvas.figure.subplots_adjust(left=0.1, right=0.97, wspace=0.3, hspace=0.3)

    from mpl_toolkits.mplot3d.axes3d import get_test_data

    # set up a figure twice as wide as it is tall
    fig = canvas.figure

    # ===============
    #  First subplot
    # ===============
    # set up the axes for the first plot
    ax = canvas.figure.add_subplot(1, 2, 1, projection='3d')

    # plot a 3D surface like in the example mplot3d/surface3d_demo
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)
    from matplotlib import cm

    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)
    ax.set_zlim(-1.01, 1.01)
    fig.colorbar(surf, shrink=0.5, aspect=10)

    # ===============
    # Second subplot
    # ===============
    # set up the axes for the second plot
    ax = fig.add_subplot(1, 2, 2, projection='3d')

    # plot a 3D wireframe like in the example mplot3d/wire3d_demo
    X, Y, Z = get_test_data(0.05)
    ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

    contianerWidget.myax = ax
    contianerWidget.myctrol = ctrol
    contianerWidget.mycanvas = canvas
    self.docks["main"].setWidget(contianerWidget)

def td2(self, args):
    self.setDockName('main', f'')

    contianerWidget = QWidget(self.form)
    lay = QVBoxLayout(self.form)
    lay.setContentsMargins(0, 0, 0, 0)
    contianerWidget.setLayout(lay)

    canvas = FigureCanvas(Figure(figsize=(5, 3)))
    lay.addWidget(canvas)
    ctrol = MyNavigationToolbar2QT(canvas, self.form)
    canvas.figure.subplots_adjust(left=0.1, right=0.97, wspace=0.3, hspace=0.3)
    ax = canvas.figure.subplots()

    np.random.seed(19680801)

    def polygon_under_graph(xlist, ylist):
        """
        Construct the vertex list which defines the polygon filling the space under
        the (xlist, ylist) line graph.  Assumes the xs are in ascending order.
        """
        return [(xlist[0], 0.), *zip(xlist, ylist), (xlist[-1], 0.)]

    ax = canvas.figure.add_subplot(projection='3d')

    # Make verts a list such that verts[i] is a list of (x, y) pairs defining
    # polygon i.
    verts = []

    # Set up the x sequence
    xs = np.linspace(0., 10., 26)

    # The ith polygon will appear on the plane y = zs[i]
    zs = range(4)

    for i in zs:
        ys = np.random.rand(len(xs))
        verts.append(polygon_under_graph(xs, ys))

    poly = PolyCollection(verts, facecolors=['r', 'g', 'b', 'y'], alpha=.6)
    ax.add_collection3d(poly, zs=zs, zdir='y')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim(0, 10)
    ax.set_ylim(-1, 4)
    ax.set_zlim(0, 1)

    contianerWidget.myax = ax
    contianerWidget.myctrol = ctrol
    contianerWidget.mycanvas = canvas
    self.docks["main"].setWidget(contianerWidget)


def movea(self, args):
    self.setDockName('main', f'')

    contianerWidget = QWidget(self.form)
    lay = QVBoxLayout(self.form)
    lay.setContentsMargins(0, 0, 0, 0)
    contianerWidget.setLayout(lay)

    canvas = FigureCanvas(Figure(figsize=(5, 3)))
    lay.addWidget(canvas)
    ctrol = MyNavigationToolbar2QT(canvas, self.form)
    canvas.figure.subplots_adjust(left=0.1, right=0.97, wspace=0.3, hspace=0.3)

    np.random.seed(19680801)

    axsrc, axzoom = canvas.figure.subplots(nrows=2)
    axsrc.set(xlim=(0, 1), ylim=(0, 1), autoscale_on=False,
              title='Click to zoom')
    axzoom.set(xlim=(0.45, 0.55), ylim=(0.4, 0.6), autoscale_on=False,
               title='Zoom window')

    x, y, s, c = np.random.rand(4, 200)
    s *= 200

    axsrc.scatter(x, y, s, c)
    axzoom.scatter(x, y, s, c)

    def on_press(event):
        if event.button != 1:
            return
        x, y = event.xdata, event.ydata
        axzoom.set_xlim(x - 0.1, x + 0.1)
        axzoom.set_ylim(y - 0.1, y + 0.1)
        canvas.figure.canvas.draw()

    canvas.mpl_connect('button_press_event', on_press)

    contianerWidget.myax = axsrc
    contianerWidget.myctrol = ctrol
    contianerWidget.mycanvas = canvas
    self.docks["main"].setWidget(contianerWidget)

def readstl(self, args):
    self.setDockName('main', f'显示数模')
    contianerWidget = QWidget(self.form)
    lay = QVBoxLayout(self.form)
    lay.setContentsMargins(0, 0, 0, 0)
    contianerWidget.setLayout(lay)

    self.vtkWidget = QVTKRenderWindowInteractor(contianerWidget)
    vtkWidget = self.vtkWidget
    lay.addWidget(vtkWidget)

    colors = vtk.vtkNamedColors()
    filename = '42400-IDGH.stl'
    reader = vtk.vtkSTLReader()
    reader.SetFileName(filename)

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    # Create a rendering window and renderer
    ren = vtk.vtkRenderer()
    ren.SetBackground(colors.GetColor3d("ivory_black"))
    vtkWidget.GetRenderWindow().AddRenderer(ren)
    # Create a renderwindowinteractor
    iren = vtkWidget.GetRenderWindow().GetInteractor()

    # Assign actor to the renderer
    ren.AddActor(actor)

    # Enable user interface interactor
    iren.Initialize()

    self.axes1 = MakeAxesActor()
    axes1 = self.axes1
    self.om1 = vtk.vtkOrientationMarkerWidget()
    om1 = self.om1
    om1.SetOrientationMarker(axes1)
    # Position lower left in the viewport.
    om1.SetInteractor(iren)
    om1.EnabledOn()
    om1.InteractiveOn()
    self.docks["main"].setWidget(contianerWidget)

def MakeAxesActor():
    axes = vtk.vtkAxesActor()
    axes.SetShaftTypeToCylinder()
    axes.SetXAxisLabelText('X')
    axes.SetYAxisLabelText('Y')
    axes.SetZAxisLabelText('Z')
    axes.SetTotalLength(2.0, 2.0, 2.0)
    axes.SetCylinderRadius(0.5 * axes.GetCylinderRadius())
    axes.SetConeRadius(1.025 * axes.GetConeRadius())
    axes.SetSphereRadius(1.5 * axes.GetSphereRadius())
    return axes

def readmesh(self, args):
    self.setDockName('main', f'显示网格')
    contianerWidget = QWidget(self.form)
    lay = QVBoxLayout(self.form)
    lay.setContentsMargins(0, 0, 0, 0)
    contianerWidget.setLayout(lay)



    self.vtkWidget2 = QVTKRenderWindowInteractor(contianerWidget)
    vtkWidget = self.vtkWidget2
    lay.addWidget(vtkWidget)

    fileName = 'spanner.vtk'
    colors = vtk.vtkNamedColors()

    lut = vtk.vtkLookupTable()
    lut.SetHueRange(0.0, 0.66667)
    _i = 8
    reader = vtk.vtkDataSetReader()
    reader.SetScalarsName(f'thickness{_i}')
    reader.SetVectorsName(f'displacement{_i}')
    reader.SetFileName(fileName)
    reader.Update()

    warp = vtk.vtkWarpVector()
    warp.SetInputData(reader.GetUnstructuredGridOutput())

    connect = vtk.vtkConnectivityFilter()
    connect.SetInputConnection(warp.GetOutputPort())
    connect.SetExtractionModeToSpecifiedRegions()
    connect.AddSpecifiedRegion(0)
    connect.AddSpecifiedRegion(1)

    mold = vtk.vtkGeometryFilter()
    mold.SetInputConnection(connect.GetOutputPort())

    moldMapper = vtk.vtkDataSetMapper()
    moldMapper.SetInputConnection(mold.GetOutputPort())
    moldMapper.ScalarVisibilityOff()

    moldActor = vtk.vtkActor()
    moldActor.SetMapper(moldMapper)
    moldActor.GetProperty().SetColor(colors.GetColor3d("ivory_black"))
    moldActor.GetProperty().SetRepresentationToWireframe()

    connect2 = vtk.vtkConnectivityFilter()
    connect2.SetInputConnection(warp.GetOutputPort())
    connect2.SetExtractionModeToSpecifiedRegions()
    connect2.AddSpecifiedRegion(2)

    parison = vtk.vtkGeometryFilter()
    parison.SetInputConnection(connect2.GetOutputPort())

    normals2 = vtk.vtkPolyDataNormals()
    normals2.SetInputConnection(parison.GetOutputPort())
    normals2.SetFeatureAngle(60)

    parisonMapper = vtk.vtkPolyDataMapper()
    parisonMapper.SetInputConnection(normals2.GetOutputPort())
    parisonMapper.SetLookupTable(lut)
    parisonMapper.SetScalarRange(0.12, 1.0)

    parisonActor = vtk.vtkActor()
    parisonActor.SetMapper(parisonMapper)

    cf = vtk.vtkContourFilter()
    cf.SetInputConnection(connect2.GetOutputPort())
    cf.SetValue(0, 0.5)

    contourMapper = vtk.vtkPolyDataMapper()
    contourMapper.SetInputConnection(cf.GetOutputPort())

    contours = vtk.vtkActor()
    contours.SetMapper(contourMapper)

    ren = vtk.vtkRenderer()
    ren.AddActor(moldActor)
    ren.AddActor(parisonActor)
    ren.AddActor(contours)
    ren.SetBackground(colors.GetColor3d("AliceBlue"))

    # ren.GetActiveCamera().SetPosition(0,0,0)
    # ren.GetActiveCamera().SetFocalPoint(0.141547, 12.298821, -0.245166)
    # ren.GetActiveCamera().SetViewUp(-0.500000, 0.000000, 0.866025)
    # ren.GetActiveCamera().SetClippingRange(36.640827, 78.614680)

    vtkWidget.GetRenderWindow().AddRenderer(ren)
    # Create a renderwindowinteractor
    iren = vtkWidget.GetRenderWindow().GetInteractor()
    iren.Initialize()

    self.axes1 = MakeAxesActor()
    axes1 = self.axes1

    self.om1 = vtk.vtkOrientationMarkerWidget()
    om1 = self.om1
    om1.SetOrientationMarker(axes1)
    om1.SetInteractor(iren)
    om1.EnabledOn()
    om1.InteractiveOn()
    ren.ResetCamera()

    self.docks["main"].setWidget(contianerWidget)