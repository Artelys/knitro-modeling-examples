# Knitro modeling examples

The goal of this repository is to show nonlinear programming models for some applications and their resolution with the nonlinear programming solver [Artelys Knitro](https://www.artelys.com/solvers/knitro/).

## Largest diameter

A toy problem with a black-box function, and which illustrates non-convexity.

* [Python](largest_diameter_python/largest_diameter_python.ipynb)
* [Julia](largest_diameter_julia/largest_diameter_julia.ipynb)
<p align="center">
<img src="https://github.com/Artelys/knitro-modeling-examples/blob/main/largest_diameter_python/shape.png" align=center height="128"> &nbsp;
→
<img src="https://github.com/Artelys/knitro-modeling-examples/blob/main/largest_diameter_python/shape_with_diameter.png" align=center height="128">
</p>

## Hydro unit commitment problem

* [Pyomo](hydro_unit_commitment_pyomo/hydro_unit_commitment_pyomo.ipynb)
* [amplpy ](hydro_unit_commitment_amplpy/hydro_unit_commitment_amplpy.ipynb)
* [JuMP](hydro_unit_commitment_jump/hydro_unit_commitment_jump.ipynb)
<p align="center">
<img src="https://github.com/Artelys/knitro-modeling-examples/blob/main/hydro_unit_commitment_pyomo/schema_hydro_leg.png" align=center height="128"> &nbsp;
<img src="https://github.com/Artelys/knitro-modeling-examples/blob/main/hydro_unit_commitment_pyomo/discharge.png" align=center height="128">
</p>

## Portfolio optimization

* [Pyomo](portfolio_optimization/portfolio_optimization.ipynb)
<p align="center">
<img src="https://github.com/Artelys/knitro-modeling-examples/blob/main/portfolio_optimization/portfolio_optimization.png" align=center height="128"> &nbsp;
</p>

## K-means clustering

* [Pyomo](k_means_clustering/k_means_clustering.ipynb)
* [amplpy](k_means_clustering_amplpy/k_means_clustering_amplpy.ipynb)
<p align="center">
<img src="https://github.com/Artelys/knitro-modeling-examples/blob/main/k_means_clustering/data.png" align=center height="128"> &nbsp;
→
<img src="https://github.com/Artelys/knitro-modeling-examples/blob/main/k_means_clustering/clusterdata.png" align=center height="128">
</p>

## Single row facility layout problem

* [Pyomo](single_row_facility_layout/single_row_facility_layout.ipynb)
<p align="center">
<img src="https://github.com/Artelys/knitro-modeling-examples/blob/main/single_row_facility_layout/solution_random.png" align=center height="128"> &nbsp;
→
<img src="https://github.com/Artelys/knitro-modeling-examples/blob/main/single_row_facility_layout/solution_knitro.png" align=center height="128">
</p>

## Polygon clustering

* [Pyomo](polygon_clustering_pyomo/polygon_clustering_pyomo.ipynb)
<p align="center">
<img src="https://github.com/Artelys/knitro-modeling-examples/blob/main/polygon_clustering_pyomo/polygons.png" align=center height="128"> &nbsp
→
<img src="https://github.com/Artelys/knitro-modeling-examples/blob/main/polygon_clustering_pyomo/clustered_polygons.png" align=center height="196">
</p>

---

[Free trial licenses](https://www.artelys.com/solvers/knitro/programs/) are available to run these examples locally.
