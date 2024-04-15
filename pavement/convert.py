#!/usr/bin/python3

# Script to normalize/cleanup data in this directory. Notably, this is actually
# run from a Jupyter notebook that isn't committed in this repo yet.

import pandas as pd
import numpy as np

pavement_filename = 'tabula-City of Berkeley_2022 PMP Update_PTAP 23 Final Report-filtered.csv'
pci2023 = pd.read_csv(pavement_filename)
pci2023['Last MnR Date'] = pd.to_datetime(pci2023['Last MnR Date'])
pci2023['PCI DATE'] = pd.to_datetime(pci2023['PCI DATE'])
pci2023['L'] = pci2023['L'].str.replace(',', '').astype(int)
pci2023['DISTRICT'] = pci2023['DISTRICT'].str.split(',')
pci2023['AREA (SqFt)'] \
    = pci2023['AREA (SqFt)'].str.replace(',', '').astype(int)
pci2023['Renovation Age (Years)'] = np.floor(
    (pd.Timestamp('2022-07-20') -
     pd.to_datetime(pci2023['Last MnR Date'])).dt.days / 365.)
pci2023.index \
    = pci2023['STREET ID'].astype(str) + pci2023['SEC ID'].astype(str)
pci2023['Last Work Year'] = pci2023['Last MnR Date'].dt.year

repair_mapping = {
    'CONCRETE REPAIR': "0 - Light Maintenance",
    'DEEP PATCH': "0 - Light Maintenance",
    'FDR': "3 - Heavy Rehab",
    'FIBER MICROSURFACING': "0 - Light Maintenance",
    'LIGHT REHAB': "2 - Light Rehab",
    'MEDIUM AC OVERLAY (2 INCHES)': "2 - Light Rehab",
    'MILL AND THICK OVERLAY': "3 - Heavy Rehab",
    'MILL AND OVERLAY W/FABRIC': "3 - Heavy Rehab",
    'MILL AND OVERLAY': "3 - Heavy Rehab",
    'MILL AND THIN OVERLAY': "2 - Light Rehab",
    'OVERLAY': "3 - Heavy Rehab",
    'RECONSTRUCT PCC': "4 - Reconstruct",
    'RECONSTRUCT STRUCTURE (AC)': "4 - Reconstruct",
    'RECONSTRUCT STRUCTURE (PCC)': "4 - Reconstruct",
    'RECONSTRUCT SURFACE (AC)': "4 - Reconstruct",
    'RECONSTRUCT': "4 - Reconstruct",
    'RUBBERIZED CAPE SEAL': "1 - Heavy Maintenance",
    'SLURRY SEAL': "0 - Light Maintenance",
    'THICK OVERLAY W/FABRIC': "3 - Heavy Rehab",
    'THICK AC OVERLAY(2.5 INCHES)': "3 - Heavy Rehab",
    'THIN AC OVERLAY(1.5 INCHES)': "1 - Heavy Maintenance",
    'THIN OVERLAY w/FABRIC': "1 - Heavy Maintenance",
    'THIN OVERLAY': "1 - Heavy Maintenance"
}
pci2023['Treatment Category'] \
    = pci2023['Last MnR Treatment'].replace(repair_mapping)
fc_map = {
    'R': 'Residential/Local',
    'C': 'Collector',
    'A': 'Arterial',
}
pci2023['Functional Classification'] = pci2023['FC'].replace(fc_map)
pci2023['Length (feet)'] = pci2023['L']
pci2023['Width (feet)'] = pci2023['W']
surface_map = {
    'A': 'Asphalt',
    'C': 'Asphalt over Portland cement',
    'O': 'Overlay of asphalt over asphalt',
    'P': 'Portland cement'
}
pci2023['Surface'] = pci2023['ST'].replace(surface_map)

export_cols = [
    'DISTRICT', 'STREET ID', 'STREET NAME', 'SEC ID', 'BEG LOCATION',
    'END LOCATION', 'AREA (SqFt)', 'PCI DATE', 'PCI', 'Last MnR Date',
    'Last MnR Treatment', 'Renovation Age (Years)', 'Last Work Year',
    'Treatment Category', 'Functional Classification', 'Length (feet)',
    'Width (feet)', 'Surface'
]

pci2023[export_cols].to_csv('berkeley-pci-2023.csv')
