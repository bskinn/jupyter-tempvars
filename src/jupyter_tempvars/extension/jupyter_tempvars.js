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
    var comm_name = "_jupyter_tempvars_comm"
    var settings

    return {
        load_ipython_extension: function () {

            var register_comms = () => {
                Jupyter.notebook.kernel.execute(
                    `if "_Comm" not in dir():
                        from ipykernel.comm import Comm as _Comm
                        _jupyter_tempvars_comm = _Comm(target_name='${comm_name}')`
                );

                if ( ! (comm_name in Jupyter.notebook.kernel.comm_manager.targets)) {
                    Jupyter.notebook.kernel.comm_manager.register_target(
                        comm_name,
                        (comm, msg) => {
                            comm.on_msg( m => {settings = m.content.data})
                        }
                    );
                }

            }

            console.log('[jupyter-tempvars] patching CodeCell.execute');
            var orig_execute = CodeCell.prototype.execute;

            CodeCell.prototype.execute = function (stop_on_error) {
                /* Register comms if needed */
                register_comms()

                console.log('[jupyter-tempvars] retrieving settings')
                Jupyter.notebook.kernel.execute("_jupyter_tempvars_comm.send(_jupyter_tempvars_settings)")
                console.log(settings)

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
