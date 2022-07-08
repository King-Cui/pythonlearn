from pdf2image import convert_from_path
convert_from_path('06-20工作记录.pdf', 300, "output", fmt="JPEG", output_file="essay", thread_count=1)