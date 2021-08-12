.. MM_JSON_Schema documentation master file, created by
   sphinx-quickstart on Thu May 06 04:56:44 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

What is MMSchema?
==========================

.. container:: text-justify

    MMSchema is a specification for classical particle mechanics with emphasis on molecular systems. The schema provides standardized data objects that enable interoperability between
    different molecular mechanics codes without restricting any particular workflow.

.. 
   image:: images/mmschema.png
   :alt: MMSchema

Currently, MMSchema is a `JSON <https://www.json.org>`_ schema; comptability with the `hdf5 <https://www.hdfgroup.org/solutions/hdf5>`_ format is being developed as well.


Core Models
===========

.. container:: text-justify

    MMSchema adopts an object-oriented view of classical mechanics by dividing it into its constituent core objects: initial state, inter-particle potential,
    and final state (statics) or trajectory (dynamics). Each core model represents a building block that is an integral part of the computation. The 3 core models in MMSchema are:

    - Molecule: represents a basic molecule object for MM, or more generally the N-body state in classical mechanics.
    - ForceField: represents force fields for MM, or more generally inter-particle potentials in classical mechanics.
    - Trajectory: represents trajectories in dynamical systems.

.. image:: images/objects.png
   :alt: statics
   :align: center
   :width: 850

.. container:: text-justify

    For classical statics, the MMSchema models `Molecule` and `ForceField` would represent the initial/final states and the inter-particle potential, respectively, as shown in the figure above.
    Likewise, `Trajectory` would represent simulation output of dynamical systems.

.. container:: text-justify

   Each object in MMSchema is uniquely defined by a set of fields and (when suitable) their associated units as well. The schema is designed to be flexible as much as
   possible by providing a general specification for computational particle mechanics, but **MMSchema does not standardize any specific workflow**. Instead, MMSchema strives to provide a starting point
   for specific application areas based on or related to MM such as energy minimization, force field assignment and construction, molecular dynamics, advanced sampling, ... to name a few.
   The schemas for these domains or applications are handled by `MMIC <https://mm-portal.netlify.app/mmic>`_ components that define the input and output models for each procedure. Since MMSchema is not 
   restricted to the atomic scale, it can also be used for coarse-graining as well as multiscale methods that evolve multiple spatial and/or temporal scales.
   In fact, *any particle-based Newtonian method can use MMSchema and further customize/extend it*.


Contents
--------

.. toctree::
   :caption: Contents
   :maxdepth: 1
   
   faq
   examples

.. toctree::
   :maxdepth: 1
   :caption: Topology
 
   auto_molecule

.. toctree::
   :maxdepth: 1
   :caption: ForceField

   auto_forcefield
   auto_nonbonded
   auto_bonds
   auto_angles
   auto_dihedrals

.. toctree::
   :maxdepth: 1
   :caption: Collections
   
   auto_trajectory
