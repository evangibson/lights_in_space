## Schema for Creating a Bounded Area Dataset
- Summary
- Known Geometries
- Monte Carlo Approximations
- Heuristic methods

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

### Known Geometries
As stated earlier, many exact area solutions exist for Venn diagrams that meet particular conditions. Therefore, plane data can be generated using methods developed by [researchers]. The following methods will be employed to generate relevant data:

- Fartlek's method
- Giocanno's algorithm

In addition to Venn diagrams that adhere to the parameters of [methods] above, the the present paradigm can accommodate data that can be implied by a random-generating system. These cases are as follows:
- Single eclipsing circles 
- Planes that have entirely separated circles
- Two circle planes
- ...
