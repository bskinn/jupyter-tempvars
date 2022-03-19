/**
 * jupyter_tempvars.js
 * 
 * (needs improving)
 * Wrap all cell-executed code with a TempVars context manager
 * to handle temporary variables.
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

    return {
        load_ipython_extension: function () {
            console.log('[jupyter-tempvars] initializing metadata')
            let md = Jupyter.notebook.metadata;
            md["tempvars"] = {};
            let tv = md["tempvars"];
            tv["universal"] = false;

            // tv["set_universal"] = (val) => {tv["universal"] = val};

            console.log('[jupyter-tempvars] defining helpers');
            

            console.log('[jupyter-tempvars] patching CodeCell.execute');
            var orig_execute = CodeCell.prototype.execute;

            CodeCell.prototype.execute = function (stop_on_error) {
                const is_tempvars = (e) => e == "tempvars";

                var tags = this.metadata.tags || [];  // Could do this by inspecting first line of cell text, too

                if (tags.some(is_tempvars)) {
                    var orig_text = this.get_text();
                    
                    var new_text = orig_text;

                    new_text = new_text.replace("\n", "\n    ");
                    new_text = "from tempvars import TempVars\nwith TempVars(starts=['t_']):\n    " + new_text;

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