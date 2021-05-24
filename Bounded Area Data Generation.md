## Schema for Creating a Bounded Area Dataset

[[toc]]

___
### Summary
Modern supervised learning algorithms and heuristics require large data to either train or localize upon their objectives. The objective of the present project is to effectively _approximate the two-dimensional area of Venn diagrams_. This work will focus on a paradigm that involves arbitrarily drawn circles where the known data are their center coordinates (x and y) and the length of their radii (r). 

Calculus-driven solutions to this overlapping area problem require exceptionally sophisticated parameters on well-controlled planes (and do not apply to many arbitrary circle placements). Probabilistic methods (such as Monte Carlo approximations), in general, produce largely accurate results within their study constraints. However, such methods require scalable computing power that reduces the practical simulation of sufficiently high amounts of test objects.

Therefore, this project will explore the overlapping Venn diagram by first generating a large data set using a combinatorial approach of geometric (exact), probabilistic (Monte Carlo), and heuristic methods. Hopefully, this relatively slow approach can yield large and diverse enough data to employ machine-learning methods against the same area problem.

The present subsection deals with the data generation techniques used by the present researcher to create two-dimensionally bound groups of circles with diverse overlapping qualities. The researcher ensures that the following "special conditions" are met and sampled within the data:
- Partially overlapping circles
- Eclipsing circles
- Non-overlapping circles
- Hybrid combinations of the above examples

Each method described herein will produce data in the following schema (expressed as a Python dictionary): 
``` python 
{
  plane_1:{plane: [{x:1, y:2, r:3},
                 {x:3, y:2, r:4},
                  ...,
                  {x:4, y:1, r:2}],
          area: 32.432221123},
    
 plane_2:{plane: [{x:11, y:2, r:4},
                 {x:9, y:4, r:4},
                  ...,
                  {x:3, y:1, r:2}],
          area: 37.43211230203},
          
          ...
          
  plane_n:{plane: [{x:1, y:2, r:3},
                 {x:3, y:2, r:9},
                  ...,
                  {x:3, y:11, r:11}],
           area: 35.67320203}
          
}                  
```
___
### Known Geometries
As stated earlier, many exact area solutions exist for Venn diagrams that meet particular conditions. Therefore, plane data can be generated using methods developed by [researchers]. The following methods will be employed to generate relevant data:

- Fartlek's method
- Giocanno's algorithm

In addition to Venn diagrams that adhere to the parameters of [methods] above, the the present paradigm can accommodate data generation patterns that enable exact area solutions. These cases are as follows:
- Single eclipsing circles 
- Planes that have entirely separated circles
- Two circle planes
- ...

The cases above represent opportunities to express data whose area can be calculated using the following formula:

$$a = πr^2$$

Provided the areas of the wholly overlapping figures are calculated using the largest circle in each set, this technique should significantly boost model training against commonly confounding conditions. Additionally, calculating a circle's area by using $$a = πr^2$$ is less computationally expensive than Monte Carlo approximation (and enjoys perfect precision).

### Monte Carlo Methods

When estimating the area of polygons on a two dimensional plane, Monte Carlo methods allow for ...

$$
a_p \approx a \frac{p_c}{p_n}
$$


Presently, the present data generation schema accommodates derivations of Monte Carlo methods. The first method samples the total state space in each simulation for random point generation. In other words, the first methods allowable range of coordinates are bounded by the static parameters established before the random generation of a state space's circles. 

[An image showing that circles can appear anywhere on the plane](image)

Using the first method,

The second method will only cast estimation points within a box determined by the minimum and maximum x and y coordinates in each set of circles 

___

### Formula Variable Index

- Let $$a_p$$= Total area of polygon covered space on a two-dimensional plane. 
- Let $$r$$ =  Radius of a given circle.
- Let $$x$$ = Coordinate value indicating a point's horizontal distance from the y-axis.
- Let $$y$$ = Coordinate value indicating a point's vertical distance from the x-axis.
- Let $$a$$ = Total area of a two-dimensional plane.
- Let $$