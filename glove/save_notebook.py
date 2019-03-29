
# coding: utf-8

# In[5]:


import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert import PDFExporter
import nbconvert
import datetime


# In[6]:


def save_notebook(notebook_filename):
    now = str(datetime.datetime.now()).replace(" ","").replace(".","-").replace(":","-")
    with open(notebook_filename) as f:
        nb = nbformat.read(f, as_version=4)

    # ep = nbconvert.ExecutePreprocessor(timeout=600, kernel_name='python3')

    # ep.preprocess(nb, {'metadata': {'path': './'}})

    pdf_exporter = PDFExporter()

    pdf_data, resources = pdf_exporter.from_notebook_node(nb)
    file_result_name = "results/" + notebook_filename.replace(".ipynb",now) +".pdf"
    
    with open(file_result_name, "wb") as f:
        f.write(pdf_data)
        f.close()
    return file_result_name

