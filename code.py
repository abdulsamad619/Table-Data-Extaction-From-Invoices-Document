
from tabula import read_pdf
from tabulate import tabulate
import tabula

df = read_pdf("pdf_1_AWFA02-user3_5fd169861ba88 page 6.PDF",pages="all")  # address of pdf file
tabula.convert_into("pdf_1_AWFA02-user3_5fd169861ba88 page 6.PDF", "pdf_1_AWFA02-user3_5fd169861ba88 page 6.csv",
                    output_format="csv", pages='all')
print(tabulate(df))

