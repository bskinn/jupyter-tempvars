/**
 * jupyter_tempvars.js
 *
 * (needs improving)
 * Wrap all cell-executed code with a TempVars context manager
 * to handle temporary variables.
 *
 * Code-patching implementation adapted from the execution_dependencies
 * Jupyter extension:
 *
 *  https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tree/master/src/jupyter_contrib_nbextensions/nbextensions/execution_dependencies
 *
 *
 * @author  Brian Skinn, https://github.com/bskinn
 *
 */

define([
  'base/js/namespace',
  'notebook/js/codecell'
], function (Jupyter, codecell) {

    "use strict";

    var CodeCell = codecell.CodeCell
    var c_log = (msg) => {console.log(`[jupyter-tempvars] ${msg}`);};
    const is_tempvars = (tag) => tag.startsWith("tempvars");

    return {
        load_ipython_extension: function () {
            c_log('importing TempVars');
            /* Timeout is needed because kernel isn't immediately available when extension
             * loading is initiated */
            setTimeout(() => {Jupyter.notebook.kernel.execute("from tempvars import TempVars as _TempVars");}, 2000);

            c_log('patching CodeCell.execute');
            var orig_execute = CodeCell.prototype.execute;

            CodeCell.prototype.execute = function (stop_on_error) {
                var tags = this.metadata.tags || [];  // Could do this by inspecting first line of cell text, too

                if (tags.some(is_tempvars)) {
                    var orig_text = this.get_text();
                    var new_text = orig_text;

                    tags.forEach( tag => {  // Switch to accumulating all starts/ends, and only using one TempVars?
                        if ( tag.startsWith("tempvars-start-") ) {
                            new_text = new_text.replaceAll("\n", "\n    ");
                            new_text = `with _TempVars(starts=['${tag.substring(15)}']):\n    ${new_text}`;
                        }
                        if ( tag.startsWith("tempvars-end-") ) {
                            new_text = new_text.replaceAll("\n", "\n    ");
                            new_text = `with _TempVars(ends=['${tag.substring(13)}']):\n    ${new_text}`;
                        }
                    });

                    this.set_text(new_text);
                    orig_execute.call(this, stop_on_error);
                    this.set_text(orig_text);
                } else {
                    orig_execute.call(this, stop_on_error);
                }
            };
        }
    };
});
