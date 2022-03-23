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
    // var comm_manager
    var comm_name = "_jupyter_tempvars_comm"
    var settings
    // var awaiting_settings

    var c_log = (msg) => {console.log(`[jupyter-tempvars] ${msg}`);};

    return {
        load_ipython_extension: function () {

            // var register_kernel_comm = () => {
            //     c_log("registering kernel comm");
            //     Jupyter.notebook.kernel.execute(
            //         `
            //         if "_Comm" not in dir():
            //             from ipykernel.comm import Comm as _Comm
            //         if "${comm_name} not in dir():
            //             ${comm_name} = _Comm(target_name='${comm_name}')
            //         `
            //     );
            // }

            var register_frontend_comm = () => {
                // c_log("binding comm manager")
                // comm_manager = Jupyter.notebook.kernel.comm_manager

                c_log("registering frontend comm");
                Jupyter.notebook.kernel.comm_manager.register_target(
                    comm_name,
                    (comm, msg) => {
                        comm.on_msg( m => { settings = m.content.data; })
                    }
                );


            }

            c_log('patching CodeCell.execute');
            var orig_execute = CodeCell.prototype.execute;

            CodeCell.prototype.execute = function (stop_on_error) {
                // /* Always attempt kernel comm (re)bind (needed after kernel restart) */
                // register_kernel_comm();

                /* Only rebind the frontend comm if it's not registered */
                if ( ! (comm_name in Jupyter.notebook.kernel.comm_manager.targets)) {
                    register_frontend_comm();
                }

                c_log('retrieving settings before execution');
                // awaiting_settings = true
                // Jupyter.notebook.kernel.execute("_jupyter_tempvars_comm.send(_jupyter_tempvars_settings)")
                // await comm_manager.comms[keys(comm_manager.comms)]
                // while ( Jupyter.notebook.kernel._pending_messages.length > 0 ) { console.log(Jupyter.notebook.kernel._pending_messages); }
                // setTimeout(() => {console.log(settings)}, 2000)
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

                c_log('retrieving settings after execution');
                console.log(settings);
            };
        }
    };
});
