r"""``jupyter_tempvars`` *IPython extension registration function module*.

``jupyter_tempvars`` is a Jupyter notebook extension providing automatic
per-cell temporary variables management.

**Author**
    Brian Skinn (brian.skinn@gmail.com)

**File Created**
    18 Mar 2022

**Copyright**
    \(c) Brian Skinn 2022

**Source Repository**
    https://github.com/bskinn/jupyter-tempvars

**Documentation**
    *(pending)*

**License**
    The MIT License; see |license_txt|_ for full license terms

**Members**

"""

from IPython.core.magic import Magics, magics_class, line_magic, register_line_magic
from IPython.core.magics.display import Javascript
    
# Make sure not import IPython.display.Javascript?

    
# @magics_class
# class TempvarsMagics(Magics):
    
#     universal = False
    
#     @line_magic
#     def tempvars(self, line):
#         return self.shell
        
#         # self.shell.user_ns is the user variables!


def load_ipython_extension(ipython):
    """Register the magics and configure the globals."""
    # This use of Javascript doesn't work)
    Javascript("console.log('loading extension');")

    # ipython.register_magics(TempvarsMagics)
    
    # @register_line_magic
    # def vardir(line):
    #     nonlocal ipython
    #     print(dir(eval(line)))
    
    # @register_line_magic
    # def inject_ipython(line):
    #     nonlocal ipython
    #     globals().update({'ipython': ipython})
    
    @register_line_magic
    def tempvars(line):
        subcommand, arg = line.strip().split(" ")
        print(f"sc: {subcommand}, arg: {arg}")
        
        if subcommand == "universal":
            print('universal reached')
            #TODO: Error if not a boolean word
            
            # These uses don't work either.
            Javascript("console.log('printy');")
            Javascript(f"Jupyter.notebook.metadata['tempvars']['universal'] = {arg.lower()};")
