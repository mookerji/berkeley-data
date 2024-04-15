## Berkeley Pavement

### 2023 Pavement Management Plan

This directory contains parsed CSV data about pavement quality in Berkeley.

- `tabula-City of Berkeley_2022 PMP Update_PTAP 23 Final Report-filtered.csv`
  * Extracted using [Tabula][tabula] from the [2023 Berkeley PMP][source_ptap_2023].
- `berkeley-pci-2023.csv`
  * Post-processed from Tabula file into a format more easily parseable with
    Pandas' `pd.read_csv` function. We've also normalized the data, using the
    PMP glossary to convert abbreviations (e.g., 'P' to 'Portland cement' in the
    'Surface' column).

[source_ptap_2023]: https://berkeleyca.gov/sites/default/files/documents/City%20of%20Berkeley_2022%20PMP%20Update_PTAP%2023%20Final%20Report.pdf
[tabula]: https://tabula.technology/
