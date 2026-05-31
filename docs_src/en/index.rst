.. tsutsuji documentation master file, created by konawasabi
   sphinx-quickstart on Fri Mar 18 23:41:00 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

====================================
Documents for Tsutsuji trackcomputer
====================================

Introduction
-------------

Tsutsuji trackcomputer is a Python script designed to assist in creating map files for Bve Trainsim 5/6.

Its main purpose is to build all tracks using own-track syntax (Curve, Gradient) and convert them into other-track syntax (Track.X, Track.Y, etc.) relative to one of the tracks.

During conversion to other-track syntax, in addition to track coordinates, the following parameters are also converted:

* Horizontal curve / Vertical curve relative radius
* Transition curves
* Cant
* Cant rotation center
  
To get started, please see :doc:`Tutorial Basic Functions <tutorial_first>`.

Contents
---------

.. toctree::
   :maxdepth: 2

   tutorial
   referenceguide
   keyshortcut
   tsutsuji API (Under construction) <tsutsuji>

Repository
-----------
  
* https://github.com/konawasabi/tsutsuji-trackcomputer


Acknowledgements
-----------------

* For the Latitude/Longitude to Cartesian coordinate conversion routine, we use the code published by sw1227 at the following URL:
  
  * https://qiita.com/sw1227/items/e7a590994ad7dcd0e8ab
