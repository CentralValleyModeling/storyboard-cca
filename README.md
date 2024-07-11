# Storyboard CCA

The dashboard to display a highly curated story-board for the Climate Adapatation Studies results.

## Quick start

To get things set up, and to serve the site on your local machine, follow the following steps.

```powershell
conda env create -f environment.yaml -y
conda activate dev_storyboard_cca
uvicorn src.storyboard_cca.main:app --reload
```
