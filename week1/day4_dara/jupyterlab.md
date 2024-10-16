# JupyterLab

Up to now, your workflow relied on the Spyder IDE, in which you executed Python code interactively within the console (effectively "IPython"), or non-interactively via Python scripts. 

As an alternative, we will cover the basics of using the JupyterLab interface, highlighting the common use-cases for it, and also how it differs from the Spyder IDE.

JupyterLab can be started via the main menu of the Anaconda Navigator:
<div>
<img src="https://raw.githubusercontent.com/ChpcTraining/css2024_notes/main/week1/day4_dara/images/jupyter_lab.png" width=300 style="display: block; margin: auto;" />
</div>

which will automatically open up a webpage in your local web browser, at usually the following URL: `http://localhost:8888/lab/tree`. 

### The Basics

#### Main menu (launcher screen)
<div>
    <img src="https://raw.githubusercontent.com/ChpcTraining/css2024_notes/main/week1/day4_dara/images/jupyterlab_main_view.png" width=800 style="display: block; margin: auto;" />
</div>

Besides the File Browser on the left, you will be presented with a number of different components that you may start up:
1. Notebook
2. Console 
3. Terminal
4. Text File
5. Markdown File
6. Python File
7. Show Contextual Help

#### Some key reasons for using JupyterLab over Spyder
- Notebooks offer data scientists arguably a more convenient and interactive way of working on their datasets within not just the Python framework, but also R and others.
  
- Custom (split) views

  
  e.g.
  <div>
    <img src="https://raw.githubusercontent.com/ChpcTraining/css2024_notes/main/week1/day4_dara/images/jupyterlab_layout.png" width=800 style="display: block; margin: auto;" />
  </div>

- Developing markdown content
  
- Multiple independent kernels, each with own Console Editors/Cell Output Views

- Built-in rendering for e.g. CSV, image and even PDF files.

- And more...!


#### A quick tour of notebooks
Notebooks essentially combine the features of scripting with that of the console: lines of code can be grouped into individual blocks called "cells" that can be executed/manipulated in any desired order. For an indvidual cell, we can click on it and use `Shift + Enter` to execute. Alternatively, to execute all cells in an orderly fashion, we can use the "Run All" option from the "Run" menu dropdown.

Instead of adding code comments in the usual way (i.e. lines beginning with `#`), we can can use Markdown formatted cells (notice that the headings we create allow cells below them to collapse!).

<div>
    <img src="https://raw.githubusercontent.com/ChpcTraining/css2024_notes/main/week1/day4_dara/images/first_notebook.png" width=500 style="display: block; margin: auto;" />
</div>


A useful feature that we listed above is that of Cell Output Views -- this allows one to keep a reference of some desired output always at hand. To create such a view for the output of a specific cell block, right click on the cell and click on "Create New View For Cell Output":
|||
-- | --
<img src="https://raw.githubusercontent.com/ChpcTraining/css2024_notes/main/week1/day4_dara/images/output_views_part1.png" width=450>| <img src="https://raw.githubusercontent.com/ChpcTraining/css2024_notes/main/week1/day4_dara/images/output_views_part2.png" width=400>

This may be quite handy in the beginning when exploring data, since it avoids the need to keep scrolling up to view such content generated previously. Note though that whenever that particular cell block is re-run, if the output changes then so will that in the output view.


### Pandas example

Using a package you should now be quite familiar with, let's grab some real-world data available on the web -- in this case a table from Wikipedia that we can import into a Pandas dataframe directly:

```python
import pandas as pd

wiki_url = 'https://en.wikipedia.org/wiki/List_of_potentially_habitable_exoplanets'
df = pd.read_html(wiki_url, match="Object")[0]
print(df)
```

The above should produce the following output:
```python
	Object	Star	Star type	Mass (M⊕)	Radius (R⊕)	Density (g/cm3)	Flux (F⊕)	Teq (K)	Period (days)	Distance (ly)	Refs/Notes
0	Earth (reported for reference)	Sun	G2V	1.00	1.00	5.514	1.00	255	365.25	0	Only planet known to support life.
1	Venus (reported for reference)	Sun	G2V	0.815	0.9499	5.243	1.911	244.261	224.7	4.2×10^-6	[5]
2	Gliese 12 b	Gliese 12	M4V	0.88+0.39 −0.26	1.03±0.11	4.44	1.6±0.2	315	12.76144±0.00006	40	[6]
3	Gliese 163 c	Gliese 163	M3V	≥6.80	—	—	1.25	277	25.6	49	[1]
4	Gliese 180 c	Gliese 180	M2V	≥6.40	—	—	0.78	239	24.3	39	Not confirmed[1][7]
...	...	...	...	...	...	...	...	...	...	...	...
62	TRAPPIST-1e	TRAPPIST-1	M8V	0.69	0.92	5.65	0.65	230	6.1	41	Confirmed to be rocky[49][50]
63	TRAPPIST-1f	TRAPPIST-1	M8V	1.04	1.04	3.3 ± 0.9	0.37	200	9.2	41	Confirmed to be rocky[49][50]
64	TRAPPIST-1g	TRAPPIST-1	M8V	1.32	1.13	4.186	0.25	182	12.4	41	Confirmed to be rocky[49][50]
65	Wolf 1069 b	Wolf 1069	M5V	≥1.26	~1.08	—	0.65	250	15.6	31.2	[51]
66	Wolf 1061c	Wolf 1061	M3V	≥3.41	~1.60	—	1.30	271	17.9	13.8	[1]
```

You will notice that the data needs a bit of cleaning (e.g. some incomplete/null values, and some are only providing approximate/bounded values). Just as a quick demonstration, let's consider the columns `Teq` and `Period` only, and perform a cleanup:
```python
df_teq_vs_period_cleaned_nan = df[["Object", "Teq (K)", "Period (days)"]].dropna()
df_teq_vs_period_cleaned_teq = df_teq_vs_period_cleaned_nan[~df_teq_vs_period_cleaned_nan['Teq (K)'].isin(['214 [9]', '256+61 −17', '~280'])]
df_teq_vs_period_final_clean = df_teq_vs_period_cleaned_teq[~df_teq_vs_period_cleaned_teq['Period (days)'].isin(['12.76144±0.00006'])].reset_index(drop=True)
```
The above should yield:
```python
df_teq_vs_period_final_clean

	Object	Teq (K)	Period (days)
0	Earth (reported for reference)	255	365.25
1	Venus (reported for reference)	244.261	224.7
2	Gliese 163 c	277	25.6
3	Gliese 180 c	239	24.3
4	Gliese 229 Ac	216	121.9
5	Gliese 357 d	200	55.7
6	Gliese 514 b	202	140.4
7	Gliese 667 Cc	277	28.1
8	Gliese 1002 b	231	10.3
9	GJ 1002 c	182	21.2
10	GJ 1061 c	275	6.7
11	GJ 1061 d	218	13.0
12	GJ 3293 d	223	48.1
13	HD 40307 g	226	197.8
14	K2-9b	279	18.4
15	K2-72e	261	24.2
16	K2-288Bb	207	31.4
17	Kepler-22b	261	289.9
18	Kepler-62e	264	122.4
19	Kepler-62f	204	267.3
20	Kepler-174d	206	247.4
21	Kepler-186f	188	129.9
22	Kepler-283c	248	92.7
23	Kepler-296e	276	34.1
24	Kepler-296f	225	63.3
25	Kepler-442b	233	112.3
26	Kepler-440b	273	101.1
27	Kepler-443b	247	177.7
28	Kepler-452b	261	384.8
29	Kepler-705b	243	56.1
30	Kepler-1229b	213	86.8
31	Kepler-1410b	274	60.9
32	Kepler-1540b	250	125.4
33	Kepler-1544 b	248	168.8
34	Kepler-1606b	277	196.4
35	Kepler-1649c	237	19.5
36	Kepler-1652b	244	38.1
37	Kepler-1653b	258	140.3
38	Kepler-1701b	275	169.1
39	LHS 1140 b	226	24.7
40	LP 890-9 c	272	8.46
41	Luyten b	258	18.65
42	Proxima Centauri b	228	11.186
43	Ross 128 b	280	9.87
44	Teegarden's Star b	264	4.91
45	Teegarden's Star c	199	11.4
46	TOI-700 d	246	37.4
47	TOI-700 e	273	27.8
48	TOI-715 b	234	19.29
49	TRAPPIST-1d	258	4.05
50	TRAPPIST-1e	230	6.1
51	TRAPPIST-1f	200	9.2
52	TRAPPIST-1g	182	12.4
53	Wolf 1069 b	250	15.6
54	Wolf 1061c	271	17.9
```
Then, let's convert each column to a numpy array:
```python
import numpy as np
teq = df_teq_vs_period_final_clean["Teq (K)"].to_numpy().astype(float)
period = df_teq_vs_period_final_clean["Period (days)"].to_numpy().astype(float)
```
and plot various relationships:
```python
import matplotlib.pyplot as plt
plt.xlabel("Period (days)")
plt.ylabel("Teq (K)")
plt.title("Exoplanets in the habitable zone")
plt.scatter(period, teq)
plt.xlabel("Period (days)")
plt.ylabel("Count")
plt.title("Exoplanets in the habitable zone")
plt.hist(period)
plt.xlabel("Teq (K)")
plt.ylabel("Count")
plt.title("Exoplanets in the habitable zone")
plt.hist(teq)
```
||||
-- | -- | -- 
<img src="https://raw.githubusercontent.com/ChpcTraining/css2024_notes/main/week1/day4_dara/images/scatter_period_teq.png" width=350>| <img src="https://raw.githubusercontent.com/ChpcTraining/css2024_notes/main/week1/day4_dara/images/histogram_period.png" width=350>| <img src="https://raw.githubusercontent.com/ChpcTraining/css2024_notes/main/week1/day4_dara/images/histogram_teq.png" width=350>

We may want to export our cleaned-up dataset to say a csv file:
```python
df_teq_vs_period_final_clean.to_csv('exoplanet_cleaned_teq_vs_period.csv', index = True)
```

We can at anytime open the saved csv file within JupyterLab, which will provide a very nice formatted view of the contents.

Finally, let's apply some final touches to our notebook that will not only benefit us when revisiting it, but also be helpful to others who you might want to share it with.



