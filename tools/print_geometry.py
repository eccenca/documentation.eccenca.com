"""What the print edition measures images by: the text column and two densities.

The width of the column decides how sharp an image prints, so the builder
(`build_pdf`), the tool that sizes images in the sources (`image_widths`) and
the preflight report (`pdf_preflight`) have to agree on it. They share these
values rather than each keeping their own (tasks/spec.md, §5 and §11).
"""
from __future__ import annotations

# The text column of the A4 page, in the three units the tools work in.
COLUMN_CM = 16
COLUMN_INCHES = COLUMN_CM / 2.54
TEXT_WIDTH_PT = COLUMN_INCHES * 72

# What print asks for: images are resampled to 300 ppi at their printed width
# (BoD, tasks/spec.md, §6), and the preflight fails below it.
PRINT_PPI = 300
# Below this density an original is too coarse to print at that size: the build
# lists it and `dec-tool image-widths` narrows it (backlog P15, P24).
LOW_RESOLUTION_PPI = 150
