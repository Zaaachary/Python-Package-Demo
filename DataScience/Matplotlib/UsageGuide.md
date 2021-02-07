# Usage Guide
[matplotlib docs](https://matplotlib.org/tutorials/index.html)
## General Concepts
Everything in matplotlib is organized in a *hierarchy* (阶层). Top of the *hierarchy* is the "state-machine environment" which is provided by the `matplotlib.pyplot` module.


## Part of Figure
### Figure 图形
The whole figure. The figure keeps track of all the child Axes, a smattering of 'special' artists (titles, figure legends, etc), and the canvas.

A figure can have any number of Axes, but to be useful should have at least one.
```
fig = plt.figure()

fig.suptitle('No axes on this figure')

fig, ax_lst = plt.subplots(2, 2)
```

### Axes 坐标系
A given figure can contain many Axes, but a given Axes object can only be in one Figure.

The `Axes` contains two (or three in the case of 3D) `Axis` objects which take care of the data limits.The data limits can also be controlled via set via the `set_xlim()` and `set_ylim()` Axes methods. Each Axes has a title (set via `set_title()`), an x-label (set via `set_xlabel()`), and a y-label set via `set_ylabel()`).
### Axis 轴线
graph limits, marks, ticklabels.

The combination of the correct `Locator ` and `Formatter` gives very fine control over the tick locations and labels.

### Artist
Basically everything we can see on the figure is an artist (even the Figure, Axes, and Axis objects). This includes *Text objects, Line2D objects, collection objects, Patch objects...* When the figure is rendered, all of the artists are drawn to the `canvas`. Most Artists are tied to an Axes, such an Artist cannot be shared by multiple Axes, or moved from one to another.
## Types of inputs to plotting functions
All of plotting functions expect `np.array` or `np.ma.masked_array` as input. 'Array-like' objects (like pandas) and `np.matrix`may not work as intended.

It is best to convert these to `np.array` object prior to plotting.
```
# pandas.DataFrame
a = pandas.DataFrame(np.random.rand(4,5), columns = list('abcde'))
a_asndarray = a.values

# np.matrix
b = np.matrix([[1,2],[3,4]])
b_asarray = np.asarray(b)
```

## Matplotlib, pyplot and pylab: how are they related?
`Matplotlib` is the whole package; `matplotlib.pyplot` is a module in `matplotlib`; and `pylab` is a module that gets installed alongside `matplotlib`.

`Pyplot` provides the state-machine interface to the underlying object-oriented plotting library. The state-machine implicitly and automatically creates figures and axes to achieve the desired plot. (**exp02**)

The first call to `plt.plot` will **automatically create the necessary figure and axes** to achieve the desired plot. Subsequent ( 随后的) calls to `plt.plot ` **re-use** the current axes and each add another line. Setting the title, legend, and axis labels also automatically use the current axes and set the title, create the legend, and label the axis respectively.

`pylab` is a convenience module that bulk imports `matplotlib.pyplot` and `numpy` in a single name space. `pylab` is deprecated and its use is strongly discouraged because of namespace pollution. Use `pyplot` instead.

**↑** `pylab` 让 `numpy` 和 `matplotlib` 用一个 namespace

非交互的 plotting 最好用 pyplot 来创建，不用面向对象接口。

## Coding Style
pyplot style **exp03**
function signature  **exp04**

