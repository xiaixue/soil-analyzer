# Soil Mechanics Analyzer

 Read this in other languages: [Español](www..com), [中文](www..com)
***

The program analyzes and generates a report as a PDF. It can make two analysis, sieve and Atterberg analysis to your given soil data sample.
Run the `soils_data.py`

_NOTE: Input all your data in grams_
When first running it, choose the language then your analysis type
```
Which analysis would you like to run?
1. Sieve Analysis
2. Plasticity Analysis
3. Both
```
>Be aware, if you choose option 1 only and your sample ends up needing plasticity analysis to appropietly classify it, you will need to pick option 'Both' and input the plasticity data, otherwise the USCS will be assigned as '--'.

>Same goes if you only pick option 2, the USCS will be only based on the given plastic data.

For the sieve analysis data, you will be required to input the grams per mesh and the total lastly.
```
Enter the values of the soil by mesh. If there is a value you don't have, write 'None' or press Enter 
    Grams for 4": 
...
    Grams for 270:
    Grams for 400:
    Σ = 3620.0 g
    What is the weight of the total mass?: 
```
For the atterberg analysis, it is detailed how you should introduce your data.
> You can only introduce 6 samples for the liquid limit and 2 for the plastic limit.

> If you have less than 6 samples, when you are finish write "exit".

The following is an example of how yo introduce the data.
```
Input your laboratory data through Casagrande's method with the following order and a space between. Everything with the same units.
    #Hits ID Weight recipient Weight recipient+wet soil Weight recipient+dried soil
  --> 39 HGY-3S 12.25 20.87 16.02
  --> 28 SIU-54 12.63 21.88 16.60
  --> 19 IDS-00 17.63 27.06 21.58
  --> 11 OMG-33 16.84 25.85 20.48
  --> exit
Input your laboratory data of the plastic limit. Everything with the same units.
  ID  Weight recipient Weight recipient+wet soil Weight recipient+dried soil
  --> 51 3.44 4.98 4.7
  --> 67 4.05 4.93 4.71
```
---
* `class Soils`
  
  This class takes your sections as matrix, and is optional to input additional data. You can specify the

    * `d136()` This function computes the diameter of the mesh when the 60, 30 and 10 percent passes the mesh through a logharitmic interpolation, Cc and Cu.

      **Parameters: _None_** 
    
      **Returns: _dictionary_** 
      
      * **d60:**  _(float) or (str)_  Diameter of the mesh where the 60% of the sample passes, if there isn't, it will be '--'.
      * **d30:**  _(float) or (str)_ Diameter of the mesh where the 30% of the sample passes, if there isn't, it will be '--'.
      * **d10:**  _(float) or (str)_ Diameter of the mesh where the 10% of the sample passes, if there isn't, it will be '--'.
      * **cu:** _(float) or (str)_  $C_u$, if there isn't, it will be '--'.
      * **cc:**  _(float) or (str)_  $C_c$, if there isn't, it will be '--'.

    * `sucs_pre()` Gets the percentages of the particle types of your tested sample.

      **Parameters: _None_** 

      **Returns: _dictionary_** 
      
      * **sand:**  _(float)_ Percentage of sand in the sample.
      * **gravel:**  _(float)_ Percentage of gravel in the sample.
      * **fines:**  _(float)_ Percentage of fines in the sample.
      * **sucs:**  _(float) or (str)_ USCS type if the data is enough to classify it correctly, otherwise it will be assign as '--'

    * `plasticity(lld, pld)` This function will find and add the corresponding population that comes from other sections and end in incomplete sections where you do not know the total.

      **Parameters:** 
      
      * **_lld_**: List of lists, with the information of each sample for the liquid limit calculation. Each element must have the following format:

        [Number of Hits _(int)_ , ID _(str)_, Recepient Weight _(float)_, Recipient + Wet Soil weight _(float)_, Recipient + Dried Soil weight _(float)_]
      
      * **_pld_**: List of lists, with the information of each sample for the plastic limit calculation. Each element must have the following format:

        [ ID _(str)_, Recepient Weight _(float)_, Recipient + Wet Soil weight _(float)_, Recipient + Dried Soil weight _(float)_ ]
    
      **Returns: _dictionary_** 
      
      * **ll:**  _(float)_ Liquid Limit of the sample (at 25 hits).
      * **pl:**  _(float)_ Liquid Limit of the sample (average from your measured data)
      * **fw:**  _(float)_ Slope of the logarithmic equation from the curve fitting $\left(w_c=F_wlog(x)+cte\right)$.
      * **cte:**  _(float)_ Constant of the logarithmic equation from the curve fitting $\left(w_c=F_wlog(x)+cte\right)$.
      * **sucs:** _(str)_  USCS classification.
      * **Ip:**  _(float)_ Plastic Index of the soil
      * **IpA:** _(float)_ Plastic Index of the line A when there is LL.
      * **hits:** _(list)_ Axis of hits, for matters of plotting.
      * **wc:** _(list)_ Axis of water content, for matters of plotting.
      * **x:** _(list)_ Axis of hits directly from your input, for matters of plotting.
      * **y:** _(list)_ Axis of water content computed directly from your input, for matters of plotting.
---
Sample Data for you to try
>Form Data

    Diamond H.
    5-6 m
    LA, CAL
    GJM-238DR
    Sample without smell and brown color.
    ASTM-11-33
    1.01.2000
    Eng. Matt Damon
    Eng. John Doe.

>Sieve Analysis

    0

    0
    75
    125
    70
    125
    100
    125
    80


    300


    1000

    870

    400

    200

    150


    3700

>Atterberg Analysis

    39 1  12.25 20.87 16.02
    28 20  12.63 21.88 16.60
    19 80  17.63 27.06 21.58
    11 84  16.84 25.85 20.48
    exit
    51 3.44 4.98 4.7
    67 4.05 4.93 4.71

   