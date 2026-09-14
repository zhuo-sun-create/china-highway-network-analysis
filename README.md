# China Highway Network Analysis and Interactive Visualization

An interactive visualization and regional analysis project for China's motorway network, built with OpenStreetMap data.

## Live Demo

[Open the Interactive Highway Map](https://zhuo-sun-create.github.io/china-highway-network-analysis/)

[View the Network Analysis Dashboard](https://zhuo-sun-create.github.io/china-highway-network-analysis/highway_network_analysis.html)

## Features

- Interactive visualization of motorway networks
- Coverage across 31 mapped regions
- Regional map selection and city locator
- Road name and route number search
- Clickable road details
- Regional motorway segment ranking
- Estimated motorway length comparison
- Mobile-friendly interface
- Compressed and regionally split data loading

## Technology Stack

- Python
- OpenStreetMap
- Leaflet.js
- JavaScript
- HTML / CSS
- Gzip data compression

## Data Source

The road data comes from OpenStreetMap and primarily uses roads tagged as `highway=motorway`.

The data represents a static map snapshot. It does not provide real-time traffic conditions, and data completeness has not been professionally surveyed.

## Analysis Method

Road length is estimated from road-node coordinates using the Haversine formula. Regional segment counts are grouped by mapped region. Cross-boundary roads may be counted in more than one region.

## Project Purpose

This project was developed to practice:

- Transportation data processing
- GIS-based road network visualization
- Interactive web mapping
- Large-scale data organization
- Mobile web performance optimization
- Regional transportation network analysis

## Author

孙卓 
交通工程专业本科生
