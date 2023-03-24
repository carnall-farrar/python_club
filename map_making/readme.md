## Getting Started

Before you can run the lsoa_map_making notebook there are several things you need set up on your laptop

### Prerequisites
We use conda as it deals with all the dependencies needed for geopandas

- conda - Please ask Moof to install anaconda on your laptop https://www.anaconda.com/

### Installation

Once you have conda please following these steps:

1. Create a folder in your Documents called 'Coding'
2. Open a terminal and navigate to that folder using
   ```
   cd Documents/Coding
   ```
3. Clone the repo
   ```
   git clone https://github.com/carnall-farrar/python_club.git
   ```
4. Navigate into the cloned folder
   ```
   cd python_club
   ```
5. Install the conda environment
   ```
   conda env create -f environment.yml
   ```

6. Navigate into the map_making folder
   ```
   cd map_making
   ```
7. Open jupyter notebook from the terminal and this will open in your internet browser

    This command is used to open with default kernel as your conda environment
   ```
   jupyter notebook --MultiKernelManager.default_kernel_name=python_club
   ```

8. Open lsoa_map_making.ipynb notebook and you can now make your map!
