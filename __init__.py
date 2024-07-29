from .paddleocr import (
    PaddleOCR,
    PPStructure,
    draw_ocr,
    draw_structure_result,
    save_structure_res,
    download_with_progressbar,
    sorted_layout_boxes,
    convert_info_docx,
    to_excel,
)
import importlib.metadata as importlib_metadata

try:
    __version__ = importlib_metadata.version(__package__ or __name__)
except importlib_metadata.PackageNotFoundError:
    __version__ = "0.0.0"

__all__ = [
    "PaddleOCR",
    "PPStructure",
    "draw_ocr",
    "draw_structure_result",
    "save_structure_res",
    "download_with_progressbar",
    "sorted_layout_boxes",
    "convert_info_docx",
    "to_excel",
]
