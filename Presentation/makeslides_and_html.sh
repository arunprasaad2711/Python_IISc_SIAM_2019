#!/bin/bash
# jupyter nbconvert SIAM2019_Presentation.ipynb --to slides
jupyter nbconvert SIAM2019_Presentation.ipynb --to html
jupyter nbconvert SIAM2019_Presentation.ipynb --to slides --SlidesExporter.reveal_scroll=True
